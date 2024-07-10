"""
This is the class to define the ride. It contains three components:
1) rideNumber -> Signifies the RideNumber of the current ride
2) rideCost -> Signifies the estimated cost of the ride.
3) tripDuration -> Signifies the estimated time in minutes of the ride.
"""

class Ride:
    def __init__(self, rideNumber, rideCost, tripDuration):
        self.rideNumber = rideNumber
        self.rideCost = rideCost
        self.tripDuration = tripDuration


    """
        Method to know if the current ride cost is less than or equal to a different ride.
        If the ride cost is the same, the ride with the smallest trip duration is considered.
    """
    def less_than(self, different_ride):
        if self.rideCost < different_ride.rideCost:
            return True
        elif self.rideCost > different_ride.rideCost:
            return False
        elif self.rideCost == different_ride.rideCost:
            if self.tripDuration > different_ride.tripDuration:
                return False
            else:
                return True
