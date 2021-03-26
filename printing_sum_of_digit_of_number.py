num=int(input("Enter a number:"))
s=0
while num>0:
  last_digit=num%10
  s=s+last_digit
  num=num//10
print("SUM=",s)
