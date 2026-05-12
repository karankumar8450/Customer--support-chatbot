# 🤖 Customer Support Chatbot

A rule-based customer support chatbot built in Python. Handles common customer queries like complaints, feedback, account issues, and order status — all through a simple terminal interface.

---

## Features

- Greeting and farewell detection
- Complaint handling
- Feedback collection (positive & negative)
- Account issue resolution (login, password, signup)
- Order status queries (tracking, price, delivery, cancellation)
- Saves full chat history to a local file

---

## How to Run

Make sure Python is installed, then run:

```bash
python chat.py
```

---

## Project Structure

```
chat-system/
├── chat.py        # Main chatbot code
├── .gitignore     # Files excluded from GitHub
└── README.md      # This file
```

---

## Example Conversation

```
Enter your name: Karan
Bot: Hello Karan! Welcome to our chat system.

Karan: hello
Bot! Hey there!

Karan: order
Bot: What can I help you with?
  1. Complaint
  2. Feedback
  3. Account Issue
  4. Order Status
  5. Exit

Your choice: 4
Bot: hello! How can i help you with your order: where is my order
Bot! 📦 Your order is on the way! Current location: Dispatch Center.
```

---

## Built With

- Python 3
- No external libraries — only built-in `random` module

---

## Author

**Karan** — first Python project | learning AI/ML
