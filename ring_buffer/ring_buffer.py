class RingBuffer:

    def __init__(self, capacity):
        # set capacity limit
        self.capacity = capacity
        # set index
        self.index = 0
        # instantiate empty storage list
        self.storage = []

    def append(self, item):
        # if len of storage is less than capacity
        if len(self.storage) < self.capacity:
            # append item
            self.storage.append(item)
        # otherwise
        else:
            # storage index is equal to that item
            self.storage[self.index] = item
        # increase index count by 1
        self.index += 1

        # if index and capacity are equal
        if self.index == self.capacity:
            # index reset to 0
            self.index = 0

    def get(self):
        # return storage list
        return self.storage
