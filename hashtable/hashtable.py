from linked_list import LinkedList
import sys
sys.path.append('../hashtable/linked_list')

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f'HashTableEntry({repr(self.key)}, {repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        # Your code here

        # self.capacity = [None] * MIN_CAPACITY
        self.storage = [LinkedList()] * MIN_CAPACITY
        self.count = 0
        self.capacity = capacity




    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        """
        Returns: The FNV-1a (alternate) hash of a given string
        """
        # determines the index into which the data is put
        #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        seed = 0

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in key:
            hash = hash ^ ord(char)
            hash = hash * FNV_prime
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # returns an index value for a key
        return self.fnv1(key) % len(self.storage)
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        # stores value in a particular slot
        slot = self.hash_index(key)        
        current = self.storage[slot].head

        # for little to no collisions
        # find the slot for the key
        # search the liked list for the key
        # if found, update it
        # if not found, make a new HashTableEntry and
        # add it to the list

        while current:
            if current.key == key:
                current.value = value
            current = current.next

        entry = HashTableEntry(key, value)
        self.storage[slot].insert_at_head(entry)
        self.count += 1



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        self.put(key, None)
        self.count -=1 

        # for little to no collisions
        # find the slot for the key
        # search the liked list for the key
        # if found, delete it from the linked list, then
        # return the delted value
        # if not found, return None


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # gets the value from a particular slot
        slot = self.hash_index(key)
        current = self.storage[slot].head
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None


        # for little to no collisions
        # find the slot for the key
        # search the liked list for the key
        # if found return value
        # if not found, return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # 1. Allocate a new array of bigger size, typically double the previous size
        # 2. Traverse the old hash table => O(n) over the number of elems in the hash table
        #       for each of its elems:
        #           figure its slot in the bigger, new array
        #           put it there
        
        if self.get_load_factor() >= 0.7:
            old_storage = self.storage
            self.storage = [LinkedList()] * new_capacity
            for item in old_storage:
                current = item.head
                while current:
                    self.put(current.key, current.value)
                    current = current.next
            self.capacity = new_capacity



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
