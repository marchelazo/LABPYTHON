import requests 
from win10toast import ToastNotifier #PROGRAMA PARA WINDOWS


response = requests.get('https://api.gyazo.com')#Utilize este sitio porque no estaba en linea, usar 'https://www.isitdownrightnow.com/' para porbar sitios
if response.status_code == 200:
    toaster = ToastNotifier()
    toaster.show_toast(f"UPTIME CHECKER","EL SITIO INGRESADO ESTA EN LINEA")
else:
        toaster = ToastNotifier()
        toaster.show_toast(f"UPTIME CHECKER","EL SITIO INGRESADO NO EN LINEA")


