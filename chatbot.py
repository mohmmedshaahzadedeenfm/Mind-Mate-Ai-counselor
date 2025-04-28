
# from flask import *
# import pathlib
# import textwrap
# import google.generativeai as genai
# import os

# from IPython.display import display, Markdown

# chatb=Blueprint("chatbot",__name__)

# # Google Gemini API Key
# GOOGLE_API_KEY = 'AIzaSyAdbPNd0d037Wad2-DZ8PKPzidNJ4H6anE'

# genai.configure(api_key=GOOGLE_API_KEY)

# model = None
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)
#         model = genai.GenerativeModel('gemini-1.5-flash')
#         break

# def to_markdown(text):
#     text = text.replace('*', ' ')
#     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# def generate_gemini_response(prompt):
#     # Add context to the prompt to focus on medicinal plants and Ayurveda
#     context_prompt = f"This conversation focuses on mental health relief and wellness strategies.. {prompt}"
#     response = model.generate_content(context_prompt)
#     return response.text

# @chatb.route('/chatbot')
# def chatbot():
#     return render_template("chatbot.html")

# @chatb.route('/chat', methods=['GET','POST'])
# def chat():
#     user_message = request.json.get('message')
#     # Optional: Filter user input to check for relevant topics
#     # if not ('-' in user_message.lower() or 'helth relif' in user_message.lower() or 'wellness' in user_message.lower()):
#     #     return jsonify({'response': 'Please ask questions related to mental health relief and wellness strategies'})
#     gemini_response = generate_gemini_response(user_message)

#     return jsonify({'response': gemini_response})
    



# # if __name__ == '__main__':
# #     chatbot.run(debug=True)




# # ChatBot - All About


# # import pathlib
# # import textwrap
# # import google.generativeai as genai
# # import os
# # from flask import Flask, request, jsonify, render_template
# # from IPython.display import display, Markdown

# # app = Flask(__name__)

# # GOOGLE_API_KEY = 'AIzaSyAzL1VBdXYPWO1CCWcx7-tDiEd2-zgJvlQ'

# # genai.configure(api_key=GOOGLE_API_KEY)

# # model = None
# # for m in genai.list_models():
# #     if 'generateContent' in m.supported_generation_methods:
# #         print(m.name)
# #         model = genai.GenerativeModel('gemini-1.5-flash')
# #         break

# # def to_markdown(text):
# #     text = text.replace('*', ' ')
# #     return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# # def generate_gemini_response(prompt):
# #     response = model.generate_content(prompt)
# #     return response.text

# # @app.route('/')
# # def home():
# #     return render_template("index.html")

# # @app.route('/chat', methods=['POST'])
# # def chat():
# #     user_message = request.json.get('message')
# #     gemini_response = generate_gemini_response(user_message)
# #     return jsonify({'response': gemini_response})

# # if __name__ == '__main__':
# #     app.run(debug=True)


from flask import Flask, request, jsonify, render_template, Blueprint
import textwrap
import google.generativeai as genai
import os

# Initialize Blueprint for modularity
chatb = Blueprint("chatbot", __name__)

# Retrieve API key from environment variable
GOOGLE_API_KEY = os.getenv("AIzaSyAdbPNd0d037Wad2-DZ8PKPzidNJ4H6anE")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables. Set it before running the app.")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Select the correct model
model = None
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Using model: {m.name}")
        model = genai.GenerativeModel('gemini-1.5-flash')
        break

if not model:
    raise RuntimeError("No valid Gemini AI model found. Check your API key or permissions.")

# Markdown formatting function
def to_markdown(text):
    text = text.replace('*', ' ')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Function to generate chatbot response
def generate_gemini_response(prompt):
    context_prompt = f"This conversation focuses on mental health relief and wellness strategies: {prompt}"
    response = model.generate_content(context_prompt)
    return response.text

# Chatbot page route
@chatb.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

# Chat API endpoint
@chatb.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '').strip()

    if not user_message:
        return jsonify({'response': 'Please provide a valid input.'})

    gemini_response = generate_gemini_response(user_message)
    return jsonify({'response': gemini_response})

# # Main Flask App
# app = Flask(__name__)
# app.register_blueprint(chatb)

# # Home route
# @app.route('/')
# def home():
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)