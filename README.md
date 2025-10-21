# 🧩  APT-LOGIC-SOLVER

A simple **Flask + HTML/CSS/JS** web application that automatically finds the **correct answers** from a JSON question set by checking each option against **bcrypt-hashed answers**.

---

## 🚀 Features

- 🧮 **Automatic answer detection** — Reads `questions.json` and checks each option via bcrypt.
- 💻 **Beautiful UI** — Responsive HTML, CSS, and JavaScript frontend with clean layout.
- ⚡ **Real-time results** — Shows both:
  - Full question cards with correct options highlighted
  - Compact “Answers Only” view beside it
- 📂 **JSON Upload or Paste** — Works with uploaded files or pasted JSON text.
- 🔒 **Secure** — bcrypt ensures safe verification of answers.

---

## 🧱 Project Structure

APT-LOGIC-SOLVER/
│
├── app.py # Flask backend server
├── index.html # Frontend UI (HTML/CSS/JS)
├── questions.json # Example JSON file with questions & bcrypt-hashed answers
├── requirements.txt # Python dependencies
└── README.md # Documentation
