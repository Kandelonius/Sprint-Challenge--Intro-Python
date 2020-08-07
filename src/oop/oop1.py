# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle():  # master class
    def __init__(self):
        pass


class FlightVehicle(Vehicle):  # based from Vehicle
    def __init__(self):
        super().__init__()
        pass


class GroundVehicle(Vehicle):  # based from Vehicle
    def __init__(self):
        super().__init__()
        pass


class Starship(FlightVehicle):  # based from FlightVehicle
    def __init__(self):
        super().__init__()


class Airplane(FlightVehicle):  # based from FlightVehicle
    def __init__(self):
        super().__init__()
        pass


class Car(GroundVehicle):  # based from GroundVehicle
    def __init__(self):
        super().__init__()
        pass


class Motorcycle(GroundVehicle):  # based from GroundVehicle
    def __init__(self):
        super().__init__()
        pass
