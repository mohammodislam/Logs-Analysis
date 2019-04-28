import psycopg2

pathForArticle = {
    '/article/candidate-is-jerk': 26,
    '/article/bears-love-berries': 25,
    '/article/bad-things-gone': 23,
    '/article/goats-eat-googles': 27,
    '/article/trouble-for-troubled': 30,
    '/article/balloon-goons-doomed': 24,
    '/article/so-many-bears': 29,
    '/article/media-obsessed-with-bears': 28
}

db = psycopg2.connect("dbname=news")
log_cursor = db.cursor()
articles_cursor = db.cursor()

q_log = """
SELECT   path,
         COUNT(path) AS dupe_cnt
FROM     log
GROUP BY path
HAVING   COUNT(path) > 1
ORDER BY COUNT(path) DESC
LIMIT 9
""";
q_articles = """
select id, title from articles
"""
log_cursor.execute(q_log)
articles_cursor.execute(q_articles)
article_dict = {}
articles = articles_cursor.fetchall()
for article in articles:
    article_dict[article[0]] = article[1]

logs = log_cursor.fetchall()
for log in logs:
    if log[0] == '/':
        continue
    article_id = pathForArticle[log[0]]
    print(article_dict[article_id], " - ",log[1],"views")
