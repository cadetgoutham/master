class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class linkedlist:
    def __init__(self):
        self.Head = None
        self.last = None
        self.count = 0

    def Insertnode(self, data):
        new_node = Node(data)
        if self.Head == None:
            self.Head = new_node
            self.count += 1
        else:
            last = self.Head
            while last.next:
                last = last.next
            new_node.prev = last
            last.next = new_node
            self.last = last.next
            self.count += 1

    def search(self, ele):
        index = 1
        node = self.Head
        while node:
            if node.data == ele:
                return index
            index += 1
            node = node.next
        return -1

    def traverse(self):
        node = self.Head
        print("Linked list",end="")
        while node:
            print(" ->", node.data, end="")
            node = node.next
        print("")

    def deletenode(self, ele):
        index = self.search(ele)
        if index == -1:
            print("Given element is not found...")
        else:
            if index == 1:
                node = self.Head.next
                self.Head = node
                self.count -= 1
            elif index == self.count:
                print("entered")
                node = self.last.prev
                node.next = None
                self.last = node
                self.count -= 1
            else:
                node = self.Head
                for i in range(1, index-1):
                    node = node.next
                temp = node.next.next
                node.next = temp
                temp.prev = node
                self.count -= 1

    def insertpos(self, ele, pos):
        status = self.search(ele)
        if status != -1:
            print(f"Given element '{ele}'is already present in linked list")
            return 0
        if pos > self.count + 1:
            print("Can't insert at given position...")
            return 0
        new_node = Node(ele)
        if pos == 1:
            new_node.next = self.Head
            self.Head.prev = new_node
            self.Head = new_node
            self.count += 1
        elif pos == self.count+1:
            node = self.last
            node.next = new_node
            new_node.prev = node
            self.last = new_node
            self.count += 1
        else:
            node = self.Head
            for i in range(1, pos-1):
                node = node.next
            temp = node.next
            node.next = new_node
            new_node.prev = node
            new_node.next = temp
            temp.prev = new_node
            self.count += 1

    def reverse(self):
        node = self.last
        print("Linked list", end="")
        while node:
            print(" ->", node.data, end="")
            node = node.prev
        print("")

List = linkedlist()
List.Insertnode(10)
List.Insertnode(20)
List.Insertnode(30)
List.Insertnode(40)
List.Insertnode(50)
List.traverse()
List.reverse()
print(List.search(10))
List.deletenode(50)
List.traverse()
List.insertpos(100, 1)
List.insertpos(200, 6)
List.insertpos(120, 3)
print(List.count)
List.traverse()
List.reverse()