Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.rand)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    help(random.rand)
AttributeError: module 'random' has no attribute 'rand'
>>> help(random.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.

>>> random.randint(1, 100)
99
>>> help(random.choice)
Help on method choice in module random:

choice(seq) method of random.Random instance
    Choose a random element from a non-empty sequence.

>>> random.choice(["Palmeiras", "Santos", "Flamento", "SPORT", "Ceara"])
'Santos'
>>> random.choice(["Palmeiras", "Santos", "Flamento", "SPORT", "Ceara"])
'Flamento'
>>> random.choice(["Palmeiras", "Santos", "Flamento", "SPORT", "Ceara"])
'SPORT'
>>> random.choice(["Palmeiras", "Santos", "Flamento", "SPORT", "Ceara"])
'SPORT'
>>> random.choice(["Palmeiras", "Santos", "Flamento", "SPORT", "Ceara"])
'Santos'
>>> lista = ["Anderson", "Joao", "Maria, "Pedro", "Thiago"]
	     
SyntaxError: invalid syntax
>>> lista = ["Anderson", "Joao", "Maria]
	     
SyntaxError: EOL while scanning string literal
>>> lista = ['Joao', 'Maria', 'Pedro', 'Thiago', 'Rafael']
	     
>>> random.shuffle(lista)
	     
>>> lista
	     
['Rafael', 'Thiago', 'Pedro', 'Joao', 'Maria']
>>> 
	     
>>> 
	     
>>> lista
	     
['Rafael', 'Thiago', 'Pedro', 'Joao', 'Maria']
>>> 
