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
With ERRORS AS
(SELECT COUNT(time::timestamp::date), time::timestamp::date
FROM log
WHERE status != '200 OK'
GROUP BY (time::timestamp::date)
ORDER BY (time::timestamp::date) DESC),
ALL_REQUEST AS
(SELECT COUNT(time::timestamp::date), time::timestamp::date
FROM log
GROUP BY (time::timestamp::date)
ORDER BY (time::timestamp::date) DESC)
Select (ERRORS.count::numeric / ALL_REQUEST.count)*100
From ERRORS
INNER JOIN ALL_REQUEST
ON ERRORS.time::timestamp::date = ALL_REQUEST.time::timestamp::date
WHERE (ERRORS.count::numeric / ALL_REQUEST.count)*100 > 1;
"""
log_cursor.execute(q_log)
logs = log_cursor.fetchall()

for log in logs:
    print('{error}%'.format(
        error=round(log[0], 2))
    )
