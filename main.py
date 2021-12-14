# set, vers, virg
import sys
import csv


def formatNumber(n, digits):
    formatter = formatter = '{:.' + '{}'.format(digits) + 'f}'
    x = round(n, digits)
    return formatter.format(x)


def getClassifiedClass(s1, s2, s3):
    if(s1 > s2 and s1 > s3):
        return 1
    elif(s2 > s1 and s2 > s3):
        return 2
    elif(s3 > s1 and s3 > s2):
        return 3
    else:
        return 0


def mainCsv():
    file1 = open(sys.argv[1])
    file2 = open(sys.argv[2])
    file3 = open(sys.argv[3])

    csvreader1 = csv.reader(file1)
    csvreader2 = csv.reader(file2)
    csvreader3 = csv.reader(file3)
    # print(csvreader1)

    rows1 = []
    rows2 = []
    rows3 = []

    for row in csvreader1:
        rows1.append(row)
    for row in csvreader2:
        rows2.append(row)
    for row in csvreader3:
        rows3.append(row)

    print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
        's1', 's2', 's3', 'cs', 'p1', 'p2', 'p3', 'pd'))
    for i in range(len(rows1)-1):
        if(i != 0):
            s1 = 0
            s2 = 0
            s3 = 0

            p1 = 0
            p2 = 0
            p3 = 0

            cs = 0
            pd = 0

            # sum
            s1 = formatNumber(float(rows1[i][4].replace('*', ''))+float(rows1[i]
                                                                        [4].replace('*', ''))+float(rows1[i][4].replace('*', '')), 3)
            s2 = formatNumber(float(rows1[i][5].replace('*', ''))+float(rows1[i]
                                                                        [5].replace('*', ''))+float(rows1[i][5].replace('*', '')), 3)
            s3 = formatNumber(float(rows1[i][6].replace('*', ''))+float(rows1[i]
                                                                        [6].replace('*', ''))+float(rows1[i][6].replace('*', '')), 3)
            cs = getClassifiedClass(s1, s2, s3)

            # product
            p1 = formatNumber(float(rows1[i][4].replace('*', ''))*float(rows1[i]
                                                                        [4].replace('*', ''))*float(rows1[i][4].replace('*', '')), 3)
            p2 = formatNumber(float(rows1[i][5].replace('*', ''))*float(rows1[i]
                                                                        [5].replace('*', ''))*float(rows1[i][5].replace('*', '')), 3)
            p3 = formatNumber(float(rows1[i][6].replace('*', ''))*float(rows1[i]
                                                                        [6].replace('*', ''))*float(rows1[i][6].replace('*', '')), 3)

            pd = getClassifiedClass(p1, p2, p3)

            # print(s1, s2, s3, cs, p1, p2, p3, pd)
            print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
                s1, s2, s3, cs, p1, p2, p3, pd))


mainCsv()
