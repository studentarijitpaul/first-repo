class Employee: 
    company = input(" enter your company name : ")
    employee = input("enter your name")
    def show(self):
       print(f"the name of the employe is{employee}and the company is {company}")


class coder :
    language = input ( "what is your fav language  ")
    def printlanguage(self):
        print(f"out of all language here is your language")


class progermmer(Employee, coder ): 
    print("All details done")
    
    
a = progermmer()
