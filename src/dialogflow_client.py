import os
from google.cloud import dialogflowcx_v3beta1 as dialogflow

PROJECT_ID = os.getenv("PROJECT_ID")
LOCATION = "global"
AGENT_ID = os.getenv("AGENT_ID")

def detect_intent_text(session_id, text, language_code="en"):
    client = dialogflow.SessionsClient()
    session_path = f"projects/{PROJECT_ID}/locations/{LOCATION}/agents/{AGENT_ID}/sessions/{session_id}"

    text_input = dialogflow.TextInput(text=text)
    query_input = dialogflow.QueryInput(text=text_input, language_code=language_code)

    response = client.detect_intent(session=session_path, query_input=query_input)
    return response.query_result.response_messages
