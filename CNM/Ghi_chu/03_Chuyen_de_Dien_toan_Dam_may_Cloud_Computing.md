# Chuyên đề 03: Điện toán Đám mây (Cloud Computing) Toàn tập
**Học phần:** Công nghệ Mới nổi và Đổi mới (CNM / MIS01)  
**Học viện Ngân hàng (Banking Academy of Vietnam - HVNH)**  
**Giảng viên:** TS. Đinh Trọng Hiếu

---

## 1. Định nghĩa & 5 Đặc tính Cốt lõi theo Chuẩn NIST

Điện toán đám mây là mô hình cho phép truy cập qua mạng thuận tiện, theo yêu cầu tới một nhóm tài nguyên điện toán dùng chung có thể cấu hình được (ví dụ: mạng, máy chủ, lưu trữ, ứng dụng và dịch vụ) mà có thể được cung cấp và giải phóng nhanh chóng với nỗ lực quản lý tối thiểu hoặc sự tương tác tối thiểu với nhà cung cấp dịch vụ.

5 đặc tính bắt buộc theo NIST:
1. **Tự phục vụ theo nhu cầu (On-demand Self-service):** Người dùng có thể tự động cấp phát tài nguyên điện toán (như thời gian máy chủ, dung lượng lưu trữ) khi cần mà không cần tương tác thủ công với con người tại nhà cung cấp.
2. **Truy cập mạng rộng rãi (Broad Network Access):** Tài nguyên có sẵn qua mạng và được truy cập thông qua các cơ chế tiêu chuẩn hỗ trợ đa nền tảng (điện thoại di động, máy tính bảng, máy tính xách tay).
3. **Dùng chung tài nguyên (Resource Pooling):** Tài nguyên điện toán của nhà cung cấp được gom lại để phục vụ nhiều người dùng (Multi-tenant), được phân bổ động theo nhu cầu. Khách hàng thường không biết chính xác vị trí vật lý của tài nguyên (Location Independence).
4. **Co giãn nhanh chóng (Rapid Elasticity):** Tài nguyên có thể được cung cấp và giải phóng co giãn linh hoạt (Scale-up / Scale-down, Scale-out / Scale-in), mang lại cảm giác tài nguyên là vô hạn đối với người dùng.
5. **Dịch vụ được đo lường (Measured Service):** Hệ thống đám mây tự động kiểm soát và tối ưu hóa việc sử dụng tài nguyên bằng cách tận dụng khả năng đo lường (Metering) ở mức độ chi tiết phù hợp với loại dịch vụ (dung lượng lưu trữ, băng thông, số yêu cầu xử lý, tài khoản người dùng hoạt động). Chi phí chi trả dựa trên mức độ sử dụng thực tế (Pay-as-you-go).

---

## 2. Các Mô hình Dịch vụ (Cloud Service Models)

```
+---------------------------------------------------------------+
|                      MÔ HÌNH TRÁCH NHIỆM CHIA SẺ               |
+----------------------+--------------------+-------------------+
|     IaaS             |       PaaS         |       SaaS        |
| (Infrastructure)     |    (Platform)      |    (Software)     |
+----------------------+--------------------+-------------------+
| [Khách hàng quản lý]:| [Khách quản lý]:   | [Nhà cung cấp     |
| - Ứng dụng (App)     | - Ứng dụng (App)   |  quản lý TOÀN BỘ]:|
| - Dữ liệu (Data)     | - Dữ liệu (Data)   | - Ứng dụng        |
| - Môi trường runtime |                    | - Dữ liệu         |
| - Middleware         | [Nhà CC quản lý]:  | - Runtime         |
| - Hệ điều hành (OS)  | - Runtime          | - Middleware      |
|                      | - Middleware       | - Hệ điều hành    |
| [Nhà CC quản lý]:    | - Hệ điều hành     | - Ảo hóa          |
| - Ảo hóa             | - Ảo hóa           | - Máy chủ         |
| - Máy chủ vật lý     | - Máy chủ vật lý   | - Lưu trữ         |
| - Lưu trữ (Storage)  | - Lưu trữ          | - Mạng kết nối    |
| - Mạng (Networking)  | - Mạng kết nối     |                   |
+----------------------+--------------------+-------------------+
```

