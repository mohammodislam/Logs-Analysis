# Logs-Analysis

Logs-Analysis looks at an SQL Databases and Answers 3 Questions: 

1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)


## Getting Started
1. Install and setup PostgreSQL: https://www.postgresql.org/download/
2. Create new database using command `CREATE DATABASE news;`
3. Download news data sql file from http://bit.ly/2VQ54bm and add data(from newsdata.sql) to the new database created using command `psql -d news -f newsdata.sql`


## Run code, see result
On your terminal run the command `python number*.py` and see the expected result.
