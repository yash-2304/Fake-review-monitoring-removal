# 🛡️ Fake Product Review Monitoring & Removal System

This project is a simple Flask web application that detects and removes fake product reviews. It uses basic rule-based logic and sentiment analysis to flag suspicious reviews and provides a clean interface for review submission and moderation.

## 🚀 Features

- Submit product reviews through a web interface
- Automatically detects potentially fake reviews:
  - Overly positive sentiment
  - Too short
  - Excessive use of exclamation marks
- Flag and remove fake reviews with a single click

## 💡 How It Works

The system uses [TextBlob](https://textblob.readthedocs.io/en/dev/) to perform sentiment analysis and simple heuristics to flag fake reviews. These include:

- Sentiment polarity greater than 0.9
- Review length under 5 words
- More than 3 exclamation marks

## 📂 Project Structure

```
📦fake-review-monitor
├── fake_review_monitoring.py     # Flask backend logic
├── templates
│   └── index.html                # Frontend HTML + CSS
└── README.md
```

## 🧪 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/fake-review-monitor.git
   cd fake-review-monitor
   ```

2. Install dependencies:
   ```bash
   pip install flask textblob
   python -m textblob.download_corpora
   ```

3. Run the Flask app:
   ```bash
   python fake_review_monitoring.py
   ```

4. Open your browser:
   ```
   http://127.0.0.1:5002
   ```

## 📸 Screenshots

> 📌 Add screenshots here of the form, submitted reviews, and flagged results.

## 🛠️ Future Improvements

- Machine learning-based fake review detection
- Persistent database (SQLite/MySQL)
- User login & moderation dashboard
- CSV export of reviews

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more information.

---

Built with ❤️ using Flask and TextBlob.
