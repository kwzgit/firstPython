#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------
# Name ReadMysqlToExcel
# Author DELL
# Date  2020/4/28
# 读取mysql数据存入excel
# -------------------------------
import pymysql
from readFile.ReadWriteExcel import save_in_xl
mysql_info = {
    'user': 'root',
    'password': 'diagbot@20180822kwz',
    'host': '192.168.21.235',
    'database': 'diagbot-app',
    'charset': 'utf8'
}
# 获取mysql连接
def getMysqlCon():
    mysqlCon = pymysql.connect(**mysql_info)
    return mysqlCon

def readMysql2Excel():
    bigDict = {}
    dicts_list = []
    mysqlCon = getMysqlCon()
    cursor = mysqlCon.cursor()
    sql = 'SELECT diag,iteam,it,bet FROM `doc_diag_lises` order by diag '
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            dictData = {}
            dictData['疾病'] = str(row[0])
            dictData['大项'] = row[1]
            dictData['小项'] = row[2]
            dictData['范围'] = row[3]
            # dicts_list.append(dictData)
            if row[0] not in bigDict:
                dataList = []
                dataList.append(dictData)
                bigDict[str(row[0]).replace('[','').replace(']','')] = dataList
            else:
                hhList = bigDict[row[0]]
                hhList.append(dictData)
                bigDict[str(row[0]).replace('[','').replace(']','')] = hhList
    except:
        print('操作mysql失败')
    cursor.close()
    mysqlCon.close()
    return bigDict
if __name__ == '__main__':
   dataList =  readMysql2Excel()
   for diag in dataList:
       print(diag)
       save_in_xl(dataList[diag], 'e:/deeee', cut_cursor='\n', save='old', sheetname=diag)



