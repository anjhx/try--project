from no_element import NoElement

class ListNode:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size
    def add_last(self, key):
        old_tail = self._tail
        self._tail = ListNode(key)
        if old_tail is None:
            self._head = self._tail
        else:
            old_tail.next = self._tail
        self._size += 1
    def index_of(self, key):
            idx = -1       
            walk = self._head
            while walk is not None:
                
                idx += 1
                if walk.key == key:
                    return idx
                else:
                    walk = walk.next
            raise IndexError
        
    #i是1开示 
    def get_node(self, i) -> ListNode:
        if i < 1 or i > self._size+1:
            raise IndexError('Out of bounds')
        elif i == self._size+1:
            return self._tail
        else:
            cnt = 1
            walk = self._head
            while cnt < i:
                walk = walk.next
                cnt += 1
            return walk

    def get(self, i):
        walk = self.get_node(i)
        assert walk is not None
        return walk.key
    def remove_first(self):
        if self._size==0:
            raise IndexError('Remove from empty linked list')
        else:
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            self._size -= 1
    

    def swap(self, n1, n2):  
        prevNode1 = None;  
        prevNode2 = None;  
        node1 = self._head;  
        node2 = self._head;  
          
        #Checks if list is empty  
        if(self._head == None):  
            return;  
              
        #If n1 and n2 are equal, then list will remain the same  
        if(n1 == n2):  
            return;  
              
        #Search for node1  
        while(node1 != None and node1.key != n1):  
            prevNode1 = node1;  
            node1 = node1.next;  
              
        #Search for node2  
        while(node2 != None and node2.key != n2):  
            prevNode2 = node2;  
            node2 = node2.next;  
              
        if(node1 != None and node2 != None):  
              
            #If previous node to node1 is not None then, it will point to node2  
            if(prevNode1 != None):  
                prevNode1.next = node2;  
            else:  
                self._head  = node2;  
                  
            #If previous node to node2 is not None then, it will point to node1  
            if(prevNode2 != None):  
                prevNode2.next = node1;  
            else:  
                self._head  = node1;  
                  
            #Swaps the next nodes of node1 and node2  
            temp = node1.next;   
            node1.next = node2.next;   
            node2.next = temp;  
        else:  
            print("Swapping is not possible"); 





class MinPQ:
    """A max binary heap."""

    def __init__(self, ):
        self.ll = LinkedList()
        #self.ll.add_last (None)# append a dummy key at index 0
        
    def size(self):
        global ll
        return self.ll.size()

    def is_empty(self):
        return self.size() == 0

    def _swap(self, i, j):
        global ll
        #self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
        

        m = self.ll.get_node(i)
        n = self.ll.get_node(j)
       

        self.ll.swap(m.key,n.key)



       

    def _more(self, i, j):
        global ll
        #return self._pq[i] < self._pq[j]
        a = self.ll.get_node(i)
        #print(a.key)
        b = self.ll.get_node(j)
        return a.key > b.key

    def _swim(self, k):
        #print(k)
        while k > 1 and self._more(k//2, k):
            self._swap(k//2, k)
            k//= 2   
               
    def _sink(self, k):
        while 2 * k <= self.size():
            j = 2 * k
            if j < self.size() and self._more(j, j + 1):
                j += 1
            if not self._more(k, j):
                break
            self._swap(k, j)
            k = j

    def insert(self, key):
        global ll
        self.ll.add_last(key)
        #print(self.ll.size())
        self._swim(self.size())
        #assert self._is_min_heap()
        
       #self._pq.append(key)
       #self._swim  (self.size())
       #assert self._is_max_heap()

    def min(self):
        global ll
        if self.is_empty():
            raise NoElement
        return self.ll._head.key

    def del_min(self):
        global ll
        if self.is_empty():
            raise NoElement
        root = self.ll._head
        self._swap(1, self.size())
        #self._pq.pop()
        self.ll.remove_first()
        self._sink(1)
        #assert self._is_min_heap()
        return root

    def _is_min_heap_ordered(self, k):
        if k > self.size():
            return True
        left = 2 * k
        right = 2 * k + 1
        if left <= self.size() and self._more(k, left):
            return False
        if right <= self.size() and self._more(k, right):
            return False
        return self._is_min_heap_ordered(left) and self._is_min_heap_ordered(right)

    def _is_min_heap(self):
        if self.ll._head is None:
            return False
        return self._is_min_heap_ordered(1)

if __name__ == '__main__':
    pq = MinPQ()
    
    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(4)
    pq.insert(5)
    pq.insert(6)
    print(pq.ll.get(1))
    pq.del_min()
    print(pq.min)
    #print(pq.ll.get(1))
    ##print(pq.min())
    #pq.del_min()
    #print(pq.min())
    #pq.insert(2)
    #pq.insert(3)
    #print(pq._is_min_heap())