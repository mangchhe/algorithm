import sys
from collections import defaultdict

tree_seq = defaultdict(int)
total = 0

for text in sys.stdin.readlines():
    tree_seq[text.rstrip()] += 1
    total += 1

for key, value in sorted(tree_seq.items()):
    print("%s %.4f" % (key, value / total * 100))
