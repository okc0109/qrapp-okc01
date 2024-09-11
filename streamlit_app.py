import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

# 앱 제목
st.title("QR Code Generator")

# 입력 받을 텍스트
text = st.text_input("Enter text or URL for QR Code:")

# QR 코드 생성 버튼
if st.button("Generate QR Code"):
    if text:
        # QR 코드 생성
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        # 이미지를 생성하고 표시
        img = qr.make_image(fill="black", back_color="white")
        img = img.convert("RGB")

        # 이미지를 Streamlit에서 표시하기 위해 BytesIO 사용
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        st.image(buffer.getvalue())

        # 이미지 다운로드 버튼 추가
        st.download_button(
            label="Download QR Code",
            data=buffer,
            file_name="qr_code.png",
            mime="image/png"
        )
    else:
        st.warning("Please enter a text or URL.")
