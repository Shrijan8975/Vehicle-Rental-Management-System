from vehiclemgnt import VehicleMgmt
from riderMgmt import RiderMgnt
def riderMenuMgnt():
    ch=0
    user=RiderMgnt()
    userMgnt=VehicleMgmt()
    while(ch != 8):
        print('''
           1. Show all Vehicle
           2. Search Vehicle by Id
           3. Search Vehicle by rent
           4. Search Vehicle by name
           5. Search vehicle by type
           6. Issue Vehicle 
           7. Return Vehicle
           8. Exit 
           ''')

        try:
            ch=int(input("Enter your choice: "))
        except ValueError:
            print("ch value should be numeric..")
        else:
            if(ch == 1):
                userMgnt.showallvehicle()
            elif(ch == 2):
                id=input("Enter Vehicle id to be searched eg.MH12-GH1232: ")
                userMgnt.searchVehiclebyId(id)
            elif(ch == 3):
                rent=input("Enter Vehicle rent to be searched eg.5000: ")
                userMgnt.searchVehiclebyRent(rent)
            elif(ch == 4):
                nm=input("Enter Vehicle name to be searched eg.MG-Hector: ")
                userMgnt.searchVehiclebyNm(nm)
            elif(ch == 5):
                v_type=input("Enter vehicle type eg.Sedan: ")
                userMgnt.searchVehiclebyType(v_type)
            elif(ch == 6):
                id=input("Enter Vehicle id to Issue Vehicleeg.MH12-GH1232 : ")
                rname=input("Enter rider name for Vehicle : ")
                date_of_issue=input("Enter issue date of vehicle as (DD/MM/YYYY): ")
                start_point=input("Enter starting point of vehicle: ")
                end_point=input("Enter end point of vehicle: ")
                user.leaveVehicle(id,rname,date_of_issue,start_point,end_point)
            elif(ch==7):
                id=input("Enter Vehicle id to Return Vehicle: ")
                date_of_return=input("Enter return date of vehicle as (DD/MM/YYYY): ")
                user.returnVehicle(id,date_of_return)
            else:
                print("Thank you visit again...")

if(__name__=="__main__"):
    riderMenuMgnt()

    
