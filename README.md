# metweather Project

## Overview
The metweather project is a Django-based web application that provides weather data through a RESTful API. It allows users to retrieve weather information by sending requests to specific endpoints.

## Project Structure
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

## Docker Setup
To build and run the application using Docker, use the following commands:
```
docker-compose up --build
```

## API Endpoints
- **Weather Summary**: `POST /weather-summary/`
  - Expects a JSON body with a `dataset_url` field.
  
- **Weather List**: `GET /weather-list/`
  - Returns a list of all weather data entries.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.