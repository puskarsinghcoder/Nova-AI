from ai_engine import process_message
from actions import send_reply

print("================================")
print("        🤖 NOVA AI")
print("================================")
print("NOVA AI is running...")
print("Type 'exit' to stop.\n")

while True:
    message = input("You: ")

    if message.lower().strip() == "exit":
        print("NOVA AI: Goodbye! 👋")
        break

    reply = process_message(message)

    send_reply(reply)
