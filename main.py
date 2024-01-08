class List():
    def __init__(self, data = None, next_ = None):
        self.data = data
        self.next_ = next_
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_
    
    def set_data(self, data):
        self.data = data
    
    def set_next(self, next_):
        self.next_ = next_
    

class LinkList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_list = List(data)
        cur_list = self.head
        if cur_list is None:
            self.head = new_list
            return
        while cur_list.get_next():
            cur_list = cur_list.get_next()
        cur_list.set_next(new_list)
    
    def show(self):
        cur_list = self.head
        output = ''
        while cur_list:
            output += str(cur_list.get_data()) + ' > '
            cur_list = cur_list.get_next()
        print(output)
    
    def lengt(self):
        cur_list = self.head
        count = 0
        while cur_list:
            count += 1
            cur_list = cur_list.get_next()
            print(count)
    
    def push_front(self, data):
        new_list = List(data)
        cur_list = self.head
        new_list.set_next(cur_list)
        self.head = new_list
    
    def remove_front(self):
        cur_list = self.head
        self.head = cur_list.get_next()
    
    def remove_back(self):
        cur_list = self.head
        while cur_list.get_next():
            cur_list = cur_list.get_next()
        cur_list.set_next(None)
    
    def value_at(self, index):
        cur_list = self.head
        count = 0
        while cur_list:
            if count == index:
                return cur_list.get_data()
            count += 1
            cur_list = cur_list.get_next()
        print('Индекс находится вне диапазона')

    def insert(self, index, data):
        new_list = List(data)
        cur_list = self.head
        count = 0
        while cur_list.get_next():
            if index == 0:
                self.push_front(data)
                return
            if count + 1 == index:
                list_after_cur = cur_list.get_next()
                cur_list.set_next(new_list)
                new_list.set_next(list_after_cur)
                return
            count += 1
            cur_list = cur_list.get_next()
        print('Индекс находится вне диапазона')

    def remove(self, index):
        cur_list = self.head
        count = 0
        while cur_list.get_next():
            if index == 0:
                self.remove_front()
                return
            if count + 1 == index:
                list_to_remove = cur_list.get_next()
                list_after_remove = list_to_remove.get_next()
                cur_list.set_next(list_after_remove)
                return
            count += 1
            cur_list = cur_list.get_next()
        print('Индекс находится вне диапазона')

    def reverse_(self):
        rev = None
        next_ = None
        cur_list = self.head
        while cur_list:
            next_ = cur_list.get_next()
            cur_list.set_next(rev)
            rev = cur_list
            cur_list = next_
        self.head = rev

my_list = LinkList()
my_list.append(4)
my_list.append(6)
my_list.append(24)
my_list.append(12)
my_list.show()
my_list.push_front(46)
my_list.show()
print(my_list.value_at(2))
my_list.lengt()
my_list.show()
my_list.remove_back()
my_list.show()
my_list.remove_front()
my_list.show()
my_list.insert(2, 15)
my_list.show()
my_list.remove(-1)
my_list.show()
my_list.reverse_()
my_list.show()
