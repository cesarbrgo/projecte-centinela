import literals as lit
import functions as fun

def main():
        stop=1
        primer=1
        datanorepeat=fun.insert_asignatura()
        nomasignatura=datanorepeat[0]
        nomprofesor=datanorepeat[1]
        while stop !=0:
            fun.insert_data(nomasignatura,nomprofesor, primer)
            stop=int(input(lit.final))
            primer=primer+1
        fun.end_register()
if __name__ == '__main__':
    main()
