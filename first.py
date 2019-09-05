#First Python Program by Tony Lee
def foo():
  print('interesting')

def combine (a, b, idxA):
  if (idxA == len(a)):
    print (b)
    return
  else:
    c = b[:]
    b.append (a[idxA])
    idxA = idxA + 1
    combine (a, b, idxA)
    combine (a, c, idxA)


foo()
a = [1, 2, 3]
b = []
combine(a,b,0)
