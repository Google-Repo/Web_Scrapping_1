###########WEB-SCRAPING-1###############
###########PROJECT-SCRAPE THE DATA FROM WIKIPEDIA STARS DATA#############

#importing all modules here:

from bs4 import BeautifulSoup
import requests
import time
import csv

# Configuring the URL
START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

# Send a GET request to the URL
response = requests.get(START_URL)

# Sleep to ensure the page loads completely (you can adjust the time)
time.sleep(5)

# Create a function to scrape the data
def scrape():
    headers = ["Proper name", "Distance", "Mass", "Radius"]
    empty_data = []
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find the table containing the star data
    table = soup.find("table", {"class": "wikitable"})

    # Loop through table rows
    for row in table.find_all("tr")[1:]:  # Skip the header row
        columns = row.find_all("td")
        temp_list = []

        for column in columns:
            temp_list.append(column.get_text(strip=True))

        # Append data to the empty_data list
        empty_data.append(temp_list)

    # Write data to a CSV file
    with open("scrapper_2.csv", "w", newline="", encoding="utf-8") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(empty_data)

# Call the scrape function
scrape()
