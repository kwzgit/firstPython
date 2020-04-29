#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------
# Name 150neo4j
# Author DELL
# Date  2020/3/18
# 往图谱中更新icd10
# -------------------------------
from py2neo import Graph,Node, Relationship
import pymysql
class ne4o150:
    def __init__(self):
        # neo4j
        self.neo4j150 = 'bolt://192.168.31.150:7686'
        self.graph = Graph(self.neo4j150)
        # 241mysql
        self.user = 'root'
        self.passwd = 'lantone'
        self.host = '192.168.2.241'
        self.database = 'med'
        self.charset = 'utf8'
        self.con = pymysql.Connect(user=self.user,
                               password=self.passwd,
                               host=self.host,
                               database=self.database,
                               charset=self.charset)


ne4o150 = ne4o150()
dictData = {}

cursor121 = ne4o150.con.cursor()
sql = 'SELECT guolin_code,guolin_name FROM `icd10` ';
cursor121.execute(sql)
results = cursor121.fetchall()
for row in results:
    code = row[0]
    name = row[1]
    dictData[name] = code
cursor121.close()
ne4o150.con.close()

sgd = ne4o150.graph
tx = sgd.begin()
diagnoses = tx.run('match(d:diagnose) return collect(d.name) as digs').data()[0]['digs']
for dig in diagnoses:
    print()
    if dig in dictData.keys():
        icd10 = dictData[dig]
        tx.run('match(d:diagnose) where d.name="{0}" set d.icd10="{1}"'.format(dig,icd10))
    else:
        tx.run('match(d:diagnose) where d.name="{0}" set d.icd10="{1}"'.format(dig, ""))

tx.commit()






