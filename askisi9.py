# askisis-septevriou

count=0
a= raw_input("dwse arithmo")
while 1:
    digits=[]
    for i in range(len(a)):
        digits.append(a[i])
    if (len(digits)==1):
        break
    else:
        a=1
    for i in range(len(digits)):
        a=int(a)
        a*=int(digits[i])
    a=str(a)
    count+=1
print count
