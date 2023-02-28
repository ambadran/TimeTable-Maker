
class Stack:
    '''
    A LIFO singly linked-list
    '''
    def __init__(self):
        self._container = []  # This is the behind the curtain datatype for a stack

    def push(self, value: int):
        self._container.append(value)

    def pop(self) -> int:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

    def to_tuple(self) -> tuple:
        return tuple(self._container)

    def __eq__(self, other) -> bool:
        return self._container == other._container

    def __hash__(self):
        return hash(str(self._container))
