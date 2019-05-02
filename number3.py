import psycopg2

db = psycopg2.connect("dbname=news")
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

Select * 
From ERRORS 
INNER JOIN ALL_REQUEST
ON ERRORS.time::timestamp::date = ALL_REQUEST.time::timestamp::date;
"""
log_cursor.execute(q_log)
logs = log_cursor.fetchall()

for log in logs:
    errPercentage = round((log[0]/log[2])*100, 2)
    timeMonthName = log[1].strftime("%B")
    timeDay = log[1].strftime("%d")
    timeYear = log[1].strftime("%Y")
    if errPercentage > 1:
        print(timeMonthName,timeDay,",",timeYear, "-",errPercentage, "% errors")
    
