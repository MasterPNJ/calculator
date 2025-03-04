import argparse
from calculator import Calculator

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-op", "--operation", help="(sum, average)")
    parser.add_argument("-val1", "--first_value", type=int, help="Give the firt value")
    parser.add_argument("-val2", "--second_value", type=int, help="Give the second value")

    args = parser.parse_args()
    calc = Calculator()

    if args.operation == 'sum':
        print(f'{args.first_value} + {args.second_value} = {calc.mysum(args.first_value, args.second_value)}')
    elif args.operation == 'average':
        result = calc.myaverage(args.first_value, args.second_value)
        print(f'({args.first_value} + {args.second_value}) / 2 = {result}')
    else :
        print('The function is not taken into account in our calculator')