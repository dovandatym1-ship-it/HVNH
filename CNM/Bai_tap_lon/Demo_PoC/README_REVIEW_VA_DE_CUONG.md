# Đánh giá và hoàn thiện đề tài

## 1. Kết luận
**Hướng đề tài phù hợp để phát triển thành bài tập lớn; thư mục ban đầu chưa đủ để coi là bài nộp hoàn chỉnh.** Bản sửa là PoC học thuật có thể chạy local và có đánh giá định lượng. Không phải hệ thống chống gian lận production, không chứng minh hiện trạng hoặc hiệu quả tại MB.

**Tên đề xuất:** “Ứng dụng học máy hỗ trợ phát hiện giao dịch nghi ngờ gian lận: xây dựng và đánh giá PoC trên dữ liệu tổng hợp trong bối cảnh nghiên cứu MB”.

Không giữ “xử lý hướng sự kiện/thời gian thực tại MB” như năng lực đã triển khai vì chưa có broker, hệ thống nguồn hay tích hợp ngân hàng. Có thể giữ kiến trúc hướng sự kiện ở phần lộ trình đề xuất.

### Căn cứ rà soát
- Đề gốc DOCX trong thư mục cha, phần mục tiêu, nội dung và tiêu chí đánh giá; đối chiếu bản Markdown `YEU_CAU_BAI_TAP_LON_CNM.md`.
- Bốn file gốc của PoC được lưu trong `backup_before_review/`.
- Không thấy báo cáo hoàn chỉnh hoặc slide bảo vệ trong thư mục PoC đã kiểm tra. Không kết luận chúng không tồn tại ở nơi khác.
- **Lưu ý nguồn:** phần tóm lược Markdown ghi 25–40 trang và 15–20 slide; không tìm thấy hai định lượng này trong văn bản DOCX gốc đã trích. Chưa coi đó là quy định bắt buộc, cần xác nhận giảng viên. Không sửa tài liệu môn học ngoài phạm vi PoC.

## 2. Phát hiện và xử lý
| Vị trí bản gốc | Mức độ | Vấn đề / tác động | Đã xử lý |
|---|---|---|---|
| train_model.py / phân phối giờ | Chặn chạy | Tổng xác suất không bằng 1, generator lỗi | Chuẩn hóa tổng trọng số; test tái lập |
| app.py / KPI, benchmark, độ trễ | Nghiêm trọng | Số ghi cứng dễ bị hiểu là thực nghiệm hoặc số liệu MB | KPI theo phiên, metrics từ test, latency đo inference |
| app.py / XAI | Nghiêm trọng | Điểm heuristic bị gọi là đóng góp mô hình | Dùng pred_contribs của booster; test tính cộng đóng góp |
| app.py / SOC feed | Cao | Trạng thái và điểm dựng độc lập, có thể mâu thuẫn | Dùng chung risk_engine với simulator |
| train_model.py / đánh giá | Cao | Thiếu validation, baseline, lưu kết quả | Chia 60/20/20, chọn ngưỡng trên validation, xuất metrics/CSV |
| app.py / khởi tạo | Cao | Tự train bộ khác với train_model.py | Chỉ nạp artifact, thiếu thì dừng rõ ràng |
| app.py / pháp lý, chặn tiền | Nghiêm trọng | Tuyên bố tuân thủ và hành động thật không có bằng chứng | Gỡ cam kết, chỉ đề xuất mô phỏng; không tự khóa tài khoản |
| feature new_beneficiary | Cao | Lẫn tuổi tài khoản, người nhận mới và tài khoản rác | Thống nhất người nhận chưa từng được người gửi chuyển trước giao dịch; 0=mới, 1=đã từng |
| hướng dẫn / notebook | Cao | Pipeline khác nhau, thiếu requirements, đường dẫn cứng | Đồng bộ source, bổ sung dependency, bỏ public tunnel mặc định |
| toàn bộ bộ nộp | Cao | Chưa có đầy đủ phân tích nghiệp vụ, nghiên cứu, khả thi và minh chứng | Bổ sung khung dưới đây; phần chưa có nguồn giữ là việc cần hoàn thiện |

## 3. Mục tiêu nghiệp vụ và phạm vi
### Vấn đề nghiên cứu, không phải kết luận về MB
Đề xuất khảo sát liệu chấm điểm học máy có hỗ trợ ưu tiên giao dịch cần kiểm tra, so với một bộ quy tắc đơn giản, trong điều kiện tỷ lệ nhãn gian lận thấp. Chưa có số liệu nội bộ để khẳng định MB thiếu năng lực này hoặc đang xử lý thủ công.

