import datetime
from datetime import datetime, timedelta
    
# -----------------------------------------------------------------
# Function Name:        Validate Integer Input
# Function Purpose:     Validate any integer data
# -----------------------------------------------------------------
def Validate_Integer_Input( int_Input ):
   try:
        int_Input = int(int_Input)
        if(int_Input > 0):
            global strFlag
            strFlag = True 
        else:
            print("Value Must Be Positive")
   except ValueError:
        int_Input = int(0)
        print("Value must exist and be numeric")
   return int_Input





# -----------------------------------------------------------------
# Function Name:        Validate String Input
# Function Purpose:     Validate any string data
# -----------------------------------------------------------------
def Validate_String_Input( str_Input ):
   try:
        str_Input = str(str_Input)
        if str_Input == "":
            print("Value must exist")
        else:
            global strFlag
            strFlag = True
   except ValueError:
        str_Input = str("")
        print("Value must exist.")
   return str_Input

# -----------------------------------------------------------------
# Function Name:        Validate String Input for bikes
# Function Purpose:     Validate the string data given for bike type
# -----------------------------------------------------------------
def Validate_String_Input_Bikes( str_Input ):
   try:
        str_Input = str(str_Input)
        if(str_Input == "mountain" or str_Input == "touring" or str_Input == "road"):
            global strFlag
            strFlag = True 
        else:
            print("Value must be mountian, road, or touring")
   except ValueError:
        str_Input = str("")
        print("You must insert something.")
   return str_Input

# -----------------------------------------------------------------
# Function Name:        Validate String Input for bikes
# Function Purpose:     Validate the string data given for bike type
# -----------------------------------------------------------------

def Validate_Integer_Input_Basis( int_Input ):
   try:
        int_Input = int(int_Input)
        if int_Input > 0:
            if (int_Input == 1 or int_Input == 2 or int_Input == 3):
                global strFlag
                strFlag = True 
            else:
                print("Value must be a 1, 2, or 3.")
        else:
            print("Value Must Be Positive")
   except ValueError:
        int_Input = int(0)
        print("Value Must be Numeric")
   return int_Input

