from pathlib import Path
import argparse

def showdir(path='.'):
    p = Path(path)
    for file in p.iterdir():
        yield file.name

parser = argparse.ArgumentParser(prog='ls',add_help=False,description='list all files')
parser.add_argument('path',nargs='?',default='.',help='path help')
parser.add_argument('-l',action='store_true')
parser.add_argument('-h',action='store_true')
parser.add_argument('-a','--all',action='store_true')

if __name__ == '__main__':
    args = parser.parse_args(('e:/',))
    parser.print_help()
    print('args=',args)
    print(args.path,args.l,args.h,args.all)
    for file in showdir(args.path):
        print(file)
        