import requests

city = 'charlotte'

url = "https://community-open-weather-map.p.rapidapi.com/find"

querystring = {"q":"london","cnt":"0","mode":"null","lon":"0","type":"link, accurate","lat":"0","units":"imperial, metric"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "4adf3b1b96mshbfea239c4b3144dp121a6ajsnab9b3858cb69"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)