from try import Guest

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