class BikeRental:
    
    def __init__(self):
        """
        Our constructor class that instantiates bike rental shop.
        """
        self.mountain_bikes = 0
        self.road_bikes = 0
        self.touring_bikes = 0

        self.stock = {
            "mountain": mountain_bikes,
            "road": road_bikes,
            "touring": touring_bikes
        }

    def displaystock(self):
        """
        Displays the bikes currently available for rent in the shop.
        """
        print("We currently have {} mountian bikes available to rent.".format(self.stock['mountain']))
        print("We currently have {} touring bikes available to rent.".format(self.stock['touring']))
        print("We currently have {} road bikes available to rent.".format(self.stock['road']))

        return self.stock

    def rentBikeOnHourlyBasis(self, n, bikeType):

        """
        Rents a bike on hourly basis to a customer.
        """
        # reject invalid input 
        if n <= 0:
            print("Number of bikes should be positive!")
            return False
        # do not rent bike is stock is less than requested bikes
        
        elif n > self.stock[bikeType]:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock[bikeType]))
            return False
        # rent the bikes        
        else:
            now = datetime.now()                      
            print("You have rented {} bike(s) on hourly basis today at {}.".format(n, now.strftime("%I:%M %p")))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            return True     
     
    def rentBikeOnDailyBasis(self, n, bikeType):
        """
        Rents a bike on daily basis to a customer.
        """
        
        if n <= 0:
            print("Number of bikes should be positive!")
            return False
        elif n > self.stock[bikeType]:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock[bikeType]))
            return False
    
        else:
            now = datetime.now() 
            print("You have rented {} bike(s) on daily basis today at {}.".format(n, now.strftime("%I:%M %p")))
            print("You will be charged $20 for each day per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            return True 
        
    def rentBikeOnWeeklyBasis(self, n, bikeType):
        """
        Rents a bike on weekly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return False

        elif n > self.stock[bikeType]:
            print("Sorry! We currently only have {} bikes available to rent. Please try again.".format(self.stock[bikeType]))
            return False        
        
        else:
            now = datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {}.".format(n, now.strftime("%I:%M %p")))
            print("You will be charged $60 for each week per bike.")
            print("We hope that you enjoy our service.")
            self.stock[bikeType] -= n
            return True 
    
    
    def returnBike(self, request):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
       
        # extract the tuple and initiate bill
        rentalBasis, rentalTime, bikes, name, bikeType  = request
        bill = 0
        discount = 0
        discountedbill = 0
        global TotalDailyRevenue
        # issue a bill only if all three parameters are not null!
        if rentalTime and rentalBasis and bikes:
            self.stock[bikeType] += bikes
            now = datetime.now() #+ timedelta(days = 8, hours = 5)
            rentalPeriod = now - rentalTime
            
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * bikes
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * bikes
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * bikes
            
            
            
            print("Thanks for returning your bike {}. Hope you enjoyed our service!".format(name))
            print('You rented {} {} bikes.'.format(bikes, bikeType))
            if rentalBasis == 1:
                if rentalPeriod.seconds <= 3600:
                    print('You rented the bike(s) for 1 hour')
                    bill = 5 * bikes
                else:
                    print('You rented the bike(s) for {} hours'.format(round(rentalPeriod.seconds / 3600)))
            elif rentalBasis == 2:
                if rentalPeriod.days <= 1:
                    print('You rented the bike(s) for 1 day')
                    bill = 20 * bikes
                else:
                    print('You rented the bike(s) for {} day(s)'.format(round(rentalPeriod.days)))
            elif rentalBasis == 3:
                if rentalPeriod.days <= 7:
                    print('You rented the bike(s) for 1 week.')
                    bill = 60 * bikes
                else:
                    print('You rented the bike(s) for {} week(s)'.format(round(rentalPeriod.days/7)))

            # family discount calculation
            if (3 <= bikes <= 5):
                print("You are eligible for Family rental promotion of 30% discount")
                discount = bill * 0.3

            print('The total before discount is {}'.format(bill))
            print('The discount amount is {}'.format(discount))
            print('The final total is {}'.format(bill-discount))
            total = bill - discount
            TotalDailyRevenue += total
            return bill
        else:
            print("Are you sure you rented a bike with us?")
            return None

class Customer:
    def __init__(self, name, customer_id, bikeType, rentalBasis, rentalTime, bikes):
        """
        Our constructor method which instantiates various customer objects.
        """
        self.name = name
        self.customer_id = customer_id
        self.bikeType = bikeType
        self.rentalBasis = rentalBasis
        self.rentalTime = rentalTime
        self.bikes = bikes
    
    def requestBike(self):
        global TotalDailyBikes
        """
        Takes a request from the customer for the number of bikes.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        
        # implement logic for invalid input
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Invalid input. Number of bikes should be greater than zero!")
            return -1
        else:
            self.bikes = bikes
            TotalDailyBikes += bikes
        return self.bikes
     
    def returnBike(self, rentalBasis, rentalTime, bikes, name, bikeType):
        """
        Allows customers to return their bikes to the rental shop.
        """
        if rentalBasis and rentalTime and bikes and name and bikeType:
            return rentalTime, rentalBasis, bikes, name, bikeType  
        else:
            return 0,0,0,0,0
        
###################
## Main Routine
###################
TotalDailyBikes = int(0)
TotalDailyRevenue = float(0)
customerlist = []
flag = True
strFlag = False

while strFlag is False:
    mountain_bikes = input("Enter the number of mountain bikes available: ")
    mountain_bikes = Validate_Integer_Input (mountain_bikes)

strFlag = False

while strFlag is False:
    road_bikes = input("Enter the number of road bikes available: ")
    road_bikes = Validate_Integer_Input (road_bikes)

strFlag = False

while strFlag is False:
    touring_bikes = input("Enter the number of touring bikes available: ")
    touring_bikes = Validate_Integer_Input (touring_bikes)

strFlag = False



shop1 = BikeRental()
BikeRental.mountain_bikes = mountain_bikes
BikeRental.road_bikes = road_bikes
BikeRental.touring_bikes = touring_bikes



while True:
        print("Select an option:")
        print("1. New Customer Rental")
        print("2. Rental Return")
        print("3. Show Inventory")
        print("4. End of Day")
        print("5. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            #-----------------
            #Get and Validate
            #-----------------
            while strFlag is False:
                name = input("Enter customer name: ")
                name = Validate_String_Input(name)
            strFlag = False
            while strFlag is False:
                customer_id = input("Enter customer ID: ")
                customer_id = Validate_Integer_Input(customer_id)
            strFlag = False
            while strFlag is False:
                bikes = input("Enter the number of bikes you would like to rent: ")
                bikes = Validate_Integer_Input(bikes)
            strFlag = False
            print("Bike types available: mountain, road, touring")
            while strFlag is False:
                bikeType = input("Enter the type of bike: ").lower()
                bikeType = Validate_String_Input_Bikes(bikeType)
            strFlag = False
            while strFlag is False:
                rentalBasis = input("Enter rental type (hourly(1)/daily(2)/weekly(3)): ")
                rentalBasis = Validate_Integer_Input_Basis(rentalBasis)
            strFlag = False
            #--------------
            #Rent The Bike
            #--------------
            if rentalBasis == 1:
                rentalTime = datetime.now()
                flag = shop1.rentBikeOnHourlyBasis(bikes, bikeType)
            elif rentalBasis == 2:   
                rentalTime = datetime.now()
                flag = shop1.rentBikeOnDailyBasis(bikes, bikeType)
            elif rentalBasis == 3:
                rentalTime = datetime.now()
                flag = shop1.rentBikeOnWeeklyBasis(bikes, bikeType)
           
            #--------------------------------
            # If enough bikes, store customer
            #--------------------------------

            if flag is True:
            # Store the customer object in the list
                newCustomer = Customer(name, customer_id, bikeType, rentalTime, rentalBasis, bikes)
                customerlist.append(newCustomer)
            #for obj in customerlist:
                #print(obj.name, obj.customer_id, bikeType, rentalTime, rentalBasis, bikes, sep=' ')
         
        elif choice == '2':
            name = input('Enter customer name: ')
            customer = next((cust for cust in customerlist if cust.name == name), None)
            if customer:
                request = customer.returnBike(customer.rentalBasis, customer.rentalTime, customer.bikes, customer.name, customer.bikeType)
                shop1.returnBike(request)
                customerlist.remove(customer)
            else:
                print('No customer with that name was found.')
            
        elif choice == '3':
            shop1.displaystock()
        elif choice == '4':
            print('There were {} bikes rented today.'.format(TotalDailyBikes))
            print('There was ${:,.2f} colleced today in revenue.'.format(TotalDailyRevenue))
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")