* **IaaS (Hạ tầng như một dịch vụ):** AWS EC2, Google Compute Engine, Microsoft Azure VMs.
* **PaaS (Nền tảng như một dịch vụ):** AWS Elastic Beanstalk, Google App Engine, Heroku.
* **SaaS (Phần mềm như một dịch vụ):** Microsoft 365, Google Workspace, Salesforce, Zoom.

---

## 3. Các Mô hình Triển khai (Deployment Models)

1. **Đám mây Công cộng (Public Cloud):** Hạ tầng thuộc sở hữu của bên thứ ba (AWS, Microsoft, Google), chia sẻ tài nguyên giữa nhiều tổ chức. Ưu điểm: Chi phí ban đầu bằng 0, không cần bảo trì hạ tầng, khả năng mở rộng vô hạn.
2. **Đám mây Riêng (Private Cloud):** Hạ tầng dành riêng duy nhất cho một tổ chức, có thể đặt tại trung tâm dữ liệu nội bộ (On-premise) hoặc do bên thứ ba lưu trữ. Ưu điểm: Kiểm soát tối đa, bảo mật tuyệt đối, đáp ứng yêu cầu tuân thủ nghiêm ngặt của ngành Ngân hàng.
3. **Đám mây Lai (Hybrid Cloud):** Kết hợp giữa Public Cloud và Private Cloud, kết nối với nhau qua mạng riêng ảo an toàn (VPN/Direct Connect). Đây là **mô hình tối ưu nhất cho các Ngân hàng thương mại Việt Nam**:
   - Dữ liệu Core Banking cốt lõi và thông tin tài khoản mật lưu tại Private Cloud để tuân thủ Thông tư 09/2020/TT-NHNN.
   - Các cổng giao tiếp khách hàng, ứng dụng Mobile Banking mở rộng và phân tích dữ liệu lớn triển khai linh hoạt trên Public Cloud để đáp ứng lưu lượng truy cập đột biến.
4. **Đám mây Cộng đồng (Community Cloud):** Chia sẻ hạ tầng giữa các tổ chức có cùng mục đích hoặc yêu cầu tuân thủ (ví dụ: Đám mây liên ngân hàng cho cổng thanh toán quốc gia Napas).

---

## 4. Công nghệ Nền tảng: Ảo hóa, Container & Serverless

### 4.1. Ảo hóa (Virtualization) & Hypervisor
* **Ảo hóa:** Kỹ thuật tạo ra phiên bản ảo của tài nguyên điện toán (phần cứng, máy chủ, lưu trữ, mạng) trên một hạ tầng vật lý duy nhất.
* **Hypervisor Type 1 (Bare-metal):** Chạy trực tiếp trên phần cứng máy chủ vật lý mà không cần hệ điều hành máy chủ (Ví dụ: VMware ESXi, Microsoft Hyper-V, KVM, Xen). Đạt hiệu năng cao, chuyên dùng trong trung tâm dữ liệu doanh nghiệp.
* **Hypervisor Type 2 (Hosted):** Chạy dưới dạng một phần mềm trên hệ điều hành máy chủ chủ quản (Ví dụ: VMware Workstation, Oracle VirtualBox). Chủ yếu dùng cho môi trường phát triển và thử nghiệm cá nhân.

### 4.2. Container (Docker) vs. Máy ảo (Virtual Machine)

