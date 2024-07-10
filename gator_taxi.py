import sys

from ride_model import Ride
from min_heap import MinHeap
from min_heap import MinHeapNode
from red_black_tree import RedBlackTree, RBTNodeClass


"""
This function is responsible for inserting a new ride into the heap and the Red Black Tree
"""

def insert_ride_into_heap_and_rbt(ride, heap, rbt):
    # If the ride with the given ride number already exists, we should not
    # allow an insert with the same ride number.
    if rbt.get_ride_with_key(ride.rideNumber) is not None:
        append_message_to_output(None, "Duplicate RideNumber", False)
        sys.exit(0)
        return
    rbt_node = RBTNodeClass(None, None)
    min_heap_node = MinHeapNode(ride, rbt_node, heap.curr_size + 1)
    #Inserting the ride into the Heap
    heap.insert(min_heap_node)
    # Inserting the ride into the Red Black Tree
    rbt.insert(ride, min_heap_node)

"""
This function will combine all the outputs that are required to be outputted to the output file and place them in the file
"""


def append_message_to_output(ride, message, list):
    file = open("output.txt", "a")
    if ride is None:
        file.write(message + "\n")
    else:
        message = ""
        if not list:
            message += ("(" + str(ride.rideNumber) + "," + str(ride.rideCost) + "," + str(ride.tripDuration) + ")\n")
        else:
            if len(ride) == 0:
                message += "(0,0,0)\n"
            for i in range(len(ride)):
                if i != len(ride) - 1:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + "),")
                else:
                    message = message + ("(" + str(ride[i].rideNumber) + "," + str(ride[i].rideCost) + "," + str(
                        ride[i].tripDuration) + ")\n")

        file.write(message)
    file.close()

# This method is used to get the information of the ride with the given rideNumber from the Red Black Tree
def print_ride(rideNumber, rbt):
    result = rbt.get_ride_with_key(rideNumber)
    if result is None:
        append_message_to_output(Ride(0, 0, 0), "", False)
    else:
        append_message_to_output(result.ride, "", False)


# This method is used to get all the ride information whose ride cost lies between 'low' and 'high' from the Red Black Tree
def print_rides(low, high, rbt):
    list = rbt.get_rides_in_range(low, high)
    append_message_to_output(list, "", True)


# This method is used to fetch the right that has the next lowest cost. In case of tie, the ride with the shortest duration is picked.
def get_next_ride(heap, rbt):
    if heap.curr_size != 0:
        popped_node = heap.pop()
        rbt.delete_node(popped_node.ride.rideNumber)
        append_message_to_output(popped_node.ride, "", False)
    else:
        append_message_to_output(None, "No active ride requests", False)


# This method is used to completly remove the ride from the Red Black Tree.
def cancel_ride(ride_number, heap, rbt):
    heap_node = rbt.delete_node(ride_number)
    if heap_node is not None:
        heap.delete_heap_element(heap_node.min_heap_index)


# This method is used to update the trip duration of a particular ride.
def update_ride(rideNumber, new_duration, heap, rbt):
    rbt_node = rbt.get_ride_with_key(rideNumber)
    if rbt_node is None:
        print("")
        # append_to_output(None, "No ride found to update", False)
    elif new_duration <= rbt_node.ride.tripDuration:
        heap.update_heap_element(rbt_node.min_heap_node.min_heap_index, new_duration)
    elif rbt_node.ride.tripDuration < new_duration <= (2 * rbt_node.ride.tripDuration):
        cancel_ride(rbt_node.ride.rideNumber, heap, rbt)
        insert_ride_into_heap_and_rbt(Ride(rbt_node.ride.rideNumber, rbt_node.ride.rideCost + 10, new_duration), heap, rbt)
    else:
        cancel_ride(rbt_node.ride.rideNumber, heap, rbt)


if __name__ == "__main__":
    heap = MinHeap()
    rbt = RedBlackTree()
    file = open("output.txt", "w")
    file.close()

    filename = sys.argv[1]
    file = open(filename, "r")
    for s in file.readlines():
        n = []
        for num in s[s.index("(") + 1:s.index(")")].split(","):
            if num != '':
                n.append(int(num))
        if "Insert" in s:
            insert_ride_into_heap_and_rbt(Ride(n[0], n[1], n[2]), heap, rbt)
        elif "Print" in s:
            if len(n) == 1:
                print_ride(n[0], rbt)
            elif len(n) == 2:
                print_rides(n[0], n[1], rbt)
        elif "UpdateTrip" in s:
            update_ride(n[0], n[1], heap, rbt)
        elif "GetNextRide" in s:
            get_next_ride(heap, rbt)
        elif "CancelRide" in s:
            cancel_ride(n[0], heap, rbt)

