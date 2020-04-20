##Email Slicer Marcelo Garcia 

email = input("Imgrese su direccion de correo porfavor: ").strip()

usuario = email[:email.index("@")]
dominio = email[email.index("@")+1:]

mensaje = " Su usuario es :'{}' y el dominio es '{}'".format(usuario,dominio)


print(mensaje)