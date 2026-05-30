# Smartnode Call Classification System

## Problem Statement

Smartnode's customer support team handles a large number of customer and dealer queries every day. Manually listening to call recordings and identifying whether an issue is **Closed**, **Open**, or **Urgent** is time-consuming and increases the workload on the support team.

The objective of this project is to develop an AI-based Proof of Concept (POC) that automatically converts call recordings into text and classifies each communication into one of three categories:

* **Closed** – Issue resolved
* **Open** – Issue pending
* **Urgent** – Immediate action required

This solution helps improve support team efficiency, reduce manual effort, and prioritize customer requests more effectively.

---

# Features

* Upload customer support call recordings
* Convert audio recordings to text using OpenAI Whisper
* Automatically classify calls into:

  * Closed
  * Open
  * Urgent
* Store call details, transcripts, and predictions in PostgreSQL
* Confidence score for each prediction
* REST API built using FastAPI
* Interactive API documentation using Swagger UI

---

# Tech Stack

## Backend

* FastAPI
* Python

## Database

* PostgreSQL
* SQLAlchemy

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

## Speech-to-Text

* OpenAI Whisper

## Additional Libraries

* Pandas
* Joblib
* NumPy
* Python Dotenv

---

# Project Structure

```text
smartnode-call-classifier/
│
├── app.py
├── database.py
├── models.py
├── classifier.py
├── stt.py
├── train.py
│
├── uploads/
│
├── model/
│   └── call_classifier.pkl
│
├── data/
│   └── labeled_dataset.csv
│
├── requirements.txt
└── .env
```

---

# Workflow

```text
Audio Recording
        ↓
OpenAI Whisper
        ↓
Transcript Generation
        ↓
TF-IDF Vectorization
        ↓
Logistic Regression Model
        ↓
Closed / Open / Urgent
        ↓
Store Results in PostgreSQL
```

---

# Database Tables

## Calls

Stores uploaded audio file details.

| Column      | Description      |
| ----------- | ---------------- |
| id          | Primary Key      |
| filename    | Audio file name  |
| uploaded_at | Upload timestamp |

---

## Transcripts

Stores generated transcript text.

| Column          | Description          |
| --------------- | -------------------- |
| id              | Primary Key          |
| call_id         | Related call ID      |
| transcript_text | Generated transcript |

---

## Predictions

Stores classification results.

| Column     | Description                 |
| ---------- | --------------------------- |
| id         | Primary Key                 |
| call_id    | Related call ID             |
| label      | Closed/Open/Urgent          |
| confidence | Prediction confidence score |

---

# Installation

## Clone Repository

```bash
git clone <repository-url>
cd smartnode-call-classifier
```

---

## Create Virtual Environment

```bash
python -m venv myenv
```

### Activate Environment

#### macOS/Linux

```bash
source myenv/bin/activate
```

#### Windows

```bash
myenv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# PostgreSQL Setup

Create a database:

```sql
CREATE DATABASE smartnode_db;
```

Create a `.env` file:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/smartnode_db
```

Example:

```env
DATABASE_URL=postgresql://postgres:admin123@localhost:5432/smartnode_db
```

---

# Training the Model

Update the dataset:

```text
data/labeled_dataset.csv
```

Train the model:

```bash
python train.py
```

Output:

```text
Model saved successfully!
```

Generated model:

```text
model/call_classifier.pkl
```

---

# Running the Application

Start FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## Analyze Call Recording

### POST /analyze

Upload an audio file (`.wav`, `.mp3`, `.m4a`)

### Sample Response

```json
{
  "success": true,
  "call_id": 1,
  "filename": "sample.wav",
  "transcript": "Server is down and customers cannot login",
  "prediction": "Urgent",
  "confidence": 93.42
}
```

---

# Machine Learning Model

### Text Vectorization

* TF-IDF Vectorizer

### Classification Algorithm

* Logistic Regression

### Output Labels

| Label  | Meaning                   |
| ------ | ------------------------- |
| Closed | Issue resolved            |
| Open   | Issue pending             |
| Urgent | Immediate action required |

---

# Future Enhancements

* React-based Dashboard
* Authentication & Authorization
* BERT-based Classification
* Real-time Call Processing
* Analytics Dashboard
* Docker Deployment
* Cloud Hosting

---

# Author

**Pal Patel**


---

# Conclusion

The Smartnode Call Classification System demonstrates the practical application of Artificial Intelligence, Machine Learning, Natural Language Processing, Speech-to-Text technology, FastAPI, and PostgreSQL to automate customer support workflows and improve issue prioritization.
