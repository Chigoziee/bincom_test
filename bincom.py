#!/usr/bin/env python
# coding: utf-8

# In[38]:


import sqlalchemy
import pandas as pd
import mysql.connector


my_conn = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="caesarcot11",
      database="bincom")
data = pd.read_sql('''SELECT lga_id, party_abbreviation, SUM(party_pu_total) party_lga_total
                         FROM (SELECT pu.lga_id, pu.ward_id, p.polling_unit_uniqueid, p.party_abbreviation, SUM(p.party_score) party_pu_total
                               FROM announced_pu_results p
                               JOIN polling_unit pu
                               ON p.polling_unit_uniqueid = pu.uniqueid
                               group by 1, 2, 3, 4
                               ORDER BY 1)Table1
                         GROUP BY 1, 2
                      ''',my_conn)
data.to_csv('party_lga_total.csv', index = False)

