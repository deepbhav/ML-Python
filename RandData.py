import random
import sys
import pandas as pd
import numpy as np


def readCSV():

    data= pd.read_csv("CSV_File.csv", header=None)

    print(data)


def main():

    try:
        fp = open("CSV_File.csv", "w")

        for j in range(int(sys.argv[1])):
            fp.write("Test_Case_Name" + str(j+1)+" ")
            for i in range(20):
                data=random.randint(40, 80)
                fp.write(str(data))
                fp.write(" ")
            fp.write("\n")

    except Exception as e:
        print("Error: " + e)

    finally:
        fp.close()


if __name__ == "__main__":
    main()
    print("CSV_Contents"+"\n")
    readCSV()