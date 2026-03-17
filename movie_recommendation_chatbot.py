
!pip install scikit-learn joblib ipywidgets

import pandas as pd
import ipywidgets as widgets
from IPython.display import display
import time

from google.colab import files

uploaded = files.upload()

df = pd.read_csv('movie_db.csv', encoding='latin-1')

df['Genre'] = df['Genre'].str.lower()
df['Language'] = df['Language'].str.lower()
df['Movie'] = df['Movie'].str.title()

greetings = ['hi', 'hello', 'hey', 'namaste', 'hola', 'hai']
thanks_keywords = ['thanks', 'thank you', 'thank u', 'thx']

chat_output = widgets.Output(layout=widgets.Layout(border='1px solid gray', height='300px', overflow='auto'))
user_input = widgets.Text(placeholder='Type your message here and press Enter', description='You:', layout=widgets.Layout(width='80%'))

enter_button = widgets.Button(description='Enter', button_style='success', layout=widgets.Layout(width='10%'))
clear_button = widgets.Button(description='Clear Chat', button_style='warning', layout=widgets.Layout(width='10%'))
input_box = widgets.HBox([user_input, enter_button, clear_button])

session = {"genre": None, "language": None}

# Helper extraction functions
def extract_genre(text):
    text_lower = text.lower()
    for genre in df['Genre'].unique():
        if genre in text_lower:
            return genre
    return None

def extract_language(text):
    text_lower = text.lower()
    for lang in df['Language'].unique():
        if lang in text_lower:
            return lang
    return None

def extract_number(text):
    words = text.lower().split()
    for word in words:
        if word.isdigit():
            return int(word)
    return None

# Recommendation logic
def recommend_movies(genre, language, top_n=3):
    filtered = df[(df['Genre'] == genre) & (df['Language'] == language)].copy()
    if filtered.empty:
        return f"No movies found for genre '{genre}' and language '{language}'."
    top_movies = filtered.sort_values(by='Rating', ascending=False).head(top_n)
    response = f"Top {min(top_n, len(top_movies))} {genre.title()} movies in {language.title()}:\n"
    for _, row in top_movies.iterrows():
        response += f"- {row['Movie']} (Rating: {row['Rating']})\n"
    return response

# Chat display
def print_user_message(msg):
    with chat_output:
        print(f"🧑: {msg}\n")

def print_bot_message(msg):
    with chat_output:
        print("🤖 is typing...")
    time.sleep(1)
    with chat_output:
        print(f"🤖: {msg}\n")

# Core logic
def process_message(user_msg):
    user_msg = user_msg.strip()
    if not user_msg:
        return

    print_user_message(user_msg)
    lower_msg = user_msg.lower()

    if lower_msg in ['quit', 'exit']:
         print_bot_message("Goodbye! 👋 Have a great day! You can restart the chat anytime.")
         session["genre"] = None
         session["language"] = None
         return


    if lower_msg in greetings:
        print_bot_message("Hello! 👋 Tell me a movie genre and language you prefer, or just one and I'll ask for the other.")
        return

    if any(thx in lower_msg for thx in thanks_keywords):
        print_bot_message("You're welcome! 😊 Want more recommendations? Just say a genre or language.")
        session["genre"] = None
        session["language"] = None
        return

    genre = extract_genre(user_msg)
    language = extract_language(user_msg)

    if genre:
        session["genre"] = genre
    if language:
        session["language"] = language

    num_movies = extract_number(user_msg) or 3

    if session["genre"] and session["language"]:
        response = recommend_movies(session["genre"], session["language"], num_movies)
        print_bot_message(response)
        session["genre"], session["language"] = None, None
    elif session["genre"]:
        available_langs = ', '.join(df[df['Genre'] == session["genre"]]['Language'].unique())
        print_bot_message(f"Great! Which language do you prefer? Available for {session['genre'].title()}: {available_langs}")
    elif session["language"]:
        available_genres = ', '.join(df[df['Language'] == session["language"]]['Genre'].unique())
        print_bot_message(f"You chose {session['language'].title()} language. Which genre do you like? Available genres: {available_genres}")
    else:
        print_bot_message("Please mention a genre and language like 'romance in Hindi' or 'action Telugu movies'.")

# Events
def on_enter_clicked(b):
    process_message(user_input.value)
    user_input.value = ''

def on_clear_clicked(b):
    chat_output.clear_output()
    session["genre"] = None
    session["language"] = None
    with chat_output:
        print("🤖: Chat cleared. Say hi to start a new conversation!\n")

def on_text_submit(change):
    process_message(change.value)
    user_input.value = ''

enter_button.on_click(on_enter_clicked)
clear_button.on_click(on_clear_clicked)
user_input.on_submit(on_text_submit)

display(chat_output, input_box)