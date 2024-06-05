from main import Propertymanagement

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



