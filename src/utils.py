
import nltk
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = nltk.stem.WordNetLemmatizer()

# Sample corpus for the chatbot
corpus = """
Hello! I am an AI-powered chatbot. How can I assist you today?
I can help you with general information, answer questions, or just chat with you.
Feel free to ask me anything, and I'll do my best to respond!
"""

# Tokenizing 
sent_tokens = nltk.sent_tokenize(corpus)
word_tokens = nltk.word_tokenize(corpus)

def preprocess(text):
    """Preprocess the text by tokenizing and lemmatizing."""
    tokens = nltk.word_tokenize(text.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in string.punctuation]
    return lemmatized_tokens

def greeting(sentence):
    """Return a greeting response if the user's input is a greeting."""
    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey")
    GREETING_RESPONSES = ["Hello!", "Hi!", "Hey!", "Greetings!", "How can I assist you today?"]
    
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def generate_response(user_input):
    """Generate a response to the user's input."""
    chatbot_response = ''
    sent_tokens.append(user_input)
    
    tfidf_vectorizer = TfidfVectorizer(tokenizer=preprocess, stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(sent_tokens)
    
    cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix)
    similar_index = cosine_similarities.argsort()[0][-2]
    
    flat = cosine_similarities.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if req_tfidf == 0:
        chatbot_response = "I'm sorry, I didn't understand that. Could you rephrase?"
    else:
        chatbot_response = sent_tokens[similar_index]
    
    sent_tokens.remove(user_input)
    
    return chatbot_response
