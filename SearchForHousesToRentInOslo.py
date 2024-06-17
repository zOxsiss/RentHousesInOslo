import requests
from bs4 import BeautifulSoup


url = "https://www.finn.no/realestate/lettings/search.html?location=0.20061"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

# Find house
element = soup.find(id="page-results")
houses = element.find_all(class_="col-span-2 mt-16 flex justify-between sm:mt-4 sm:block space-x-12 font-bold whitespace-nowrap")
address = element.find_all(class_="text-14 text-gray-500")
print(houses[0].text)
n = 0  # House id
# House address, price and size in m^2
for price in houses:
    if address[n].text == "Oslo":
        n += 1
        continue
    else:
        print(address[n].text, n)
        size, sep, amount = price.text.partition('m²')
        print(amount.rstrip("kr"), n)
        print(size, sep, n)
        print("  ")
        n += 1
