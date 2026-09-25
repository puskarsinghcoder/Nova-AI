def process_message(message):
    text = message.lower().strip()

    if text == "heyy":
        return "Hello 👋 How can I help you?"

    elif text == "hello":
        return "Heyy 👋 How can I help you?"

    elif text == "hi":
        return "Hello 👋 How can I help you?"

    elif text in ["thanks", "thank you"]:
        return "You're welcome! 😊"

    elif text in ["bye", "goodbye"]:
        return "Goodbye! 👋"

    else:
        return "I received your message. 🤖"
