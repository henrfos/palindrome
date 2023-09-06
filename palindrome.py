class Stack:

    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
        

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


inp = input("Enter your word:")
palindrome_checker = check_palindrome(inp)
print(palindrome_checker)
