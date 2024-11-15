import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyDtKAatfeegY7qzoQDh4ZM44ik6GqBbxoI"

import os
import google.generativeai as genai
from PIL import Image


os.environ['GOOGLE_API_KEY'] = "AIzaSyDtKAatfeegY7qzoQDh4ZM44ik6GqBbxoI"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def send_text_request(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def image_analysis_request(image_path):
    model = genai.GenerativeModel('gemini-pro-vision')
    image = Image.open(image_path)
    response = model.generate_content(["Analyze the image", image])
    return response.text

# if __name__ == '__main__':
while True:
    user_input = input("You: ")
    if ' show image' in user_input.lower():
        image_path = input("Enter the path of the image file: ")
        output = image_analysis_request(image_path)
        print("Assistant:", output)


    elif(user_input=="stop"):
        break    
    else:
        output = send_text_request(user_input)
        print("Assistant:", output)