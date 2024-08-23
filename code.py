import pandas as pd
import requests

def get_city(latitude, longitude, api_key):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json().get('results', [])
        if results:
            for component in results[0]['address_components']:
                if 'locality' in component['types']:
                    return component['long_name']
                elif 'administrative_area_level_1' in component['types']: #If you want district information, you need to do 2
                    return component['long_name']
    return "Not Found"

api_key = 'YOUR_API_KEY_HERE' #Your API key that you can access from Google Cloud Platform
data = pd.read_csv('C:/path_to_your_file.csv') #File containing coordinates
data['City'] = data.apply(lambda row: get_city(row['Latitude'], row['Longitude'], api_key), axis=1)
data.to_excel('C:/path_to_save_file.xlsx', index=False) #Output
