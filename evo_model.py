import networkx as nx 
import matplotlib.pyplot as plt
import random
import math
import time

def create_graph():
	G=nx.Graph()
	#G.add_nodes_from(range(1,101))
	for i in range(1,101):
		G.add_node(i)
	return G

def visualise(G,t):
	time.sleep(1)
	labeldict=get_labels(G)
	nodesize=get_size(G)
	color_array=get_colors(G)
	nx.draw(G,labels=labeldict,node_size=nodesize,node_color=color_array)
	plt.savefig('evolution.png')
	plt.clf()
	plt.cla()
	nx.write_gml(G,'evolution_'+str(t)+'.gml')

def assign_BMI(G):
	for each in G.nodes():
		G.node[each]['name']=random.randint(15,40)
		G.node[each]['type']='person'

def get_size(G):
	array1=[]
	for each in G.nodes():
		if G.node[each]['type']=='person':
			array1.append(G.node[each]['name']*25)
		else :
			array1.append(1000)
	return array1

def get_labels(G):
	dict1={}
	for each in G.nodes():
			dict1[each]=G.node[each]['name']
	return dict1

def add_foci_nodes(G):
	n=G.number_of_nodes()
	i=n+1
	foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
	for j in range(0,5):
		G.add_node(i)
		G.node[i]['name']=foci_nodes[j]
		G.node[i]['type']='foci'
		i+=1

def get_colors(G):
	c=[]
	for each in G.nodes():
		if G.node[each]['type']=='person':
			if G.node[each]['name']==15:
				c.append('green')
			elif G.node[each]['name']==40:
				c.append('yellow')
			else:
				c.append('blue')
		else:
			c.append('red')
	return c

def get_foci_nodes():
	f=[]
	for each in G.nodes():
		if G.node[each]['type']=='foci':
			f.append(each)
	return f

def get_person_nodes():
	p=[]
	for each in G.nodes():
		if G.node[each]['type']=='person':
			p.append(each)
	return p


def add_foci_edges():
	foci_nodes=get_foci_nodes()
	person_nodes=get_person_nodes()
	for each in person_nodes:
		r=random.choice(foci_nodes)
		G.add_edge(each,r)

def homophily(G):
	pnodes=get_person_nodes()
	for u in pnodes:
		for v in pnodes:
			if u!=v:
				diff=abs(G.node[u]['name']-G.node[v]['name'])
				p=float(1)/(diff+1000)
				r=random.uniform(0,1)
				if r<p:
					G.add_edge(u,v)

def cmn(u,v,G):
	nu=set(G.neighbors(u))
	nv=set(G.neighbors(v))
	return len(nu & nv)


def closure(G):
	array1=[]
	for u in G.nodes():
		for v in G.nodes():
			if u!=v and (G.node[u]['type']=='person' or G.node[v]['type']=='person'):
				k=cmn(u,v,G)
				p=1-math.pow((1-0.000001),k)
				tmp=[]
				tmp.append(u)
				tmp.append(v)
				tmp.append(p)
				array1.append(tmp)
		for each in array1:
			u=each[0]
			v=each[1]
			p=each[2]
			r=random.uniform(0,1)
			if r<p:
				G.add_edge(u,v)

def change_bmi(G):
	fnodes=get_foci_nodes()
	for i in fnodes:
		if G.node[i]['name']=='eatout':
			for j in G.neighbors(i):
				if G.node[j]['name'] != 40:
					G.node[j]['name']+=1
		if G.node[i]['name']=='gym':
			for j in G.neighbors(i):
				if G.node[j]['name'] != 15:
					G.node[j]['name']-=1


G=create_graph()
assign_BMI(G)
add_foci_nodes(G)
add_foci_edges()
time.sleep(10)
t=0
visualise(G,t)
nx.write_gml(G,'evolution_0.gml')
for t in range(0,10):
	homophily(G)
	closure(G)
	change_bmi(G)
	visualise(G,t+1)