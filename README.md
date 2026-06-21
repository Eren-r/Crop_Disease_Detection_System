# 🌱 AI-Powered Crop Disease Detection System

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-red)
![Computer Vision](https://img.shields.io/badge/Computer-Vision-green)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-teal)
![Agriculture AI](https://img.shields.io/badge/AI-Agriculture-success)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

## 🚀 Overview

An AI-powered crop disease detection system that automatically identifies crop types and diagnoses plant diseases from uploaded leaf images using Deep Learning and Computer Vision.

The system uses a multi-stage classification pipeline:

1. Detects the crop type (Potato or Tomato)
2. Loads the appropriate disease classification model
3. Predicts the disease condition
4. Returns disease information and treatment recommendations through a FastAPI REST API

This project demonstrates practical applications of Artificial Intelligence in Agriculture (AgriTech), helping farmers and agricultural professionals identify crop diseases quickly and accurately.

---

## 🎯 Problem Statement

Crop diseases significantly impact agricultural productivity and food security.

Traditional disease identification requires expert knowledge and can be time-consuming.

This system provides an AI-driven solution capable of:

* Automated crop identification
* Disease classification
* Fast diagnosis
* Knowledge-based recommendations
* API integration for mobile or web applications

---

## ✨ Features

### 🌿 Crop Classification

Supported Crops:

* Potato
* Tomato

The system first identifies the crop type before performing disease analysis.

---

### 🦠 Disease Detection

#### Tomato Diseases

* Early Blight
* Late Blight
* Healthy

#### Potato Diseases

* Early Blight
* Late Blight
* Healthy

---

### 📚 Knowledge-Based Recommendations

After disease prediction, the system retrieves:

* Disease Information
* Symptoms
* Causes
* Prevention Measures
* Treatment Recommendations

from a JSON-based knowledge base.

---

## 🧠 Deep Learning Architecture

### Crop Classifier

Model:

* ResNet18
* Transfer Learning Architecture
* Custom Fully Connected Layer

Purpose:

* Identify crop category

---

### Disease Classifiers

Separate models trained for:

* Tomato Disease Detection
* Potato Disease Detection

Architecture:

* ResNet18
* Custom Output Layers
* PyTorch Implementation

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Deep Learning

* PyTorch
* TorchVision

### Computer Vision

* PIL (Pillow)
* Image Transformations

### API Development

* FastAPI

### Data Handling

* JSON Knowledge Base

### Model Architecture

* ResNet18

---

## 📂 Project Structure

```text
Crop-Disease-Detection/
│
├── main.py
│
├── models/
│   ├── crop_classifier.pth
│   ├── tomato_disease.pth
│   └── potato_disease.pth
│
├── knowledge_base/
│   ├── tomato.json
│   └── potato.json
│
├── requirements.txt
├── README.md
│
└── sample_images/
```

---


### Start API Server

```bash
uvicorn main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000/docs
```

---

## 🔍 API Endpoint

### Predict Crop Disease

```http
POST /predict
```

### Input

Upload a leaf image:

```form-data
image : leaf_image.jpg
```

### Example Response

```json
{
  "crop": "Tomato",
  "disease": "Early_Blight",
  "details": {
    "symptoms": "Dark spots on leaves",
    "cause": "Fungal infection",
    "treatment": "Apply recommended fungicide"
  }
}
```

---

## 📈 Applications

* Smart Farming
* Precision Agriculture
* Crop Monitoring
* Agricultural Advisory Systems
* AgriTech Platforms
* Mobile Farming Applications

---

## 🎓 Skills Demonstrated

* Deep Learning
* Computer Vision
* Image Classification
* Transfer Learning
* PyTorch
* REST API Development
* FastAPI
* Agricultural AI
* Model Deployment Concepts

---

## 🔮 Future Enhancements

* Support More Crops
* Confidence Score Prediction
* Mobile Application Integration
* Cloud Deployment
* Real-Time Camera Detection
* Disease Severity Analysis
* Explainable AI Visualizations
* Farmer Recommendation Dashboard

---

## 👨‍💻 Developer

Eren

AI • Machine Learning • Computer Vision • Data Science

Building intelligent systems that solve real-world problems through Artificial Intelligence and Deep Learning.

⭐ If you found this project useful, consider giving it a star on GitHub.
