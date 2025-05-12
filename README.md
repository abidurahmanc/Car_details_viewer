# Car Details Web Application

A simple web app built with Flask that allows users to select a car from a dropdown menu and view its details and image.
Car details are loaded from a CSV file, and images are fetched dynamically from Google Image Search.

---

## Features

- 🔍 Searchable dropdown list of cars using Select2.
- 📄 Detailed specifications displayed on selection.
- 🖼️ Live car image fetched from Google.
- 🧩 Responsive and clean UI.
- 📊 Data-driven using a CSV file.

---

## How It Works

* Car names are loaded from newCarsIndia.csv into a dropdown using Jinja2.
* When a user selects a car and clicks "Get Details", an AJAX request is sent to the Flask backend.
* The backend filters the car’s details and fetches an image via Google Image scraping.
* Details and image are returned and displayed dynamically.

## Screenshots
![Screenshot 2025-05-12 164117](https://github.com/user-attachments/assets/367bd985-478f-49ed-82b4-2d6db54f9e5a)

![Screenshot 2025-05-12 164204](https://github.com/user-attachments/assets/1e5e58c3-1da7-4b1a-851e-9582b62449d3)

![Screenshot 2025-05-12 164145](https://github.com/user-attachments/assets/a340500a-54bf-46de-a0d3-70e7846f8f12)
