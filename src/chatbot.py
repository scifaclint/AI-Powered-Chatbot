

from utils import preprocess, greeting, generate_response

def chatbot():
    print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
    while True:
        user_response = input().lower()
        if user_response == 'bye':
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif user_response in ['thanks', 'thank you']:
            print("Chatbot: You're welcome!")
            break
        else:
            if greeting(user_response) is not None:
                print("Chatbot:", greeting(user_response))
            else:
                print("Chatbot:", generate_response(user_response))

if __name__ == "__main__":
    chatbot()
