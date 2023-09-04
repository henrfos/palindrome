class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return self.size


class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def check_palindrome(word):

    queue = Queue()
    stack = Stack()

    for letter in word:
        queue.enqueue(letter)
        stack.push(letter)

    np = "Not Palindrome"
    pp = "Palindrom"

    for i in range(len(word)):
        if queue.dequeue() != stack.pop():
            return np
    return pp


m = input("Enter your word:")
palindrome_checker = check_palindrome(m)
print(palindrome_checker)