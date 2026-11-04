# App điều khiển Hub (bản thử nghiệm)

App Android bọc trang điều khiển Bluetooth. Có tự nối lại hub và tự cập nhật giao diện khi có tính năng mới.

## A. Cài lần đầu (chỉ làm một lần)

1. Tạo tài khoản GitHub (miễn phí), tạo kho mới tên ví dụ `hub-app`, chọn **Public**.
   (Kho Public thì app mới tải được bản cập nhật. Trong kho không có mã PIN nào, PIN chỉ nằm trong hub và điện thoại của bạn.)
2. Tải **toàn bộ nội dung** thư mục này lên kho (nút *Add file → Upload files*, kéo thả cả thư mục `www`, `scripts`, `.github` và các file lẻ).
   Nếu thư mục `.github` không lên được, bấm *Add file → Create new file*, gõ tên `.github/workflows/build-apk.yml` rồi dán nội dung file đó vào.
3. Vào tab **Actions** → chọn **Build APK** → **Run workflow**. Đợi 5-10 phút cho đến khi có dấu xanh.
4. Vào mục **Releases** (cột bên phải trang kho) → tải `hub-control.apk` về điện thoại → mở file để cài (Android sẽ hỏi cho phép cài từ nguồn ngoài, chọn cho phép).
5. Mở app → cho phép Bluetooth/Thiết bị ở gần → bấm **Kết nối** → chọn `DongHo-ESP32`. Từ lần sau app tự nối.
6. Vào tab **Cài đặt**: nhập mã PIN, và nhập tên kho vào ô *Kho GitHub* (ví dụ `tenban/hub-app`) rồi bấm **Kiểm tra cập nhật**.

Nếu bước 3 báo lỗi đỏ: mở lần chạy đó, chép dòng lỗi gửi cho tôi.

## B. Khi có tính năng mới

- **Chỉ đổi giao diện/tính năng trang** (hầu hết trường hợp): tôi gửi `app.html` mới. Bạn vào kho → thư mục `www` → bấm `app.html` → biểu tượng bút chì (hoặc *Upload files* ghi đè) → dán/ghi đè → *Commit*. Mở app, nó tự tải bản mới (hoặc vào Cài đặt → Kiểm tra cập nhật) rồi bấm **Áp dụng giao diện mới**. Không cần cài lại APK.
- **Đổi phần vỏ app** (thêm quyền, thêm plugin): tôi sửa `package.json`/script, bạn upload, GitHub tự build APK mới. App sẽ báo **Tải APK mới** trong Cài đặt, bấm tải và cài đè (không mất dữ liệu vì dùng cùng khóa ký).

## C. Gỡ lỗi

- Giao diện tải thêm bị lỗi 2 lần liền sẽ tự bỏ và quay về bản gốc trong app. Hoặc: Cài đặt → **Về giao diện gốc của app**.
- Muốn đổi sang hub khác: Cài đặt → **Chọn lại hub**.
- File `hub-release.keystore` là khóa ký APK. Giữ nguyên, đừng xóa, nếu không cài đè bản mới sẽ bị Android từ chối.
