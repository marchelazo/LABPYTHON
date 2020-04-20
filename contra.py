##Password Generator
import random

caracteres = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$_"

largo = input("Ingrese el largo de su contraseña: ")
largo = int(largo)

contra = ''

for l in range(largo):
        contra += random.choice(caracteres)
        print(contra)