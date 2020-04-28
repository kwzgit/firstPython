# -*- coding: utf-8 -*-
from py2neo import Graph

graphHost='bolt://localhost:7687'
graphUser = "neo4j"
graphPassphrase = "123456"

graph=Graph(graphHost, auth=(graphUser,graphPassphrase))
datas=graph.nodes
for node in datas:
    print(node)








