import tkinter as tk
import requests as rq
from tkinter import ttk
import pycountry

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Weather App')
        self.configure(bg = '#0F172A')
        
                        
        self.columnconfigure(0,weight = 1)
        self.rowconfigure(0,weight = 1)
        
        frame = InputFrame(self)
        frame.grid(row = 0,column = 0)
  
class InputFrame(tk.Frame):
        def __init__(self,parent):
            super().__init__(parent,bg='#0F172A')
            
            self.columnconfigure(0,weight = 1)
            
            
            self.enter =tk.Entry(self,bg = '#1E293B',fg = '#FFFFFF')
            self.enter.grid(row = 1,column = 0,padx = 10,pady =10)
            self.btn = tk.Button(self,text = 'SUBMIT',bg = '#0EA5E9',fg = '#FFFFFF',command = self.on_click)
            self.btn.grid(row = 2,column = 0,padx = 5,pady = 5)
            self.label1 = tk.Label(self,text = 'Weather App',font = ("Arial",14,"bold"),bg = '#38BDF8')
            self.label1.grid(row = 0,column = 0)
            self.label2 = tk.Label(self,text = "  ",font=("Arial", 10, "bold"),bg='#0F172A', fg='#FFFFFF')
            self.label2.grid(row = 3,column = 0,padx = 5,pady = 5)
            
        def fetch_weather(self,city_name):
            api_key = "3806d8e45ebc87c04a04bc9bd4573bbd"

            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
            
            response = rq.get(url)
            data = response.json()
            
            if data["cod"] == 200:
                self.weather = data["weather"][0]["main"]
                self.temp = data["main"]["temp"]
                self.hum = data["main"] ["humidity"]
                self.ws = round(data["wind"] ["speed"]*3.6,1)
                country_code = data["sys"]["country"] 
                self.country = pycountry.countries.get(alpha_2=country_code).name 
                self.name = data["name"]
                return True
            else:
                return False
            
        def on_click(self):
            self.place = self.enter.get()
            if self.place:
                success = self.fetch_weather(self.place)
                if success:
                    self.label2.config(text = f"{self.name} \nCountry : {self.country} \nWeather : {self.weather} \nTemperature : {self.temp}° C \nHumidity : {self.hum}% \nWind Speed : {self.ws} kph \n")
                else:
                    self.label2.config(text = 'place not found')
                self.enter.delete(0,tk.END)
            
        
    


if __name__ == "__main__":
    app = Application()
    app.mainloop()
