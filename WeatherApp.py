import tkinter as tk
from tkinter import font
import requests

h = 500
w = 600

def test_function(a):
    print("Text Entered in Entry is :",a) 
def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temperature = weather['main']['temp']

        final_str = "City: %s \nConditions: %s \nTemperature (°C): %s" % (name, description, temperature)
    except:
        final_str = "Oops!! \nThere was a problem retrieving that information !!"

    return final_str


def get_weather(city):
    weather_key = "ec322ec2c5650f6ca414eebde213f3df"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = { 'AppID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json() # json will convert the response into Python Dictionary
    label['text'] = format_response(weather)
   # print(weather['name'])
   # print(weather['weather'][0]['description'])
   # print(weather['main']['temp'])

root = tk.Tk()

canvas = tk.Canvas(root, height=h, width=w)
canvas.pack()

background_image = tk.PhotoImage(file = "landscape.png") # or put complete path of the image
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1 , relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=5)
frame.place(relwidth=0.75, relheight=0.1, relx=0.5, rely=0.1, anchor="n") # anchor="n" to put frame in centre

entry = tk.Entry(frame, font=('Microsoft Himalaya',22))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Show Weather", font=('Microsoft Himalaya',18), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n") # anchor="n" to put frame in centre

label = tk.Label(lower_frame, font=('Microsoft Himalaya',25) ,anchor="nw", justify="left", bd=4)
label.place(relwidth=1, relheight=1)

# print(tk.font.families()) # to know all the fonts present in tkinter

root.mainloop()


