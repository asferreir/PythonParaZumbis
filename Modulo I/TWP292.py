"""
DEF FUNCTIONS
"""

def épar(x):
        return x%2 == 0


"""
DEF FUNCTIONS

CALCULAR O FATORIAL DE 10
"""
def fat(n):
        f = 1
        while n > 0:
                f = f * n
                f = n - 1
        return f