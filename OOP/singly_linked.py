class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):	    # added this line, takes a value
        new_node = SLNode(val)	        # create a new instance of our Node class using the given value
        current_head = self.head        # save the current head in a variable
        new_node.next = current_head	# SET the new node's next TO the list's current head
        self.head = new_node	        # SET the list's head TO the node we created in the last step
        return self	                    # return self to allow for chaining
    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
        runner = runner.next 	        # set the runner to its neighbor
        return self	                    # once the loop is done, return self to allow for chaining
    def add_to_back(self, val):
        if self.head == None:	        # if the list is empty
            self.add_to_front(val)	    # run the add_to_front method
        return self	                    # let's make sure the rest of this function doesn't happen if we add to the front

        new_node = SLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	        # increment the runner to the next node in the listcopy
        return self                     # return self to allow for chaining

    def remove_from_front(self)         # remove the first node and return its value
        if self.head != None:
            runner = self.head    
        if self.head.next == None:      # if the self.head/original head has .next = None, meaning nothing comes after, then remove by setting .head to none
            self.head = None
        while runner.next != None:          # While runner's .next is not set to None, meaning there are still values after it
            runner = runner.next            # set our runner to the next node's value
            if runner.next.next == None:    # If runner's next.next holds value of None, then no additional values in list, so remove
                runner.next = None
        else: 
            print("No nodes exist")       # if current nodes .head holds value of None, then doesn't exist so return False as list doesn't exist (no starting node)
            return False

    def remove_from_back(self)          # remove the last node and return its value
        if self.head != None:
            runner = self.head
        if self.head.next == None:      # if list comprised of only one element, remove that element
            self.head = None
            if runner.next == None:
                runner = None
        else:
            print("No nodes exist")
            return False


    def remove_val(self, val)           # remove the first node with the given value
        if self.head != None:
            runner = self.head
        if self.head.next == val:
            self.head.next = None
            print(self.head)
        while runner.next != val:
            runner = runner.next
            if runner.next.next == val:
                runner.next.next = None
        else:
            print("No nodes exist")
            return False
                

    def insert_at(self, val, n)         # insert a node with value val as the nth node in the list
    # i'll come back to this... it's daunting




