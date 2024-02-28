# Project Overview

This project involves retrieving addresses for official boutiques of designer brands and service stations around designer outlets. Two tasks have been divided into two separate scripts, `task1.py` and `task2.py`, each with its specific functionality.


## Task 1 - `task1.py`

### Description
This script extracts addresses of official boutiques for the Cartier brand in the UK, specifically in London. It utilizes web scraping techniques to parse the Cartier store locator webpage and retrieves the required information.

### Steps
1. Make a request to the Cartier store locator page.
2. Parse the HTML content using BeautifulSoup.
3. Extract the relevant data from the script element on the webpage.
4. Convert the data into a pandas DataFrame and rename columns.
5. Save the addresses to a CSV file.

## Task 2 - `task2.py`

### Description
This script focuses on retrieving addresses for service stations around designer outlets using Google Maps links. It follows a similar approach to web scraping, extracting information from the HTML content of the Google Maps link.

### Steps
1. Make a request to the Google Maps link for service stations.
2. Parse the HTML content using BeautifulSoup.
3. Extract the relevant data, which may involve finding specific HTML elements.
4. Save the addresses to a CSV file.

## How to Run

1. Ensure you have the required libraries (`requests`, `BeautifulSoup`, `pandas`) installed.
2. Execute `main.py` to run the tasks.

## Notes

- Ensure internet connectivity for web scraping tasks.
- Check for potential changes in website structures that may affect the web scraping process.
- The CSV files (`addresses.csv`) will be generated in the same directory as the scripts.

Feel free to adapt and modify the code to suit your specific needs.


