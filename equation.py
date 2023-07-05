import sys
import math

def main(args):
    b = list(map(int, args[1:])) if len(args) == 4 else [1, 4, 4] 

    def decor(func):
        def wrap(b):
            d = b[1]**2 - 4*b[0]*b[2]
            return func(b,d) if d >= 0 else 'Уравнение не имеет решений'
        return wrap

    @decor
    def result(b,d):
        return (-b[1]+math.sqrt(d))/2*b[0], (-b[1]-math.sqrt(d))/2*b[0]
    
    print(result(b))

if __name__ == '__main__':
    main(sys.argv)