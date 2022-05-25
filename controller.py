class Controller:
    def __init__(self):
        self.move_queue = []

    def enqueue(self, dir):
        print(f'Adding {dir} to the movement queue')
        self.move_queue.append(dir)

    def dequeue(self):
        if len(self.move_queue) == 0:
            return None

        return self.move_queue.pop(0)

    def clear_queue(self):
        self.move_queue.clear()