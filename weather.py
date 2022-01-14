import http.client
import tkinter

myCity = 'charlotte'

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "4adf3b1b96mshbfea239c4b3144dp121a6ajsnab9b3858cb69"
    }

conn.request("GET", "/weather?q={myCity}&lat=0&lon=0&callback=test&id=2172797&lang=null&units=imperial&mode=xml", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#city weather function
def getWeather():
    try:
        city = cityName.get()
        windowDisplay.delete(tkinter.END)
        windowDisplay.insert(city)
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
cityButton = tkinter.Button(window, text="Search", command=getWeather())
cityButton.grid(row=0, column=2)

#window display
windowDisplay = tkinter.Text(window, height=10, width=60)
windowDisplay.grid(row=1, column=0, columnspan = 4)


window.mainloop()

