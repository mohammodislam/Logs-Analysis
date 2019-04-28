import psycopg2


db = psycopg2.connect("dbname=news")
log_cursor_total = db.cursor()
log_cursor_error = db.cursor()
q_log = """
SELECT time::timestamp::date, COUNT(time::timestamp::date) FROM log GROUP BY (time::timestamp::date)
"""
q_log_err = """
SELECT COUNT(time::timestamp::date) FROM log WHERE status != '200 OK' GROUP BY (time::timestamp::date) 
"""
log_cursor_total.execute(q_log)
log_cursor_error.execute(q_log_err)
logs = log_cursor_total.fetchall()
log_errors = log_cursor_error.fetchall()

# for log in log_errors:
#     print("Error: ",log)

# for log in logs:
#     print("Total: ", log)

for err, log in zip(log_errors, logs):
    answer = str(round(((err[0]/log[1])*100), 2))
    if float(answer) > 1:
        print(log[0], answer,"%")


