from flask import Flask, render_template, request, jsonify

app= Flask(__name__)

# Basic route to serve the chatbot page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Process the user message and generate a response
    bot_response= process_message(response)
    return jsonify({'response': bot_response})

def process_message(response):
    # Replace with OpenAI methods.
    return f"Echo: {message}"

if __name__ == '__main__':
    app.run(debug=True)