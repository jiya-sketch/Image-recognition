# 🖼️ Image Detection using Deep Learning

A Streamlit-based Image Detection application that identifies objects in uploaded images using a pre-trained **MobileNetV2** deep learning model. The model is trained on the **ImageNet** dataset and can recognize over **1,000 object categories**.

---

## 📌 Project Overview

This project demonstrates how **Computer Vision** and **Deep Learning** can be used to classify objects from images. Instead of training a model from scratch, it uses **Transfer Learning** with MobileNetV2, enabling accurate predictions while reducing computational requirements.

---

## ✨ Features

- 📤 Upload JPG, JPEG, or PNG images
- 🧠 Object recognition using MobileNetV2
- 📊 Displays the predicted object
- 📈 Shows prediction confidence
- 🏆 Displays Top-5 predictions
- ⚡ Fast inference using TensorFlow
- 🎨 Interactive Streamlit interface

---

## 🛠️ Technologies Used

- Python
- Streamlit
- TensorFlow / Keras
- MobileNetV2
- NumPy
- Pillow

---

## 📂 Project Structure

```text
Image-Detection/
│
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

## 🔄 Project Workflow

```text
Upload Image
      │
      ▼
Image Preprocessing
      │
      ▼
MobileNetV2 Model
      │
      ▼
Object Prediction
      │
      ▼
Display Results
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/image-detection.git
cd image-detection
```

### Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 🌐 Live Demo

**Local Development**

```
http://localhost:8501
```

**Public Deployment**

Replace this section with your deployed Streamlit URL after publishing the app.

---

## 📷 Supported Image Formats

- JPG
- JPEG
- PNG

---

## 🧠 Model Information

- **Model:** MobileNetV2
- **Dataset:** ImageNet
- **Classes:** 1000+
- **Framework:** TensorFlow/Keras

---

## 📊 Example Output

- Detected Object
- Confidence Score
- Top-5 Predictions

---

## 📌 Future Improvements

- Webcam-based object detection
- Real-time video detection
- Multiple object detection
- Custom model training
- Bounding box visualization
- Detection history

---

## 👩‍💻 Author

**Jiya Gupta**

B.Tech CSE (Data Science)

---

## 📄 License

This project is intended for educational and learning purposes.
