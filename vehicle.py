class Vehicle:
    def __init__(self,id="MH12-CS1256",nm="TATA-Nano",rent=3000,v_type="Passenger",avail=1):
        self.id=id
        self.name=nm
        self.rent=rent
        self.v_type=v_type
        self.avail=avail
    def __str__(self):
        data = self.id + "," + self.name + "," + str(self.rent)+","+self.v_type+","+str(self.avail)
        return data

if(__name__=="__main__"):
    v=Vehicle("MH12-BC1111","Mahindra-Thar",5000,"SUV",1)
    print(v)