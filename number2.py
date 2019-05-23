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

article_author_cursor = db.cursor()
q_article_author = """
SELECT authors.name,COUNT(articles.title)
FROM articles
INNER JOIN authors ON articles.author = authors.id
INNER JOIN log ON CONCAT('/article/', articles.slug) = log.path
GROUP BY authors.name
ORDER BY COUNT(articles.title) DESC;
"""
article_author_cursor.execute(q_article_author)
article_author = article_author_cursor.fetchall()

for aa in article_author:
    print('{article_name} - {article_view}views'.format(
        article_name=aa[0], article_view=aa[1]))
