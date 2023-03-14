from serpapi import GoogleSearch

params = {
  "q": "Apple",
  "tbm": "isch",
  "ijn": "0",
  "api_key": "2c6fb04e9977afd291124be243194a28b0cfa1a1b6c960a98e8e1d08308787a6"
}

search = GoogleSearch(params)
results = search.get_dict()
images_results = results["images_results"]
#def display_results():
