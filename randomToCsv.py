import random
from functools import wraps
from ClassForPrint import ClassForPrint as PrintMeth

def main():
    myMeth = PrintMeth()
    decorVariable = myMeth.dumpToCsv

    def createData(num: int = 200):
        def deco(func):
            @wraps(func)
            def wrap(*args):
                print("2: ", func.__name__)
                data = [["id", "FirstRand", "SecondRand", "ThirdRand"]]
                for i in range(num):
                    data.append([i] + func(*args))
                return data
            return wrap

        return deco

    @decorVariable
    @createData(300)
    def randomFunc(*args):
        return [random.randint(args[0], args[1]) for _ in range(args[2])]

    randomFunc(1, 100, 3)

if __name__ == '__main__':
    main()