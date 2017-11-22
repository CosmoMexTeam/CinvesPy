# Importamos la paqueteria de networkx
import networkx as nx

# Es necesario importar MatplotLib.pyplot para graficar
import matplotlib.pyplot as plt

# Num. de nodos
N = 10

# Prob. de conexi\'on
p = 0.5

# Creamos un grafo Erdos-Renyi con N nodos
G = nx.erdos_renyi_graph(10,0.4)

# Definimos la posici\'on de cada nodo en el plano coordenado
# Network incluye funciones que lo hacen siguiente distintas configuraciones 
# como: draw_circular; draw_random; draw_spectral; draw_spring; draw_shell
#pos = nx.circular_layout(G)

# Dibujamos la red completa i.e. nodos y enlaces
nx.draw(G,pos,
        node_color='red',
        node_size=1500,
        alpha=0.8,
        with_labels=True,
        linewidths=5,
        font_size=25)

# Dibujar solo los nodos 0 y 1 con atributos particulares
nx.draw_networkx_nodes(G,pos,
                       nodelist=[0,4],
                       node_color='b',
                       node_size=1500,
                       alpha=1.)

plt.show()

#print 'El grado de nodo'
#print G.degree()

#fig, ax = plt.subplots()
#plt.hist(nx.degree(G).values())
#plt.xlabel('Degree')
#plt.ylabel('Number of Subjects')
#plt.savefig('network_degree.png')

#print '--> MEDIDA DE LONGITUD DE CAMINOS CORTOS <--'


#print
#print 'El camino corto entre el nodo 0 y 4 es:'
#print(nx.shortest_path(G,source=0,target=4))

#print
#print 'La longitud del camino corto'
#print nx.shortest_path_length(G)

#print
#print 'La longitud del camino corto entre el nodo 0 y 4 es:'
#print nx.shortest_path_length(G,source=0,target=4)

#print
#print 'El promedio de la longitud del camino corto'
#print nx.average_shortest_path_length(G)




print '--> MEDIDA DE AGRUPAMIENTO <--'

print 'El coeficiente de agrupamiento de cada nodo es:'
print 
print nx.clustering(G)

print
print 'El coeficiente de agrupamiento del nodo 0 es:'
print nx.clustering(G,0)

print 
print 'El promedio del coeficiente de agrupamiento es:'
print nx.average_clustering(G)

print
print 'El n\'umero de triangulos en cada nodo es: '
print nx.triangles(G)



















# Dibujar todos los enlaces con grosor y color
#nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

# Dibujar un solo enlace con grosor y color particular
#nx.draw_networkx_edges(G,pos,edgelist=[(0,1)],width=8,alpha=1.,edge_color='r')























# Puedo definir mi propia posicion. Por ejemplo
#Gi = nx.erdos_renyi_graph(4,0.5)
#my_pos = {0: (40, 20), 1: (20, 30), 2: (40, 30), 3: (30, 10)} 
#nx.draw(Gi,pos,node_color='r',node_size=1500,alpha=0.8,with_labels=True)
#plt.axis('off')
#plt.show()

# Tambien podemos crear objetos para realizar diferentes tareas. Por ejemplo:
# Hacer un objeto que dibuje el grafo con distintos atributos

#import networkx as nx
#import matplotlib.pyplot as plt

#from Functions import Draw_Network

#G = nx.erdos_renyi_graph(10,0.5)

#draw = Draw_Network(G)

#draw.Topology('Grafo1',save=True)
#plt.show()


#G=nx.Graph()

#G.add_node(1,pos=(1,1))
#G.add_node(2,pos=(2,2))
#G.add_edge(1,2)
#pos=nx.get_node_attributes(G,'pos')
#print pos
#Out[7]: {1: (1, 1), 2: (2, 2)}