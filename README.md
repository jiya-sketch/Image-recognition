# 🧠 VisionAI — Intelligent Image Recognition System

<div align="center">

### *Transforming Pixels into Intelligent Predictions*

An AI-powered Image Recognition web application built using **Python**, **TensorFlow**, **MobileNetV2**, and **Streamlit** that identifies objects from uploaded images with high accuracy using **Transfer Learning**.

<br>

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow">
<img src="https://img.shields.io/badge/Streamlit-Web%20Application-FF4B4B?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv">
<img src="https://img.shields.io/badge/ImageNet-1000%2B%20Classes-success?style=for-the-badge">

</div>

---

# 📖 Overview

Image recognition is one of the most impactful applications of Artificial Intelligence and Computer Vision. Instead of relying on handcrafted rules for every possible object, modern deep learning models learn visual patterns directly from millions of labeled images.

**VisionAI** leverages **Transfer Learning** through the **MobileNetV2** architecture, enabling accurate object recognition while remaining computationally efficient. Rather than training a neural network from scratch, the project utilizes a model pre-trained on the **ImageNet** dataset containing over **one million images** across **1,000+ object categories**.

The application allows users to upload an image, automatically preprocesses it, performs inference using the neural network, and presents the predicted object along with confidence scores through an intuitive Streamlit interface.

---

# 🎯 Objectives

- Build an intelligent image recognition system.
- Demonstrate the practical application of Transfer Learning.
- Perform accurate object classification using a pre-trained neural network.
- Create an interactive web application for real-time image inference.
- Showcase an end-to-end Deep Learning deployment workflow.

---

# ✨ Features

- 📤 Upload JPG, JPEG, and PNG images
- 🧠 Deep Learning–based object recognition
- 🚀 MobileNetV2 pre-trained on ImageNet
- 📊 Confidence score for predictions
- 🏆 Top-5 predicted classes
- ⚡ Fast inference
- 💻 Interactive Streamlit interface
- 📱 Responsive user experience

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Deep Learning | TensorFlow / Keras |
| Neural Network | MobileNetV2 |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Image Processing | Pillow |
| Numerical Computing | NumPy |

---

# 🏗️ System Architecture

```text
                    User Uploads Image
                            │
                            ▼
                 Image Preprocessing
                            │
                            ▼
              Resize to 224 × 224 Pixels
                            │
                            ▼
          MobileNetV2 Feature Extraction
                            │
                            ▼
              Deep Learning Inference
                            │
                            ▼
              Softmax Probability Scores
                            │
                            ▼
               Top-5 Object Predictions
                            │
                            ▼
              Interactive Streamlit UI
```

---

# 🔄 Project Workflow

```text
Upload Image
      │
      ▼
Resize & Normalize
      │
      ▼
Feature Extraction
      │
      ▼
Deep Neural Network
      │
      ▼
Probability Distribution
      │
      ▼
Object Classification
      │
      ▼
Prediction Display
```

---

# 📂 Project Structure

```text
VisionAI/
│
├── app.py
├── requirements.txt
├── runtime.txt
├── README.md
│
├── assets/
│
├── models/
│
└── images/
```

---

# 🧠 Deep Learning Model

**Model Name**

MobileNetV2

**Framework**

TensorFlow / Keras

**Training Dataset**

ImageNet

**Number of Classes**

1000+

**Learning Strategy**

Transfer Learning

---

# ⚙️ How It Works

### Step 1 — Image Upload

The user uploads an image through the Streamlit interface.

↓

### Step 2 — Image Preprocessing

The uploaded image is resized to **224 × 224 pixels**, converted into numerical tensors, and normalized according to MobileNetV2 preprocessing requirements.

↓

### Step 3 — Feature Extraction

The pre-trained MobileNetV2 network extracts high-level visual features such as shapes, textures, edges, and object structures.

↓

### Step 4 — Prediction

The neural network computes probability scores for over **1,000 ImageNet object categories**.

↓

### Step 5 — Results

The application displays:

- Predicted object
- Confidence score
- Top-5 predictions

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/VisionAI.git
```

Move into the project directory

```bash
cd VisionAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

# 📊 Expected Output

The application displays:

- Uploaded Image
- Predicted Object
- Prediction Confidence
- Top-5 Predictions

---

# 📸 Supported Formats

- JPG
- JPEG
- PNG

---

# 🌍 Real-World Applications

- Autonomous Vehicles
- Medical Image Analysis
- Retail Product Recognition
- Smart Surveillance
- Wildlife Monitoring
- Manufacturing Quality Inspection
- Agricultural Crop Analysis
- Inventory Management
- Robotics
- E-commerce Image Classification

---

# 📈 Skills Demonstrated

- Deep Learning
- Transfer Learning
- Computer Vision
- Image Classification
- TensorFlow
- Neural Networks
- Streamlit Deployment
- Python Development
- AI Application Design
- Git & GitHub

---

# 🔮 Future Enhancements

- 📹 Real-Time Webcam Recognition
- 🎥 Video Object Detection
- 🌐 Cloud Deployment
- 📱 Mobile Integration
- 🎯 Custom Dataset Training
- 📊 Prediction Analytics Dashboard
- 🔍 Object Localization with Bounding Boxes
- 🤖 Multi-Object Recognition

---

# 👩‍💻 Developer

**Jiya Gupta**

**B.Tech – Computer Science & Engineering (Data Science)**

Passionate about Artificial Intelligence, Deep Learning, Computer Vision, and Data Science.

---

# 📄 License

This project is intended for educational and learning purposes.

---

<div align="center">

### ⭐ If you found this project interesting, consider giving it a star!

*"Teaching machines to see the world, one image at a time."*

</div>
