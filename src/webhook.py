from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(force=True)
    intent = req.get("fulfillmentInfo", {}).get("tag")

    if intent == "book_flight":
        return jsonify({"fulfillment_response": {"messages": [{"text": {"text": ["Flight booked successfully!"]}}]}})
    else:
        return jsonify({"fulfillment_response": {"messages": [{"text": {"text": ["Sorry, I didn’t understand."]}}]}})

if __name__ == "__main__":
    app.run(port=8080, debug=True)
