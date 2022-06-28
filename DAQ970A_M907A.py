
#import visa
import time



class Transistor:
    def __init__(self, x_binary, y_binary, x_dec, y_dec):
        self.x_binary = x_binary
        self.y_binary = y_binary
        self.x_dec = int(x_dec)
        self.y_dec = int(y_dec)

    def print_tran(self):
        print("x_dec: " + str(self.x_dec))
        print("y_dec: " + str(self.y_dec))
        print("x_binary: " + str(self.x_binary))
        print("y_binary: " + str(self.y_binary))


def decimalToBinary(n):
    binary = bin(n).replace('0b', '')
    x = binary[::-1]
    while len(x) < 5:
        x+='0'
    binary = x[::-1]
    return binary

def getTran(tran_list):
    tran_num = input("Enter desired transistor number: ")
    print(" ")
    return tran_list[int(tran_num) - 1]

def main():

    #rm = visa.ResourceManager()
    #SCPI_DAQ970A = rm.open_resource('')



    transistor_list = []
    for x in range(0,32):
        for y in range(0,24):
            if y >= 0 and y < 4:
                if x < 9:
                    x_binary = decimalToBinary(x)
                    y_binary = decimalToBinary(y)
                    transistor_list.append(Transistor(str(x_binary), str(y_binary), str(x), str(y)))

            if y >= 4 and y < 8:
                if x < 16:
                    x_binary = decimalToBinary(x)
                    y_binary = decimalToBinary(y)
                    transistor_list.append(Transistor(str(x_binary), str(y_binary), str(x), str(y)))

            if y >= 8:
                x_binary = decimalToBinary(x)
                y_binary = decimalToBinary(y)
                transistor_list.append(Transistor(str(x_binary), str(y_binary), str(x), str(y)))

# MSB     LSB
# x1      x5
# y1      y5

    while True:
        print("0: Close program")
        print("1: Find specific transistor")
        print("2: Iterate over all transistors row by row")
        sel = input("Enter choice: ")

        if sel == "2":
            for x in transistor_list:
                x.print_tran()
                #SCPI_DAQ970A.write(':SOURce:DIGital:DATA:BYTE %d,(%s)' % (x.x_dec, '@201'))
                #SCPI_DAQ970A.write(':SOURce:DIGital:DATA:BYTE %d,(%s)' % (x.y_dec, '@201'))
                #time.sleep()
                print( " ")

        if sel == "1":
            x = getTran(transistor_list)
            x.print_tran()
            #SCPI_DAQ970A.write(':SOURce:DIGital:DATA:BYTE %d,(%s)' % (x.x_dec, '@201'))
            #SCPI_DAQ970A.write(':SOURce:DIGital:DATA:BYTE %d,(%s)' % (x.y_dec, '@201'))
            #time.sleep()
            print(" ")

        if sel == "0":
            #SCPI_DAQ970A.close()
            #rm.close()
            break




if __name__ == "__main__":
    main()
