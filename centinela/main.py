import literals as lit
import functions as fun

def main():
        quarts=0
        primer=1
        duracio=int(input(lit.duracio))
        while duracio<60 or duracio>999 or duracio%15!=0:
            print(lit.errorduracio)
            duracio = int(input(lit.duracio))
        datanorepeat=fun.insert_asignatura()
        nomasignatura=datanorepeat[0]
        nomprofesor=datanorepeat[1]
        dia=datanorepeat[2]
        mes=datanorepeat[3]
        any=datanorepeat[4]
        hora=datanorepeat[5]
        while duracio>=quarts:
            fun.insert_data(nomasignatura,nomprofesor,dia, mes, any, hora, primer)
            quarts=quarts+15
            primer=primer+1

if __name__ == '__main__':
    main()
