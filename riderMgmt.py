from vehiclemgnt import VehicleMgmt
from os import path
from datetime import datetime
class RiderMgnt:
    def addUser(self):
        fp=open("IssueInfo.txt","a")
        fp.write("\n")
        fp.close()

    def showallVehicle(self):
        try:
            fp=open("VehicleInfo.txt","r")
        except:
            print("File not found..")
        else:
            data=fp.read()
            print(data)
            fp.close()

    def searchVehiclebyId(self,id):
        VehicleMgmt.searchVehiclebyId(id)
    
    def searchVehiclebyName(self,nm):
        VehicleMgmt.searchVehiclebyNm(nm)

    def searchVehiclebyrent(self,rent):
        VehicleMgmt.searchVehiclebyRent(rent)
    
    def searchVehiclebytype(self,v_type):
        VehicleMgmt.searchVehiclebyType(v_type)
    
    def leaveVehicle(self,id,rname,date_of_issue,start_point,end_point):
        riderlist=[]
        flag=False
        if(path.exists("VehicleInfo.txt")):
            try:   
                with open("VehicleInfo.txt","r") as fp:
                    for line in fp:
                        data=line.split(",")
                        if(data[0].lower()==id.lower()): 
                            print(" Record found...\n",line)
                            flag=True
                            try:
                                if(int(data[4])==1):
                                    Result= id+"," +rname +","+date_of_issue+","+start_point+","+end_point
                                    print(" HAPPY JOURNEY..")
                                    with open("IssueInfo.txt","a") as fp1:
                                        fp1.write(Result)
                                        fp1.write("\n")
                                    data[4]="0\n"
                                else:
                                    print("already the vehicle on rent")
                                    
                            except:
                                pass
                            
                        line=",".join(data)
                        #line+="\n"
                        riderlist.append(line)
            except FileNotFoundError:
                print("File does't exist with the given file name..")
            else:  
                if(flag==False):
                    print('Vehicle not found with given Id')
                else:
                    with open("VehicleInfo.txt","w") as fp:
                        for rider in riderlist:
                            fp.write(rider)
        else:
            print("Path does't exist..")
    
    def returnVehicle(self,id,date_of_return):
        riderlist=[]
        flag=False
        if(path.exists("IssueInfo.txt")):
            with open("IssueInfo.txt","r") as fp:
                for line in fp:
                    data=line.split(",")
                    if(data[0].lower()==id.lower()):
                        print(" Rider record found..\n",line)
                        flag=True
                        try:
                            date_of_issue=data[2]
                            date_of_issue=date_of_issue.split("/")
                            year=int(date_of_issue[2])
                            month=int(date_of_issue[1])
                            day=int(date_of_issue[0])
                            try:
                                date_of_issue=datetime(year,month,day)
                            except ValueError:
                                print(" Please check issue date and correct it...")
                            else:
                                date_of_return=date_of_return.split("/")
                                year=int(date_of_return[2])
                                month=int(date_of_return[1])
                                day=int(date_of_return[0])
                            try:
                                date_of_return=datetime(year,month,day)
                            except ValueError:
                                print(" Please check return date and correct it.. ")
                            else:
                                diff=(date_of_return-date_of_issue).days
                                with open("VehicleInfo.txt","r") as fp:
                                    for line in fp:
                                        data=line.split(",")
                                        if(data[0].lower()==id.lower()):
                                            rent_per_day=int(data[2])
                                            if(diff>0):
                                                total_days=diff+1
                                                print(" Total days are: ",total_days)
                                                total_rent=total_days*rent_per_day
                                                print(" Now your rent is: Rs.",total_rent)
                                                print(" Thank you for visiting...")
                                            else:
                                                print(" You should pay: Rs.",rent_per_day)
                                break
                        except:
                            print(" Please enter date correctly")
                    line=",".join(data)
                    riderlist.append(line)
                   
        
            if(flag==False):
                print("Please enter correct vehicle id")
            else:
                with open("IssueInfo.txt","w") as fp:
                    for main in riderlist:
                        fp.write(main)
                riderlist=[]  
                try:
                    with open("VehicleInfo.txt","r") as fp1:
                        for line in fp1:
                            data=line.split(",")
                            try:
                                if(data[0].lower()==str(id).lower()):
                                    data[4]="1\n"
                            except:
                                print("Particular Vehicle is not available")    
                            else:
                                line=",".join(data)
                            riderlist.append(line)
                except FileNotFoundError:
                    print("File does't exist ...")
                else:    
                    with open("VehicleInfo.txt","w") as fs:
                        for dates in riderlist:
                            fs.write(str(dates))    
        else:
            print("Path does't exist..")            

                    