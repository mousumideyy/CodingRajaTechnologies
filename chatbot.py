import nltk
from nltk.tokenize import word_tokenize
import spacy
import random

# Sample dataset of conversations
conversations = [
    {"input": "Hello!", "output": "Hi there! How can I assist you today?"},
    {"input": "How are you?", "output": "I'm doing well, thank you! How about you?"},
    {"input": "What's the weather like today?", "output": "The weather is sunny."},
    {"input": "Tell me a joke.", "output": "Why don't scientists trust atoms? Because they make up everything!"},
    {"input": "Goodbye", "output": "Goodbye! Have a great day!"}
]

# Text Preprocessing
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    return tokens

# Intent Recognition
def recognize_intent(tokens):
    greetings = ["hello", "hi", "hey"]
    weather_related = ["weather"]
    joke_related = ["joke"]
    
    if any(token in greetings for token in tokens):
        return "greeting"
    elif any(token in weather_related for token in tokens):
        return "weather"
    elif any(token in joke_related for token in tokens):
        return "joke"
    else:
        return "other"

# Response Generation
def generate_response(intent):
    if intent == "greeting":
        return random.choice(["Hi!", "Hello!", "Hey there!"])
    elif intent == "weather":
        return "The weather is sunny."
    elif intent == "joke":
        return "Why don't scientists trust atoms? Because they make up everything!"
    else:
        return "I'm sorry, I didn't understand that."

# User Interaction
def chat():
    print("Chatbot: Hi there! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        processed_input = preprocess_text(user_input)
        intent = recognize_intent(processed_input)
        response = generate_response(intent)
        print("Chatbot:", response)

# Learning and Improvement (Not implemented in this simple example)

if __name__ == "__main__":
    # Initialize NLTK
    nltk.download('punkt')
    # Start the chat
    chat()
