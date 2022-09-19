

Repeat = True

while Repeat == True:
    Number1 = 1
    Number2 = 1
    Final_Number = int(input("30이하의 정수를 입력하세요:"))
    if Final_Number <= 30:
        while Number1 <= Final_Number:
            print(Number2)
            Number3 = Number1 + 1
            Number1 += 1
            Number2 = str(Number2) + str(Number3)
    else:
        print("숫자가 너무 큽니다.")
        Repeat = False
        Repeat = True
            
