from flask import Flask, request

# Create a Flask web application
app = Flask(__name__)

# Define a route for receiving messages via HTTP POST requests
@app.route('/send', methods=['POST'])
def receive_message():
    # Get the JSON data from the request
    data = request.json
    # Print the received message to the server console
    print(f"Received: {data['message']}")
    # Return a JSON response indicating acknowledgment
    return {'response': 'ACK'}

# Start the Flask application if this script is executed directly
if __name__ == '__main__':
    # Run the app in debug mode and allow threaded requests
    app.run(debug=True, threaded=True)
