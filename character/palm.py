import google.generativeai as palm

class AIResponse:
    def __init__(self, api_key: str):
        palm.configure(api_key=api_key)

    def generate_resp(self, prompt: str) -> str:
        try:
            response = palm.chat(messages=[str(prompt)])
            return response.last
        except Exception as e:
            raise AIResponseError(f"Failed to generate AI response: {e}") from e

class AIResponseError(Exception):
    pass



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