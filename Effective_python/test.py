# def index_file(handle):
#     offset = 0
#     for line in handle:
#         if line:
#             yield offset
#         for letter in line:
#             offset += 1
#             if letter == ' ':
#                 yield offset

# import itertools
# from pathlib import Path
# import os

# parent_dir = Path(__file__).resolve().parent
# for filename in os.listdir(parent_dir):
#     if filename == 'address.txt':
#         with open(os.path.join(parent_dir, filename)) as f:
#             it = index_file(f)
#             results = itertools.islice(it, 0, 10)
#             print(list(results))
# with open('D:\Workspace\Learning\Deep_dive\Effective_python\address.txt', 'r') as f:
    # it = index_file(f)
    # results = itertools.islice(it, 0, 10)
    # print(list(results))
# from collections.abc import Iterable, Iterator

# class Test:
#     def __init__(self) -> None:
#         pass
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# print(isinstance(Test, Iterable))
# print(isinstance(Test, Iterator))

# class DictionaryRecord:
#     def __init__(self, data) -> None:
#         self._data = data

#     def __getattribute__(self, name: str):
#         print(f'* Called __getattribute__({name!r})')
#         data_dict = super().__getattribute__('_data')
#         return data_dict[name]

# data = DictionaryRecord({'foo': 3})
# print('foo: ', data.foo)

from typing import Final, NewType, Literal
from collections import namedtuple
from dataclasses import dataclass

@dataclass
class Error:
    error_code: Literal[1,2,3,4,5]
    disposed_of: bool

Error(0, False)

