import random
import pyfiglet
import os
import yagmail

banner= pyfiglet.figlet_format("AlphaKeyGen")
print(banner)

print("v1.2.3")

email= "alphakey.gen@gmail.com"
contraseña= "hceslbejpcmvunrv"
yag = yagmail.SMTP(user=email, password=contraseña)
satis = 1
while satis == 1:
    #Esta estructura nos ayuda a validar que no entre una letra, un vacio
    #Que se valide la entrada de un numero, y este no sea menor a 8 ni mayor a 75
    
    while True:
        long=input("Por favor introduzca el numero de caracteres que quiere que tenga su contraseña:\n")
        if long.isnumeric():
                long=int(long)
                if long > 60 or long < 8:
                    print ("Las contraseñas estandar normales tienen de entre 8 a 35 caracteres")
                else:
                    break
        
    while True:
        minus= "abcdefghijklmnopqrstuvwxyz"
        mayus= minus.upper()
        num= "1234567890"
        carac="!#$%&/@"
        recip=""
        while True:
            usar_minus=input("¿Desea que su contraseña tenga minusculas?: Responda con \n1=Si 2=No\n")
            if usar_minus.isnumeric():
                usar_minus=int(usar_minus)
                if usar_minus >0 and usar_minus<3:
                    if usar_minus == 1:
                        usar_minus=True
                        break
                    else:
                        usar_minus==2
                        minus=""
                        break

        while True:
            usar_mayus=input("¿Desea que su contraseña tenga mayusculas?: Responda con \n1=Si 2=No\n")
            if usar_mayus.isnumeric():
                usar_mayus=int(usar_mayus)
                if usar_mayus>0 and usar_mayus<3:
                    if usar_mayus==1:
                        usar_mayus=True
                        break
                    else:
                        usar_mayus==2
                        mayus=""
                        break
        
        while True:
            usar_num=input("¿Desea que su contraseña tenga numeros?: Responda con \n1=Si 2=No\n")
            if usar_num.isnumeric():
                usar_num=int(usar_num)
                if usar_num>0 and usar_num<3:
                    if usar_num==1:
                        usar_num=True
                        break
                    else:
                        usar_num==2
                        num=""
                        break
        
        while True:
            usar_carac=input("¿Desea que su contraseña tenga caracteres especiales?: Responda con \n1=Si 2=No\n")
            if usar_carac.isnumeric():
                usar_carac=int(usar_carac)
                if usar_carac>0 and usar_carac<3:
                    if usar_carac==1:
                        usar_carac=True
                        break
                    else:
                        usar_carac==2
                        carac=""
                        break
        recip=minus+mayus+num+carac
        if recip=="":
            print("Al menos debes escoger un conjunto de caracteres para generar tu contraseña segura")
        else:
            recip!=""
            break

    elec=[]
    if usar_minus==True:
        elec.append(random.choice(minus))
    if usar_mayus==True:
        elec.append(random.choice(mayus))
    if usar_num==True:
        elec.append(random.choice(num))
    if usar_carac==True:
        elec.append(random.choice(carac))
    
    while len(elec)<long:
        elec+=random.choice(recip)
    
    random.shuffle(elec)

    passwd= "".join(elec)
    print ("Su contraseña generada aleatoriamente es: ",passwd)
    archivo = open("contra.txt","w",encoding="utf-8")
    archivo.write("Este es el respaldo de tu contraseña generada:\n")
    archivo.write("Tu contraseña es:\n")
    archivo.write(passwd)
    archivo.close()

    while True:
        satis=input("¿Esta satisfecho con su contraseña?: \n1=Si 2=No\n")
        if satis.isnumeric():
            satis=int(satis)
            if satis>0 and satis<3:
                if satis==1:
                    satis = 0
                    break
                if satis==2:
                    satis=1
                    os.remove('contra.txt')
                    break

while True:
    final= input("¿Desea que le enviemos su contraseña a su Gmail?:responda con \n1=Si 2=No\n")
    if final.isnumeric():
        final=int(final)
        if final>0 and final<3:
            if final == 1:
                
                while True:
                    destinatario=input("Por favor escriba su gmail:\n")
                    domain=("@gmail.com")
                    if destinatario.endswith(domain) and " " not in destinatario:
                        break
                    else:
                        print("Ingrese un correo Gmail válido")

                asunto = ("Respaldo de tu contraseña generada con AlphaKeyGen")
                html = "<h1>¡Hola! Aqui se encuentra tu contraseña generada</h1>"
                mensaje = ("Gracias por usar AlphaKeyGen")

                yag.send(destinatario, asunto, [mensaje,html], attachments=['contra.txt'])
                
                print("Su contraseña fue enviada")
                break
            else:
                break
os.remove('contra.txt')
print("Gracias por usar nuestro generador de contraseñas")

banner1= pyfiglet.figlet_format("Thanks",font="hollywood")
print(banner1)