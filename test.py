from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import time

# Define the template for the chatbot
template = """
     Answer the question below.
     Here is the conversation history: {context}
     
     Question : {question}
     Answer: 
"""

# Initialize the model
model = OllamaLLM(model="mistral")

# Create the prompt from the template
prompt = ChatPromptTemplate.from_template(template)

# Combine prompt and model to create the chain
chain = prompt | model

print("Initializing...")

def stream_response(input_data):
    # Generate the full response first
    response = chain.invoke(input_data)

    # Simulate streaming by outputting small chunks incrementally
    chunk_size = 10  # Define the size of each chunk to be streamed (in characters)
    for i in range(0, len(response), chunk_size):
        chunk = response[i:i + chunk_size]  # Get the next chunk
        print(chunk, end="", flush=True)  # Print the chunk, flush to force immediate output
        time.sleep(0.05)  # Simulate typing delay (adjust as needed for speed)
    print()  # Move to the next line after the full response

def handle_conversation():
    context = ""  # Initial empty context
    print("Welcome to the AI ChatBot! Type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")  # Capture user input
        if user_input.lower() == "exit":
            print("Bye Bye! Have a nice day")
            break
        
        # Add user question to the context
        context += f"User: {user_input}\n"
        
        # Prepare the input for the model
        input_data = {
            "context": context,
            "question": user_input
        }
        
        print(f"AI: Wait for a few moments! I am generating the response for you...")
        
        # Stream the response in real-time (simulated)
        stream_response(input_data)
        
        # Add model's answer to the context (assume the response is complete at this point)
        context += f"AI: {chain.invoke(input_data)}\n"

# Start the conversation
handle_conversation()
