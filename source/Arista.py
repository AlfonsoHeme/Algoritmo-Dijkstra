from source.Nodo import *
import random
import math

class Arista:

	def __init__(self,nodo_A,nodo_B):
		self.__aristas = []
		self.__idArista = nodo_A.getId()
		self.__nodo_A = nodo_A
		self.__nodo_B = nodo_B
		self.__costos = []
		self.__aristas.append(nodo_B.getId())
		self.__costos.append(random.randint(1,100))

	
	def getId(self):
		return self.__idArista

	def getNodoA(self):
		return self.__nodo_A

	def getNodoB(self):
		return self.__nodo_B

	def getCostos(self):
		return self.__costos

	def getCosto(self,index):
		return self.__costos[index]

	def getGrado(self):
		return len(self.__aristas)

	def set_Arista(self, nodo):
		self.__aristas.append(nodo.getId())
		self.__costos.append(random.randint(1,100))

	def containsArista(self,nodo):
		if(isinstance(nodo,int)):
			return (nodo in self.__aristas)
		else:
			return (nodo.getId() in self.__aristas)

	def getAristas(self):
		return self.__aristas

	def getRandom(self):
		return random.randint(0,len(self.__aristas[self.__nodo_A]))