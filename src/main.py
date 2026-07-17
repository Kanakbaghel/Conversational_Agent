from dialogflow_client import detect_intent_text

if __name__ == "__main__":
    session_id = "test-session"
    user_input = input("You: ")
    responses = detect_intent_text(session_id, user_input)
    for r in responses:
        print("Bot:", r.text.text[0])
