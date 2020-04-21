from win10toast import ToastNotifier #PROGRAMA PARA WINDOWS
import datetime
import time


def main():
    tiempo=1 #para cada vez que itere pasan "tiempo" en segs
    usr=int(input("Por favor Ingrese un numero para empezar la cuenta regresiva: "))
    ter=usr
    for i in range(usr+1):
        ter=ter-1 #tiene que ser uno para que llegue a cero, porbe con otros y solo si el numero ingresado se podia dividir y si daba 0
        print(usr-i)
        time.sleep(tiempo)
        if ter==0:
            toaster = ToastNotifier()
            toaster.show_toast("BOMBA","BOOM!")
main()