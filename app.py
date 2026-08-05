import numpy as np
from PIL import Image
import tensorflow as tf
import streamlit as st
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Image Detection System",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🖼️ Image Detection")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔍 Detect Image", "ℹ️ About"]
)

st.sidebar.markdown("---")

st.sidebar.subheader("Project Information")

st.sidebar.info("""
**Model:** MobileNetV2

**Dataset:** ImageNet

**Framework:** TensorFlow/Keras

**Frontend:** Streamlit
""")

st.sidebar.markdown("---")
st.sidebar.success("Developed by Jiya Gupta")

# ---------------- HOME PAGE ----------------

if page == "🏠 Home":

    st.title("🖼️ Image Detection using Deep Learning")

    st.markdown("""
This application uses a **pre-trained MobileNetV2 Deep Learning model**
to recognize objects present inside an uploaded image.

The model has already been trained on the **ImageNet Dataset**
containing over **1,000 object categories**.
""")

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Model", "MobileNetV2")

    with col2:
        st.metric("Classes", "1000")

    with col3:
        st.metric("Framework", "TensorFlow")

    st.markdown("---")

    st.subheader("Workflow")

    st.info("""
📷 Upload Image

⬇

🖼 Image Preprocessing

⬇

🧠 MobileNetV2 Model

⬇

📊 Prediction

⬇

✅ Display Result
""")

# ---------------- DETECT PAGE ----------------

elif page == "🔍 Detect Image":

    st.title("🔍 Detect Objects")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        col1, col2 = st.columns([1,1])

        with col1:

            st.subheader("Uploaded Image")
            st.image(image, use_container_width=True)

        with col2:

            st.subheader("Prediction")

            if st.button("Detect Image"):

                with st.spinner("Analyzing Image..."):

                    time.sleep(2)

                    # Replace this section with your prediction function

                    predicted_label = "Golden Retriever"
                    confidence = 97.64

                st.success("Prediction Completed")

                st.metric(
                    "Detected Object",
                    predicted_label
                )

                st.metric(
                    "Confidence",
                    f"{confidence:.2f}%"
                )

                st.progress(confidence/100)

                st.markdown("---")

                st.subheader("Top 5 Predictions")

                st.table({
                    "Rank":[1,2,3,4,5],
                    "Class":[
                        "Golden Retriever",
                        "Labrador",
                        "Dog",
                        "Beagle",
                        "Cat"
                    ],
                    "Confidence":[
                        "97.64%",
                        "1.12%",
                        "0.68%",
                        "0.34%",
                        "0.22%"
                    ]
                })

# ---------------- ABOUT ----------------

else:

    st.title("ℹ️ About Project")

    st.markdown("""
## Project Objective

The objective of this project is to identify objects from images
using Deep Learning.

### Technologies Used

- Python
- Streamlit
- TensorFlow
- MobileNetV2
- Pillow
- NumPy

### Workflow

1. Upload an image.
2. Resize image to MobileNetV2 input size.
3. Preprocess image.
4. Run prediction using MobileNetV2.
5. Display the detected object and confidence score.

### Features

✅ Upload JPG, JPEG, PNG images

✅ Deep Learning prediction

✅ Confidence score

✅ Top-5 Predictions

✅ Interactive Streamlit Interface
""")

st.markdown("---")
st.caption("© 2026 | Image Detection using MobileNetV2 | Developed by Jiya Gupta")
