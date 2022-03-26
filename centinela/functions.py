import csv
import literals as lit
import datetime

#la funcio inserir asignatura afeigeix els parametres generals de la asignatura que es repetiran durant el programa
#aquesta funcio comprova si existeix el fitcher per a crear el nous registres
def insert_asignatura():

    registre = dict()
    registre[' curs '] = input(lit.msg1)
    registre[' aula '] = input(lit.msg2)
    alumnes=int(input(lit.msg3))
    while alumnes<1 or alumnes>9999:
        alumnes = int(input(lit.msg3))
    registre[' numeroalumnes '] = alumnes
    profesors=int(input(lit.msg4))
    while profesors<1 or profesors>alumnes:
        profesors = int(input(lit.msg4))
    registre[' numeroprofesors '] = profesors
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    print("la data actual es:",date)
    year = date.strftime("%Y")
    year=int(year)
    month=currentDateTime.month
    day=currentDateTime.day
    registre[' dia '] = str(day)+'/'+str(month)+'/'+str(year)
    hora= currentDateTime.hour
    registre[' hora '] = hora
    nomprofesor=input(lit.nomprofesors)
    registre[' nomprofesors '] = nomprofesor
    nomasignatura=input(lit.nomasignatura)
    registre[' assignatura '] = nomasignatura
    insert_registre_asignatura(registre)
    return nomasignatura, nomprofesor

#la funcio inserir data serveix per inserir registres de valors de CO humitat i demes un cop ja s'han inserit els prametres de l'asignatura
#la funcio comprova si es el primer registre per tal ficar un header on es posin els valors dels parametres
def insert_data(nomasignatura,nomprofesor,primer):

    registre = dict()
    registre[' nomasignatura '] = nomasignatura
    registre[' nomprofesor '] = nomprofesor
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    registre[' data '] = date
    min = currentDateTime.minute
    hour=currentDateTime.hour
    registre[' hora ']=str(hour)+':'+str(min)
    CO=int(input("introdueix el registre de CO: "))
    while CO<1 or CO>9999:
        CO = int(input("introdueix el registre de CO: "))
    registre[' CO ']=CO
    temp= int(input("introdueix la temp: "))
    while temp < 1 or temp > 9999:
        temp = int(input("introdueix la temp: "))
    registre[' temperatura ']=temp
    humitat=int(input("introdueix l'humitat relativa (entre 0 i 100):"))
    while humitat>100 or humitat<1:
        humitat = int(input("introdueix l'humitat relativa (entre 0 i 100):"))
    registre[' humitatrelativa ']=humitat
    insert_registre(registre, primer)

#funcio per a inserir els registres de valors
def insert_registre(registre, primer):
    try:
        with open('files/centinella.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = [' nomasignatura ', ' nomprofesor ', ' data ', ' hora ', ' CO ',' temperatura ',' humitatrelativa ']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if primer==1:
                    print(lit.crea)
                    writeCSV.writeheader()
            writeCSV.writerow(registre)
    except:
        print(lit.noinserir)
    else:
        print(lit.inserir)


#funcio per a inserir el registre general de l'asignatura
def insert_registre_asignatura(registre):
    path='files/centinella.csv'
    header=existint_file(path)

    try:
        with open('files/centinella.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = [' curs ', ' aula ', ' numeroalumnes ', ' numeroprofesors ', ' dia ',' hora ',' nomprofesors ',' assignatura ']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if header==0:
                    print(lit.crea)
                    writeCSV.writeheader()
            writeCSV.writerow(registre)
    except:
        print(lit.noinserir)
    else:
        print(lit.inserir)

#aquesta funció comprova si existeix el ficher
def existint_file(path):
    try:
        f = open(path, "r")
    except FileNotFoundError:
        print(lit.noexiste)
        header=0
    else:
         header=1
         f.close()
    finally:
        return header

#funcio finalitzar serveix per inserir els valors que es necesiten registrar un cop s'ha acabat d'inserir registres
def end_register():
    no=1
    registre=dict()
    oberta=int(input(lit.principaloberta))
    tancada=int(input(lit.principaltancada))
    while oberta+tancada<1:
        print(lit.errorportes)
        oberta = int(input(lit.principaloberta))
        tancada = int(input(lit.principaltancada))
    registre[" porta "]="tancada: "+ str(tancada)+"min, "+ "oberta "+ str(oberta)+" min."

    oberta2=int(input(lit.secundariaoberta))
    tancada2=int(input(lit.secundariatancada))
    no=int(input(lit.no))
    while oberta2+tancada2<1 or no==0:
        print(lit.errorportes)
        oberta2 = int(input(lit.secundariaoberta))
        tancada2 = int(input(lit.secundariatancada))
        no = int(input(lit.no))
    registre[" porta2 "]="tancada: "+ str(tancada2)+" min, "+ "oberta "+ str(oberta2)+" min."
    if no == 0:
        registre[" porta2 "]="no hi ha porta secundaria"
    no=1

    internaoberta=int(input(lit.internaoberta))
    internatancada=int(input(lit.internatancada))
    no=int(input(lit.no))
    while internaoberta+internatancada<1 or no==0:
        print(lit.errorportes)
        internaoberta = int(input(lit.internaoberta))
        internatancada = int(input(lit.internatancada))
        no = int(input(lit.no))
    registre[" finestresinternes "]=" tancada: "+ str(internatancada)+" min, "+ "oberta "+ str(internaoberta)+" min. "
    if no == 0:
        registre[" finestresinternes "]="no hi ha finestra interna. "
    no=1

    externaoberta = int(input(lit.externaoberta ))
    externatancada = int(input(lit.externatancada ))
    no = int(input(lit.no))
    while externatancada  + externaoberta< 1 or no == 0:
        print(lit.errorportes)
        externaoberta = int(input(lit.externaoberta ))
        externatancada  = int(input(lit.externatancada ))
        no = int(input(lit.no))
    registre[" finestresexternes "] = "tancada: " + str(externatancada) + " min, " + " oberta: " + str(externaoberta) + " min. "
    if no == 0:
        registre[" finestrexternes "] = "no hi ha finestres. "
    no = 1

    creuada=int(input("hi ha hagut ventilacio creuada a la clase? 1-si 2-no"))
    while creuada<1 or creuada>2:
        creuada = int(input("hi ha hagut ventilacio creuada a la clase? 1-si 2-no"))
    if creuada==1:
        registre[" ventilacio creuada "] ="Si hi ha hagut ventilacio creuada. "
    else:
        registre[" ventilacio creuada "] = "Si hi ha hagut ventilacio creuada. "
    insert_final(registre)

#funcio per inserir els registres de les dades de final de l'asignatura
def insert_final(registre):
    path='files/centinella.csv'
    header=existint_file(path)
    try:
        with open('files/centinella.csv', 'a', encoding='utf-8', newline='') as csvfile:
            fieldnames = [' porta ', ' porta2 ', ' finestresinternes ', ' finestresexternes ', ' ventilacio creuada ']
            writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
            print(lit.crea)
            writeCSV.writeheader()
            writeCSV.writerow(registre)
    except:
        print(lit.noinserir)
    else:
        print(lit.inserir)