| Tiêu chí | Máy ảo (Virtual Machine - VM) | Container (Docker) |
| :--- | :--- | :--- |
| **Mức độ trừu tượng** | Ảo hóa ở tầng Phần cứng (Hardware-level) | Ảo hóa ở tầng Hệ điều hành (OS-level) |
| **Hệ điều hành khách** | Bắt buộc phải có Guest OS riêng (chiếm nhiều GB) | Chia sẻ chung Nhân hệ điều hành máy chủ (Host Kernel) |
| **Thời gian khởi động** | Vài phút | Vài phần trăm giây (mili-giây) |
| **Tiêu tốn tài nguyên** | Nặng, cố định mức RAM và vCPU cấp phát | Siêu nhẹ, chỉ cấp phát dung lượng thực tế ứng dụng dùng |
| **Khả năng đóng gói** | Khó di chuyển giữa các hạ tầng khác nhau | Tính khả chuyển tối đa (Build Once, Run Anywhere) |

### 4.3. Điều phối Container với Kubernetes (K8s) & Microservices
* **Kiến trúc Microservices:** Chia nhỏ ứng dụng cồng kềnh (Monolith) thành tập hợp các dịch vụ nhỏ, độc lập, giao tiếp qua API (RESTful hoặc gRPC). Mỗi dịch vụ có thể triển khai, nâng cấp và mở rộng quy mô độc lập.
* **Kubernetes (K8s):** Nền tảng mã nguồn mở hàng đầu thế giới để tự động hóa việc triển khai, mở rộng quy mô và quản lý các ứng dụng container hóa:
  - **Tự động phục hồi (Self-healing):** Tự khởi động lại container bị lỗi, thay thế và chấm dứt container không phản hồi.
  - **Cân bằng tải & Khám phá dịch vụ (Service Discovery & Load Balancing).**
  - **Tự động co giãn theo chiều ngang (Horizontal Pod Autoscaling - HPA):** Tự động tăng số lượng bản sao (Pods) khi tải CPU/RAM tăng cao.

### 4.4. Điện toán Phi máy chủ (Serverless Computing / FaaS)
* Không có nghĩa là không có máy chủ, mà lập trình viên **hoàn toàn không cần bận tâm về việc quản lý máy chủ**.
* Chỉ cần tải mã nguồn lên (Function as a Service: AWS Lambda, Azure Functions, GCP Cloud Functions).
* Đám mây tự động kích hoạt thực thi khi có sự kiện (Event-driven) và tự tắt khi kết thúc; chi phí tính chính xác đến từng 1 mili-giây. Zero Idle Cost (khi không có giao dịch thì chi phí bằng 0).

---

## 5. Dữ liệu Lớn (Big Data) trên Đám mây & Bảo mật Ngân hàng

### 5.1. Xử lý Dữ liệu Lớn: Hadoop vs. Spark
* **Apache Hadoop:** Kiến trúc phân tán dựa trên đĩa từ:
  - **HDFS (Hadoop Distributed File System):** Hệ thống tệp phân tán lưu trữ dữ liệu trên nhiều nút máy chủ.
  - **MapReduce:** Mô hình lập trình xử lý dữ liệu song song qua 2 pha Map (ánh xạ) và Reduce (tổng hợp).
* **Apache Spark:** Đột phá xử lý dữ liệu trong bộ nhớ RAM (**In-memory Computing**), cho tốc độ xử lý nhanh gấp 100 lần Hadoop MapReduce, đặc biệt phù hợp cho các thuật toán Machine Learning và phân tích luồng dữ liệu thời gian thực.

### 5.2. Tiêu chuẩn An toàn & Bảo mật Đám mây trong Ngân hàng
* **Khung pháp lý Việt Nam:** Tuân thủ **Thông tư 09/2020/TT-NHNN** quy định về an toàn hệ thống thông tin trong hoạt động ngân hàng; **Nghị định 13/2023/NĐ-CP** về bảo vệ dữ liệu cá nhân.
* **Tiêu chuẩn quốc tế:**
  - **PCI-DSS (Payment Card Industry Data Security Standard):** Tiêu chuẩn bảo mật dữ liệu thẻ thanh toán.
  - **ISO/IEC 27001:** Hệ thống quản trị an toàn thông tin.
  - **SOC 2 Type II:** Đánh giá độc lập về kiểm soát bảo mật, tính sẵn sàng và tính bảo mật dữ liệu của nhà cung cấp đám mây.
