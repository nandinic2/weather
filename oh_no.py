# Make http requests
import requests
url = 'https://api.nasa.gov/neo/rest/v1/feed?start_date=2018-10-23&end_date=2018-10-23&api_key=840Z9eF8rBWjajJAfWhW4ZbiTyWcL7ZYBZp95Scl'
# API call
data = requests.get(url)
print(data.text)
how_many = data['element_count']
print(how_many)
