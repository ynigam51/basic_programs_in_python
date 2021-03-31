n=12345
N=n
c=0
while N>0:
	N=N//10
	c+=1
rev=0
N=n
while c>0:
	last_digit=N%10
	rev=rev+last_digit*10**c
	c-=1
	N=N//10
print(rev)
                        
