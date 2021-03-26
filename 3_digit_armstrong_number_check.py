#In the case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example, 153 is an Armstrong number because
num=int(input("Enter a thre Digit Number:"))
N=num#taking brackup of num
s=0
while num>0:
  last_digit=num%10
  s=s+last_digit**3
  num=int(num/10) #you can also use num//10

if s==N:
  print("Yes it is an armstrong number")
else:
  print("Not an armstrong number") 
