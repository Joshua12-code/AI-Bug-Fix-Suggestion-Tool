# 🛠️ AI Bug Fix Suggestion Tool

An **AI-powered web application** designed to help developers automatically detect and suggest fixes for bugs in their code. This tool leverages **Google Gemini LLM** (via API) to provide intelligent bug fix recommendations and code improvements, streamlining the debugging process for developers.

---

## 📜 Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Screenshots](#screenshots)
- [Setup Instructions](#setup-instructions)
- [Gemini LLM Integration](#gemini-llm-integration)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 📖 About the Project

Debugging code is a common yet time-consuming task in software development. The **AI Bug Fix Suggestion Tool** assists developers by:

- Analyzing submitted code
- Identifying potential issues
- Suggesting optimized or corrected versions of the code

The frontend provides a rich code editor experience while the backend connects with **Gemini LLM API** to handle AI logic and suggestion processing.

---

## 🧰 Tech Stack

| Layer        | Technology                        |
|--------------|-----------------------------------|
| Frontend     | React.js, JavaScript, Tailwind CSS|
| Backend      | Node.js, Express.js               |
| AI Service   | Google Gemini API (Large Language Model) |
| Code Editor  | Monaco Editor                     |
| HTTP Client  | Axios                             |
| Version Control | Git & GitHub                   |

---

## 🚀 Features

- 🔍 Submit buggy code and receive intelligent AI-generated suggestions
- ✨ Monaco Editor with syntax highlighting and line numbers
- 🔗 Backend API integration for LLM communication
- 📡 Handles code in JavaScript, Python, Java (extendable)
- ⚙️ Easy to integrate with any CI/CD pipeline

---

## 🧠 Gemini LLM Integration

We use **Google Gemini Pro (or Gemini 1.5)** API to analyze and suggest bug fixes. Here's how it works:

### 🔗 Connectivity Flow:
1. User pastes code into the editor and clicks **"Fix Bug"**.
2. Code is sent from the frontend (`React`) via `Axios` to the backend (`Express`).
3. Backend constructs a structured prompt and sends it to the Gemini LLM API using `Google Generative AI SDK` or direct REST endpoint.
4. Gemini LLM analyzes the prompt and responds with bug descriptions and corrected code.
5. Backend parses the response and sends it back to the frontend for display.

### 🔐 Example Code to Connect with Gemini:
```js
import { GoogleGenerativeAI } from "@google/generative-ai";

const genAI = new GoogleGenerativeAI(process.env.GEMINI_API_KEY);

export const getBugFix = async (req, res) => {
  const { code } = req.body;

  const model = genAI.getGenerativeModel({ model: "gemini-pro" });
  const prompt = `Analyze the following code and suggest a fixed version:\n\n${code}`;
  const result = await model.generateContent(prompt);
  const suggestion = await result.response.text();

  res.json({ suggestion });
};
