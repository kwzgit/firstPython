#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------
# Name 150yanke
# Author DELL
# Date  2020/4/29
# 图谱眼科数据导出excel,每个病一个sheet
# -------------------------------
from py2neo import Graph,Node, Relationship
from readFile.ReadWriteExcel import save_in_xl
class ne4o150:
    def __init__(self):
        # neo4j
        self.neo4j150 = 'bolt://192.168.31.150:7686'
        self.graph = Graph(self.neo4j150)

dictData = {}
ne4o150 = ne4o150()
graph_150 = ne4o150.graph
tx = graph_150.begin()
diag_type_content = tx.run('match(d:疾病)-[r]->(k) where k.name in ["眼科","眼科中心"]  with distinct collect(d.name) as j \
unwind j as h \
with h as diag \
match(k:疾病)-[r]->(o) where k.name=diag with k.name as diag,type(r) as type,o.name as content  \
return diag,type,collect( distinct content) as contents order by diag').data()
tx.commit()
if diag_type_content:
    for data in diag_type_content:
        diag = str(data['diag']).replace("[","").replace("]","")
        type = data['type']
        contents = "、".join(data['contents'])
        data = {}
        data['类型'] = type
        data['内容'] = contents
        if diag not in dictData:
            dataList = []
            dataList.append(data)
            dictData[diag] = dataList
        else:
            jj = dictData[diag]
            jj.append(data)
            dictData[diag] = dataList

for diag in dictData:
    save_in_xl(dictData[diag], 'e:/yanke', cut_cursor='\n', save='old', sheetname=diag)

