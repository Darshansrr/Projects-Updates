print("Simple Calculator")
print("\n Addition[1],Subraction[2],Multiplication[3],Division[4]")

First_num=int(input("Enter the first number:"))
Second_num=int(input("Enter the second number:"))

a=int(input("enter the method number mention above like 1,2,3,4 :"))

if a==1:
    print(First_num+Second_num)
elif a==2:
    print(First_num-Second_num)
elif a==3:
    print(First_num*Second_num)
elif a==4:
    print(First_num/Second_num)
else:
    print("you enter the wrong order!.. Please enter the correct number order mention above")

