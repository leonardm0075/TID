
import re
import pandas as pd
import os
from matplotlib import pyplot as plt

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)


def main():


    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 150)
    pd.set_option('display.float_format', lambda x: '%0.10f' % x)

    directory = 'C:\\Users\\leona\\Desktop\\JPL\\parse_data\\iterate'

    for filename in os.listdir(directory):
        iterate_dir = directory + "\\" + filename
        main_list = []
        vddx = []
        all_vddx_averages = []
        num_files = 0
        for name in sorted_alphanumeric(os.listdir(iterate_dir)):
            print(name)
            if name.endswith(".txt"):
                incoming = open(iterate_dir + "\\" + name, "r")
                num_lines = sum(1 for line in open(iterate_dir + "\\" + name))
                line_list = []
                num_files = num_files + 1
                for x in range(num_lines):
                    line = incoming.readline()
                    if x >= 3:
                        output = re.split(r",", line)

                        for i in range(len(output)):
                            output[i] = output[i].strip()
                            output[i] = output[i].replace("[", "")
                            output[i] = output[i].replace("]", "")

                        # line_list is a list of lists
                        line_list.append(output)

                main_list.append(line_list)
                df1 = pd.DataFrame(line_list, columns=['VDDIO(V)', 'VDD(V)', 'VDDY(V)', 'VDDX(V)', 'VDDIO(A)', 'VDD(A)', 'VDDY(A)', 'VDDX(A)'])
                print(df1)
                print(" ")

        for x in range(num_files):
            for i in range(len(line_list)):
                # x is the number of files/gatechains (1 gatechain per file)
                vddx.append(main_list[x][i][7])
            temp = 0

            for j in range(len(vddx)):
                temp += float(vddx[j])
            average = temp/len(vddx)
            all_vddx_averages.append(average)

        df2 = pd.DataFrame(all_vddx_averages, columns= ['VDDX Current Average'])
        print("---------------------------------------\n")
        print(df2)
        print(" ")

        vddx_save = open("VDDX_current.txt", "a")
        vddx_save.write(str(all_vddx_averages) + "\n")
        vddx_save.close()





        # plt.plot(tid_dose[0], all_vddx_averages)

        # plt.ylabel('Current (A)')
        # plt.xlabel('TID Dose')
        # plt.title('TID Dosage vs VDDX Leakgae Current')
        # plt.show()

        #o = open("file3.txt", "w+")
        #o.write(str(df))

if __name__ == '__main__':
    main()


# Notes: Remember the format of the read in txt files have to have the first line empty, the second line with the timestamp and third with the titles so that the fourth is the beginning of the data

# empty line
# ===== Thu Jun  9 08:52:25 2022  =====
# VDDIO(V), VDD(V),   VDDY(V),   VDDX(V), VDDIO(A), VDD(A),  VDDY(A), VDDX(A)