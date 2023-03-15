from os import path
class VehicleMgmt:
    def addVehicle(self,v1):
        fp=open("VehicleInfo.txt","a")
        fp.write(str(v1))
        fp.write("\n")
        fp.close()

    def showallvehicle(self):
        try:
            sp=open("VehicleInfo.txt","r")
        except FileNotFoundError:
            print("File Not Found..")
        else:
            data=sp.read()
            print(data)
            sp.close()

    def searchVehiclebyId(self,id):
        if(path.exists("VehicleInfo.txt")):
            try:
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        if(data[0].lower()==id.lower()):
                            print(" Record of vehicle found..\n",line)
                            break 
                    else:
                        print("Vehicle not found with these Id")
            except FileNotFoundError:
                print("File does't exist with the given file name..")
        else:
            print("path does't exist..")

    def searchVehiclebyNm(self,nm):
        if(path.exists("VehicleInfo.txt")):
            try:
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        if(data[1].lower()==nm.lower()):
                            print(" Record of vehicle found..\n",line)
                            break
                    else:
                        print("Vehicle not found with this name")
            except FileNotFoundError:
                print("File does't exist with the given file name..")
        else:
            print("Path does't exist..")

    def searchVehiclebyRent(self,rent):
        flag=False
        if(path.exists("VehicleInfo.txt")):
            try:
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        try:
                            if(data[2]==str(rent)):  #if(str(rent) in line):
                                print(" Record found..\n",line)
                                flag=True
                                break
                        except:
                            pass
                if(flag==False):
                    print("Vehicle not found with this rent")

            except FileNotFoundError:
                print("File does't exist with the given file name..")
            
        else:
            print("Path does't exist..")
    
    def searchVehiclebyType(self,v_type):
        flag=False
        if(path.exists("VehicleInfo.txt")):
            try:
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        if(data[3].lower()==str(v_type).lower()):
                            print(" Record of vehicle found..\n",line)
                            flag=True
                            continue
                            
                if(flag==False):
                    print("This type of vehicle not found")
            except FileNotFoundError:
                print("File does't exist with the given file name..")
        else:
            print("Path does't exist..")

    def editVehiclebyId(self,id):
        vehiclelist=[]
        flag=False
        if(path.exists("VehicleInfo.txt")):
            try:
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        try:    
                            if(data[0].lower()==id.lower()):
                                print(" Record found...\n",line)
                                flag=True
                                ans=input("Do you want to change Vehicle name? (y/n): ")
                                if(ans=="y"):
                                    data[1]=input("Enter new vehicle name: ")
                                
                                ans=input("Do you want to change vehicle rent? (y/n): ")
                                if(ans=="y"):
                                    data[2]=input("Enter new vehicle rent: ")
                                #in below line we'll join all  data into string by delimeter as ,
                                line=",".join(data)
                                #line we'll contain modified data
                                print("New data updated..")
                            vehiclelist.append(line)
                        except:
                            pass 
                        
            except FileNotFoundError:
                print("File does't exist with the given file name..")
            else:
                if(flag==False):
                    print("Record not found with this Id...")
                else:
                    with open("VehicleInfo.txt","w") as fp:
                        for vehicle in vehiclelist:
                            fp.write(vehicle)
        else:
            print("Path does't exist...")

    def deleteVehiclebyId(self,id):
        vehiclelist=[]
        flag=False
        if(path.exists("VehicleInfo.txt")):
            try:    
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        try:
                            if(data[0].lower()==id.lower()):
                                print(" Record Removed...\n",line)
                                flag=True
                            else:
                                vehiclelist.append(line)
                        except:
                            print("Vehicle not found with this Id")
            except FileNotFoundError:
                print("File does't exist with the given file name..")
            else:
                if(flag==False):
                    print("Record not found with this Id..")
                else:
                    with open("VehicleInfo.txt","w") as fp:
                        for vehicle in vehiclelist:
                            fp.write(vehicle)
        else:
            print("Path not found...")
