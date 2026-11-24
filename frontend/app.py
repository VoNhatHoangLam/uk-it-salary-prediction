import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import streamlit as st


api_url = os.getenv("SALARY_API_URL", "http://127.0.0.1:8000").rstrip("/")

st.title("Dự đoán lương ngành IT tại Anh")

with st.form("salary_prediction"):
    job_title = st.text_input("Chức danh công việc")
    submitted = st.form_submit_button("Dự đoán")

if submitted:
    if not job_title.strip():
        st.warning("Hãy nhập chức danh công việc.")
    else:
        request = Request(
            f"{api_url}/predict",
            data=json.dumps({"job_title": job_title.strip()}).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urlopen(request, timeout=10) as response:
                st.json(json.load(response))
        except HTTPError as error:
            if error.code == 503:
                st.info("Mô hình dự đoán chưa sẵn sàng.")
            else:
                st.error(f"API trả về lỗi HTTP {error.code}.")
        except (URLError, TimeoutError):
            st.error("Không thể kết nối tới API dự đoán.")
