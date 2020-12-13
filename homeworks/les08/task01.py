"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""
import pprint

n = int(input("Сколько друзей встретилось? "))

hand_shake = [[0 for _ in range(n)] for _ in range(n)]

for i in range(0, len(hand_shake)):
    for j in range(i + 1, len(hand_shake[i])):
        hand_shake[i][j] = 1

pprint.pprint(hand_shake, width=500)

s = sum([sum(el) for el in hand_shake])

print("Всего рокопожатий: ", s)
