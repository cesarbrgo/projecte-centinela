import csv
import literals as lit
import datetime

def insert_asignatura():

    registre = dict()
    registre[' curs '] = int(input(lit.msg1))
    registre[' aula '] = input(lit.msg2)
    registre[' numeroalumnes '] = input(lit.msg3)
    registre[' numeroprofesors '] = input(lit.msg4)
    dia=int(input(lit.dia))
    while dia<1 or dia>30:
        print("el dia ha de ser entre 1 i 30")
        dia = int(input(lit.dia))
    mes=int(input(lit.mesos))
    while mes<1 or mes>12:
        print("el mes ha de ser entre 1 i 12")
        mes = int(input(lit.mesos))
    any=int(input(lit.anys))
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    print("la data actual es:",date)
    year = date.strftime("%Y")
    year=int(year)
    while any<1970 or any> year:
        any = int(input(lit.anys))
    registre[' dia '] = str(dia)+'/'+str(mes)+'/'+str(any)
    hora= int(input(lit.hores))
    while hora<8 or hora>24:
        hora = int(input(lit.hores))
    registre[' hora '] = hora
    nomprofesor=input(lit.nomprofesors)
    registre[' nomprofesors '] = nomprofesor
    nomasignatura=input(lit.nomasignatura)
    registre[' assignatura '] = nomasignatura
    insert_registre_asignatura(registre)
    return nomasignatura, nomprofesor, dia, mes, any, hora

def insert_data(nomasignatura,nomprofesor,dia, mes, any, hora, primer):

    registre = dict()
    registre[' nomasignatura '] = nomasignatura
    registre[' nomprofesor '] = nomprofesor
    registre[' data '] = str(dia)+'/'+str(mes)+'/'+str(any)
    time=int(input("introdueix l'hora: "))
    while time<hora:
        print("error la hora no pot ser avans que l'hora de clase")
        time = int(input("introdueix l'hora: "))
    registre[' hora ']=time
    registre[' CO ']=input("introdueix el registre de CO: ")
    registre[' temperatura ']=input("introdueix la temperatura")
    registre[' humitatrelativa ']=input("introdueix l'humitat relativa")
    insert_registre(registre, primer)

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