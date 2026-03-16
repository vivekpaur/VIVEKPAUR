from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample endpoint for home
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the Flask Backend!'}), 200

# Sample endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    # Example prediction logic
    prediction = some_ml_model.predict(data['input'])  # Replace with your ML model's prediction method
    return jsonify({'prediction': prediction}), 200

# Sample endpoint to get all data
@app.route('/data', methods=['GET'])
def get_data():
    # Here you would retrieve data from your database or source
    data = retrieve_data()  # Replace with your method to retrieve data
    return jsonify({'data': data}), 200

if __name__ == '__main__':
    app.run(debug=True)