#!/usr/bin/env python3
import psycopg2
import sys

try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print("Unable to connect!")
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
else:
    print("Connected!")

log_cursor = db.cursor()
q_log = """
SELECT articles.title,COUNT(articles.title)
FROM log
INNER JOIN articles ON log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY COUNT(articles.title) DESC
LIMIT 3
"""
log_cursor.execute(q_log)
logs = log_cursor.fetchall()

for log in logs:
    print('"{article}" - {count} views'.format(article=log[0], count=log[1]))
