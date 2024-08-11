import random
n = random.randint(1,100)
a =-1
guesses = 0

while(a!=n):
    guesses += 1
    a = int(input("gusses a no  : "))
    if(a>n):
        print("lower number please")

    elif(a<n):
        print ("higher number please")
    
    else:
        print("you gusse the correct answer")

print(f"you have guesses the number {n} correctly in {guesses} attempts")
