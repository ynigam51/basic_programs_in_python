n=int(input("enter a number:"))
N=n
c=0
while N>0:
  N=N//10
  c+=1
print("Number of digit:",c)
