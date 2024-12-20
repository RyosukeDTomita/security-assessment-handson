import mysql.connector

db_config = {
    "host": "mysql",
    "user": "root",
    "password": "password",
    "database": "user_info",
    "port": 3306,
}

try:
    # MySQLに接続
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    print("MySQLに接続成功")

    # SQLインジェクションの脆弱性があるクエリ
    user_id = "john"
    # password = "johnpassword"
    password = "' OR '1'='1"
    query = f"SELECT * FROM users WHERE user_id = '{user_id}' AND password = '{password}'"
    print(f"Executing Query: {query}")  # デバッグ用
    cursor.execute(query)
    result = cursor.fetchone()
    tables = cursor.fetchall()
    print(result)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    conn.close()
