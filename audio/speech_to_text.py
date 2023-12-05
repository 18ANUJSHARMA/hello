'''import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def transcribe(self):
        audio = self.recognizer.listen(self.microphone, timeout=5)
        text = self.recognizer.recognize_google(audio)
        return text'''

import speech_recognition as sr
import googletrans
from googletrans import Translator
def translation_hindi_to_english(Text):
    line=str(Text)
    translator = Translator()
    result = translator.translate(line)
    data= result.text
    print(f"You : {data}.")
    return data

cache = {}
class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def transcribe(self):
        recognizer = sr.Recognizer()
        with self.microphone as source:
            print('Listening...')

            try:
                recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                return translation_hindi_to_english(text)

               # return text
            except sr.WaitTimeoutError:
                #print("Stopped listening.")
                #return ''
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
               # print("s")
                #return ''
                pass
            except KeyboardInterrupt:
                #print("s")
                return "disconnect call"
                
# Create an instance of the SpeechToText class
#speech_to_text = SpeechToText()

# Transcribe speech to text
#speech = speech_to_text.transcribe()
