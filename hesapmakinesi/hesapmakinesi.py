num1 = int(input("birinci sayiyi giriniz:"))
num2 = int(input("ikinci sayiyi giriniz:"))

op=input("bir islem seciniz(+,-,*,/):")


if op =="+":
    print(num1,"+",num2,"=",num1+num2)
elif op =="-":
    print(num1 ,"-" , num2 ,"=" , num1-num2 )
elif op =="*":
    print(num1 ,"*" , num2 ,"=" , num1*num2 )
elif op =="/":
    print(num1 ,"/" , num2 ,"=" , num1/num2 )
else:
    print("programimizda boyle bir islem gecerli degildir.")