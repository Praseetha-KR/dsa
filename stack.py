class Stack:
    def __init__(self):
        self.arr = []

    def top(self):
        size = len(self.arr)
        return self.arr[(size - 1)] if (size >= 1) else ''

    def push(self, elem):
        self.arr.append(elem)

    def pop(self):
        size = len(self.arr)
        return self.arr.pop() if (size >= 1) else ''

    def is_empty(self):
        return self.arr == []

    def display(self):
        return self.arr


if __name__ == '__main__':
    s = Stack()

    def top_stack():
        print('Top: %s' % s.top())
        print('Stack: %s' % s.display())

    def push_stack():
        s.push(raw_input('Enter element to push: '))
        print('Stack: %s' % s.display())

    def pop_stack():
        print('Deleted: %s' % s.pop())
        print('Stack: %s' % s.display())

    def is_empty_stack():
        print('Is empty: %s' % s.is_empty())

    while(True):
        choice = int(raw_input('\n1. push\n2. pop\n3. top\n4. is_empty \
            \nchoice: '))
        switcher = {
            1: push_stack,
            2: pop_stack,
            3: top_stack,
            4: is_empty_stack
        }
        func = switcher[choice]
        func()
