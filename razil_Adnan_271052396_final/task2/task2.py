# Decimal to binary number using recursion : Given a decimal number as input, we need to
# write a program to convert the given decimal number into an equivalent binary number.
# Examples : Input : 7 Output :111
# Input :10 Output :1010
# def decintobinary:
#
book=[]
properties={"propid":[]}
class Propertymanagement:
    global properties
    def __init__(self,propid,name,location,description,pricen,availabilty_status):
        self.propid=propid
        self.name=name
        self.location=location
        self.description=description
        self.pricenight=pricen
        self.availability= availabilty_status
        self.list=[self.name,self.location,self.description,self.pricenight,self.availability]

    def add_properties(self):
        self.properties[self.propid].append(self.list)
    def show_properties(self):
        for i in properties[self.propid]:
            print(i)

class Host:
    global properties
    def __init__(self,propid,name,location,description,pricen,availabilty_status,h_name,h_contact):
        self.h_name=h_name
        self.h_cont=h_contact
        self.propid = propid
        self.name = name
        self.location = location
        self.description = description
        self.pricenight = pricen
        self.availability = availabilty_status
        self.obj=Propertymanagement(propid,name,location,description,pricen,availabilty_status)
        self.properties = {self.propid: []}
        self.list = [self.name, self.location, self.description, self.pricenight, self.availability]
        self.properties = {self.propid: []}
        self.profile = []
        self.profile.append(self.h_name)
        self.profile.append(self.h_cont)

    def add_properties(self):
        properties[self.propid].append(self.list)

    def show_properties(self):
        for i in properties[self.propid]:
            print(i)

    def show_profile(self):
        print(self.profile)
class Guest:
    global properties
    def __init__(self, propid, name, location, description, pricen, availabilty_status, g_name, g_contact):
        self.g_name = g_name
        self.g_cont = g_contact
        self.propid = propid
        self.name = name
        self.location = location
        self.description = description
        self.pricenight = pricen
        self.availability = availabilty_status
        self.obj = Propertymanagement(propid, name, location, description, pricen, availabilty_status)
        self.properties = {self.propid: []}
        self.list = [self.name, self.location, self.description, self.pricenight, self.availability]
        self.profile=[]
        self.profile.append(self.g_name)
        self.profile.append(self.g_cont)
        book=[]
    def show_properties(self):
        for i in properties[self.propid]:
            print(i)
    def show_profile(self):
        print(self.profile)



class Bookingsystem():
    global book,properties

    def __init__(self,booking_id,property,checkin,checkout,booking_status,propid, name, location, description, pricen, availabilty_status, g_name, g_contact):
        self.guest=Guest(propid, name, location, description, pricen, availabilty_status, g_name, g_contact)
        self.booking_id=booking_id
        self.property=property
        self.checkin=checkin
        self.checkout=checkout
        self.bookingstatus=booking_status
        self.g_name = g_name
        self.g_cont = g_contact
        self.propid = propid
        self.name = name
        self.location = location
        self.description = description
        self.pricenight = pricen
        self.availability = availabilty_status


    def booking(self):
        self.guest.show_properties()
        prop=input("enter the property id you would like to buy")
        book[self.booking_id]=prop
        properties.pop(prop)

host=Host(4,4,4,4,4,6,"m",5)
host.add_properties()
book1=Bookingsystem(1,45,4,4,4,4,4,4,4,4,6,"mum",5)
book1.booking()















