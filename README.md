# 🛠️ AI Bug Fix & Suggestion Tool

An intelligent code analysis tool powered by **Google Gemini LLM** that detects bugs, suggests fixes, and provides improved versions of the input code using Natural Language Processing and AI.

---

## 📌 Project Description

**AI Bug Fix & Suggestion Tool** is a web-based application that allows developers to paste or write code into an editor and receive:

- 🔍 A list of identified **issues** in the code.
- 💡 AI-generated **suggestions** to improve code quality.
- 🔧 A **corrected version** of the code.
<img width="1846" height="1056" alt="Screenshot 2025-07-11 014040" src="https://github.com/user-attachments/assets/a8ac6842-9f33-46f4-b60e-f45114bdc0ef" />

This tool is designed to enhance productivity, reduce debugging time, and provide learning feedback, especially for students, beginner developers, and code reviewers.

---

## ⚙️ Tech Stack

### 🔵 Frontend
- **React.js** – For building responsive UI.
- **CodeMirror** – For a syntax-highlighted code editor.
- **HTML/CSS** – For styling and structure.

### 🟢 Backend
- **Node.js + Express.js** – Handles API requests.
- **Google Gemini Pro API (LLM)** – Used for natural language understanding and code fixing.
- **Axios** – For handling HTTP requests from frontend to backend.

### 🧠 AI/LLM Integration
- **Google Gemini Pro** – A powerful LLM (Large Language Model) capable of understanding programming languages, identifying issues, and suggesting context-aware fixes.
- Prompt engineering is used to structure the input for the Gemini model and parse the results into actionable insights.

---

## 🚀 Features

- 📝 Paste or write code in a rich code editor.
- ⚠️ Detect bugs and errors using AI.
- 💬 Receive suggestions for better coding practices.
- 🔄 View the AI-corrected version of your code.
- 🔎 Analysis feedback is shown instantly in an interactive UI.

---

## 📷 Screenshots

### ✅ Code Editor Interface
![Code Editor](./screenshots/Screenshot%202025-07-11%20013955.png)

---

### 🔄 Analyzing State
![Analyzing](./screenshots/Screenshot%202025-07-11%20014014.png)

---

### 🧠 AI Suggestions and Fixes
![Fix Suggestions](./screenshots/Screenshot%202025-07-11%20014040.png)

---

## 🔗 How It Works

1. ✍️ The user enters or pastes code into the editor.
2. ⚙️ On clicking **"Analyze Code"**, the frontend sends the code to the backend via an API.
3. 🤖 The backend formulates a structured prompt and sends it to the **Gemini LLM**.
4. 📬 The AI responds with:
   - Detected bugs/issues
   - Improvement suggestions
   - The corrected code
5. 🖥️ Results are displayed on the same page for review.

---

## 🏗️ Folder Structure

ai-bug-fix-tool/
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ └── Editor.js
│ │ ├── App.js
│ │ └── index.js
│
├── backend/
│ ├── server.js (Handles API & LLM integration)
│
├── .gitignore
├── README.md


---

## 🧑‍💻 Developer Guide

### Prerequisites

- Node.js and npm installed
- API Key for Google Gemini (via Vertex AI or PaLM API)
- Git (for cloning and versioning)

### Installation Steps

```bash
# Clone the repo
git clone https://github.com/Joshua12-code/AI-Bug-Fix-Suggestion-Tool.git
cd AI-Bug-Fix-Suggestion-Tool

# Install dependencies for frontend
cd frontend
npm install

# Run the frontend
npm start

# Setup backend (in separate terminal)
cd ../backend
npm install
node server.js
