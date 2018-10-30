import json, requests
# Information for weather of New York City:
latitude = "40.7141667"
longitude = "-74.0063889"
api_key = "d2f730b58dff4f9beda20db37e3973d0"
#latitude = input("What is the latitude?")
# Asks user for latitude
#longitude = input("What is the longitude?")
# Asks user for longitude
#api_key = input("What is your api key?")
# Asks user for api key
arr = [api_key, latitude, longitude]
# Puts all the input into an array

def url(arr):
    url = "https://api.darksky.net/forecast/"+arr[0]+"/"+arr[1]+","+arr[2]
    # creates the url using information from the array
    return(url)

url = url(arr)
# Sets the url under the variable url by calling the function above.

data = requests.get(url).json()
# Requests to program to make the api call

ans = input("Do you want to know the percent humidity, temp, summary or all three?")
# Asks the user value they are looking for

def info(request):
    for x in arr:
        temp = data["currently"]["temperature"]
        summary = data['currently']['summary']
        percentage = data["currently"]["humidity"]
        if request == "percent humidity":
            percentage = percentage*100
            # Converts decimal value into a percentage
            return percentage
            # outputs the percentage
        elif request == 'temp':
            return temp," degrees Fahrenheit"
            # outputs temperature in degrees Fahrenheit
        elif request == "summary":
            return "It is currently ",summary
            # outputs the summary in a sentence
        elif request == "all three":
            return "It is currently ",summary,".",temp," degrees Fahrenheit and there is",percentage," percent humidity"
print(info(ans))
# Calling the function using the answer from the question asked before
