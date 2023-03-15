from admin import adminMenuMgmt
from rider import riderMenuMgnt
import random
if(__name__=="__main__"):
    print('''
        1. Admin Menu for Vehicle
        2. Rider Menu for Vehicle
        ''')
    try:
        ch=int(input("Enter your choice: "))
    except:
        print("Value of choice should be numeric..")
    else:
        if(ch==1):
            for i in range(0,3):
                user_nm = input("Enter admin username: ")
                pswd = input("Enter admin password: ")
                if( user_nm == "Adminvehicle" and pswd == "Adminvehicle123" ):
                    x=random.randint(1000,9999)
                    print(x)
                    try:
                        y=int(input("Enter captcha shown: "))
                    except ValueError:
                        print("Please enter correct captcha..")
                        print(2-i,"Attempts left")

                    else:
                        if(x==y):
                            print("Admin login Successful..")
                            adminMenuMgmt()
                            break
                        else:
                            print("Invalid captcha please try again")
                            print(2-i,"Attempts left")
                else:
                    print(" Invalid credentials.. ")
                    print(2-i,"Attempts left")

            else:
                print("Program is terminated..")
        elif(ch==2):
            for i in range(0,3):
                user_nm_rider=input("Enter Rider username: ")
                r_pswd=input("Enter Rider pswd: ")
                if( user_nm_rider == "Rider" and r_pswd == "Rider123"):
                    x=random.randint(1000,9999)
                    print(x)
                    try:
                        y=int(input("Enter captcha shown: "))
                    except ValueError:
                        print("Please enter correct captcha..")
                        print(2-i,"Attempts left")
                    else:
                        if(x==y):
                            print("Rider login succcessful..")
                            riderMenuMgnt()
                            break
                        else:
                            print("Invalid captcha please try again")
                            print(2-i,"Attempts left")
                else:
                    print("Invalid Credentials..")
                    print(2-i,"Attempts left")
            else:
                print("Program is terminated..")
        else:
            print("Thank you for visiting..")
