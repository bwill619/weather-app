import http.client
import tkinter

#tkinter creation
window = tkinter.Tk()
window.title("City Weather App")

#label
cityLabel = tkinter.Label(window, text="City Name")
cityLabel.grid(row=0, column=0)

#textbar
cityName = tkinter.StringVar()
cityText = tkinter.Entry(window, textvariable=cityName)
cityText.grid(row=0, column=1)

#button

#window display


window.mainloop()



#API call
conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "4adf3b1b96mshbfea239c4b3144dp121a6ajsnab9b3858cb69"
    }

conn.request("GET", "/find?q=charlotte&mode=null&lon=0&type=link%2C%20accurate&lat=0&units=imperial%2C%20metric", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


