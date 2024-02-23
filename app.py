from rasa.core.agent import Agent
from flask import Flask, request, jsonify

app = Flask(__name__)
model_path = "./modelRasa.gz"

# Load the Rasa model
agent = Agent.load(model_path)

@app.route("/predict", methods=["POST"])
async def predict():
    # Get the message from the request body
    data = request.get_json(force=True)
    message = data.get("message")

    # Handle missing message gracefully (optional)
    if not message:
        return jsonify({"error": "Missing message in request body"})

    # Process the message with Rasa (await the coroutine)
    response = await agent.handle_text(message)

    # Return the JSON-formatted response
    return jsonify(response)


if __name__ == "__main__":
    app.run()
