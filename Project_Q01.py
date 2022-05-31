import random
random.random()

def response(ans):
    
    negResponse = ["No, Please try again", "Wrong. Try once more.", "No. Keep trying."]
    posResponse = ["Very good!", "Nice work!", "Keep up the good work!"]
    
    if ans == True:
        return posResponse[random.randint(0,2)]
    
    elif ans == False:
        return negResponse[random.randint(0,2)]

def calculator():
    
    incorrect = 0
    correct = 0
    
    difficulty = int(input("Enter Difficulty Level (1 or 2): "))
    
    Option1 = print("\n","1 = Addition ","\n","2 = Subtraction ","\n","3 = Multiplication ","\n","4 = Division ","\n","5 = Mixed Operations ","\n")
    Option2 = int(input("Enter the operation (1 to 5): "))
    
    while True:

        if difficulty == 1:
            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            if Option2 == 4 and num2 == 0:
                num2 = 1

        elif difficulty == 2:
            num1 = random.randint(0,99)
            num2 = random.randint(0,99)
        
        if Option2 == 1:
            symbol = "+"
            
        elif Option2 == 2:
            if num1<num2:
                num1,num2 = num2,num1
            symbol = "-"
            
        elif Option2 == 3:
            symbol = "*"
            
        elif Option2 == 4:
            symbol = "/"
            
        elif Option2==5:
            
            Option2 = random.randint(1,4)
            symbols = ["+","-","*","/"]
            symbol = symbols[Option2-1]
            
            if Option2==2:
                if num1<num2:
                    num1,num2 = num2,num1

        print("How much is ", num1, symbol, num2)
        
        if Option2 == 1:
            
            while True:
                
                user = int(input("Enter your answer (-1 to exit): "))
                if user == num1 + num2:
                    print(response(True))
                    correct += 1
                    break
                
                elif user == -1:
                    print("-"*30)
                    print("Number of correct answers: ", correct)
                    print("Number of incorrect answers: ", incorrect)
                    print("\n","Thanks for playing!")
                    return
                
                elif user != num1 + num2:
                    print(response(False))
                    incorrect += 1
                    continue
                

        elif Option2 == 2:
            
            while True:
                
                user = int(input("Enter your answer (-1 to exit): "))
                if user == num1 - num2:
                    print(response(True))
                    correct += 1
                    break
                
                elif user == -1:
                    print("-"*27)
                    print("Number of correct answers: ", correct)
                    print("Number of incorrect answers: ", incorrect)
                    print("\n","Thanks for playing!")
                    return
                
                elif user != num1 - num2:
                    print(response(False))
                    incorrect += 1
                    continue
        
        elif Option2 == 3:
            
            while True:
                
                user = int(input("Enter your answer (-1 to exit): "))
                if user == num1 * num2:
                    print(response(True))
                    correct += 1
                    break
                
                elif user == -1:
                    print("-"*30)
                    print("Number of correct answers: ", correct)
                    print("Number of incorrect answers: ", incorrect)
                    print("\n","Thanks for playing!")
                    return
                
                elif user != num1 * num2:
                    print(response(False))
                    incorrect += 1
                    continue

        elif Option2 == 4:
            
            while True:
                
                user = int(input("Enter your answer (-1 to exit): "))
                if user == num1 // num2:
                    print(response(True))
                    correct += 1
                    break
                
                elif user == -1:
                    print("-"*30)
                    print("Number of correct answers: ", correct)
                    print("Number of incorrect answers: ", incorrect)
                    print("\n","Thanks for playing!")
                    return
                
                elif user != num1 // num2:
                    print(response(False))
                    incorrect += 1
                    continue
            
calculator()
