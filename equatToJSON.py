import os, csv, math
from ClassForPrint import ClassForPrint as PrintMeth

def main():
    obj = PrintMeth()
    myPrint = obj.dumpToJSON

    def decor(func):
        def quardro():
            x = iter(func())
            result = {}
            while (True):
                try:
                    b = list(map(int, next(x)))
                    d = b[2]**2 - 4*b[1]*b[3]
                    res = (round((-b[2]+math.sqrt(d))/2*b[1], 2), round((-b[2]-math.sqrt(d))/2*b[1], 2)) if d >= 0 else 'Уравнение не имеет решений'
                    result[b[0]] = res
                except StopIteration:
                    break
            return result
        return quardro

    @myPrint
    @decor
    def data():
        PATH_TO_FILE = os.path.join(os.getcwd(), 'DumpedFiles', 'data.csv')
        data = []
        with open(PATH_TO_FILE, 'r', newline='') as f_read:
            csv_read = csv.reader(f_read, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            data = [row for row in csv_read]

        yield from data[1:]

    # x = decor(data)

    data()



if __name__ == '__main__':
    main()