#!/usr/bin/env python3
#import visa
import time

def main():

# Open each even sma line first then open all the odss (corresponds to the columns) for the amount
# of time it takes for the b1500 to collect data from each of the transistors in the column


    even_lines = ['04','06','08','10','12','14','16','18','20','22']
    odd_lines = ['05','07','09','11','13','15','17','19','21','23']

    #rm = visa.ResourceManager()
    #SCPI_DAQ_970A = rm.open_resource('')

# Slot 1: SMA 1-20
# Slot 2: SMA 20-24
    for x in even_lines:
        if int(x) <= 20:
            index = '@1' + x
            print(index)
            #SCPI_DAQ_970A.write(':ROUTe:OPEN(%s)'%('@101'))
            #SCPI_DAQ_970A.write(':ROUTe:CLOSe(%s)'%('@101'))
            #time.sleep()

    for x in even_lines:
        if int(x) > 20:
            index = '@2' + x
            print(index)
            #SCPI_DAQ_970A.write(':ROUTe:OPEN(%s)'%('@101'))
            #SCPI_DAQ_970A.write(':ROUTe:CLOSe(%s)'%('@101'))
            #time.sleep()


    for x in odd_lines:
        if int(x) <= 20:
            index = '@1' + x
            print(index)
            #SCPI_DAQ_970A.write(':ROUTe:OPEN(%s)'%('@101'))
            #SCPI_DAQ_970A.write(':ROUTe:CLOSe(%s)'%('@101'))
            #time.sleep()

    for x in odd_lines:
        if int(x) > 20:
            index = '@2' + x
            print(index)
            #SCPI_DAQ_970A.write(':ROUTe:OPEN(%s)'%('@101'))
            #SCPI_DAQ_970A.write(':ROUTe:CLOSe(%s)'%('@101'))
            #time.sleep()



    #SCPI_DAQ_970A.close()
    #rm.close()




if __name__ == "__main__":
    main()
