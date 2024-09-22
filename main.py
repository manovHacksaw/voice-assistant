import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import pyaudio
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to female (use [1] for female)
engine.setProperty("rate", 128)  # Set speech speed

# Greet the user
engine.say('I am awake Sir')
engine.say('What do you want me to do for you?')
engine.runAndWait()

# Initialize the Ollama model
model = OllamaLLM(model="mistral")  # Use your preferred model

# Define the template for the chatbot
template = """
You are a virtual assistant named Jarvis. You assist users by performing tasks or providing information. Here is the conversation history: {context}

Question: {question}
Answer: 
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to make the assistant talk
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to take command from the user
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        talk('I am listening')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()  # Convert command to lowercase for easy comparison
            if 'jarvis' in command:
                command = command.replace('jarvis', '')  # Remove the keyword "Jarvis"
            print(command)
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that.")
            return ''
        except sr.RequestError:
            talk("Sorry, I am having trouble connecting.")
            return ''
        return command

# Main function to handle commands
def run_eren():
    context = ""  # Initialize the conversation context
    while True:
        command = take_command()
        if command == '':
            continue  # Skip empty commands

        # Add user command to context for better responses
        context += f"User: {command}\n"

        # Generate a response using the Ollama model
        input_data = {
            "context": context,
            "question": command
        }
        response = chain.invoke(input_data)
        context += f"AI: {response}\n"  # Update context with the AI response

        # Make the assistant talk back the generated response
        talk(response)

        # If exit command
        if 'exit' in command:
            talk('I am going offline. If you need me, just run the program again. Goodbye!')
            break

# Run the virtual assistant
run_eren()
