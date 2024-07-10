
# Gator Taxi Application

## Overview
Developed a ride-sharing software using Python to efficiently manage multiple ride requests simultaneously. The application leverages Red-Black Tree and Min Heap data structures to store and manage ride information.

## Features
- **Print(rideNumber):** Retrieves and prints trip details efficiently.
- **Print(rideNumber1, rideNumber2):** Prints all trips within a given range.
- **Insert(rideNumber, rideCost, tripDuration):** Adds new rides while maintaining data integrity.
- **GetNextRide():** Fetches and removes the ride with the lowest cost.
- **CancelRide(rideNumber):** Deletes a specific ride from the system.
- **UpdateTrip(rideNumber, new_tripDuration):** Updates trip duration or creates new trips based on changes.

## Technical Details
- **Tech Stack:** Python
- **Data Structures:** Red-Black Tree, Min Heap
- **Complexity:**
  - Print(rideNumber): O(log n)
  - Print(rideNumber1, rideNumber2): O(log n + S)
  - Insert(rideNumber, rideCost, tripDuration): O(log n)
  - GetNextRide(): O(log n)
  - CancelRide(rideNumber): O(log n)
  - UpdateTrip(rideNumber, new_tripDuration): O(log n)

## Usage
The application is designed to manage ride requests with the following attributes:
1. **rideNumber:** Unique Integer identifier for each ride.
2. **rideCost:** The estimated cost (in integer dollars) for the ride.
3. **tripDuration:** The total time (in integer minutes) needed to get from pickup to destination.

## Functions
- **Print(rideNumber):** Prints the triplet (rideNumber, rideCost, tripDuration).
- **Print(rideNumber1, rideNumber2):** Prints all triplets within the specified range.
- **Insert(rideNumber, rideCost, tripDuration):** Inserts a new ride into the system.
- **GetNextRide():** Outputs the ride with the lowest cost and deletes it from the system.
- **CancelRide(rideNumber):** Deletes the specified ride from the system.
- **UpdateTrip(rideNumber, new_tripDuration):** Updates the trip duration or cancels the trip based on the new duration.

## Contact
For any queries, please reach out to:
- **Name:** Venkata Satya Sai Subhash Vadlamani
- **Email:** v.vadlamani@ufl.edu
- **UFID:** 4326-8265
