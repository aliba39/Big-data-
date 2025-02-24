import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time

base_url = "https://www.gutenberg.org/browse/scores/top?page="
books = []
page_num = 1

max_pages = 100 

for page_num in tqdm(range(1, max_pages + 1), desc="جلب الكتب", unit="صفحة"):
    url = f"{base_url}{page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    book_links = soup.select("ol li a")
    
    if not book_links:
        print(f"تم الوصول إلى نهاية البيانات بعد {page_num - 1} صفحة.")
        break
    
    for book in book_links:
        title = book.text
        link = "https://www.gutenberg.org" + book["href"]
        books.append((title, link))
    
    time.sleep(1) 

with open("gutenberg_books.txt", "w", encoding="utf-8") as f:
    for title, link in books:
        f.write(f"{title} - {link}\n")

print(f"تم استخراج {len(books)} كتابًا من موقع Gutenberg ✅")
