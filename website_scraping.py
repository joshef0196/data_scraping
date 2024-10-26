import requests
from bs4 import BeautifulSoup
import os

# URL of the page to scrape
url = "https://subslikescript.com/movie/Pie_in_the_Sky-13628362"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Check if request was successful 

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Try to locate the transcript text by its class "full-script"
transcript = soup.find("div", class_="full-script")

# Check if the transcript is found
if transcript:
    script_text = transcript.get_text(separator="\n")
else:
    # If not found, print the structure of the page to troubleshoot
    print("Transcript not found. Here is the page structure:")
    print(soup.prettify()[:1000])  # Print first 1000 characters of the HTML for inspection
    script_text = "Transcript not found."

# Define the path to save the file on the desktop
desktop_path = os.path.join(os.path.expanduser("~"), "Documents", "Titanic_transcript.txt")

# Save the script to a .txt file on the desktop
with open(desktop_path, "w", encoding="utf-8") as file:
    file.write(script_text)

print(f"Transcript saved to {desktop_path}")
