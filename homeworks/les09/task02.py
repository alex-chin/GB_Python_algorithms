"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import Counter
from pprint import pprint


class Node:
    def __init__(self, freq, value, left=None, right=None):
        self.freq = freq
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return f'\n({self.value}:{self.freq}, left={self.left}, right={self.right})'
        # return f'Node(freg={self.freq}, value={self.value}, left={self.left}, right={self.right})'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        return Node(self.freq + other.freq, None, left=self, right=other)

    @staticmethod
    def has_path(root, value, path):
        if not root:
            return False
        if root.value == value:
            return True
        if Node.has_path(root.left, value, path):
            path.append('0')
            return True
        if Node.has_path(root.right, value, path):
            path.append('1')
            return True
        return False


def build_tree(alphabet):
    tree = [Node(value, key) for key, value in alphabet.items()]

    while 1:
        tree.sort(key=lambda item: item.freq)
        if len(tree) < 2:
            break
        node = tree[0] + tree[1]
        del tree[0]
        del tree[0]
        tree = [node] + tree
    return tree


def codec_houf(buf):
    alphabet = Counter(buf)
    tree = build_tree(alphabet)[0]
    for key in alphabet.keys():
        path = []
        Node.has_path(tree, key, path)
        alphabet[key] = ''.join(path[:])
    return dict(alphabet)


if __name__ == '__main__':
    phrase = 'beep boop beer!'
    print('Фраза : ', phrase)
    codec = codec_houf(phrase)
    print("Алфавит: ", codec)
    sec = [codec[sym] for sym in phrase]
    print("Фраза по символам: ", sec)
    print("Фраза закодированная в 16-форме: ", hex(int(''.join(sec), base=2)))
