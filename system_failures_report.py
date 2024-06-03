#!/usr/bin/env python3.11

import mysql.connector

DB_USER = 'user'
DB_PASS = 'pass'
DB_HOST = 'locahost'
DB_NAME = 'database_name'


def generate_report(cursor) -> list:
    query = """
    SELECT CONCAT(c.first_name, ' ', c.last_name) AS customer,
    COUNT(e.status) AS failures
    FROM customers c
    JOIN campaigns cp ON c.id = cp.customer_id
    JOIN events e ON cp.id = e.campaign_id
    WHERE e.status = 'failure'
    GROUP BY c.id
    HAVING COUNT(e.status) > 3;
    """

    cursor.execute(query)
    result = cursor.fetchall()
    return result


def create_connection():
    try:
        connection = mysql.connector.connect(
                                    user=DB_USER,
                                    password=DB_PASS,
                                    host=DB_HOST,
                                    database=DB_NAME)
    except Exception as e:
        print(f'Something went wrong. Error: {e} ')
        exit(1)

    return connection


def main():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    report = generate_report(cursor)
    for item in report:
        print(f"Customer: {item['customer']} | Failures: {item['failures']}")


if __name__ == '__main__':
    main()
