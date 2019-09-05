
#  File: TestLinkedList.py
#  Description: Test the Linked List with given function

#  Student Name: Woongchan Lee
#  Student UT EID: WL8863

#  Partner Name: Dohyun Kim
#  Partner UT EID: DK25659

#  Course Name: CS 313E
#  Unique Number: 85575
#  Date Created: 07/22/2019
#  Date Last Modified: 07/22/2019


class Link (object):
    def __init__ (self, data = 0, next = None):
        self.data = data
        self.next = next

    # return a String representation of a Link
    def __str__(self):
        s = ''
        s += str(self.data)
        return s


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.size = 0

    # get number of links
    def get_num_links(self):
        current = self.first

        while current != None:
            self.size += 1
            current = current.next

        return self.size

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if current == None:
            self.first = new_link
            return

        while current.next != None:
            current = current.next

        current.next = new_link

    # add an item in an ordered list in ascending order
    def insert_in_order(self, data):
        new_link = Link(data)
        previous = self.first
        current = self.first
        if current == None:
            self.first = new_link

        while current.next != None:
            if previous.data < new_link.data < current.data:
                new_link.next = current
                previous.next = new_link
                break
            previous = current
            current = current.next

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        while current != None:
            if current.data == data:
                return current.data
            current = current.next
        return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        while current != None:
            if current.data == data:
                return current.data
            elif data < current.next.data and data != current.data:
                return None
            current = current.next

    # Delete and return Link from an unordered list or None if not found
    def delete_link(self, data):
        previous = self.first
        current = self.first

        if current == None:
            return None

        while current.data != data:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if current == self.first:
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        s = ''
        current = self.first
        counter = 0
        while current != None:
            if counter % 10 == 9:
                s += str(current.data)
                current = current.next
                counter += 1
                s += "\n"
            s += str(current.data)
            s += "  "
            current = current.next
            counter += 1
        return s

    # Copy the contents of a list and return new list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first

        if current == None:
            return None

        while current != None:
            new_list.insert_last(current.data)
            current = current.next

        return new_list

    # Reverse the contents of a list and return new list
    def reverse_list(self):
        new_list = LinkedList()
        current = self.first

        if current == None:
            return None

        while current != None:
            new_list.insert_first(current.data)
            current = current.next

        return new_list

    # Sort the contents of a list in ascending order and return new list
    def sort_list(self):
        current = self.first
        # check if list is empty
        if self.is_empty():
            return None
        # add linked list elements into array to sort
        new_list = LinkedList()
        list = []
        num = 0
        while current != None:
            num = str(current.data)
            list.append(int(num))
            current = current.next
        # sort list
        list.sort()
        # revert list back into linked list form
        while len(list) > 0:
            new_list.insert_last(list.pop(0))
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        current = self.first
        if self.is_empty() or current.next == None:
            return True
        while current.next != None:
            if current.data > current.next.data:
                return False
            current = current.next
        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first == None

    # Merge two sorted lists and return new list in ascending order
    def merge_list(self, other):
        new_list = LinkedList()
        if self.is_empty() and other.is_empty():
            return None
        if self.is_empty():
            return other
        if other.is_empty():
            return self
        current = self.first
        while current != None:
            new_list.insert_last(current)
            current = current.next
        current = other.first
        while current != None:
            new_list.insert_last(current)
            current = current.next
        new_list = new_list.sort_list()
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current_self = self.first
        current_other = other.first

        if self.is_empty() and other.is_empty():
            return True
        elif self.is_empty() or other.is_empty():
            return False

        while current_self != None or current_other != None:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    def remove_duplicates(self):
        new_list = LinkedList()
        current = self.first

        if self.is_empty():
            return None

        while current != None:
            if new_list.find_unordered(current.data) == None:
                new_list.insert_last(current.data)
            current = current.next
        return new_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    lst = LinkedList()
    lst.insert_first(2)
    lst.insert_first(8)
    lst.insert_first(9)
    lst.insert_first(11)
    lst.insert_first(15)
    lst.insert_first(97)
    lst.insert_first(36)
    lst.insert_first(24)
    lst.insert_first(73)
    lst.insert_first(1)
    lst.insert_first(59)
    print("\ninsert_first() Tests")
    print("Added 2, 8, 9, 11, 15, 97, 36, 24, 73, 1, 59")
    print("List:", lst)

    # Test method insert_last()
    lst.insert_last(7)
    print("\ninsert_last() Tests")
    print("Added 7 to linked list")
    print("List:", lst)

    # Test method insert_in_order()
    lst = LinkedList()
    lst.insert_first(97)
    lst.insert_first(63)
    lst.insert_first(54)
    lst.insert_first(33)
    lst.insert_first(22)
    lst.insert_first(19)
    lst.insert_first(18)
    lst.insert_first(17)
    lst.insert_first(3)
    lst.insert_first(2)
    lst.insert_first(1)
    print("\ninsert_in_order() Tests")
    print("Original list:", lst)

    lst.insert_in_order(4)  # insert_in_order()
    print("Added 4 in list:", lst)

    # Test method get_num_links()
    print("\nget_num_links() Tests")
    print("List:", lst)
    print("Number of links in list:", lst.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    # Sample unordered list
    lst = LinkedList()
    lst.insert_first(2)
    lst.insert_first(8)
    lst.insert_first(9)
    lst.insert_first(11)
    lst.insert_first(15)
    lst.insert_first(97)
    lst.insert_first(36)
    lst.insert_first(24)
    lst.insert_first(73)
    lst.insert_first(1)
    lst.insert_first(59)

    print("\nfind_unordered() Tests")
    print("Original list:", lst)
    print("When there is the data:", lst.find_unordered(2))  # when there is the data
    print("When there isn't the data:", lst.find_unordered(44))  # when there isn't the data

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    # Sample ordered list
    lst = LinkedList()
    lst.insert_first(97)
    lst.insert_first(63)
    lst.insert_first(54)
    lst.insert_first(33)
    lst.insert_first(22)
    lst.insert_first(19)
    lst.insert_first(18)
    lst.insert_first(17)
    lst.insert_first(3)
    lst.insert_first(2)
    lst.insert_first(1)

    print("\nfind_ordered() Tests")
    print("Original list:", lst)
    print("When there is the data:", lst.find_ordered(2)) # when there is the data
    print("When there isn't the data:", lst.find_ordered(44)) # when there isn't the data

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    # Sample unordered list
    lst = LinkedList()
    lst.insert_first(2)
    lst.insert_first(8)
    lst.insert_first(9)
    lst.insert_first(11)
    lst.insert_first(15)
    lst.insert_first(97)
    lst.insert_first(36)
    lst.insert_first(24)
    lst.insert_first(73)
    lst.insert_first(1)
    lst.insert_first(59)

    print("\ndelete_link() Tests")
    print("Original list:", lst)
    print("When there is the data:", lst.delete_link(2)) # when there is the data
    print("When there isn't the data:", lst.delete_link(44)) # when there isn't the data

    # Test method copy_list()
    # Sample unordered list
    lst = LinkedList()
    lst.insert_first(4)
    lst.insert_first(2)
    lst.insert_first(9)
    lst.insert_first(16)
    lst.insert_first(33)
    lst.insert_first(97)
    lst.insert_first(77)
    lst.insert_first(24)
    lst.insert_first(42)
    lst.insert_first(1)
    lst.insert_first(59)

    print("\ncopy_list() Tests")
    print("Original list:", lst)
    print("copy list:", lst.copy_list())

    # Test method reverse_list()
    lst = LinkedList()
    lst.insert_first(4)
    lst.insert_first(2)
    lst.insert_first(9)
    lst.insert_first(16)
    lst.insert_first(33)
    lst.insert_first(97)
    lst.insert_first(77)
    lst.insert_first(24)
    lst.insert_first(42)
    lst.insert_first(1)
    lst.insert_first(59)

    print("\nreverse_list() Tests")
    print("Original list:", lst)
    print("Reverse list:", lst.reverse_list())

    # Test method sort_list()
    lst = LinkedList()
    lst.insert_last(4)
    lst.insert_last(3)
    lst.insert_last(7)
    lst.insert_last(9)
    lst.insert_last(5)
    lst.insert_last(2)
    print("\nsort_list() Tests")
    print("Original list:", lst)
    print("Sorted list:", lst.sort_list())

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print("\nis_sorted() Tests")
    print("List1:", lst)
    print("List1 is sorted:", lst.is_sorted())
    print("List2:", lst.sort_list())
    print("List2 is sorted:", lst.sort_list().is_sorted())


    # Test method is_empty()
    print("\nis_equal() Tests")
    lst = LinkedList()
    print("List:")
    print("The list is empty:", lst.is_empty())
    lst.insert_last(3)
    lst.insert_last(9)
    lst.insert_last(4)
    print("List:", lst)
    print("The list is empty:", lst.is_empty())

    # Test method merge_list()
    lst1 = LinkedList()
    lst2 = LinkedList()
    lst1.insert_last(2)
    lst1.insert_last(4)
    lst1.insert_last(6)
    lst2.insert_last(1)
    lst2.insert_last(3)
    lst2.insert_last(5)
    print("\nmerge_list() Tests")
    print("List1:", lst1)
    print("List2:", lst2)
    lst1 = lst1.merge_list(lst2)
    print("Merged (and ascending) list:", lst1)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    lst1 = LinkedList()
    lst2 = LinkedList()
    lst3 = LinkedList()
    lst1.insert_last(1)
    lst1.insert_last(3)
    lst1.insert_last(6)
    lst2.insert_last(1)
    lst2.insert_last(3)
    lst2.insert_last(6)
    lst3.insert_last(4)
    lst3.insert_last(3)
    lst3.insert_last(6)
    print("\nis_equal() Tests")
    print("List1:", lst1, "\nList2:", lst2, "\nList 1 and List 2 are equal:", lst1.is_equal(lst2))
    print("List1:", lst1, "\nList3:", lst3, "\nList 1 and List 3 are equal:", lst1.is_equal(lst3))

    # Test remove_duplicates()
    lst = LinkedList()
    lst.insert_last(5)
    lst.insert_last(3)
    lst.insert_last(7)
    lst.insert_last(5)
    lst.insert_last(5)
    lst.insert_last(7)
    lst.insert_last(2)
    print("\nremove_duplicates() Tests")
    print("Original list:", lst)
    print("No duplicates list:", lst.remove_duplicates())

if __name__ == "__main__":
    main()