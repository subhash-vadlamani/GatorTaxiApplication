class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.curr_size = 0

    def insert(self, ele):
        """
        We insert an element at the end of the list and use the 'heapify_up' method to bubble the element up the heap
        to it's right place.
        :param ele:
        :return:
        """
        self.heap_list.append(ele)
        self.curr_size += 1
        self.heapify_up(self.curr_size)

    def heapify_up(self, i):
        """
        This method is used to bubble up the minimum element after the addition of the new element at the end of the heap list.
        After the completion of this method, the min heap property is maintained and all the elements in the data strucutre
        are less than it's children.
        :param i:
        :return: Nothing
        """
        while (i // 2) > 0:
            if self.heap_list[i].ride.less_than(self.heap_list[i // 2].ride):
                self.swap(i, (i // 2))
            else:
                break
            i = i // 2

    def swap(self, ind1, ind2):
        temp = self.heap_list[ind1]
        self.heap_list[ind1] = self.heap_list[ind2]
        self.heap_list[ind2] = temp
        self.heap_list[ind1].min_heap_index = ind1
        self.heap_list[ind2].min_heap_index = ind2

    def heapify_down(self, i):
        """

        Here, we compare the ride cost of the current index element with that of the minimum child.
        If the cost of the ride at the current index is less than that of the cost of the ride at
        the index of the minimum child, then we swap the elements at the current index and the
        minimum child.
        :param i:
        :return:
        """
        while (i * 2) <= self.curr_size:
            ind = self.get_min_child_index(i)
            if not self.heap_list[i].ride.less_than(self.heap_list[ind].ride):
                self.swap(i, ind)
            i = ind

    def get_min_child_index(self, i):

        """
        First, we check if there exists a right child of the current node. If there does not exist a right child,
        we will directly return the index of the left child.
        If not, we check the value of the ride costs of the left child and the right child of the given node and return
        the index of the child node which has the least value.
        :param i:
        :return:
        """
        if (i * 2) + 1 > self.curr_size:
            return i * 2
        else:
            if self.heap_list[i * 2].ride.less_than(self.heap_list[(i * 2) + 1].ride):
                return i * 2
            else:
                return (i * 2) + 1


    # Method to update the heap element when the trip duration of the ride is changed
    def update_heap_element(self, i, new_key):
        """
        We first access the node from the heap list with the index that we want to update. Later, we update
        that node in the min heap and we change the trip duration of the ride that is represented by the node.
        :param i:
        :param new_key:
        :return:
        """

        node = self.heap_list[i]
        node.ride.tripDuration = new_key
        # When the trip duration of the ride is changed, we have to change the position of the trip in the heap.
        if i == 1:
            # If the node that is updated is the root node
            self.heapify_down(i)
        elif self.heap_list[i // 2].ride.less_than(self.heap_list[i].ride):
            # If the node that is updated has a value that is higher than it's child, only the heap below it needs to be balanced
            self.heapify_down(i)
        else:
            # If the node that is updated has a value that is less than it's child, we have to bubble up he minimum element
            self.heapify_up(i)

    def pop(self):
        """
        Here, we take the first element of the min heap out, replace it with the last element of the heap
        and perform the heapify_down operation for the heap to become a min_heap again.
        :return:
        """


        if len(self.heap_list) == 1:
            return 'No Rides Available'

        root = self.heap_list[1]

        self.swap(1, self.curr_size)
        # self.heap_list[1] = self.heap_list[self.curr_size]
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(1)

        return root

    def delete_heap_element(self, i):
        """
        We are going to swap the element at the index we are trying to delete with the element at the end and
        then we are going to push the last element to the right place using the 'heapify_down' method.
        :param i:
        :return:
        """

        self.swap(i, self.curr_size)
        self.curr_size -= 1
        *self.heap_list, _ = self.heap_list

        self.heapify_down(i)




class MinHeapNode:
    def __init__(self, ride, rbt, min_heap_index):
        self.ride = ride
        self.rbTree = rbt
        self.min_heap_index = min_heap_index
