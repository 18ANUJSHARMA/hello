import openai
openai.api_key = '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'
def generate_response(prompt, temperature=0, stream=True):
  """Generates a response to a prompt using the OpenAI Chat Completion API.

  Args:
    prompt: The prompt to generate a response to.
    temperature: The temperature of the response.
    stream: Whether to return the response as a stream of chunks.

  Returns:
    A string containing the response.
  """

  response = openai.ChatCompletion.create(
      model='gpt-3.5-turbo',
      messages=[
          {'role': 'user', 'content': prompt}
      ],
      temperature=temperature,
      stream=stream
  )

  if stream:
    # Collect the stream of chunks.
    collected_chunks = []
    for chunk in response:
      collected_chunks.append(chunk)

    # Extract the message from each chunk.
    collected_messages = []
    for chunk in collected_chunks:
      chunk_message = chunk['choices'][0]['delta']
      collected_messages.append(chunk_message)

    # Return the response as a string.
    return ''.join(collected_messages)
  else:
    return response['choices'][0]['message']['content']
  

  '''import open_ai

prompt = "who is sam altman"
response = open_ai.generate_response(prompt, stream=False)
#response = open_ai.generate_response(prompt)

print(response)'''

