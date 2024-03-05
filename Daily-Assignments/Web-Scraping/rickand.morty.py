#fetch the following data from rick and morty API:
#20 characters
#20 locations
#20 episode

import requests

url = "https://rickandmortyapi.com/api/"

# Fetch 20 characters
characters_response = requests.get(url + "character/")
characters_data = characters_response.json()
characters = characters_data['results'][:20]
print(characters)

# Fetch 20 locations
locations_response = requests.get(url + "location/")
locations_data = locations_response.json()
locations = locations_data['results'][:20]
print(locations)

# Fetch 20 episodes
episodes_response = requests.get(url + "episode/")
episodes_data = episodes_response.json()
episodes = episodes_data['results'][:20]
print(episodes)

#NB : The 'results' key is commonly used to store the actual data that is being returned by the API request.