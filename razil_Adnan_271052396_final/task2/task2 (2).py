from main import Propertymanagement

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


