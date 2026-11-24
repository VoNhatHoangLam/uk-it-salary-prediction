# Dự đoán lương ngành IT tại Anh

Dự án hướng tới xây dựng mô hình dự đoán lương cho các vị trí IT tại Vương quốc Anh. Mục tiêu thu thập ít nhất 1.000 dòng dữ liệu thô.

## Cấu trúc dự án

- `data/raw/` lưu dữ liệu gốc, `data/processed/` lưu dữ liệu đã làm sạch và `data/collection/` lưu script hoặc tài liệu thu thập dữ liệu.
- `notebooks/` chứa notebook phân tích dữ liệu và thử nghiệm mô hình.
- `backend/` chứa ứng dụng FastAPI và schema Pydantic. Đặt tệp mô hình đã huấn luyện trong `backend/model/`.
- `frontend/` chứa giao diện Streamlit.
- `report/` và `presentation/` lần lượt chứa báo cáo và slide.

