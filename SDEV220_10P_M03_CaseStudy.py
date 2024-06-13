#Tracie Lindquist
#SDEV220_10P_M03_

 

class Vehicle ():
    """Class to build a vehicle"""
    def __init__(self, vehicle):
        """Initialize attirbutes of a vehicle"""
        self.vehicle = vehicle
   
    def new_vehicle(self):
        return vehicle

class Automobile(Vehicle):
    """A class to add vehicle details"""

    def __init__ (self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    
    def new_automobile(self):
        print(f'Vehicle: {vehicle}')
        print(f'Year: {year}')
        print(f'Make: {make}')
        print (f'Model: {model}')
        print (f'Doors: {doors}')
        if roof == "Y":
            print(f'Roof: Sunroof')
        else:
            print("Hard Top")
        

vehicle_prompt = "Enter the vehicle type: "
year_prompt = "Enter the year the vehicle was manufactured as XXXX: "
make_prompt= "Enter the make: "
model_prompt = "Enter the model: "
doors_prompt = "How many doors does the vehicle have: "
roof_prompt = "Does the vehile have a sunroof? Enter Y or N. "
vehicle = str(input(vehicle_prompt)).lstrip().rstrip().capitalize()
year = int(input(year_prompt))
make = input(make_prompt).lstrip().rstrip().capitalize()
model = input(model_prompt).lstrip().rstrip().capitalize()
doors = int(input(doors_prompt))
roof = input(roof_prompt).lstrip().rstrip().capitalize()



my_vehicle = Vehicle(vehicle)
my_automobile = Automobile(year, make, model, doors, roof)
my_vehicle.new_vehicle()
my_automobile.new_automobile()

