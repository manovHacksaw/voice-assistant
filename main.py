import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import pyaudio
import threading
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize the speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to female (use [1] for female)
engine.setProperty("rate", 128)  # Set default speech speed

# Function to adjust voice for emotions
def set_emotion(emotion):
    if emotion == 'happy':
        engine.setProperty('rate', 140)  # Slightly faster speech
        engine.setProperty('volume', 1.0)  # Max volume for excitement
    elif emotion == 'sad':
        engine.setProperty('rate', 100)  # Slower speech
        engine.setProperty('volume', 0.7)  # Lower volume for softer tone
    elif emotion == 'neutral':
        engine.setProperty('rate', 128)  # Normal speech rate
        engine.setProperty('volume', 0.9)  # Default volume

# Greet the user with emotion
def greet_user():
    set_emotion('happy')
    engine.say('I am awake, Sir! It’s a beautiful day, what can I do for you?')
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

# Function to make the assistant talk with emotion
def talk(text, emotion='neutral'):
    set_emotion(emotion)
    engine.say(text)
    engine.runAndWait()

# Threaded function to talk while receiving output
def threaded_talk(text, emotion='neutral'):
    set_emotion(emotion)
    engine.say(text)
    engine.runAndWait()

# Function to take command from the user
def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        talk('I am listening', 'neutral')
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()  # Convert command to lowercase for easy comparison
            if 'jarvis' in command:
                command = command.replace('jarvis', '')  # Remove the keyword "Jarvis"
            print(command)
        except sr.UnknownValueError:
            talk("Sorry, I didn't catch that.", 'sad')
            return ''
        except sr.RequestError:
            talk("Sorry, I am having trouble connecting.", 'sad')
            return ''
        return command

# Function to stream the response while speaking with emotions
def stream_response(input_data):
    # Modify this part to simulate streaming. You can chunk the response or process it word by word.
    response = chain.invoke(input_data)
    
    # Simulate chunking the response with an emotional context
    for i in range(0, len(response), 5):  # Adjust chunk size as needed
        chunk = response[i:i+50]
        print(chunk)  # Print in chunks for debugging

        # Determine emotion based on content (basic examples, can expand based on actual response content)
        emotion = 'neutral'
        if any(word in chunk for word in ['good', 'great', 'success']):
            emotion = 'happy'
        elif any(word in chunk for word in ['error', 'failed', 'trouble']):
            emotion = 'sad'

        thread = threading.Thread(target=threaded_talk, args=(chunk, emotion))
        thread.start()  # Start talking in the background
        thread.join()   # Ensure that the chunk is fully spoken before moving to the next

# Main function to handle commands
def run_eren():
    context = ""  # Initialize the conversation context
    greet_user()  # Initial greeting with emotion
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

        # Stream the response and speak it incrementally
        stream_response(input_data)

        # If exit command
        if 'exit' in command:
            talk('I am going offline. If you need me, just run the program again. Goodbye!', 'sad')
            break

# Run the virtual assistant
run_eren()
