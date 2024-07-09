import pytesseract as pt
from PIL import Image
import re
import streamlit as st
import io
import cv2
import numpy as np
TESSDATA_PREFIX = r'C:\Program Files\Tesseract-OCR'
st.set_page_config(page_title="PyTesseract", page_icon='favicon.png',menu_items=None,)
st.title("PyTesseract")
st.write('请上传图片')
image_uploader = st.file_uploader("上传图片", type=['png', 'jpg', 'jpeg'])
submit_picture = st.button("提交")
while submit_picture:
    if image_uploader is not None:
        byte_data = image_uploader.read()
        image_stream = io.BytesIO(byte_data)
        image = Image.open(image_stream)
        st.write("识别中")
        text = re.sub(r' ', '', pt.image_to_string(image, lang='chi_sim'))
        st.write('识别成功')
        st.subheader("识别结果：")
        st.write(text)
        break
    else:
        st.write("请上传图片!")
        continue
