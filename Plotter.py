import numpy as np
import matplotlib.pyplot as plt

class File:
    def __init__(self, path):
        self.load(path)

    def load(self, path):
        from itertools import zip_longest
        rows = [line.split() for line in open(path)]
        self._cols = list(zip_longest(*rows))

    def column(self, n, dtype=float):
        '''get column n as type'''
        if n == 0: return np.array(range(len(self._cols[0])))
        return np.array([dtype(s) for s in self._cols[n-1] if s])

    def __getitem__(self, n):
        return self.column(n)

def D(a, n=1):
    return (a[n:] - a[:-n]) / n

class Figure:
    def __init__(self, *arg, **kw):
        self.cmds = []

    def plot(self, x, y, *arg, **kw):
        d = len(x) - len(y)
        if d > 0:
            x, y = x[d:], y
        elif d < 0:
            x, y = x, y[-d:]
        else:
            x, y = x, y
        self.cmds.append((x, y, arg, kw))
        return self

    def clear(self):
        self.cmds.clear()

    def show(self):
        for x, y, arg, kw in self.cmds:
            plt.plot(x, y, *arg, **kw)
        plt.show()
