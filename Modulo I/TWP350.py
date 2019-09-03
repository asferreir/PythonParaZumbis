Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lista = []
>>> lista = lista()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    lista = lista()
TypeError: 'list' object is not callable
>>> lista = list()
>>> lista
[]
>>> texto = str()
>>> texto
''
>>> k = int ()
>>> k
0
>>> x = float()
>>> x
0.0
>>> dic = dict()
>>> dic
{}
>>> texto = str("abacate")
>>> texto
'abacate'
>>> texto.upper()
'ABACATE'
>>> classmethod Televisao:
	
SyntaxError: invalid syntax
>>> class Televisao:
	def __init__ (self):
		self.ligada = False
		self.canal = 2
	def muda_canal_para_baixo(self):
		self.canal -= 1
	def muda_canal_para_cima(self):
		self.canal += 1

		
>>> tv = Televisao()
>>> tv.muda_canal_para_cima()
>>> tv.canal
3
>>> tv.muda_canal_para_cima()
>>> tv.canal
4
>>> tv.muda_canal_para_baixo()
>>> tv.
SyntaxError: invalid syntax
>>> tv.canal
3
>>> 
