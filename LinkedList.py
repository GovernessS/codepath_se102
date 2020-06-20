# create a class for the node, and then 
# for the linked list itself

#pass in the data and set it equal
# to data
# next = None for now (no new data yet)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# for the actual linked list, you need to
# initialize a head, which is none for now.
class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

# step 2: some way to print elements of the list
# create append function
# check if it's empty - separate situation
    def append(self, data):
        new_node = Node(data)

        #check if list isn't empty
        if self.head is None:
            self.head = new_node
            return

        # what is list is not empty?
        last_node = self.head
        # while the next pointer does not point to Null,
        # move to the next pointer
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            print("Position is greater than length of linked list.")

        prev.next = cur_node.next
        cur_node = None

    def getLength(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count += 1
            cur_node = cur_node.next
        
        return count

    def is_palindrome(self):
        # Method 1 (String):
        '''s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s[::-1] == s'''

        # Method 2 (stack-ish):
        '''p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next

        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True'''

        # Method 3 (Two Pointers):
        p = self.head
        q = self.head
        prev = []

        i = 0
        while q:
            prev.append(q)
            q = q.next
            i += 1
        q = prev[i-1]
        #print(q.data)

        count = 1
        while count <= i//2 + 1:
            if prev[-count].data != p.data:
                return False
            p = p.next
            count += 1
        return True



# step 1: append entries into linked list
# define a linked list object

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
#llist.delete_node("B") #now do deletion at a specific position
llist.delete_node_at_pos(3) #should delete D
llist.print_list()
#llist.prepend("E")
#print(llist.head.next.data)
#llist.insert_after_node(llist.head.next, "E")
#llist.print_list()

llist_2 = LinkedList()
llist_2.append("R")
llist_2.append("A")
llist_2.append("D")
llist_2.append("A")
llist_2.append("R")

llist_3 = LinkedList()
llist_3.append("R")
llist_3.append("A")
llist_3.append("D")
llist_3.append("E")
llist_3.append("R")

print(llist_2.is_palindrome())
print(llist_3.is_palindrome())