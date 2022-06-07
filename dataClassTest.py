from dataclasses import dataclass

@dataclass
class DataClass:
  name: str
  value: int

test = DataClass("hello there", 66)
print(test.value)

test.value = 1234
print(test.value)

test.value = 66
print(test)
