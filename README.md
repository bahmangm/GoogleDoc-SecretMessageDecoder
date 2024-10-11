# GoogleDoc-SecretMessageDecoder

During an initial interview, I was provided with a link to a Google Doc containing a table like the one below, and I was asked to decode the message within the file.

![image](https://github.com/user-attachments/assets/d89e1883-0332-4965-932e-ba1c841cce4f)


This Python script scrapes data from a public Google Doc, extracts a table with coordinates and characters, and decodes a hidden message by placing the characters in a grid based on their coordinates.


## Features

- Scrapes the content of a Google Doc using the `requests` library.
- Extracts a table with three columns: x-coordinate, character, and y-coordinate.
- Places the characters into a grid and prints the decoded message.
- Uses `BeautifulSoup` to parse and extract HTML content.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bahmangm/GoogleDoc-SecretMessageDecoder.git
   cd GoogleDoc-SecretMessageDecoder

2. Install required dependencies:
   ```bash
   pip install requests beautifulsoup4

## Usage

1. Update the script with the Google Doc URL you want to scrape.

2. Run the script:
   ```bash
   python script.py
3. The decoded message will be printed in the terminal.

## Example

Here's an example Google Doc URL for testing:

[Google Doc Example](https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub)

## License

This project is licensed under the MIT License.
