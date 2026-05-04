def chatbot():
    print("🤖 Welcome to ShopEasy Customer Support!")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("🤖 Bot: Thank you for visiting ShopEasy. Have a great day!")
            break

        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Bot: Hello! How can I help you today?")

        elif "hours" in user_input or "time" in user_input:
            print("🤖 Bot: We are open from 9 AM to 9 PM, Monday to Saturday.")

        elif "product" in user_input:
            print("🤖 Bot: We offer electronics, clothing, and home appliances.")

        elif "order" in user_input:
            print("🤖 Bot: Please provide your order ID to check the status.")

        elif "contact" in user_input or "support" in user_input:
            print("🤖 Bot: You can contact us at support@shopeasy.com or call 1800-123-456.")

        else:
            print("🤖 Bot: Sorry, I didn't understand that. Can you rephrase?")


# Call the function
chatbot()