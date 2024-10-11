import requests
from bs4 import BeautifulSoup

# This helper fuction gets a table with three columns (x,character,y) and 
# prints the decoded message.
def decode_secret_message(extracted_data):
    if not extracted_data:
        return

    # Find grid dimensions based on the maximum x and y coordinates
    max_x = max([data[0] for data in extracted_data])
    max_y = max([data[2] for data in extracted_data])
    
    # Initialize the grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Place the characters in the grid
    for x, character, y in extracted_data:
        grid[y][x] = character
    
    # Print the grid
    for row in grid:
        print(''.join(row))


# Function to scrape Google Doc
def scrape_google_doc(url):
    # Step 1: Fetch the document's HTML content
    response = requests.get(url)
    
    # Ensure the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve document: {response.status_code}")
        return
    
    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 3: Extract the table rows (assuming there's only one table in the doc)
    table = soup.find('table')
    if not table:
        print("No table found in the document.")
        return
    
    # Extract rows and columns (assuming the structure is <tr> for rows, <td> for columns)
    data = []
    skip_first_row = True # the first row is header
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        if len(columns) == 3:  # Assuming 3 columns (x, Character, y)
            if skip_first_row:
                skip_first_row = False
                continue
            x_coord = int(columns[0].get_text().strip())
            char = columns[1].get_text().strip()
            y_coord = int(columns[2].get_text().strip())
            data.append((x_coord, char, y_coord))
    

    # decode the raw data
    decode_secret_message(data[1:])

# Example usage
google_doc_url = 'https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub'
scrape_google_doc(google_doc_url)