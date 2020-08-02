"""Пример создания стека через ООП"""


class StackClass:
    def __init__(self):
        self.elems = [[]]
        self.current_stack = 0
        self.stack_size_val = 5

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в начале списка"""
        if len(self.elems[self.current_stack]) > self.stack_size_val - 1:
            self.elems.append([el])
            self.current_stack += 1
        else:
            self.elems[self.current_stack].insert(0, el)

    def pop_out(self):
        val = self.elems[self.current_stack].pop(0)
        if len(self.elems[self.current_stack]) == 0:
            self.elems.pop(self.current_stack)
        return val

    def get_val(self):
        return self.elems[self.current_stack][0]

    def stack_size(self):
        print(f'Полных стеков {len(self.elems) - 1} по {self.stack_size_val} элемента(ов), в текущем стеке '
              f'{len(self.elems[len(self.elems) - 1])} элемента(ов)')
        return (len(self.elems) - 1), self.stack_size_val,  len(self.elems[len(self.elems) - 1])

    def show_stack(self):
        for el in self.elems:
            print(el)

SC_OBJ = StackClass()

print(SC_OBJ.is_empty())  # -> стек пустой

# наполняем стек
SC_OBJ.push_in(1)
SC_OBJ.push_in(2)
SC_OBJ.push_in(3)
SC_OBJ.push_in(4)
SC_OBJ.push_in(5)
SC_OBJ.push_in(6)
SC_OBJ.push_in(7)
SC_OBJ.push_in(8)
SC_OBJ.push_in(9)


SC_OBJ.show_stack()

print("========DELETE last item from current stack=============")

print(SC_OBJ.pop_out())
SC_OBJ.show_stack()

# получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
print(SC_OBJ.get_val())  # -> 8

# узнаем размер стека
print(SC_OBJ.stack_size())  # -> (1, 5, 3)

print(SC_OBJ.is_empty())  # -> стек уже непустой

# кладем еще один элемент в стек
SC_OBJ.push_in(4.4)

# убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 4.4

# снова убираем элемент с вершины стека и возвращаем его значение
print(SC_OBJ.pop_out())  # -> 8

# вновь узнаем размер стека
print(SC_OBJ.stack_size())  # -> 3
