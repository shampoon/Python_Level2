class QueueClass:
    def __init__(self):
        self.elems = []
        self.solved = []
        self.revision = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def solved_task(self):
        self.solved.insert(0, self.elems.pop())

    def size(self):
        return len(self.elems)

    def revision_task(self):
        self.revision.insert(0, self.elems.pop())

    def show_queues(self):
        print(f'Queue: {self.elems}')
        print(f'Solved: {self.solved}')
        print(f'Revision: {self.revision}')

if __name__ == '__main__':
    qc_obj = QueueClass()
    print(f'Очередь пуста?: {qc_obj.is_empty()}')  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('first')
    qc_obj.to_queue(2)
    qc_obj.to_queue('3')
    qc_obj.to_queue(4)
    qc_obj.to_queue(5)
    qc_obj.to_queue(6)
    qc_obj.to_queue(7)
    qc_obj.to_queue(8)
    qc_obj.to_queue(9)

    print(f'Очередь пуста?: {qc_obj.is_empty()}')  # -> False. Очередь пустая

    print(f'Размер очереди: {qc_obj.size()}')  # -> 9

    qc_obj.show_queues()

    qc_obj.solved_task()  # -> перемещаем в решенные задачи
    qc_obj.revision_task()  # -> перемещаем в задачи для доработки
    qc_obj.solved_task()  # -> перемещаем в решенные задачи
    qc_obj.revision_task()  # -> перемещаем в задачи для доработки
    print(f'Размер очереди: {qc_obj.size()}')  # -> 5

    qc_obj.show_queues()
