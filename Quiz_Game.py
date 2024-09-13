print("Welcome to Quiz Game !!!")
select=input("Do you want to play?? ")
score=0
if select != "yes":
    quit()
else:
    print("Lets Play...All the best")
Question1=input("Q1: Who is the current president of India?? ")
if Question1=="Modi":
    print("Congratulations !!..Answer is correct")
    score +=1
else:
    print("Incorrect Answer please check !!!")
Question2=input("Q1: Who is the current president of USA?? ")
if Question2=="Biden":
    print("Congratulations !!..Answer is correct")
    score +=1
else:
    print("Incorrect Answer please check !!!")
Question3=input("Q1: Who is the president of Tesla?? ")
if Question2=="Elon Musk|elon musk":
    print("Congratulations !!..Answer is correct")
    score +=1
else:
    print("Incorrect Answer please check !!!")
print("Congratulations!! Your score is"+str(score))





