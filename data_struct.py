from collections import Counter
import numpy as np


# класс для хранения частоты элементах в разных формалтах
class CounterStorage():
    def __init__(self, data):
        c = Counter(data)
        self.values, self.counts = c.keys(), c.values()
        self.dictlike = dict(zip(self.values, self.counts))
        self.mod = "cv"

    def __len__(self):
        return len(self.counts)

    def __getitem__(self, item):
        mod = self.mod
        if mod == "cv" or mod == "vc":
            return self.dictlike[item]
        elif mod == "tcv" or mod == "tvc":
            items = []
            for t in self.dictlike:
                if t[0] == item:
                    items += [t[1]]
            return items
        elif mod == "lvc":
            items = []
            for i, elem in enumerate(self.dictlike[0]):
                if elem == item:
                    items += [self.dictlike[1][i]]
            return items
        elif mod == "lcv":
            items = []
            for i, elem in enumerate(self.dictlike[0]):
                if elem == item:
                    items += [self.dictlike[1][i]]
            return items

    def __str__(self):
        return str(self.dictlike)

    def switch_mod(self, mod="cv"):
        self.mod = mod
        if mod == "cv":
            self.dictlike = dict(zip(self.counts, self.values))
        elif mod == "vc":
            self.dictlike = dict(zip(self.values, self.counts))
        elif mod == "tcv":
            self.dictlike = list(zip(self.counts, self.values))
        elif mod == "tvc":
            self.dictlike = list(zip(self.values, self.counts))
        elif mod == "lvc":
            self.dictlike = [list(self.values), list(self.counts)]
        elif mod == "lcv":
            self.dictlike = [list(self.counts), list(self.values)]
        else:
            raise ValueError(f'Mod "{mod}" not exist. Use one of these mods: "cv","vc","tcv","tvc","lcv","lvc"')

    def sort_by_values(self):
        mod = self.mod
        if mod == "cv":
            self.sorted_dictlike =
        elif mod == "vc":
            self.dictlike = dict(zip(self.values, self.counts))
        elif mod == "tcv":
            self.dictlike = list(zip(self.counts, self.values))
        elif mod == "tvc":
            self.dictlike = list(zip(self.values, self.counts))
        elif mod == "lvc":
            self.dictlike = [list(self.values), list(self.counts)]
        elif mod == "lcv":
            self.dictlike = [list(self.counts), list(self.values)]
        else:
            raise ValueError(f'Mod "{mod}" not exist. Use one of these mods: "cv","vc","tcv","tvc","lcv","lvc"')



s = "sodfjoisjdofs"
c = CounterStorage(s)
print(c)
c.switch_mod("lcv")
print(c)
print(c[3])
