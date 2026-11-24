# Dự đoán lương ngành IT tại Anh

Dự án hướng tới xây dựng mô hình dự đoán lương cho các vị trí IT tại Vương quốc Anh. Mục tiêu thu thập ít nhất 1.000 dòng dữ liệu thô.

## Cấu trúc dự án

- `data/raw/` lưu dữ liệu gốc, `data/processed/` lưu dữ liệu đã làm sạch và `data/collection/` lưu script hoặc tài liệu thu thập dữ liệu.
- `notebooks/` chứa notebook phân tích dữ liệu và thử nghiệm mô hình.
- `backend/` chứa ứng dụng FastAPI và schema Pydantic. Đặt tệp mô hình đã huấn luyện trong `backend/model/`.
- `frontend/` chứa giao diện Streamlit.
- `report/` và `presentation/` lần lượt chứa báo cáo và slide.

## Phân công thành viên

Cập nhật tên thành viên theo phân công của nhóm.

| Hạng mục | Thành viên |
| --- | --- |
| Thu thập và tiền xử lý dữ liệu | Chưa phân công |
| Phân tích và huấn luyện mô hình | Chưa phân công |
| Backend và frontend | Chưa phân công |
| Báo cáo và thuyết trình | Chưa phân công |

## Chạy hệ thống

Từ thư mục gốc của dự án, cài thư viện.

```powershell
python -m pip install fastapi pydantic uvicorn -r frontend/requirements.txt
```

Khởi động backend.

```powershell
python -m uvicorn backend.main:app --reload
```

Mở terminal thứ hai và chạy frontend.

```powershell
python -m streamlit run frontend/app.py
```

API mặc định chạy tại `http://127.0.0.1:8000`. Dùng `GET /health` để kiểm tra dịch vụ và mở `/docs` để xem tài liệu API. `POST /predict` hiện kiểm tra trường `job_title` và trả HTTP 503 với yêu cầu hợp lệ cho đến khi tích hợp mô hình. Có thể đặt biến môi trường `SALARY_API_URL` để giao diện gọi một địa chỉ API khác.
