def main ():

    try :
        a = int (input ( " enter a number "))
        print (a)
        return
    except Exception as e:
            print (e)
            return
    finally:
        print("hey i am inside of finally")
if __name__ == "four_day":
    print ("we are dircetly running this code")

print (__name__)

main()