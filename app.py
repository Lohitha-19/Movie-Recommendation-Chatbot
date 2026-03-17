from flask import Flask, render_template, request, jsonify
import pandas as pd
import difflib
import re

app = Flask(__name__)

# Load dataset
df = pd.read_csv("movie_db.csv", encoding="latin-1")

# Clean dataset
df['Genre'] = df['Genre'].str.lower().str.strip()
df['Language'] = df['Language'].str.lower().str.strip()
df['Movie'] = df['Movie'].str.title()

genres = list(df['Genre'].unique())
languages = list(df['Language'].unique())


# ---------- SMART DETECTION FUNCTIONS ----------

def detect_option(text, options):

    text = text.lower()

    # Direct match
    for opt in options:
        if opt in text:
            return opt

    # Typo correction
    words = re.findall(r'\w+', text)

    for word in words:
        match = difflib.get_close_matches(word, options, n=1, cutoff=0.6)
        if match:
            return match[0]

    return None


def extract_number(text):

    numbers = re.findall(r'\d+', text)

    if numbers:
        return int(numbers[0])

    return 3


# ---------- MOVIE RECOMMENDATION ----------

def recommend_movies(genre, language, top_n=3):

    filtered = df[
        df['Genre'].str.contains(genre) &
        df['Language'].str.contains(language)
    ]

    if filtered.empty:
        return ["No movies found for that combination."]

    top_movies = filtered.sort_values(by="Rating", ascending=False).head(top_n)

    result = []

    for _, row in top_movies.iterrows():
        result.append(f"{row['Movie']} ⭐ {row['Rating']}")

    return result


# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    user_msg = request.json["message"].lower()

    greetings = ["hi", "hello", "hey", "namaste"]
    bye_words = ["bye", "goodbye"]
    thanks_words = ["thanks", "thank", "thx"]

    words = re.findall(r'\w+', user_msg)

    # Greeting detection
    if any(word in greetings for word in words):
        return jsonify({
            "reply": "Hello 👋 Tell me a genre and language like 'action hindi'.",
            "type": "text"
        })

    # Bye detection
    if any(word in bye_words for word in words):
        return jsonify({
            "reply": "Goodbye 👋 Enjoy your movies!",
            "type": "text"
        })

    # Thanks detection
    if any(word in thanks_words for word in words):
        return jsonify({
            "reply": "You're welcome 😊 Want more recommendations?",
            "type": "text"
        })

    genre = detect_option(user_msg, genres)
    language = detect_option(user_msg, languages)

    number = extract_number(user_msg)

    if genre and language:

        movies = recommend_movies(genre, language, number)

        return jsonify({
            "reply": movies,
            "type": "list"
        })

    if genre:
        return jsonify({
            "reply": f"You chose {genre.title()} genre. Which language?",
            "type": "text"
        })

    if language:
        return jsonify({
            "reply": f"You chose {language.title()} language. Which genre?",
            "type": "text"
        })

    return jsonify({
        "reply": "Please tell me a genre and language like 'romance telugu movies'.",
        "type": "text"
    })


# ---------- RUN SERVER ----------

if __name__ == "__main__":
    app.run(debug=True)