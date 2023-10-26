from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/postback', methods=['POST'])
def postback():
    data = request.get_data()
    # Decode the JSON payload
    payload = json.loads(data.decode('utf-8'))
    print (payload)
    # Handle the payload, e.g., update your order status
    # You can access payload['status'], payload['order_id'], etc.

    # Return a response, e.g., an acknowledgment
    return "Postback received successfully"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443)
