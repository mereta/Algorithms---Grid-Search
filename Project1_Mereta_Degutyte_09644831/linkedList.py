from linked_list import LinkedList
from linked_list import Node


class linkedList:
    __my_list = LinkedList()

    def __init__(self):
        self.__my_list = LinkedList()

    def head(self):
        return self.__my_list.head()

    def size(self):
        p = self.__my_list.head()
        n = 0
        while p is not None:
            n += 1
            p = p.get_next()
        return n

    def is_empty(self):
        return self.__my_list.head() == None

    def contains(self, elem):
        p = self.__my_list.head()
        while p is not None:
            if p.get_element() == elem:
                return 1
            p = p.get_next()
        return 0

    def add(self, elem):
        ''' add an element to the set but make sure that the element is not already in the set (do not raise an error)
        '''
        node = Node(elem)
        p = self.__my_list.head()
        while p is not None:
            if p.get_element() == node.get_element():
                return 0
            p = p.get_next()
        self.__my_list.add_head(node)
        return 1

    def remove(self, elem):
        node = Node(elem)
        if self.__my_list.head().get_element() == node.get_element():
            self.__my_list.remove_head()
            return 1
        p = self.__my_list.head()
        if p is not None:
            while p.get_next() is not None:
                if p.get_next().get_element() == node.get_element():
                    p.set_next(p.get_next().get_next())
                    return 1
                p = p.get_next()
        return 0

    def union(self, b):
        p = b.head()
        if p is not None:
            while p is not None:
                if not self.contains(p.get_element()):
                    self.add(p.get_element())
                p = p.get_next()

    def intersection(self, b):
        p = self.head()
        while p is not None:
            if not b.contains(p.get_element()):
                self.remove(p.get_element())
            p = p.get_next()

    def difference(self, b):
        p = b.head()
        while p.get_next() is not None:
            if self.contains(p.get_element()):
                self.remove(p.get_element())
            p = p.get_next()

    def __str__(self):
        result = "-> "
        p = self.__my_list.head()
        if p is not None:
            while p is not None:
                result += "%s " % str(p.get_element())
                p = p.get_next()
        return result

