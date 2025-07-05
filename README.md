# MetWeather

MetWeather is a Django-based web application for uploading, processing, and visualizing weather data. Users can submit a dataset URL, and the app will extract, store, and display weather summaries in a user-friendly interface.

## Features

- Upload weather datasets via URL
- Extract and store weather data in a database
- REST API endpoints for weather data
- Responsive web UI for searching and viewing weather summaries

## Project Structure

- `metweather/` – Django project settings and configuration
- `weather/` – Main app with models, views, serializers, templates, and utilities
- `db.sqlite3` – SQLite database file

```
metweather/
├── weather/
│   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── utils.py
│   ├── views.py
│   └── templates/
│       └── index.html
├── metweather/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd metweather
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the database (if applicable):
   ```
   python manage.py migrate
   ```

## Running the Application
To run the application locally, use the following command:
```
python manage.py runserver
```

## Access the app

   Open [http://localhost:8000/](http://localhost:8000/) in your browser.

## Docker Setup
To build and run the application using Docker, use the following commands:
```
docker-compose up --build
```

## API Endpoints

- `POST /api/summary/`  
  Extracts weather data from a provided dataset URL.  
  **Body:** `{ "dataset_url": "<url>" }`

- `GET /api/weather/`  
  Returns all stored weather data.

## File Overview

- [weather/views.py](weather/views.py): Main API and view logic ([`WeatherSummaryAPIView`](weather/views.py), [`WeatherListAPIView`](weather/views.py))
- [weather/models.py](weather/models.py): Weather data model ([`WeatherData`](weather/models.py))
- [weather/serializers.py](weather/serializers.py): Serializers for API responses ([`WeatherDataSerializer`](weather/serializers.py))
- [weather/utils.py](weather/utils.py): Data extraction logic ([`extract_data`](weather/utils.py))
- [weather/templates/index.html](weather/templates/index.html): Main web UI

## Customization

- Update `weather/utils.py` to support new dataset formats.
- Modify `weather/templates/index.html` for UI changes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
