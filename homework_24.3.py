
class DictStack:
    def __init__(self):
        self.__dicts = {}

    def __repr__(self):
        return repr(self.__dicts)

    def push(self, input_dict):
        self.__dicts.update(input_dict)

    def pop(self):
        self.__dicts.popitem()

    def reverse(self):
        reversed_dicts = {}
        for key in sorted(self.__dicts, reverse=True):
            reversed_dicts[key] = self.__dicts[key]
        return reversed_dicts

    def index(self, item):
        for key, value in self.__dicts.items():
            if value == item:
                return key

    def last_index(self, item):
        list1 = []
        for key, value in self.__dicts.items():
            if value == item:
                list1.append({key: value})
        return list1[-1]

    def join(self, joiner):
        dictionary = ''
        for index, el in enumerate(self.__dicts):
            if index != 0:
                dictionary += f'{joiner} {el}: {self.__dicts[el]}'
            else:
                dictionary += f'{el}: {self.__dicts[el]}'
        return dictionary


d1 = DictStack()
d1.push({"0": "Masha"})
d1.push({"1": "Myhailo"})
d1.push({"2": "Lewis"})
d1.push({"3": "Bill"})
d1.push({"4": "Kate"})
d1.push({"5": "Suzan"})
d1.push({"6": "Bill"})
print(d1)
print(d1.reverse())
print(d1.index("Bill"))
print(d1.last_index("Bill"))
# d1.pop()
# print(d1)
print(d1.join('/'))
