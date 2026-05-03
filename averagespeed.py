s1=int(input("s1=:"))
s2=int(input("s2=:"))
s3=int(input("s3=:"))
t=s1+s2+s3
avg=t/3
print("Average speed=",avg)
if s1>s2 and s1>s3:
    print("s1 is greater")
elif s2>s1 and s2>s3:
    print("s2 is greater")
else:
    print("s3 is greater")