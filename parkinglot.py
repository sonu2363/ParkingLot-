import random

# Creating the ParkingLot class
class ParkingLot:
    def __init__(self, squareFootage, spotSize):
        self.spotSize = spotSize
        self.parkingLotSize = self.calculateParkingLotSize(squareFootage)
        self.parkingLot = [None] * self.parkingLotSize
        self.parkedCars = {}

    def calculateParkingLotSize(self, squareFootage):
        spotArea = self.spotSize[0] * self.spotSize[1]
        return squareFootage // spotArea

    def park(self, parkingLot):
        for spot in range(len(parkingLot.parkingLot)):
            if parkingLot.parkingLot[spot] is None:
                parkingLot.parkingLot[spot] = self
                parkingLot.parkedCars[self.licensePlate] = spot
                return "Car with license plate {} parked successfully in spot {}".format(self.licensePlate, spot)


    def isFull(self):
        for spot in self.parkingLot:
            if spot is None:
                return False  # If any spot is empty, the parking lot is not full
        return True  # If no spot is empty, the parking lot is full

# Creating the Car class
class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate

    def park(self, parkingLot):
        for spot in range(len(parkingLot.parkingLot)):
            if parkingLot.parkingLot[spot] is None:
                parkingLot.parkingLot[spot] = self
                parkingLot.parkedCars[self.licensePlate] = spot
                return "Car with license plate {} parked successfully in spot {}".format(self.licensePlate, spot)

        return "No available parking spots for car with license plate {}".format(self.licensePlate)

def generateRandomLicensePlate():
    random_number = random.randint(1000000, 9999999)
    return str(random_number)


def create_car():
    licensePlate = generateRandomLicensePlate()
    return Car(licensePlate)

def main():
    # Taking the user input
    parkingLotSize = int(input("Enter the parking lot size: "))
    spotLength = int(input("Enter the length of each parking spot: "))
    spotWidth = int(input("Enter the width of each parking spot: "))

    spotSize = (spotLength, spotWidth)

    parkingLot = ParkingLot(parkingLotSize, spotSize)

    # Create an array of cars with random license plates
    cars = []
    for _ in range(30):  # we can change 30 to the desired number of cars
        car = create_car()
        cars.append(car)

    # Parking cars in the parking lot
    for car in cars:
        result = car.park(parkingLot)
        print(result)

        # Check if the parking lot is full
        if parkingLot.isFull():
            print("Parking lot is full. Exiting the program.")
            break

if __name__ == "__main__":
    main()
