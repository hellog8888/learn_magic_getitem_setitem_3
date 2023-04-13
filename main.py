class IntegerValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError('возможны только целочисленные значения')
        setattr(instance, self.name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value=0):
        self.value = start_value

class TableValues:
    def __init__(self, rows, cols, cell=None):
        if not cell:
            raise ValueError('параметр cell не указан')

        self._rows = rows
        self._cols = cols
        self.cells = tuple(tuple(cell() for _ in range(cols)) for __ in range(rows))

    def __check_index(self, index):
        r, c = index
        if type(r) != int or not (0 <= r < self._rows) or type(c) != int or not (0 <= c < self._cols):
            raise IndexError('неверный индекс для доступа к элементам массива')

    def __setitem__(self, key, value):
        self.__check_index(key)
        self.cells[key[0]][key[1]].value = value

    def __getitem__(self, item):
        self.__check_index(item)
        return self.cells[item[0]][item[1]].value