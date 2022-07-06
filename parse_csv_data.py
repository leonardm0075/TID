#!/usr/bin/env python3

import pandas as pd
from matplotlib import pyplot as plt


def main():

    VG_N = []
    ID_N = []
    temp_columns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    df = pd.read_csv('practice.csv', names=temp_columns)

    print(df.A)
    col_list = df.A.values.tolist()

    start = 0
    stop = 0
    flag1 = 0
    temp1 = 0
    for x in col_list:
        stop = stop + 1
        if x == "DataValue" and flag1 == 0:
            start = temp1
            flag = 1
        else:
            temp1 = temp1 + 1

    start = start + 1
    df1 = pd.read_csv('practice.csv', names=["DataName", "VG_N", "ID_N"], skiprows= start, nrows=(stop-start))
    print(df1.to_string())
    df1_VGN_list = df1.VG_N.values.tolist()
    df1_IDN_list = df1.ID_N.values.tolist()

    plt.figure(1)
    plt.plot(df1_VGN_list, df1_IDN_list)
    plt.ylabel('Current')
    plt.xlabel('Voltage')
    plt.title("IV Curve")
    plt.show()
if __name__ == "__main__":
    main()
