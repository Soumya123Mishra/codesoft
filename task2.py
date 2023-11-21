number1=int(input("Enter the First Number:"))
number2=int(input("Enter the second Number:"))
symbol=(input("Enter the symbol:"))
if symbol=='+':
    print(number1+number2)
elif symbol=='-':
    print(number1-number2)
elif symbol=='*':
 print(number1*number2)
elif symbol=='/':
 print(number1/number2)

else:
   print("Here is invalid symbol")