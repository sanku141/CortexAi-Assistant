import os
from dotenv import load_dotenv
from openai import OpenAI
import pyttsx3
import datetime
import random
import webbrowser

# Load environment variables from .env (only in development)
load_dotenv()

# Get OpenAI API Key from environment
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in environment variables.")

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)
engine.setProperty("volume", 1.0)

def speak(text):
    print("Cortex:", text)
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Cortex, a helpful AI assistant like chatgpt."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def cortexActive(command):
    command = command.lower()
    if "time" in command:
        return datetime.datetime.now().strftime("It is %I:%M %p.")
    elif "date" in command:
        return datetime.date.today().strftime("Today is %B %d, %Y.")
    elif "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    elif "joke" in command:
        jokes = [
            "Why did the computer go to therapy? It had a hard drive.",
            "Why don't robots take vacations? They don't need to recharge emotionally.",
            "I would tell you a construction joke, but I'm still working on it."
        ]
        return random.choice(jokes)
    elif "how are you" in command:
        return "I'm functioning perfectly, thank you!"
    else:
        return aiProcess(command)
