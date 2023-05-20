# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import requests
import json
import os
import threading

# Models: text-davinci-003,text-curie-001,text-babbage-001,text-ada-001
model = 'text-davinci-003'
def open_ai(prompt, api_key):
    # Make the request to the OpenAI API
    response = requests.post(
        'https://api.openai.com/v1/completions',
        headers={'Authorization': f'Bearer {api_key}'},
        json={
            'model': model,
            'prompt': prompt[1],
            'temperature': 0.3,
            'max_tokens': 300
        }
    )

    result = response.json()
    final_result = ''.join(choice['text'] for choice in result['choices'])
    return final_result

# 2b. Function that gets an Image from OpenAI
def open_ai_image(prompt):
    # Make the request to the OpenAI API
    resp = requests.post(
        'https://api.openai.com/v1/images/generations',
        headers={'Authorization': f'Bearer {api_key}'},
        json={'prompt': prompt,'n' : 1, 'size': '1024x1024'}
    )
    response_text = json.loads(resp.text)

    return response_text['data'][0]['url']

def read_key(key_file):
    with open(key_file, 'r') as file:
        return file.read()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(open_ai(sys.argv, read_key('/Users/johnnykamigashima/.openai.key')))