from source.Grafo import *
from source.File import *
import random


f = File()
nodos = [30,100]
colum = [6,10]

#gf0 = Grafo()
#tam = 30
#malla = gf0.grafoMalla(3,3)

#t = gf0.Dijkstra(0)

#f.toGraphivzFile('Geografico_'+str(tam),gf0.DFS_I(4),'DFS_I')
#f.toGraphivzFile('Malla_'+str(tam),malla)
#f.toGraphivzFile('Dijkstra'+str(tam),t)
rn = 0

for data in zip(nodos,colum):
	#rn = random.randint(0,data[0]-1)
	gf0 = Grafo()
	malla = gf0.grafoMalla(data[1],int(data[0]/data[1]))
	f.toGraphivzFile('Malla_'+str(data[0]),malla)
	f.toGraphivzFile('Malla_'+str(data[0]),gf0.Dijkstra(rn),'Dijkstra')

for tam in nodos:

	#rn = random.randint(0,tam-1)

	gf = Grafo()
	erdos = gf.grafoErdosRenyi(tam,tam*8)
	f.toGraphivzFile('ErdosRenyi_'+str(tam),erdos)
	f.toGraphivzFile('ErdosRenyi_'+str(tam),gf.Dijkstra(rn),'Dijkstra')
	

	gf1 = Grafo()
	gilbert = gf1.grafoGilbert(tam,0.35)
	f.toGraphivzFile('Gilbert_'+str(tam),gilbert)
	f.toGraphivzFile('Gilbert_'+str(tam),gf1.Dijkstra(rn),'Dijkstra')
	
	gf2 = Grafo()
	geo = gf2.grafoGeografico(tam,0.35)
	f.toGraphivzFile('Geografico_'+str(tam),geo)
	f.toGraphivzFile('Geografico_'+str(tam),gf2.Dijkstra(rn),'Dijkstra')
	
	gf3 = Grafo()
	mendez = gf3.grafoDorogovtsevMendes(tam)
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),mendez)
	f.toGraphivzFile('DorogovtsevMendes_'+str(tam),gf3.Dijkstra(rn),'Dijkstra')

	gf4 = Grafo()
	albert = gf4.grafoBarabasiAlbert(tam,4)
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),albert)
	f.toGraphivzFile('BarabasiAlbert_'+str(tam),gf4.Dijkstra(rn),'Dijkstra')