### Các bên liên quan
- Nhóm học viên: xây dựng và giải thích thực nghiệm.
- Giảng viên: đánh giá phương pháp, tính minh bạch và khả năng tái lập.
- Vai trò giả định cho giải pháp tương lai: chuyên viên chống gian lận, chủ quy trình thanh toán, vận hành CNTT, quản trị mô hình, an toàn thông tin/tuân thủ, khách hàng.
- Không mặc định SOC an ninh mạng và bộ phận chống gian lận là cùng một đơn vị tại MB.

### Trong phạm vi đã cài
Sinh dữ liệu tổng hợp → train/validation/test → so sánh baseline → chấm một giao dịch → giải thích → đề xuất hành động → lịch sử phiên/CSV.

### Ngoài phạm vi
Kết nối MB/NAPAS, xác nhận nhãn thực tế, Kafka, realtime streaming, eKYC/FaceID/FIDO2, chặn/giữ tiền thật, SMS, xác thực người dùng, phân quyền, audit bền vững, HA/DR, đánh giá tuân thủ và vận hành production.

### Mục tiêu nghiệm thu PoC trước buổi bảo vệ (chưa có ngày nộp)
1. Chạy cùng pipeline từ mã nguồn; đủ 25.000 mẫu, chia 15.000/5.000/5.000.
2. Có baseline, precision, recall, F1, AP, ROC-AUC, FPR, alert rate và confusion matrix từ holdout.
3. Điểm và hành động của giao dịch trong simulator nhất quán với lịch sử.
4. Không có KPI/latency/hiệu quả kinh tế bịa; mọi số tổng hợp được ghi rõ nguồn.
5. Test các ngưỡng, dữ liệu thiếu/không hợp lệ, UI không phát sinh exception trong happy path.
Không đặt mục tiêu Recall 95%/Precision 95% rồi ghi là đã đạt. Ngưỡng chất lượng triển khai thật phải do chủ quy trình thống nhất sau khảo sát.

## 4. Quy trình nghiệp vụ tham chiếu
### As-Is giả định để so sánh (cần phỏng vấn xác nhận)
Giao dịch → kiểm soát bắt buộc + quy tắc tĩnh → bình thường tiếp tục / cảnh báo chuyển chuyên viên → kết luận → lưu kết quả. Không gọi đây là mô tả hệ thống hiện tại của MB.

### To-Be đề xuất
Giao dịch → thu thập đặc trưng trước quyết định → kiểm tra hợp lệ → chấm điểm → kết hợp policy với kiểm soát bắt buộc → xử lý:
- Điểm thấp: tiếp tục kiểm soát thông thường, không tự bỏ qua xác thực.
- Điểm trung bình: đề xuất xác thực bổ sung; loại xác thực và xử lý thành công/thất bại cần chủ quy trình quyết định.
- Điểm cao: đề xuất tạm giữ/chuyển chuyên viên, không mặc định kết luận gian lận hoặc khóa toàn bộ tài khoản.
- Lỗi/chưa đủ dữ liệu: không trả kết quả “an toàn”; thông báo cần xử lý thủ công. Cơ chế timeout, hold/release và SLA chưa triển khai.
- Chuyên viên kết luận và phản hồi nhãn: đề xuất tương lai, chưa có chức năng case management.

Luồng đã cài chỉ đến đề xuất và nhật ký phiên. Không hiển thị “đã chặn” nếu chưa có hệ thống thi hành.

## 5. Yêu cầu và tiêu chí chấp nhận
| ID | Yêu cầu | Tiêu chí quan sát được | Trạng thái |
|---|---|---|---|
| FR01 | Kiểm tra 8 trường | Thiếu trường, NaN/Inf, ngoài miền bị từ chối | Đã cài/test |
| FR02 | Chấm điểm cùng mô hình | Model JSON, thứ tự FEATURES thống nhất | Đã cài/test |
| FR03 | Phân loại hành động | Dưới t1 thấp; t1 ≤ score < t2 trung bình; score ≥ t2 cao; không làm tròn trước quyết định | Đã cài/test |
| FR04 | Giải thích theo mô hình | Tổng đóng góp + bias khớp raw margin | Đã cài/test |
| FR05 | Lịch sử và xuất dữ liệu | Mỗi lần chấm thêm dòng có ID, UTC time, đầu vào, điểm, hành động, latency | Đã cài/test happy path |
| FR06 | Đánh giá tái lập | Metrics và prediction CSV được sinh từ pipeline, test không chọn ngưỡng | Đã cài |
| NFR01 | Không nhập dữ liệu thật | Banner phạm vi luôn hiển thị | Đã cài; chưa có DLP |
| NFR02 | Minh bạch hiệu năng | Chỉ đo inference; không cam kết SLA đầu-cuối | Đã cài |
| NFR03 | Thiếu artifact | App thông báo lỗi và dừng, không tự train/phê duyệt | Đã cài, chưa fault-injection UI tự động |
| NFR04 | Vận hành thật | Auth, RBAC, audit, idempotency, timeout, monitoring | Ngoài PoC |

