#Overview
This Python script utilizes the Google Maps Geocoding API to determine the city names based on latitude and longitude coordinates. It reads a dataset from a CSV file, processes each record to fetch the corresponding city, and saves the enriched dataset with city names into an Excel file.

#Features
#API Integration: Integrates with Google Maps Geocoding API to retrieve city names based on geographic coordinates.
#Data Processing: Automatically processes a CSV file containing latitude and longitude data, appending the city information to each record.
#Output File: Outputs the processed data into an Excel file, making it easy to view and share the enriched dataset.

#Requirements
#Python: This script is written in Python and requires Python to be installed on your system.
#Pandas Library: Utilized for data manipulation and reading/writing files.
#Requests Library: Used to make HTTP requests to the Google Maps API.

#Setup
Ensure Python is installed on your system. You can download it from python.org. Install the required Python libraries using pip. Obtain an API key from Google Cloud Console for accessing the Google Maps Geocoding API. Replace 'YOUR_API_KEY_HERE' in the script with your actual API key.

#Usage
Ensure your data is in a CSV format with at least two columns for latitude and longitude. Update the file path in the script to point to your CSV file. Execute the script using Python. The script will read the input file, process each row to append city information, and save the results in an Excel file at the specified path.

#Considerations
The Google Maps Geocoding API is subject to usage limits and potential costs. Ensure you understand the billing aspects before heavy usage. Since the script processes potentially sensitive geographic data, ensure that you handle the data in compliance with applicable data protection laws.

#Support
For any issues or queries related to this script, please create an issue in the repository or contact the maintainer at ahmetaltunsuceng@gmail.com
