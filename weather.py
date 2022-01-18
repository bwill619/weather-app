import http.client
import tkinter
import requests
print(requests.__file__)

api = 'http://api.openweathermap.org/data/2.5/weather?=q'
myCity = 'charlotte'

units = '&imperial'
url = api + myCity + apiKey + units

#city weather function
def getWeather():
    try:
        url = api + myCity + apiKey + units
        weather = requests.get(url).json(['main'])
        currWeather = "The temperature is currently: " + str(weather['temp'])
        #windowDisplay.delete('1.0', tkinter.END)
        #windowDisplay.insert('1.0', currWeather)
    except:
        print("error")







#tkinter creation
window = tkinter.Tk()
window.title("City Weather App")

#label
cityLabel = tkinter.Label(window, text="Enter City Name:")
cityLabel.grid(row=0, column=0)

#textbar
cityName = tkinter.StringVar()
cityText = tkinter.Entry(window, textvariable=cityName)
cityText.grid(row=0, column=1)

#button
#cityButton = tkinter.Button(window, text="Search", command=getWeather())
#cityButton.grid(row=0, column=2)

#window display
windowDisplay = tkinter.Text(window, height=10, width=60)
windowDisplay.grid(row=1, column=0, columnspan = 4)


window.mainloop()

