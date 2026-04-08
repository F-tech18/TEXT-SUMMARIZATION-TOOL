TEXT-SUMMARIZATION-TOOL
COMPANY NAME : CODTECH IT SOLUTIONS
NAME : SYED FARHANUDDIN SAIF
INTERN ID : CTIS6987
DOMAIN : ARTIFICIAL INTELLIGENCE
DURATION: 4 WEEKS
MENTOR: NEELA SANTOSH

Perfect — here’s a **clean, professional, copy-paste README.md** for your GitHub 👇

---

# 🚀 AI Smart Summarizer

> Intelligent Multi-Format Text Summarization System using Transformer Models

---

## 📌 Overview

AI Smart Summarizer is a modern NLP-powered application that generates concise and meaningful summaries from long text using state-of-the-art transformer models.

It supports multiple output formats, tone customization, and keyword extraction — designed as a scalable backend service using FastAPI.

---

## ✨ Features

* 🔹 Transformer-based summarization (BART model)
* 🔹 Multi-format output (Paragraph & Bullet points)
* 🔹 Tone control (Formal / Simple)
* 🔹 Keyword extraction
* 🔹 FastAPI REST API
* 🔹 Production-ready modular architecture

---

## 🧠 Tech Stack

* Python
* FastAPI
* Hugging Face Transformers
* PyTorch
* Pydantic

---

## 📁 Project Structure

```
ai_summarizer/
│
├── app.py              # FastAPI application
├── summarizer.py       # Summarization logic
├── utils.py            # Keyword extraction
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/ai_summarizer.git
cd ai_summarizer
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 🚀 API Endpoint

**POST** `/summarize`

---

## 📥 Sample Request

```json
{
  "text": "Artificial Intelligence (AI) is transforming industries by enabling machines to learn from data and make decisions. It is widely used in healthcare, finance, and automation. However, challenges such as ethical concerns, data privacy, and model bias remain critical issues that need to be addressed for responsible AI development.",
  "max_length": 100,
  "min_length": 30,
  "tone": "formal",
  "format": "paragraph"
}
```

---

## 📤 Sample Response

```json
{
  "summary": "Artificial Intelligence is transforming industries by enabling data-driven decision-making. It is widely applied across sectors such as healthcare, finance, and automation. However, ethical concerns, data privacy, and bias remain significant challenges for responsible AI development.",
  "keywords": ["artificial", "intelligence", "data", "ai", "challenges"]
}
```

---

## 📌 Bullet Format Example

```json
{
  "summary": "- Artificial Intelligence is transforming industries by enabling data-driven decision-making\n- It is widely used in healthcare, finance, and automation\n- Ethical concerns, privacy, and bias remain key challenges",
  "keywords": ["artificial", "intelligence", "data", "ai", "challenges"]
}
```

---

## 🧪 API Testing (Swagger UI)

After running the server, visit:

```
http://127.0.0.1:8000/docs
```

You will get an interactive interface to test the API.

---

## 💡 Design Philosophy

> Designed as a scalable NLP microservice with extensible architecture for real-world AI applications.

---

## 📸 Output Preview

Add this image to your repo (recommended path: `assets/output.png`) and reference it:

```markdown
![Output Preview](assets/output.png)
```

---

## ❤️ Built With

* Transformers 🤗
* FastAPI ⚡
* Python 🐍

---
OUTPUT
<img width="1536" height="1024" alt="Image" src="https://github.com/user-attachments/assets/4d39eeef-ba9b-4b10-ae6e-01cdaed1433d" />

