# fake_review_monitoring.py

from flask import Flask, request, render_template, redirect, jsonify
import re
import os
from textblob import TextBlob

app = Flask(__name__)

# Mock database of reviews
reviews = []

# Simple rule-based detection for fake reviews
def is_fake_review(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    word_count = len(text.split())

    overly_positive = polarity > 0.9
    short_review = word_count < 5
    too_many_exclamations = text.count("!") > 3

    if overly_positive or short_review or too_many_exclamations:
        return True
    return False

@app.route('/')
def index():
    return render_template('index.html', reviews=reviews)

@app.route('/submit', methods=['POST'])
def submit_review():
    username = request.form['username']
    review = request.form['review']
    
    fake = is_fake_review(review)
    reviews.append({"username": username, "review": review, "fake": fake})
    return redirect('/')

@app.route('/remove_fake', methods=['POST'])
def remove_fake():
    global reviews
    reviews = [r for r in reviews if not r['fake']]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
