# 🫁 Chest Cancer Classification - Transfer Learning Based CT Scan Diagnosis

Chest Cancer Classification is an end-to-end **Deep Learning Medical Imaging Project** that predicts whether a person has **Chest Cancer** or **Normal** using CT scan images.

This project uses **Transfer Learning with VGG16** (pretrained on ImageNet) and fine-tunes it for binary classification of chest CT scan images.  
The application provides a complete **MLOps + Deployment workflow** including:

✅ Model training with TensorFlow/Keras  
✅ Experiment tracking with MLflow  
✅ Dataset versioning using DVC  
✅ Remote storage integration (DagsHub)  
✅ Flask-based web application frontend  
✅ HTML + TailwindCSS UI  
✅ Docker containerization for deployment  

---

## 🚀 Project Highlights

- 🧠 **Transfer Learning using VGG16**
- 📊 **Binary Classification**: Cancer vs Normal
- 🧪 **MLflow Experiment Tracking**
- 🌍 **DagsHub Integration** for MLflow + DVC
- 🗂️ **DVC Pipeline** for data and model version control
- 🖥️ **Flask Web App** for inference
- 🎨 **Modern UI** using HTML + TailwindCSS
- 🐳 **Dockerized Deployment**

---

## 🏥 Problem Statement

Early detection of chest cancer is critical for increasing patient survival rates. Manual diagnosis of CT scans is time-consuming and prone to human error.

This project aims to build an AI-powered system that can automatically analyze chest CT scan images and classify them into:

- **Cancer**
- **Normal**

The system is designed as a production-ready MLOps pipeline to support real-world deployment.

---

## 🎯 Objective

To build a deep learning model that:

1. Takes a CT scan image as input  
2. Predicts whether the person has chest cancer or not  
3. Deploys the model via a web application for real-time inference  

---

## 🧠 Model Used

### 🔥 VGG16 (Transfer Learning)

The model is based on **VGG16**, a popular CNN architecture pretrained on ImageNet.  
Transfer learning allows leveraging learned features such as edges, shapes, textures, and patterns, improving accuracy even with limited medical imaging datasets.

#### Workflow:
- Load pretrained VGG16
- Freeze base layers
- Add custom Dense layers for binary classification
- Train the final classifier head
- Fine-tune selected layers if required

---

## 🧾 Input & Output

### Input:
- CT Scan Image (`.jpg`, `.png`, `.jpeg`)

### Output:
- **Cancer**
- **Normal**

---

## 🏗️ Project Architecture

```
Chest-Cancer-Classification/
│
├── artifacts/                  # Saved models, checkpoints, logs
├── config/                     # Configuration files
├── src/                        # Core source code (training, utils)
├── templates/                  # HTML templates
├── research/                   # Notebooks(Experiments & EDA)
│
├── dvc.yaml                    # DVC pipeline configuration
├── params.yaml                 # Training parameters
├── requirements.txt
├── Dockerfile
├── app.py                      # Flask app
├── main.py                     # Training pipeline entry
├── mlruns/                     # MLflow logs (local)
└── README.md
```

---

## ⚙️ Tech Stack

| Category | Tools |
|---------|------|
| Deep Learning | TensorFlow, Keras |
| Model Architecture | VGG16 (Transfer Learning) |
| Experiment Tracking | MLflow |
| Dataset Versioning | DVC |
| Remote Storage | DagsHub |
| Backend | Flask |
| Frontend | HTML, TailwindCSS |
| Containerization | Docker |
| Language | Python |

---

## 📊 MLOps Pipeline (DVC + MLflow)

This project follows a complete MLOps pipeline:

### ✅ DVC Pipeline
- Data ingestion
- Data validation
- Model training
- Model evaluation
- Model saving

### ✅ MLflow Tracking
- Logs metrics (accuracy, loss, precision, recall)
- Logs artifacts (model, plots)
- Tracks hyperparameters

### ✅ DagsHub Integration
- Stores DVC remote datasets
- Stores MLflow experiments remotely
- Enables team collaboration

---

## 📌 How the Web Application Works

1. User uploads a CT scan image through the web interface.
2. Flask backend reads the image.
3. Image preprocessing is applied:
   - Resize
   - Normalize
   - Convert to tensor
4. Model performs inference.
5. Prediction is displayed as **Cancer** or **Normal**.

---

## 🖥️ Web Application UI

The UI is built using:

- HTML Templates
- Tailwind CSS Styling

The application provides a clean and responsive user interface for uploading images and viewing predictions.

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sumit-Prasad01/Chest-Cancer-Classification.git
cd Chest-Cancer-Classification
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🧪 Run Training Pipeline

```bash
python main.py
```

---

## 📊 Start MLflow UI

```bash
mlflow ui
```

Open:
```
http://127.0.0.1:5000
```

---

## 📦 Run Flask App

```bash
python app.py
```

Flask app will run at:
```
http://127.0.0.1:5000
```

---

## 🗂️ DVC Commands

### Initialize DVC
```bash
dvc init
```

### Add dataset
```bash
dvc add data/
```

### Run pipeline
```bash
dvc repro
```

### Push dataset to remote (DagsHub)
```bash
dvc push
```

---

## 🐳 Run with Docker

### Build Docker Image
```bash
docker build -t chest-cancer-classifier .
```

### Run Docker Container
```bash
docker run -p 5000:5000 chest-cancer-classifier
```

Now open:
```
http://localhost:5000
```

---

## 📌 Example Prediction Output

| Uploaded Image | Prediction |
|--------------|------------|
| CT Scan Image | Cancer / Normal |

---

## 📁 Artifacts Generated

- Trained Model (`.h5` / SavedModel format)
- MLflow experiment logs
- DVC tracked dataset versions
- Accuracy/Loss plots
- Model evaluation reports

---

## 🔮 Future Enhancements

- Add Grad-CAM visualization for explainability
- Add multi-class classification (different cancer stages)
- Deploy on cloud (AWS/GCP/Azure)
- Add CI/CD pipeline
- Add model monitoring & drift detection

---


