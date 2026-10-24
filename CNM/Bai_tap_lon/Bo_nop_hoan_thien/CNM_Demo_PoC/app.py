from pathlib import Path
import pandas as pd
import streamlit as st
import xgboost as xgb
from artifact_loader import verify_artifacts
from risk_engine import score_transaction, validate
from train_model import FEATURES, generate_synthetic_bank_data

BASE=Path(__file__).resolve().parent
st.set_page_config(page_title='PoC học thuật | Phát hiện giao dịch nghi ngờ',page_icon='🛡️',layout='wide')
st.title('AI hỗ trợ phát hiện giao dịch nghi ngờ gian lận')
st.caption('Bối cảnh nghiên cứu đề xuất: MB | Học phần Công nghệ mới nổi và Đổi mới – HVNH')
st.warning('PoC học thuật trên dữ liệu tổng hợp, không phải hệ thống MB. Không kết nối ngân hàng, không chặn tiền, không xác thực khách hàng và không chứng nhận tuân thủ pháp lý.')

@st.cache_resource
def load_checked_artifacts(stamp_model,stamp_metrics,stamp_manifest):
    return verify_artifacts(BASE)
try:
    model,report,manifest=load_checked_artifacts(
        (BASE/'fraud_model.json').stat().st_mtime_ns,
        (BASE/'metrics.json').stat().st_mtime_ns,
        (BASE/'artifact_manifest.json').stat().st_mtime_ns)
except Exception as exc:
    st.error(f'Không thể xác minh bộ mô hình và kết quả: {exc}. Hãy chạy python train_model.py; ứng dụng dừng chấm điểm khi artifact không khớp.')
    st.stop()
if 'history' not in st.session_state: st.session_state.history=[]
history=st.session_state.history
threshold=float(report['metrics']['xgboost_by_seed']['42']['threshold'])
high=float(report['demo_policy']['high_threshold'])
cols=st.columns(4)
cols[0].metric('Giao dịch mô phỏng trong phiên',len(history))
cols[1].metric('Cần xem xét trong phiên',sum(r['score']>=threshold for r in history))
cols[2].metric('Ngưỡng mô hình seed 42',f'{threshold:.3f}')
lat=[r['latency_ms'] for r in history]
cols[3].metric('Inference trung vị (ms)',f'{pd.Series(lat).median():.2f}' if lat else 'Chưa đo')
st.caption('Độ trễ là predict_proba cho một giao dịch trên máy hiện tại; không gồm mạng, xác thực hay xử lý giao dịch và không phải SLA.')
input_tab,feed_tab,eval_tab,architecture_tab=st.tabs(['Giả lập giao dịch','Lịch sử mô phỏng','Đánh giá mô hình','Kiến trúc & phạm vi'])
with input_tab:
    st.info(f'Chính sách giao diện chỉ để minh họa: thấp < {threshold:.3f}; xác thực bổ sung từ {threshold:.3f} đến dưới {high:.3f}; chuyển chuyên viên từ {high:.3f}. Điểm chưa được hiệu chỉnh thành xác suất thực tế.')
    with st.form('transaction'):
        left,right=st.columns(2)
        with left:
            amount=st.number_input('Số tiền (VND)',20_000,500_000_000,1_500_000,10_000)
            hour=st.slider('Giờ giao dịch',0,23,14)
            channel=st.selectbox('Kênh mô phỏng',[0,1,2,3],format_func=lambda i:['Mobile','Web','Thẻ/POS','Ví điện tử'][i])
            frequency=st.slider('Số giao dịch trong 10 phút, gồm giao dịch hiện tại',1,20,1)
        with right:
            device=st.checkbox('Thiết bị mới (tín hiệu mô phỏng)')
            location=st.checkbox('Vị trí bất thường (tín hiệu mô phỏng)')
            failed=st.slider('Số lần sai OTP/PIN trong 30 phút (3 = từ 3 trở lên)',0,3,0)
            beneficiary=st.checkbox('Người nhận chưa từng được người gửi chuyển trước đó')
        submit=st.form_submit_button('Chấm điểm mô phỏng',type='primary')
    if submit:
        tx={'amount':amount,'hour':hour,'channel':channel,'new_device':int(device),
            'location_anomaly':int(location),'failed_attempts':failed,
            'tx_frequency_10m':frequency,'new_beneficiary':0 if beneficiary else 1}
        try:
            result=score_transaction(model,report,tx)
            st.session_state.history.append({'demo_id':f"DEMO-{len(history)+1:05d}",**tx,**result})
            st.session_state.last_tx=tx; st.session_state.last_result=result; st.rerun()
        except Exception as exc:
            st.error(f'Không thể chấm điểm: {exc}. Chuyển kiểm tra thủ công; không tự phê duyệt.')
    if 'last_result' in st.session_state:
        result=st.session_state.last_result
        st.subheader('Kết quả chấm điểm')
        st.metric('Điểm mô hình (0–100)',f"{result['score']*100:.2f}")
        st.write('**Hành động đề xuất:**',result['action'])
        st.caption(f"Inference đo trên máy hiện tại: {result['latency_ms']:.3f} ms | Model seed: {result['model_seed']} | Run ID: {result['run_id']}")
        frame=validate(st.session_state.last_tx)
        contrib=model.get_booster().predict(xgb.DMatrix(frame),pred_contribs=True)[0]
        imp=pd.DataFrame({'Đóng góp raw margin':contrib[:-1]},index=FEATURES).sort_values('Đóng góp raw margin')
        st.subheader('Đóng góp TreeSHAP cho giao dịch mô phỏng')
        st.bar_chart(imp)
        st.caption(f'Bias={contrib[-1]:.4f}; tổng đóng góp={contrib.sum():.4f} ở raw margin. Giá trị này giải thích đầu ra của mô hình, không chứng minh nguyên nhân hay gian lận đã xảy ra.')
