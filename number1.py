import psycopg2

db = psycopg2.connect("dbname=news")
log_cursor = db.cursor()

q_log = """
SELECT articles.title, COUNT(articles.title) 
FROM log 
INNER JOIN articles ON log.path = CONCAT('/article/', articles.slug) 
GROUP BY articles.title
ORDER BY COUNT(articles.title) DESC;
""";
log_cursor.execute(q_log)
logs = log_cursor.fetchall()

for log in logs:
    print(log[0],"-",log[1],"views")
