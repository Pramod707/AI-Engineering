from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

print(api_key)









# Create a new post
# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# headers = {
#     "content-type" : "application/json",
#     "accept" : "application/json"
# }
# data = {
#     "title" : "first post",
#     "body" : "this is my first post",
#     "id" : 3
# }

# response = requests.post(url,data,headers)

# print(response.status_code)
# print(response.json())


# # Get the current temperature
# import requests

# def get_Weather(longitude,latitude):
#    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
#    response = requests.get(url)
#    data = response.json()
#    return data["current"]["temperature_2m"]

# paris = get_Weather(2.35,48.85)
# london = get_Weather(-0.125,51.51)
# hyderabad = get_Weather(78.47,17.38)

# print(paris,london,hyderabad)