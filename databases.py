#!/usr/bin/python
# -*- coding: utf-8 -*-

from psycopg2 import connect

con = None
con = connect(dbname='postgres' , user='postgres', host='localhost', password='' )
