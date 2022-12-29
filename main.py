# Tower of hanoi
def toh(n,a='a',b='b',c='c'):
  if n:
    toh(n-1,a,c,b)
    print(f'From {a} to {b}')
    toh(n-1,b,c,a)

toh(4)



#