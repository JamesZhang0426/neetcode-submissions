from collections import defaultdict
class Node:
    def __init__(self,key=0,val=0):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = defaultdict()
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node 
            next_node.prev = prev_node
            last_node = self.tail.prev
            last_node.next = node 
            node.prev = last_node 
            self.tail.prev = node 
            node.next = self.tail
            return self.hashmap[key].val
        return -1 
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            del self.hashmap[key]
            prev_node = node.prev
            next_node = node.next
            prev_node.next = next_node 
            next_node.prev = prev_node
            last_node = self.tail.prev
            last_node.next = node 
            node.prev = last_node 
            self.tail.prev = node 
            node.next = self.tail
            self.hashmap[key] = node 
        else:
            if len(self.hashmap) == self.capacity:
                firstnode = self.head.next
                nextnode = firstnode.next
                nextnode.prev = self.head
                self.head.next = nextnode 
                del self.hashmap[firstnode.key]
            prevnode = self.tail.prev
            newnode = Node(key,value)
            prevnode.next = newnode
            newnode.next = self.tail
            self.tail.prev = newnode 
            newnode.prev = prevnode
            self.hashmap[key] = newnode




        
