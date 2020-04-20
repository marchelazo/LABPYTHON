import random, string


libreriacarr=["COMPUTER SCIENCE","INGENIERIA EMPRESARIAL","ADMINISTRACION"]
libreriaamigo=["Tuki","Paola","GE","Mencos"]
libreriaedad=["18","19","20"]




historia_lenght=200

historieta= libreriaamigo + libreriacarr + libreriaedad

texto=""
texto2=""
texto3=""

#print(historieta)

for i in range(0,historia_lenght):
    aleatorio=random.randint(0,len(historieta)-1)
    texto+=historieta[aleatorio]
    aleatorio=random.randint(0,len(historieta)-1)
    texto2+=historieta[aleatorio]
    aleatorio=random.randint(0,len(historieta)-1)
    texto3+=historieta[aleatorio]

    print(f"Habia una vez un estudiate de  {texto} que comia tanto que se empezo a caer de su silla porque su silla que habia llamado {texto2} no tenia estilo ergonomico y ya estaba vieja tenia como {texto3} años  y eso no le gustaba a {texto}\n")
    break