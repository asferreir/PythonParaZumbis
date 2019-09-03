"""
DICIONARIOS
"""

>>> d = {}
>>> d["a"] = "alpha"
>>> d["o"] = "omega"
>>> d["g"] = "gama"
>>> d.keys()
dict_keys(['a', 'o', 'g'])
>>> d.values()
dict_values(['alpha', 'omega', 'gama'])
>>> "g" in d
True
>>> "x" in d
False

>>> for chave in d: print(chave)
...
a
o
g