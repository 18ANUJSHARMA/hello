from flask import Flask, render_template, request, session , redirect
from character_responce import ai_palm_response
import sys
from audio import generate_audio
from character import charcter_select

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_character = request.form.get('character')
        session['selected_character'] = selected_character
        ai_response = ai_palm_response.AIResponse("AIzaSyDiqEPDpI47Qd4Je3I3chb5-z2ZQyKu3gk", background=selected_character)
        return render_template('index.html', selected_character=selected_character, ai_response=ai_response)

    # If it's a GET request and a character is already selected, redirect to the conversation page
    if 'selected_character' in session:
        return redirect('/conversation')

    # If it's a GET request and no character is selected, render the character selection form
    return render_template('character_select.html', characters=charcter_select.select_character())

@app.route('/conversation', methods=['GET', 'POST'])
def conversation():
    if 'selected_character' not in session:
        return redirect('/')  # Redirect to character selection if no character is selected

    selected_character = session['selected_character']

    if request.method == 'POST':
        speech = request.form['speech']
        ai_response = ai_palm_response.AIResponse("AIzaSyDiqEPDpI47Qd4Je3I3chb5-z2ZQyKu3gk", background=selected_character)

        if speech.lower() == "disconnect call":
            sys.exit(0)
        elif speech.lower() == "what is your name":
            response = "I am " + selected_character
        else:
            prompt = "Stay in your character. Answer the question as a human as per your character {0}. Question: ".format(selected_character)
            response = ai_response.generate_res(prompt + speech)
            generate_audio.generate(response)
        return render_template('conversation.html', selected_character=selected_character, speech=speech, response=response, ai_response=ai_response)

    # If it's a GET request, render the conversation page
    return render_template('conversation.html', selected_character=selected_character)

if __name__ == '_main_':
    app.run(debug=True)