### Hợp đồng dữ liệu
Xem `risk_engine.py:BOUNDS` và `train_model.py:FEATURES`.
- Amount VND: 20.000–500.000.000; hour: số nguyên 0–23.
- Channel: 0 Mobile, 1 Web, 2 Thẻ/POS, 3 Ví. Phân nhóm này là giả định minh họa; tín hiệu thiết bị/OTP chưa phù hợp đồng nhất mọi kênh. Hướng mở rộng ưu tiên thu hẹp chuyển tiền số hoặc xây mô hình riêng theo kênh.
- New device/location anomaly: 0/1, đầu vào giả lập, không có dịch vụ phát hiện thật.
- Failed attempts: 0–3, 3 đại diện từ 3 trở lên trong 30 phút.
- Frequency: 1–20, 20 đại diện mức cắt ngọn, tính cả giao dịch hiện tại trong cửa sổ 10 phút.
- New beneficiary: 0 mới đối với người gửi, 1 đã chuyển trước đó; không phản ánh tuổi tài khoản nhận và không suy ra tài khoản rác.
- Với dữ liệu thật, chỉ lấy feature biết được tại thời điểm chấm; nhãn kết luận phải được quản trị riêng để tránh rò rỉ thông tin tương lai.

## 6. Kết quả thực nghiệm của bản sửa
Theo `metrics.json`, seed 42, 5.000 mẫu test, 90 nhãn dương tổng hợp:
| Chỉ số | XGBoost, ngưỡng 0,63 | Baseline, ngưỡng 2/3 |
|---|---:|---:|
| ROC-AUC | 0,9828 | 0,8733 |
| Average precision (AP) | 0,5506 | 0,2323 |
| Precision | 34,39% | 78,26% |
| Recall | 72,22% | 20,00% |
| F1 | 0,4659 | 0,3186 |
| False positive rate | 2,53% | 0,10% |
| Tỷ lệ cần kiểm tra | 3,78% | 0,46% |

XGBoost: TP=65, FP=124, FN=25, TN=4.786. Nghĩa là 189 cảnh báo có 124 báo sai theo nhãn tổng hợp. Đây là lý do không được chuyển thẳng cảnh báo thành quyết định khóa tài khoản.

**Diễn giải cân bằng:** AI thu hồi nhiều nhãn dương hơn nhưng phát sinh thêm khối lượng xử lý; baseline có precision cao hơn ở ngưỡng hiện tại. Hai ngưỡng chưa được tối ưu theo cùng một mục tiêu/năng lực vận hành, nên chỉ là so sánh mô tả. Muốn kết luận ưu thế cần cùng ngân sách cảnh báo hoặc cost function, nhiều seed/fold và dữ liệu độc lập.

**Hạn chế bắt buộc ghi:** dữ liệu do chính nhóm sinh, nhãn theo quy tắc + nhiễu; không có phân phối/nhãn thật của MB; chưa hiệu chỉnh xác suất; chưa thử drift, OOD, thời gian, khách hàng trùng lặp; tỷ lệ 1,8% là giả định. AP không gọi là diện tích PR tính bằng phép hình thang. Không suy ra khoản tiền được bảo vệ hay ROI từ kết quả này.

## 7. Khả thi và giá trị dự kiến
- **Kỹ thuật:** pipeline local chạy được; khả thi tích hợp thật chưa kiểm chứng. Cần feature store, event schema, timeout/idempotency, monitoring drift, rollback model và phân quyền.
- **Kinh tế:** lập mô hình `lợi ích ròng = tổn thất tránh được đã xác minh − chi phí hạ tầng − nhân sự kiểm tra − tổn thất do báo sai/gián đoạn`. Chưa có dữ liệu để điền số tiền; không dùng tổng giá trị giao dịch cảnh báo làm tiền tiết kiệm.
- **Tổ chức:** cần người sở hữu policy, chuyên viên kết luận và cơ chế khiếu nại/mở lại giao dịch. Chưa có xác nhận cơ cấu MB.
- **Đổi mới:** đề xuất cải tiến quy trình bằng hỗ trợ ra quyết định. XGBoost không được trình bày như thuật toán mới do nhóm sáng tạo. Chưa đủ căn cứ khẳng định “đổi mới kiến trúc” theo Henderson–Clark hay gán tuyên bố cho giảng viên.
- **Pháp lý:** bản sửa không kết luận nội dung/hiệu lực văn bản pháp luật. Muốn đưa quy định vào báo cáo phải kiểm tra bản chính thức hiện hành theo ngày nộp và lập mapping kiểm soát; không đồng nhất eKYC, nhận diện khuôn mặt của thiết bị và xác thực giao dịch.

