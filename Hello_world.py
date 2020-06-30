numbers=[1,2,3,4,5,6,7,8,9,10]

while True:
    num=input("Guess a number or type 'q' to quit: ")
    if num == "q":
        print("quit")
        break
    try:
        num=int(num)
    except ValueError:
        print("please type a number or q to quit.")
    if num in numbers:
        print("correct")
    else:
        print("Try again")
