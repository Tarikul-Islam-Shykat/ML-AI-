from time import *
import  random as r

def mistake(paragraph, user_input ):
    error = 0
    for i in range(len(paragraph)):
        try:
            if paragraph[i] != user_input[i]:
                error = error + 1
        except:
            error = error + 1
    return  error


def speed_time (start_time, end_time, userInput):
    time_delay = end_time - start_time
    time_round = round(time_delay)
    speed = len(userInput) / time_round
    return round(speed)


while True :
    check = input("Ready to test: Yes / No: ")
    if check == "yes": 
        test = [
            "In literary theory, a text is any object that can be, whether this object is a work of literature,",
             "Within the field of literary criticism,  also refers to the original information content of a particular ",
            "Since the history of writing predates the concept "
        ]
    
        test1 = r.choice(test)
    
        print("Typing Speed")
        print(test1)
    
    
        start_time = time()
        test_input = input(" Enter : ")
        end_time = time()
    
    
        print("Speed", speed_time(start_time, end_time, test_input), "w/sec")
        print("Error : " ,mistake(test1, test_input))
    elif check.lower() == "No":
        print("Thank You ")
        break
    else:
        print("Wrong input")
        



