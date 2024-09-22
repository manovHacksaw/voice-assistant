# Virtual Assistant - Jarvis

This project is a voice-activated virtual assistant named Jarvis. It utilizes speech recognition and text-to-speech technologies to interact with the user. The assistant is powered by the Ollama model for natural language processing, allowing it to respond intelligently to user queries.

## Project Progress

### Features Implemented
- **Speech Recognition**: The assistant listens for commands using the SpeechRecognition library.
- **Text-to-Speech**: Responses are spoken back to the user using the pyttsx3 library.
- **Command Handling**: The assistant can perform various tasks including:
  - Playing songs on YouTube
  - Providing the current time and date
  - Opening websites (Google, YouTube, social media, etc.)
  - Searching for information on Wikipedia
  - Responding to general inquiries
- **Ollama Integration**: The assistant uses the Ollama language model for dynamic and context-aware responses.

### Future Enhancements
- Integrate more functionalities like reminders, weather updates, etc.
- Improve the natural language understanding of the assistant.

## Getting Started

### Prerequisites
- Python 3.x
- The following Python packages:
  - `speech_recognition`
  - `pyttsx3`
  - `pywhatkit`
  - `wikipedia`
  - `langchain`
  - `ollama`
  - `pyaudio` (ensure you have the appropriate audio drivers installed)
  
### Install Olama on Your System
     - Visit the [Ollama Website](https://ollama.com/) and click on Download Button.
     - In Windows Terminal or Powershell: 
          ```bash
          ollama 
          ollama pull mistral
     Note: You can use any model available in the Ollama library that suits your system configuration, not just "mistral." Check the Ollama Documentation for more options.

### Cloning the Repository

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manovHacksaw/voice-assistant

2. **Navigate to the project directory**:
     ```bash
     cd voice-assistance

3. **Install the required packages: You can use pip to install the dependencies. It’s recommended to create a virtual environment first.**:
   ```bash
   pip install speechRecognition pyttsx3 pywhatkit wikipedia langchain ollama pyaudio langchain-ollama

**Running the ChatBot**
     ```bash
     python main.py


