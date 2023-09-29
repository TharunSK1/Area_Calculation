import requests
from bs4 import BeautifulSoup
import pandas
import connect

# Specify the number of pages to parse and the database name here
page_num_MAX = 3  # Replace with the desired number of pages
db_name = "Oyo Hotels.db"  # Replace with your desired database filename

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
scraped_info_list = []
connect.connect(db_name)

for page_num in range(1, page_num_MAX + 1):  # Include the last page
    url = oyo_url + str(page_num)
    print("Get Request for: " + url)
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"] = hotel.find("h3", {"class": "listingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streeAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "listingPrice_finalPrice"}).text

        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "hotelRating_ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"] = None

        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list = []
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper_amenity"}):
            amenities_list.append(amenity.find("span", {"class": "d-body-sm"}).text.strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)
        connect.insert_into_table(db_name, tuple(hotel_dict.values()))

dataFrame = pandas.DataFrame(scraped_info_list)
print("Creating csv file...")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(db_name)
