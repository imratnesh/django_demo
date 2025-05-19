import ollama


def chat_with_model(user_input):
    # What is capital of Germany?
    client = ollama.Client(
        host="http://localhost:11434")  # Ensure server is running
    generate_args = {
        "model": "mistral",
        "prompt": f"User: {user_input}\nAssistant:",
        "options": {
            "max_tokens": 4096,
            "temperature": 0.7
        }
    }
    response = client.generate(**generate_args)
    return response["choices"][0]["text"].strip()


# Chat interface
if __name__ == "__main__":
    print("Welcome to the Mistral Chat App!")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        answer = chat_with_model(user_query)
        print(f"Bot: {answer}")
