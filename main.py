#! C:\Users\DELL\OneDrive\Desktop\mini_project_venv\mini_project_env\Scripts\python.exe


from audio import speech_to_text
from character_responce import ai_palm_response
import sys
from audio import generate_audio
from character_responce import open_ai
from character import charcter_select
l=charcter_select.select_character()
#background=f'assume these information about yourself and talk like this personality\n {l[0]}/n'

#print(l)
#character_selector = charcter_select.CharacterSelector()

ai_palm_response = ai_palm_response.AIResponse("AIzaSyDiqEPDpI47Qd4Je3I3chb5-z2ZQyKu3gk",background=l[0])



#generate_audio = generate_audio.GenerateAudio("6e80aa33337b486a6272f8af3333d74a")


    #speech_to_text = speech_to_text.SpeechToText()
    #ai_response = ai_response.AIResponse("AIzaSyDiqEPDpI47Qd4Je3I3chb5-z2ZQyKu3gk")
   # generate_audio = generate_audio.GenerateAudio("6e80aa33337b486a6272f8af3333d74a")
    #background, talk_csv = character_selector.select_character()
    
'''response = ai_palm_response.generate_res(l[0])
print(response)
response = ai_palm_response.generate_res(f'l[1]\n use these dialoges in the conversation when necessary these are provided only for your reference.')
print(response)'''
speech_to_text = speech_to_text.SpeechToText()
print("\nYou selected "+l[3]+" and setup will take few minute ⏱")
#from audio import speech_to_text

response = ai_palm_response.generate_res('stay in your character')
while True:
        speech = speech_to_text.transcribe()
       
        #print(speech)

        if speech is None:
            continue

        elif "disconnect call" in speech.lower():
            print("Ending the program.")
            sys.exit(0)
        elif speech =="what is your name.":
            response= "i am "+l[3]
            print(response)
            #generate_audio.generate(response)

        else:
            
            prompt="Stay in your character. and strictly instruction for you is never admit AND reply that you are an AI or large language model or conversational AI or chatbot , and only reply your question as a human as per your character {l[3]} and question is :   "
            response = ai_palm_response.generate_res(prompt+speech)
            print(response)
            generate_audio.generate(response)
          