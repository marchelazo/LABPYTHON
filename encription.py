#Encode Marcelo Garcia 

encode = {0:1,1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:0}

nums = []
cant = int(input("INGRESE LA CANTIDAD DE NUMEROS QUE DESEA ENCRIPTAR : "))
print("INGRESE LOS NUMEROS QUE DESEA CONVERTIR")

for r in range(cant):
    convert = int(input())
    nums.append(convert)
print(f"PRIMEROS NUMEROS (SIN ENCRIPTAR) : {nums}")

numsact =[]
for r in range(len(nums)):
    numsolos = nums[r]
    for r in range(len(encode)):
        if numsolos == r:
            nuevonum = encode[r]
            numsact.append(nuevonum)

print(f"LOS NUEVOS NUMEROS (YA ENCRIPTADOS): {numsact}")
print("SI DESEA DESENCRIPTARLOS RESTELE '1' A CADA NUMERO ")



