def get_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"
    elif "how are you" in user_input:
        return "I'm doing well, thank you for asking."
    elif "what is your name" in user_input:
        return "I am a simple chatbot."
    elif "bye" in user_input or "goodbye" in user_input:
      return "Goodbye!"
    else:
        return "I'm not sure I understand. Can you please rephrase?"

print("Simple Chatbot started. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: " + get_response(user_input))
        break
    response = get_response(user_input)
    print("Chatbot:", response)