with feed_tab:
    st.caption('Batch tổng hợp, không phải streaming hoặc dữ liệu giao dịch trực tiếp. Lịch sử chỉ tồn tại trong phiên trình duyệt.')
    b1,b2=st.columns(2)
    with b1:
        if st.button('Sinh 20 giao dịch tổng hợp'):
            batch=generate_synthetic_bank_data(20,random_state=42+len(history))
            for _,r in batch[FEATURES].iterrows():
                tx={k:float(r[k]) if k=='amount' else int(r[k]) for k in FEATURES}
                st.session_state.history.append({'demo_id':f"DEMO-{len(st.session_state.history)+1:05d}",**tx,**score_transaction(model,report,tx)})
            st.rerun()
    with b2:
        if st.button('Xóa lịch sử phiên'):
            st.session_state.history=[]; st.session_state.pop('last_result',None); st.session_state.pop('last_tx',None); st.rerun()
    if history:
        table=pd.DataFrame(history)
        st.dataframe(table,use_container_width=True,hide_index=True)
        st.download_button('Tải CSV lịch sử mô phỏng',table.to_csv(index=False).encode('utf-8-sig'),
                           file_name='demo_history.csv',mime='text/csv')
    else: st.info('Chưa có giao dịch trong phiên.')
with eval_tab:
    st.caption(f"Run: {report['run_id']} | Split: train {report['split']['train']:,}, validation {report['split']['validation']:,}, test {report['split']['test']:,} | Nhãn dương tổng hợp: {report['positive_rate']:.2%}")
    metrics=report['metrics']; seed42=metrics['xgboost_by_seed']['42']
    comparison=pd.DataFrame({
        'Luôn dự đoán bình thường':metrics['always_negative'],
        'Quy tắc đơn giản':metrics['simple_rule'],
        'XGBoost seed 42':{k:v for k,v in seed42.items() if k!='confusion_matrix'}
    }).T
    st.subheader('So sánh trên tập test holdout')
    st.dataframe(comparison,use_container_width=True)
    st.write('Confusion matrix XGBoost seed 42: hàng = nhãn thật [0,1], cột = dự đoán [0,1].')
    st.dataframe(pd.DataFrame(seed42['confusion_matrix'],index=['Thật 0','Thật 1'],columns=['Dự đoán 0','Dự đoán 1']))
    st.subheader('Độ nhạy theo random seed trên cùng split')
    st.dataframe(pd.read_csv(BASE/'seed_results.csv').set_index('seed'),use_container_width=True)
    pr=pd.read_csv(BASE/'pr_curve_seed42.csv')
    st.subheader('Precision–Recall trên test, seed 42')
    st.line_chart(pr.set_index('recall')['precision'])
    trade=pd.read_csv(BASE/'threshold_tradeoff.csv')
    st.subheader('Đánh đổi giữa tỷ lệ cảnh báo và Recall')
    st.line_chart(trade.pivot_table(index='alert_rate',columns='model',values='recall',aggfunc='max').sort_index())
    st.warning('Nhãn sinh từ quy tắc rủi ro + nhiễu trên cùng bộ đặc trưng. Chỉ chứng minh pipeline trên dữ liệu tổng hợp; không dự báo hiệu quả tại MB và không suy ra giá trị tiền được bảo vệ. Tỷ lệ cảnh báo sai là tải kiểm tra tiềm năng, không phải giao dịch bị chặn.')
with architecture_tab:
    st.subheader('Phần đã cài và phần đề xuất')
    st.code('ĐÃ CÀI: giao diện Streamlit → kiểm tra 8 trường → XGBoost seed 42 → chính sách demo → lịch sử phiên/CSV\nĐỀ XUẤT (chưa tích hợp): kênh giao dịch → kiểm soát bắt buộc → feature service → scoring → policy có người sở hữu → xử lý giao dịch / hàng đợi chuyên viên\nCHƯA CÓ: Kafka, Core Banking, xác thực khách hàng, phân quyền, lưu trữ bền vững, HA/DR, quy trình khiếu nại, kiểm soát pháp lý production.')
    st.write('Kênh và tín hiệu vị trí/thiết bị trong giao diện đều mô phỏng. Trước pilot phải xác minh khả năng thu thập đúng thời điểm, chất lượng nhãn và quyền xử lý dữ liệu; lỗi model hoặc thiếu dữ liệu không đồng nghĩa giao dịch an toàn.')
    st.write('**Ranh giới quyết định:** PoC phát ra điểm và gợi ý thao tác cho người xem demo; không gửi lệnh chuyển tiền, giữ tiền, khóa tài khoản, OTP, FaceID hay thông báo cho khách hàng.')
