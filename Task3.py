import nltk
import random
import string

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Sample corpus
corpus = {
    "greeting": ["hello", "hi", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye", "take care"],
    "how_are_you": ["how are you", "how's it going", "how are things"],
    "name": ["what's your name", "who are you"],
    "thanks": ["thank you", "thanks", "much appreciated"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "I don't understand that."]
}

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "how_are_you": ["I'm just a bot, but I'm doing fine!", "Doing great, thanks for asking!"],
    "name": ["I'm ChatBot, your virtual assistant."],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"]
}

lemmatizer = WordNetLemmatizer()

# Preprocess text
def preprocess(sentence):
    sentence = sentence.lower()
    tokens = word_tokenize(sentence)
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in string.punctuation]
    return tokens

# Match user input to intent
def match_intent(user_input):
    tokens = preprocess(user_input)
    for intent, examples in corpus.items():
        for phrase in examples:
            phrase_tokens = preprocess(phrase)
            if set(phrase_tokens).intersection(tokens):
                return intent
    return "default"

# Chat function
def chatbot():
    print("ChatBot: Hello! I am your assistant. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("ChatBot: Goodbye! 👋")
            break
        intent = match_intent(user_input)
        print("ChatBot:", random.choice(responses.get(intent, corpus["default"])))

# Run the chatbot
chatbot()
