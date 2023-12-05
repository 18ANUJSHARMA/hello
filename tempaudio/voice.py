from flask import Flask, render_tempaudio, request
import requests
import subprocess

voice = Flask(__name__)

api_key = "a7c12521e4ce17d430379135fb0e31d6"

@voice.route('/')
def voice():
    return render_tempaudio('voice.html')

@voice.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']

    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/2EiwWnXFnvU5JabPnv8n"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, json=data, headers=headers)

    with open('..output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    subprocess.Popen(['ffplay', '-nodisp', '-autoexit', 'output.mp3'], stdin=subprocess.PIPE)

    return "Audio generated and played."

if __name__ == '__main__':
    voice.run(debug=True)
