#!/usr/bin/env python

# adiciona um zero na frente e alinha
with open(r'teste.txt', 'r') as f:
    output = open('saida.txt', 'w')
    output.write('* WEATHER DATA : Nova Xavantina, MT, Brazil (Future) RCP4.5, end century, 1season, GCM A \n \n')
    output.write('@INSI LAT LONG ELEV TAV AMP REFHT WNDHT CCO2 \n')
    output.write('MTNX -14.67 -52.35 316 -99.0 -99.0 -99.0 -99.0 532 \n')
    output.write('@DATE SRAD TMAX TMIN RAIN WIND \n')
    for line in f:
        data = line.split()    # Splits on whitespace
        # print ('{0[0]:<15}{0[1]:<15}{0[2]:<5}{0[3]:<15}{0[4]:>15}{0[5]:>8}'.format(data))
        # ll = str('{0[0]: <6}{0[1]:<5}{0[2]:<5}{0[3]:<5}{0[4]:<8}{0[5]:<8}'.format(data))
        # ll=('{:<7s}{:>5s}{:>7s}{:>7s}{:>5s}'.format(data[0],data[1],data[2],data[3], data[5]))
        mm = data
        for i in range(len(mm)):
            if len(mm[i]) == 3:
                mm[i] = str('0' + mm[i])
        mm=('{:<7s}{:>5s}{:>7s}{:>7s}{:>7s}'.format(data[0],data[1],data[2],data[3], data[5]))
        # print(ll)
        #ll = str(data)
        #ll = ll.rjust(0, " ")
        #ll = print(ll.ljust(30, ' ') + '\n')
        output.write(mm + '\n')
        #print('{: <7s}{: >5s}{: >7s}{: >7s}{: >5s}'.format(data[0],data[1],data[2],data[3], data[5]), file=output)
    output.close()


# novo autmotico que é para usar
import glob

lista_txt = glob.glob('*.txt')

for i in range(len(lista_txt)):
    # adiciona um zero na frente e alinha
    nome_in = lista_txt[i]
    nome_out = nome_in.split('.')[0] + '_saida.WTH'
    # print(nome_out)
    with open(nome_in, 'r') as f:
        f =  f.readlines()[5:]
        output = open(nome_out, 'w')
        output.write('* WEATHER DATA : XXXXXX, MT, Brazil (Future) RCPXXX, XXX century, Xseason, GCM X \n \n')
        output.write('@INSI LAT LONG ELEV TAV AMP REFHT WNDHT CCO2 \n')
        output.write('MTNX -XXXXX -XXXXX XXX -99.0 -99.0 -99.0 -99.0 XXX \n')
        output.write('@DATE SRAD TMAX TMIN RAIN WIND \n')
        for line in f:
            data = line.split()    # Splits on whitespace
            # print ('{0[0]:<15}{0[1]:<15}{0[2]:<5}{0[3]:<15}{0[4]:>15}{0[5]:>8}'.format(data))
            # ll = str('{0[0]: <6}{0[1]:<5}{0[2]:<5}{0[3]:<5}{0[4]:<8}{0[5]:<8}'.format(data))
            # ll=('{:<7s}{:>5s}{:>7s}{:>7s}{:>5s}'.format(data[0],data[1],data[2],data[3], data[5]))
            # print(ll)
            #ll = str(data)
            #ll = ll.rjust(0, " ")
            #ll = print(ll.ljust(30, ' ') + '\n')
            #output.write(mm + '\n')
            print('{:<9s}{:0>7s}{: >s}{:0>7s}{: >s}{:0>5s}{: >s}{:0>5s}{: >s}{:0>5s}'.format(data[0],data[1], '   ', data[2], '   ',data[3], '   ', data[4], '   ', data[5]), file=output)
        output.close()







# FUNCTIONA
with open(r'teste.txt', 'r') as f:
    f =  f.readlines()[5:]
    output = open('saida.txt', 'w')
    output.write('* WEATHER DATA : Nova Xavantina, MT, Brazil (Future) RCP4.5, end century, 1season, GCM A \n \n')
    output.write('@INSI LAT LONG ELEV TAV AMP REFHT WNDHT CCO2 \n')
    output.write('MTNX -14.67 -52.35 316 -99.0 -99.0 -99.0 -99.0 532 \n')
    output.write('@DATE SRAD TMAX TMIN RAIN WIND \n')
    for line in f:
        data = line.split()    # Splits on whitespace
        # print ('{0[0]:<15}{0[1]:<15}{0[2]:<5}{0[3]:<15}{0[4]:>15}{0[5]:>8}'.format(data))
        # ll = str('{0[0]: <6}{0[1]:<5}{0[2]:<5}{0[3]:<5}{0[4]:<8}{0[5]:<8}'.format(data))
        # ll=('{:<7s}{:>5s}{:>7s}{:>7s}{:>5s}'.format(data[0],data[1],data[2],data[3], data[5]))
        # print(ll)
        #ll = str(data)
        #ll = ll.rjust(0, " ")
        #ll = print(ll.ljust(30, ' ') + '\n')
        #output.write(mm + '\n')
        print('{:<9s}{:0>7s}{: >s}{:0>7s}{: >s}{:0>5s}{: >s}{:0>5s}{: >s}{:0>5s}'.format(data[0],data[1], '   ', data[2], '   ',data[3], '   ', data[4], '   ', data[5]), file=output)
    output.close()





# nao alinha por ponto
import sys
inputfile = open('teste.txt', 'r')
inputfile = inputfile.split('\n')
output = open('saida.txt', 'w')
lengths = [6,5,5,5,5,5]
for line in inputfile:
    line = line.split()
    for field, fieldlength in zip(line,lengths):
        output.write(field.rjust(fieldlength))
    output.write('\n')

