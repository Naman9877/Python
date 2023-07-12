# Make my trip
# object flight attribute from ,to, Date, traveller and class

class Flight:
    def __init__(self,source_location="Ludhiana",destination_location="Amritsar",date="15 July 2023",traveller=1,
                 traveller_class="Economy"):
        self.source_location = source_location
        self.destination_location = destination_location
        self.date = date
        self.traveller = traveller
        self.traveller_class=  traveller_class
    def fl(self):
        print("~~~~~~~~~~~~~~~~~~~~~~")
        print("Source Location is:",self.source_location)
        print("Destination Location is:",self.destination_location)
        print("Date of Flight  is :",self.date)
        print("Traveller in a flight is: ",self.traveller)
        print("Class of passenger is:",self.traveller_class)
        print("~~~~~~~~~~~~~~~~~~~~~~")

flight_1 = Flight()
flight_2 = Flight("New Delhi","Canada","20Sep,2023",2,"Buiseness")
flight_1.fl()
flight_2.fl()