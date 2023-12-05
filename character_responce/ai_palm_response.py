

import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key: str , background=None):
        palm.configure(api_key=api_key)
        background=f'assume these information about yourself and talk like this personality\n {background}/n'
        self.conversation_history = [background,'ok i will stay in this provided character personality and never talk as i am an ai model']

    def generate_res(self, prompt: str) -> str:
        try:
            # Filter out None values and messages with empty content
            messages = [msg.strip() for msg in self.conversation_history if msg is not None and msg.strip()] + [str(prompt)]
            
            # Make the API call
            response = palm.chat(messages=messages,temperature=1.0)
            
            # Update the conversation history
            self.conversation_history = messages + [response.last]
            
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response: {e}") from e

class AIResponseError(Exception):
    pass



'''import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key: str):
        palm.configure(api_key=api_key)
        self.conversation_history = []

    def generate_res(self, prompt: str) -> str:
        try:
            # Filter out messages with empty content
            messages = [msg for msg in self.conversation_history if msg.strip()] + [str(prompt)]
            
            # Make the API call
            response = palm.chat(messages=messages)
            
            # Update the conversation history
            self.conversation_history = messages + [response.last]
            
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response: {e}") from e

class AIResponseError(Exception):
    pass'''


'''import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key: str):
        palm.configure(api_key=api_key)
    
    

    def generate_res(self, prompt: str) -> str :
        try:
            response = palm.chat(messages=[str(prompt)])
            #response = response.reply(str(prompt))
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response :  {e}") from e

class AIResponseError(Exception):
    pass'''



'''import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key):
        palm.configure(api_key=api_key)

    def generate_response(self, prompt):
        response = palm.chat(messages=[str(prompt)])
        return response.last

import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key: str):
        palm.configure(api_key=api_key)

    def generate_response(self, prompt: str) -> str:
        try:
            response = palm.chat(messages=[str(prompt)])
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response: {e}") from e

class AIResponseError(Exception):
    pass'''
'''import google.generativeai as palm
 
class AIResponse:
    def _init_(self, api_key: str,background=None):
        palm.configure(api_key=api_key)
        background=f'assume these information about yourself and talk like this personality\n {background}/n'

        self.conversation_history = [background,'ok i will stay in this provided character personality and never talk as i am an ai model']
 
    def generate_res(self, prompt: str,) -> str:
        try:
            # Filter out None values and messages with empty content
            messages = [msg.strip() for msg in self.conversation_history if msg is not None and msg.strip()] + [str(prompt)]
            
            # Make the API call
            response = palm.chat(messages=messages,temperature=0.5)
           
            # Update the conversation history
            self.conversation_history = messages + [response.last]
            print(self.conversation_history)
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response: {e}") from e
 
class AIResponseError(Exception):
    pass'''