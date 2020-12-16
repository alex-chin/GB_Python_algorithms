"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class Node:
    def __init__(self, value, freq, left, right):
        self.value = value
        self.freq = freq
        self.left = left
        self.right = right


def build_tree(buf):
    freq = dict(sorted(Counter(buf).items(), key=lambda item: item[1], reverse=True))
    return freq


print(build_tree('laklajlkas jdlk jiouroew iuri ows euowieru'))
