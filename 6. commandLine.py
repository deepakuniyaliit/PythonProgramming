import sys

def sum(a,b):
    return a+b

print(len(sys.argv))
print(sys.argv[0])
print('Sum = ', sum(int(sys.argv[1]),int(sys.argv[2])))
