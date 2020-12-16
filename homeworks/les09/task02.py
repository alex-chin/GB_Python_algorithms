"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter


class Node:
    def __init__(self, freq, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right


def build_tree(buf):
    freq = {key: Node(value) for key, value in dict(Counter(buf).items()).items()}
    freq = dict(sorted(freq.items(), key=lambda item: item[1].freq, reverse=True))
    return freq


print(build_tree('laklajlkas jdlk jiouroew iuri ows euowieru'))
