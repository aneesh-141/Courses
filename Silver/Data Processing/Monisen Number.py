from math import sqrt
from math import pow

def prime (num):

  k=sqrt (num)
  for i in range (2, int (k + 1)):
    if num%i == 0:
      return False
  return True

def monisen (no):

  n=0
  num=2
  while n<no:
    m=pow (2, num)-1
    if prime (num) == True and prime (m) == True:

      n +=1
    num +=1
  return int (m), num-1

#__main__
for i in range (1,7):
  print (monisen (i))