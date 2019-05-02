import psycopg2

db = psycopg2.connect("dbname=news")
article_author_cursor = db.cursor()
q_article_author ="""
SELECT authors.name, COUNT(articles.title)
FROM articles
INNER JOIN authors ON articles.author = authors.id
INNER JOIN log ON CONCAT('/article/', articles.slug) = log.path 
GROUP BY authors.name
ORDER BY COUNT(articles.title) DESC;
"""
article_author_cursor.execute(q_article_author)
article_author = article_author_cursor.fetchall()

for aa in article_author:
    print(aa[0], "-",aa[1],"views")