import streamlit as st
from PIL import Image
import io

st.title("🗜️ Simple Image Compressor")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Original Image", use_column_width=True)

    st.subheader("Resize Options")
    width = st.number_input("Width", value=img.width, step=1)
    height = st.number_input("Height", value=img.height, step=1)

    st.subheader("Compression Quality")
    quality = st.slider("Select JPEG Quality (lower = more compression)", 1, 100, 75)

    if st.button("Compress"):
        resized_img = img.resize((int(width), int(height)))

        buffer = io.BytesIO()
        if resized_img.mode in ("RGBA", "P"):
            resized_img = resized_img.convert("RGB")

        resized_img.save(buffer, format="JPEG", quality=quality, optimize=True)
        buffer.seek(0)

        st.success("Image compressed successfully!")
        st.download_button(
            label="📥 Download Compressed Image",
            data=buffer,
            file_name="compressed.jpg",
            mime="image/jpeg"
        )
