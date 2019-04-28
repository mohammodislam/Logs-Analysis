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
article_author_cursor = db.cursor()
q_log = """
SELECT   path,
         COUNT(path) AS dupe_cnt
FROM     log
GROUP BY path
HAVING   COUNT(path) > 1
ORDER BY COUNT(path) DESC
"""
q_article_author ="""
SELECT articles.id, authors.name
FROM articles
INNER JOIN authors
ON articles.author = authors.id
"""
article_author_cursor.execute(q_article_author)
log_cursor.execute(q_log)
logs = log_cursor.fetchall()
article_author = article_author_cursor.fetchall()
article_author_dict = {}

for item in article_author:
    #item[0] is id
    #item[1] is author name
    article_author_dict[item[0]] = item[1]
    #print(item[0], item[1])

author_view = {}
for log in logs:
    if log[0] == '/':
        continue
    try:
        article_id = pathForArticle[log[0]]
        if article_author_dict[article_id] in author_view:
            prev_view = author_view[article_author_dict[article_id]]
            author_view[article_author_dict[article_id]] = log[1] + prev_view
        else:
            author_view[article_author_dict[article_id]] = log[1]
    except:
        pass


#sorting data
view_list = []
for i in author_view:
    view_list.append(author_view[i])
view_list.sort(reverse=True)

view_key_list = list(author_view.keys())

for i in view_list:
    print(list(author_view.keys())[list(author_view.values()).index(i)], "-", i, "views") 