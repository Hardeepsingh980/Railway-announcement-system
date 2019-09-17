import csv

def main(tno, tname, from_, to, pno):

    with open('db.csv', 'r', newline='') as readFile:
        reader = csv.reader(readFile)
        lines = list(reader)
        srNo = int(lines[-1][0]) + 1

    row = [str(srNo), tno, tname, from_, to, pno]

    with open('db.csv','a',newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(row)


    readFile.close()
    writeFile.close()
        

    # print(srNo)


def delete(sr):
    input_ = open('db.csv','r',newline='')
    output = open('temp.csv','w',newline='')
    writer = csv.writer(output)

    for row in csv.reader(input_):
        writer.writerow(row)

    input_.close()
    output.close()

    input_ = open('temp.csv','r',newline='')
    output = open('db.csv','w',newline='')

    writer = csv.writer(output)

    i = 0
    for row in csv.reader(input_):
        if row[0] != sr:
            i+=1
            r = [i, row[1], row[2], row[3], row[4], row[5]]
            writer.writerow(r)
            

    input_.close()
    output.close()