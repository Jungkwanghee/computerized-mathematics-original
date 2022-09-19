Repeat = True

while Repeat == True:
    Number1 = 1
    Number2 = 1
    Final_Number = input("30이하의 정수를 입력하세요:")  
    if (Final_Number.isdecimal()) == True:
        if int(Final_Number) <= 30:
            while Number1 <= int(Final_Number):
                print(Number2)
                Number3 = Number1 + 1
                Number1 += 1
                Number2 = str(Number2) + str(Number3)
        else:
            print("숫자가 너무 큽니다.")
            Repeat = False
            Repeat = True
    else:
        print("정수를 입력해주세요")
        Repeat = False
        Repeat = True
