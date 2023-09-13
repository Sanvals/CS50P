class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cannot accept more cookies")
        else:
            self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("There won't be any cookies left")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be bigger than 0")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size must be lower than capacity")
        else:
            self._size = size

def main():
    jar = Jar()
    print(jar)
    jar.deposit(6)
    print(jar)
    jar.withdraw(3)
    print(jar)

main()
