import re

import pandas as pd
from matplotlib import  pyplot as plt

def extract(gc_list1, gc_list2, gc_list3, gc_list4, index):
    main_list = []
    main_list.append(gc_list1[index])
    main_list.append(gc_list2[index])
    main_list.append(gc_list3[index])
    main_list.append(gc_list4[index])

    return main_list

def main():
    #read from VDDX.txt gate chain data

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 150)
    pd.set_option('display.float_format', lambda x: '%0.10f' % x)
    directory = "C:\\Users\\leona\\Desktop\\JPL\\parse_data\\VDDX_current.txt"
    incoming = open(directory, "r")
    num_lines = sum(1 for line in open(directory))
    gc_list = []
    for i in range(num_lines):
        gc = incoming.readline()
        output = re.split(r",", gc)
        for x in range(len(output)):
            output[x] = output[x].strip()
            output[x] = output[x].replace("[", "")
            output[x] = output[x].replace("]", "")
        gc_list.append(output)


    gc1 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 0)
    gc2 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 1)
    gc3 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 2)
    gc4 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 3)
    gc5 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 4)
    gc6 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 5)
    gc7 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 6)
    gc8 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 7)
    gc9 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 8)
    gc10 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 9)
    gc11 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 10)
    gc12 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 11)
    gc13 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 12)
    gc14 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 13)
    gc15 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 14)
    gc16 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 15)
    gc17 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 16)
    gc18 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 17)
    gc19 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 18)
    gc20 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 19)
    gc21 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 20)
    gc22 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 21)
    gc23 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 22)
    gc24 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 23)
    gc25 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 24)
    gc26 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 25)
    gc27 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 26)
    gc28 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 27)
    gc29 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 28)
    gc30 = extract(gc_list[0], gc_list[1], gc_list[2], gc_list[3], 29)


    tid_dose = [50, 100, 150, 200]

    plt.figure(1)
    plt.plot(tid_dose, gc1, "-b", label="GC1")
    plt.plot(tid_dose, gc2, "-g", label="GC2")
    plt.plot(tid_dose, gc3, "-r", label="GC3")
    plt.plot(tid_dose, gc4, "-c", label="GC4")
    plt.plot(tid_dose, gc5, "-m", label="GC5")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

    plt.figure(2)
    plt.plot(tid_dose, gc6, "-b", label="GC6")
    plt.plot(tid_dose, gc7, "-g", label="GC7")
    plt.plot(tid_dose, gc8, "-r", label="GC8")
    plt.plot(tid_dose, gc9, "-c", label="GC9")
    plt.plot(tid_dose, gc10, "-m", label="GC10")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

    plt.figure(3)
    plt.plot(tid_dose, gc11, "-b", label="GC11")
    plt.plot(tid_dose, gc12, "-g", label="GC12")
    plt.plot(tid_dose, gc13, "-r", label="GC13")
    plt.plot(tid_dose, gc14, "-c", label="GC14")
    plt.plot(tid_dose, gc15, "-m", label="GC15")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

    plt.figure(4)
    plt.plot(tid_dose, gc16, "-b", label="GC16")
    plt.plot(tid_dose, gc17, "-g", label="GC17")
    plt.plot(tid_dose, gc18, "-r", label="GC18")
    plt.plot(tid_dose, gc19, "-c", label="GC19")
    plt.plot(tid_dose, gc20, "-m", label="GC20")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

    plt.figure(3)
    plt.plot(tid_dose, gc21, "-b", label="GC21")
    plt.plot(tid_dose, gc22, "-g", label="GC22")
    plt.plot(tid_dose, gc23, "-r", label="GC23")
    plt.plot(tid_dose, gc24, "-c", label="GC24")
    plt.plot(tid_dose, gc25, "-m", label="GC25")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

    plt.figure(3)
    plt.plot(tid_dose, gc26, "-b", label="GC26")
    plt.plot(tid_dose, gc27, "-g", label="GC27")
    plt.plot(tid_dose, gc28, "-r", label="GC28")
    plt.plot(tid_dose, gc29, "-c", label="GC29")
    plt.plot(tid_dose, gc30, "-m", label="GC30")
    plt.legend(loc="upper right")
    plt.ylabel('Current (A)')
    plt.xlabel('TID Dose')
    plt.title('TID Dosage vs VDDX Leakgae Current')
    plt.show()

if __name__ == '__main__':
    main()