## 8. Đối chiếu bài tập lớn: còn gì trước khi nộp?
| Hạng mục đề | Hiện có trong PoC | Cần bổ sung bằng chứng |
|---|---|---|
| Công nghệ/bài toán/tổ chức | Đã định vị AI và bối cảnh nghiên cứu MB | Nguồn công khai/phỏng vấn chứng minh nhu cầu, không bịa hiện trạng |
| Lý thuyết | Pipeline XGBoost, mất cân bằng, giải thích | Viết cơ sở lý thuyết và trích dẫn học thuật |
| Tổng quan ứng dụng | Chưa có tổng quan đủ nguồn | Nghiên cứu trường hợp thành công/thất bại có nguồn, so sánh và bài học |
| Phân tích yêu cầu | Có scope, actor, FR/NFR, luồng tham chiếu | Xác nhận As-Is, root cause, mức ảnh hưởng |
| Thiết kế | Có kiến trúc thực thi và đề xuất tách biệt | Vẽ BPMN/kiến trúc chính thức, làm rõ failure/timeout |
| Cài đặt/thực nghiệm | Code, model, metrics, notebook, test | Chụp ảnh/video demo; Colab cần chạy trên tài khoản thật |
| Đánh giá/kiến nghị | Có baseline, hạn chế, lộ trình | Thử dữ liệu độc lập, tính cost theo giả định công khai |
| Làm việc nhóm | Chưa có tên/thành viên | Điền đóng góp thực tế, không tự gán |
| Báo cáo/slide | Chưa có bản hoàn chỉnh trong thư mục này | Biên soạn, kiểm nguồn, đóng gói theo hướng dẫn giảng viên |

### Khung báo cáo nên dùng
1. Giới thiệu và phát biểu bài toán; nguồn chứng minh, câu hỏi nghiên cứu, phạm vi.
2. Cơ sở lý thuyết và tổng quan nghiên cứu/ứng dụng có trích dẫn.
3. Phân tích nghiệp vụ: stakeholder, As-Is tham chiếu/xác minh, root cause, mục tiêu, FR/NFR, To-Be.
4. Thiết kế và triển khai PoC: dữ liệu, nhãn, feature, split, model, policy, UI, ngoại lệ.
5. Thực nghiệm: môi trường, kịch bản, baseline, kết quả, trade-off, giới hạn.
6. Khả thi kỹ thuật/kinh tế/tổ chức; rủi ro, kiến nghị, lộ trình.
7. Kết luận, đóng góp cá nhân, tài liệu tham khảo và phụ lục minh chứng.

### Các quyết định cần nhóm xác nhận
- Tên đề tài đã được giảng viên duyệt chưa? Có bắt buộc chứng minh streaming không?
- Có nguồn MB được phép dùng hay chỉ bối cảnh đề xuất? Có thể dùng bộ dữ liệu công khai độc lập không?
- Ngày nộp, dung lượng báo cáo/slide, tên và đóng góp thành viên?
- Nếu chưa có dữ liệu thật, giảng viên có chấp nhận PoC tổng hợp với giới hạn công bố rõ không?

## 9. Kiểm chứng kỹ thuật và tham khảo
- Chạy pipeline local thành công; 18 test pass gồm AppTest thao tác gửi giao dịch và thêm batch, validation biên, tính cộng TreeSHAP.
- AppTest là mô phỏng ứng dụng, không thay cho kiểm tra trực quan trên trình duyệt thật hoặc chạy runtime Colab.
- Notebook đã đồng bộ source; chưa xác minh proxy Colab trên tài khoản người dùng.
- Tài liệu chính thức đã đối chiếu: scikit-learn “Tuning the decision threshold for class prediction”; XGBoost “Python API Reference” mục pred_contribs; Streamlit “AppTest”; mã nguồn googlecolab/colabtools output/_util.py.
- Không coi bản sửa này là báo cáo hoàn chỉnh hoặc xác nhận của giảng viên.
