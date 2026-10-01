def get_response(user_input):
    """
    Identify the user's intent using keyword-based rules
    and return an appropriate predefined response.
    """

    # Normalize user input
    user_input = user_input.lower().strip()

    # Greeting
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening"]):
        return "Hello! How can I help you today?"

    # Python
    elif any(word in user_input for word in ["python", "python language"]):
        return (
            "Python is a high-level, interpreted programming language "
            "known for its simplicity, readability, and wide range of applications."
        )

    # Artificial Intelligence
    elif (
        "artificial intelligence" in user_input
        or "what is ai" in user_input
        or user_input == "ai"
    ):
        return (
            "Artificial Intelligence (AI) is a field of computer science "
            "that focuses on building systems capable of performing tasks "
            "that normally require human intelligence."
        )

    # Machine Learning
    elif (
        "machine learning" in user_input
        or "what is ml" in user_input
        or user_input == "ml"
    ):
        return (
            "Machine Learning is a branch of AI that allows computers "
            "to learn patterns from data and make predictions or decisions "
            "without being explicitly programmed for every situation."
        )

    # NLP
    elif (
        "nlp" in user_input
        or "natural language processing" in user_input
    ):
        return (
            "Natural Language Processing, or NLP, is a field of AI "
            "that enables computers to understand, process, and generate "
            "human language."
        )

    # Chatbot
    elif "chatbot" in user_input or "what can you do" in user_input:
        return (
            "I am a rule-based chatbot. I identify keywords and patterns "
            "in your message and provide predefined responses."
        )

    # Programming
    elif "programming" in user_input or "coding" in user_input:
        return (
            "Programming is the process of writing instructions that "
            "a computer can execute to solve a problem or perform a task."
        )

    # Help
    elif "help" in user_input:
        return (
            "I can answer basic questions about Python, AI, Machine Learning, "
            "NLP, programming, and chatbots."
        )

    # Thanks
    elif any(word in user_input for word in ["thank you", "thanks", "thank"]):
        return "You're welcome! I'm happy to help."

    # Exit
    elif any(word in user_input for word in ["bye", "exit", "quit", "goodbye"]):
        return "Goodbye! Have a great day!"

    # Fallback
    else:
        return (
            "I'm sorry, I don't understand that question yet. "
            "Try asking me about Python, AI, Machine Learning, NLP, "
            "programming, or chatbots."
        )


def main():
    print("=" * 50)
    print("          RULE-BASED AI CHATBOT")
    print("=" * 50)

    print("\nBot: Hello! I'm your AI assistant.")
    print("Bot: I can answer questions about Python, AI, ML, NLP, and programming.")
    print("Bot: Type 'help' to see what I can do.")
    print("Bot: Type 'bye' to exit.\n")

    while True:

        user_input = input("You: ")

        response = get_response(user_input)

        print("Bot:", response)

        # Stop the conversation when the user exits
        if any(
            word in user_input.lower().strip()
            for word in ["bye", "exit", "quit", "goodbye"]
        ):
            break


if __name__ == "__main__":
    main()