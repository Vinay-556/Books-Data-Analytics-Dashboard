
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import os

# 1. Website URL
url = "https://books.toscrape.com/"

# 2. Send request
response = requests.get(url, timeout=20)

print("Status Code:", response.status_code)

if response.status_code == 200:

    print("Connected successfully!")

    # 3. Create soup
    soup = BeautifulSoup(response.content, 'lxml')

    # 4. Find all book containers
    books = soup.find_all(
        'article',
        class_='product_pod'
    )

    print("Total Books:", len(books))
    print("\n========== BOOK DETAILS ==========\n")

    # 5. Extract book details
    book_data = []
    for index, book in enumerate(books, start=1):

        # Book name
        name = book.h3.a['title']

        # Book price
        price = book.find(
            'p',
            class_='price_color'
        ).get_text(strip=True)

        # Book rating
        rating = book.p['class'][1]

        # Availability
        availability = book.find(
            'p',
            class_='instock availability'
        ).get_text(strip=True)

        # Book link
        relative_link = book.h3.a['href']

        link = urljoin(url, relative_link)

        book_data.append({
            'Name': name,
            'Price': price,
            'Rating': rating,
            'Availability': availability,
            'Link': link
        })

       

        # Display details
        print("Book Number:", index)
        print("Name:", name)
        print("Price:", price)
        print("Rating:", rating)
        print("Availability:", availability)
        print("Link:", link)

        print("----------------------------------")

    # 6. Save to CSV
    # Save data into CSV
    print("CSV Location:", os.getcwd())
    
    with open('books_data.csv', 'w', newline='', encoding='utf-8-sig') as file:

        fieldnames = ['Name', 'Price', 'Rating', 'Availability', 'Link']

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(book_data)

    print("CSV file saved successfully!")
else:

    print("Connection failed:", response.status_code)
