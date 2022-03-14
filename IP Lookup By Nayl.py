import requests
import time

ip = input(" Enter IP : ")
print("")

response = requests.get("http://ip-api.com/json/" + ip).json()
print(response)

print(response['lat'])
print(response['lon'])
print("")
input("Appuier sur entrée pour en savoir plus ! ")
input("By Nayl")
input ("Bientot la V2")
input ("")

from pystyle import Colors, Colorate
text = "Enter IP!"
input(Colors.blue + text)