print("hello")
string = "MALAYALAM"
temp = []
for i in string:
    if i not in temp:
        temp.append(i)
        print(i, "->",string.count(i))


class Node:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print1(self):
        print("Name ->", self.name)
        print("Age ->", self.age)


p = Node("goutham", 25)
p.print1()


class Node1:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.Head = None
        self.last = None
        self.count = 0

    def insertnode(self, data):
        status = self.search(data)
        if status == -1:
            new_node = Node1(data)
            if self.Head == None:
                self.Head = new_node
                self.count += 1
            else:
                last = self.Head
                while last.next:
                    last = last.next
                last.next = new_node
                self.last = last.next
                self.count += 1
        else:
            print(f"Given element '{data}'is already present in linked list")

    def search(self, ele):
        index = 1
        node = self.Head
        while node:
            if node.data == ele:
                return index
            index += 1
            node = node.next
        return -1

    def insertpos(self, ele, pos):
        status = self.search(ele)
        if status != -1:
            print(f"Given element '{ele}'is already present in linked list")
            return 0
        if pos > self.count+1:
            print("Can't insert at given position...")
            return 0
        new_node = Node1(ele)
        if pos == 1:
            new_node.next = self.Head
            self.Head = new_node
            self.count += 1
        else:
            node = self.Head
            for i in range(1, pos-1):
                node = node.next
            temp = node.next
            node.next = new_node
            new_node.next = temp
            self.count += 1


    def delete(self, ele):
        index = self.search(ele)
        if index == -1:
            print("Given element is not found...")
        else:
            if index == 1:
                node = self.Head.next
                self.Head = node
                self.count -= 1
            else:
                print("index -> ",index)
                node = self.Head
                for i in range(1,index-1):
                    node = node.next
                node.next = node.next.next
                self.count -= 1

    def traverse(self):
        next_node = self.Head
        print("Linked list ", end="")
        while next_node:
            print("->", next_node.data, end="")
            next_node = next_node.next
        print("")


link = linkedList()
link.insertnode(10)
link.insertnode(30)
link.insertnode(40)
link.insertnode(20)
link.insertnode(60)
link.insertnode(50)
link.insertnode(50)
link.traverse()
# print(link.search(20))
link.delete(60)
link.traverse()
# link.insertpos(100, 6)
# link.insertpos(100, 6)
# link.traverse()
# option = int(input("Enter"))