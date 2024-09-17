import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)  # Corrected __name__

API_KEY = 'ba5f91612db506e0ee7a9c911b83a244'  # Replace with your actual API key

# Route to serve the frontend HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the weather API request with real data
@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')

    if city:
        # Make an API call to the real weather API
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'error': 'No city provided'}), 400

if __name__ == "__main__":  # Corrected __name__ and __main__
    app.run(debug=True)
