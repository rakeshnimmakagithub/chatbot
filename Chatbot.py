import random

def simple_chatbot():
    print("Hello! I'm your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        # Check if the user wants to exit
        if user_input.lower() == 'bye':
            print("Goodbye! Have a great day.")
            break

        # Simple responses
        greetings = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
        questions = ["How are you?", "What can I do for you?", "Anything on your mind?"]
        affirmations = ["That's great!", "Awesome!", "Good to hear!"]
        farewells = ["Goodbye!", "See you later!", "Take care!"]

        # Get a random response based on user input
        if '?' in user_input:
            bot_response = random.choice(["I'm not sure. What do you think?", "Why do you ask that?", "Interesting question!"])
        elif 'good' in user_input or 'fine' in user_input or 'well' in user_input:
            bot_response = random.choice(affirmations)
        elif 'bye' in user_input:
            bot_response = random.choice(farewells)
        elif any(greeting in user_input.lower() for greeting in ['hello', 'hi', 'hey']):
            bot_response = random.choice(greetings)
        else:
            bot_response = random.choice(["I'm not sure I understand.", "Could you please rephrase that?", "Tell me more!"])

        print(f"Bot: {bot_response}")

if __name__ == "__main__":
    simple_chatbot()

