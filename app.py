from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)


model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        size = float(data.get('size'))
        if size <= 0:
            return jsonify({'error': 'Size must be a positive number.'}), 400

        # Predict using the model
        prediction = model.predict(np.array([[size]]))
        return jsonify({'prediction': prediction[0]})
    except ValueError:
        return jsonify({'error': 'Invalid input. Please enter a numeric value.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
