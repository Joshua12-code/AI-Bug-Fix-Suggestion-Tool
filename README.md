# 🛠️ AI Bug Fix & Suggestion Tool

An intelligent code analysis tool powered by **Google Gemini LLM** that detects bugs, suggests fixes, and provides improved versions of the input code using Natural Language Processing and AI.

---

## 📌 Project Description

**AI Bug Fix & Suggestion Tool** is a web-based application that allows developers to paste or write code into an editor and receive:

* 🔍 A list of identified **issues** in the code.
* 💡 AI-generated **suggestions** to improve code quality.
* 🔧 A **corrected version** of the code.

This tool is designed to enhance productivity, reduce debugging time, and provide learning feedback, especially for students, beginner developers, and code reviewers.

---

## ⚙️ Tech Stack

### 🔵 Frontend

* **React.js** – For building responsive UI.
* **CodeMirror** – For syntax-highlighted code editing.
* **HTML/CSS** – For styling and layout.

### 🟢 Backend

* **Node.js + Express.js** – To handle requests.
* **Axios** – For communication between frontend and backend.

### 🧠 AI/LLM Integration

* **Google Gemini Pro (LLM)** – Used to analyze and enhance code by:

  * Understanding code structure.
  * Identifying bugs.
  * Suggesting improvements.
  * Returning corrected code.
* Prompt engineering is applied to format user input effectively.

---

## 🚀 Features

* 📝 Write or paste code in an editor.
* ⚠️ Detect code issues automatically using AI.
* 💬 View intelligent suggestions for code improvement.
* 🔄 Get a corrected version of your code instantly.
* 💻 Fully interactive web UI.

---

## 📷 Screenshots

### ✅ Code Editor Interface

<img width="1903" height="1072" alt="Screenshot 2025-07-11 013955" src="https://github.com/user-attachments/assets/c70d1406-72c4-4d7e-b5ad-556ea2d20224" />


### ⏳ Analyzing State

<img width="1820" height="964" alt="Screenshot 2025-07-11 014014" src="https://github.com/user-attachments/assets/d0bb539b-0ac7-46c1-87e0-ad185780f8c3" />


### 🧠 AI Suggestions and Fixes

<img width="1846" height="1056" alt="Screenshot 2025-07-11 014040" src="https://github.com/user-attachments/assets/f6fc2d93-6fa1-434d-8c9e-e2dc76cc4fca" />


---

## 🔗 How It Works

1. 🧑‍💻 User enters code into the web-based editor.
2. 📩 Frontend sends code to the backend API.
3. 🤖 Backend creates a structured prompt and sends it to **Gemini LLM**.
4. 📬 Gemini returns:

   * Bug analysis
   * Suggestions
   * Fixed code
5. 💾 Results are shown interactively on the UI.

---

## 🗂️ Folder Structure

```
ai-bug-fix-tool/
├── backend/
│   └── server.js                # Handles API & Gemini LLM logic
│
├── frontend/
│   ├── public/
│   │   └── screenshots/         # Screenshots for README
│   │       ├── editor.png
│   │       ├── analyzing.png
│   │       └── fixed-code.png
│   └── src/
│       ├── components/
│       │   └── Editor.js        # Code editor component
│       ├── App.js               # Main app layout
│       └── index.js             # App entry point
│
├── .gitignore
└── README.md
```

---

## 🧑‍💻 Developer Setup

### Prerequisites

* Node.js & npm
* API Key for **Google Gemini Pro** (via Vertex AI or PaLM API)
* Git (to clone the repo)

### Installation Steps

```bash
# Clone the project
git clone https://github.com/Joshua12-code/AI-Bug-Fix-Suggestion-Tool.git
cd AI-Bug-Fix-Suggestion-Tool

# Setup Frontend
cd frontend
npm install
npm start

# Setup Backend (open new terminal)
cd ../backend
npm install
node server.js
```

---

