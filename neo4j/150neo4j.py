#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------
# Name 150neo4j
# Author DELL
# Date  2020/3/18
# 从mysql查询出诊断依据，然后存入neo4j
# -------------------------------
from py2neo import Graph,Node, Relationship
import pymysql
class ne4o150:
    def __init__(self):
        # neo4j
        self.neo4j150 = 'bolt://192.168.31.150:7687'
        self.graph = Graph(self.neo4j150)
        # 121mysql
        self.user = 'teamdata'
        self.passwd = 'jiO2rfnYhg'
        self.host = '192.168.2.121'
        self.database = 'med'
        self.charset = 'utf8'
        self.con = pymysql.Connect(user=self.user,
                               password=self.passwd,
                               host=self.host,
                               database=self.database,
                               charset=self.charset)


ne4o150 = ne4o150()
listData = []
cursor121 = ne4o150.con.cursor()
sql = 'SELECT dis_name,type,standard,relation,unique_name,mid_result FROM `kl_diagnose_detail` ';
cursor121.execute(sql)
results = cursor121.fetchall()
for row in results:
    dictData = {}
    disName = row[0]
    type = row[1]
    standard = row[2]
    relation = row[3]
    unique_name = row[4]
    mid_result = row[5]
    dictData['disName'] = disName
    dictData['type'] = type
    dictData['standard'] = standard
    dictData['relation'] = relation
    dictData['unique_name'] = unique_name
    dictData['mid_result'] = mid_result
    listData.append(dictData)
cursor121.close()
ne4o150.con.close()
print()
# --------------------------------------------------------
sgd = ne4o150.graph
tx = sgd.begin()
for row in listData:
    disN = row['disName']
    print(disN)
    ty = row['type']
    st = row['standard']
    rel = row['relation']
    uqn = row['unique_name']
    mr = row['mid_result']
    nzNode = Node("diagnose", name=disN)
    tx.merge(nzNode, "diagnose", "name")
    if ty == 1:
        stNode = Node("symptom", name=st,synonym=rel)
        tx.merge(stNode, "symptom", "name")
        r1 = Relationship(nzNode, '症状', stNode)
        tx.merge(r1)
    elif ty == 2:
        tzNode = Node("vital", name=st, synonym=rel)
        tx.merge(tzNode, "vital", "name")
        r2 = Relationship(nzNode, '体征', tzNode)
        tx.merge(r2)
    elif ty == 3:
        lisNode = Node("lis", name=uqn, result=mr)
        tx.merge(lisNode, "lis", "name")
        r3 = Relationship(nzNode, '化验', lisNode)
        tx.merge(r3)
    elif ty == 4:
        pacsNode = Node("pacs", name=st, result=rel)
        tx.merge(pacsNode, "pacs", "name")
        r4 = Relationship(nzNode, '辅检', pacsNode)
        tx.merge(r4)
tx.commit()






