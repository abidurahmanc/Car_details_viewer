from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# Load the dataset
df = pd.read_csv("newCarsIndia.csv")
car_names = df['Car'].unique().tolist()

PLACEHOLDER_IMAGE = "https://via.placeholder.com/300?text=Image+Not+Found"

def fetch_car_image(car_name):
    """Fetch the first image URL from Google Image Search dynamically."""
    search_url = f"https://www.google.com/search?tbm=isch&q={car_name}+car"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(search_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            image_tags = soup.find_all("img")
            for img_tag in image_tags[1:]:  # Skip first image (Google logo)
                image_url = img_tag["src"]
                if image_url.startswith("http"):
                    return image_url
    except Exception as e:
        print(f"Error fetching image for {car_name}: {e}")
    
    return PLACEHOLDER_IMAGE


@app.route('/')
def home():
    return render_template('index.html', car_names=car_names)

@app.route('/get_car_details', methods=['POST'])
def get_car_details():
    car_name = request.form.get("car_name")
    result = df[df['Car'] == car_name]
    
    if not result.empty:
        car_details = result.to_dict(orient='records')[0]
        image_url = fetch_car_image(car_name)
        return jsonify({"car_details": car_details, "image_url": image_url})
    
    return jsonify({"error": "Car not found in dataset.", "image_url": PLACEHOLDER_IMAGE})

if __name__ == '__main__':
    app.run(debug=True)


