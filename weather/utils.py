import requests
from .models import WeatherData

month_names = [
    "january", "february", "march", "april", "may", "june", 
    "july", "august", "september", "october", "november", "december"
]

def extract_data(url):
    """
    Fetches summary data from the given link.
    
    Args:
        link (str): The URL to fetch the summary data from.
        
    Returns:
        dict: Parsed JSON data from the response.
    """
    try:
        response = requests.get(url)
        lines = response.text.splitlines()
        data_start = 7  # after header lines

        for line in lines[data_start:]:
            parts = line.strip().split()
            if len(parts) < 13:
                continue

            year = int(parts[0])
            monthly_values = parts[1:13]

            WeatherData.objects.update_or_create(
                year=year,
                defaults={month_names[i]: float(monthly_values[i]) if monthly_values[i] != '---' else None for i in range(12)}
            )
        data = WeatherData.objects.all()
        return data
    except requests.RequestException as e:
        print(f"Error fetching summary data: {e}")
        return {}
