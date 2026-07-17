# Conversational Agent 🤖

A Dialogflow CX–based conversational agent with Python support code for testing, fulfillment, and deployment.  
This project demonstrates end‑to‑end chatbot development: from agent design to API integration, testing, and cloud deployment.

---

## ✨ Features
- **Dialogflow CX agent exports** (`agents/`)
- **Python client** (`src/dialogflow_client.py`) for interacting with the agent
- **Webhook fulfillment** (`src/webhook.py`) for custom responses
- **Unit tests** (`tests/test_agent.py`) to validate flows and intents
- **Deployment configs** for Docker, GCP App Engine, and Heroku

---

## 🛠️ Setup
Clone the repo and install dependencies:
```bash
git clone https://github.com/Kanakbaghel/Conversational_Agent.git
cd Conversational_Agent
pip install -r requirements.txt
```

Set environment variables:
```bash
export PROJECT_ID="your-gcp-project-id"
export AGENT_ID="your-agent-id"
```

Run locally:
```bash
python src/main.py
```

---

## 🚀 Deployment

### 🔹 Google Cloud App Engine
```bash
gcloud app deploy deployment/app.yaml
```

### 🔹 Docker
```bash
docker build -t conversational-agent .
docker run -p 8080:8080 conversational-agent
```

### 🔹 Heroku
```bash
heroku create
git push heroku main
```
Make sure `Procfile` is at the root:
```
web: gunicorn src.webhook:app
```

---

## 🧪 Testing
Run unit tests:
```bash
pytest tests/
```

---

## 📂 Project Structure
```
Conversational_Agent/
│── src/                        # Core Python code
│── tests/                      # Unit tests
│── requirements.txt             # Dependencies
│── app.yaml                     # GCP deployment config
│── .gitignore                   # Repo hygiene
│── README.md                    # Documentation
│── Procfile                     # Heroku deployment
│── deployment/
│   └── Dockerfile               # Docker containerization
```

---

## 📜 License
MIT License – free to use and modify.
```
