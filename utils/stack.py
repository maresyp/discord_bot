from dataclasses import dataclass, field


@dataclass
class Stack:
    __stack: list = field(default_factory=list)

    def __str__(self):
        return f"{' '.join((str(x) for x in self.__stack))}"

    def push(self, value):
        self.__stack.append(value)

    def pop(self):
        return self.__stack.pop()

    def is_empty(self) -> bool:
        return len(self.__stack) == 0

    def peek(self):
        return self.__stack[-1]
