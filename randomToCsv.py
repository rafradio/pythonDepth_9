import sys, random
from functools import wraps
from ClassForPrint import ClassForPrint as PrintMeth

def main(args):
    myMeth = PrintMeth()
    decorVariable = myMeth.dumpToCsv
    
    rows = int(args[1]) if len(args) > 1 else 400

    def createData(num: int = 200):
        def deco(func):
            @wraps(func)
            def wrap(*args):
                print("2: ", func.__name__)
                data = [["id", "FirstRand", "SecondRand", "ThirdRand"]] + [[i] + func(*args)  for i in range(num)]
                return data
            return wrap

        return deco

    @decorVariable
    @createData(rows)
    def randomFunc(*args):
        return [random.randint(args[0], args[1]) for _ in range(args[2])]

    randomFunc(1, 100, 3)

if __name__ == '__main__':
    main(sys.argv)