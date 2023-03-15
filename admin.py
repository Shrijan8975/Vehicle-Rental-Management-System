from vehicle import Vehicle
from vehiclemgnt import VehicleMgmt
def adminMenuMgmt():
    vmgmt=VehicleMgmt()
    ch=0
    while(ch != 9):
        print('''
            1. Add Vehicle
            2. Show all vehicle
            3. Search Vehicle by vehicle Id
            4. Search Vehicle by vehicle Name
            5. Search Vehicle by vehicle rent
            6. Search Vehicle by vehicle type
            7. Edit Vehicle by Vehicle Id
            8. Remove Vehicle by vehicle Id
            9. Exit
            ''' )
        try:
            ch=int(input("Enter your choice: "))
        except ValueError:
            print("ch value should be numeric..")
        else:
            if(ch == 1):
                try:
                    v_id=input("Enter vehicle Id in the format MH12-GH1232: ")
                    v_name=input("Enter vehicle name in the format MG-Hector: ")
                    v_rent=int(input("Enter vehicle rent per day: "))
                    v_type=input("Enter type of vehicle eg.SUV: ")
                    try:
                        v_avail=int(input("Enter vehicle availability status as (1/0): "))
                    except :
                        print("Values of v_avail should be numeric and  1 or 0.. ")
                    else:
                        print("Vehicle added ..")
                        veh=Vehicle(v_id,v_name,v_rent,v_type,v_avail)
                        vmgmt.addVehicle(veh)
                except ValueError:
                    print("Values of v_rent should be numeric.. ")
                
            elif(ch == 2):
                vmgmt.showallvehicle()
            elif(ch == 3):
                id=input("Enter Vehicle Id to be searched eg.MH12-GH1232 : ")
                vmgmt.searchVehiclebyId(id)
            elif(ch == 4):
                nm=input("Enter Vehicle name to be searched eg.MG-Hector: ")
                vmgmt.searchVehiclebyNm(nm)
            elif(ch == 5):
                rent=input("Enter Vehicle rent to be searched eg.5000: ")
                vmgmt.searchVehiclebyRent(rent)
            elif(ch == 6):
                v_type=input("Enter Vehicle type to be searched eg.Sedan: ")
                vmgmt.searchVehiclebyType(v_type)
            elif(ch == 7):
                id=input("Enter Vehicle Id to be edited eg.MH12-GH1232: ")
                vmgmt.editVehiclebyId(id)
            elif(ch == 8):
                id=input("Enter Vehicle Id to be deleted eg.MH12-GH1232: ")
                vmgmt.deleteVehiclebyId(id)
            elif(ch == 9):
                print("Thank you visit again...")
            else:
                print("Invalid choice please try again")

if(__name__=="__main__"):
    adminMenuMgmt()