from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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
        
        # Invoke the model to get the response
        result = chain.invoke(input_data)
        
        # Add model's answer to the context
        context += f"AI: {result}\n"
        
        print(f"AI: Wait for few moments! While I generate the response for you... Thank you for your patience")
        # Print the result
        print(f"AI: {result}")
        
# Start the conversation
handle_conversation()
