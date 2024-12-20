from flask import Flask, request, render_template
import mysql.connector
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = Flask(__name__)

# MySQLデータベース接続情報
db_config = {
    "host": "mysql",
    "user": "root",
    "password": "password",
    "database": "user_info",
    "port": 3306,
}


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    user_id = request.form['user_id']
    password = request.form['password']

    logger.info(f"User ID: {user_id}, Password: {password}")

    try:
        # MySQLに接続
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        logger.info("Connected to MySQL")

        # SQLインジェクションの脆弱性があるクエリ
        query = f"SELECT * FROM users WHERE user_id = '{user_id}' AND password = '{password}'"
        logger.info(f"Executing Query: {query}")  # デバッグ用
        cursor.execute(query)
        result = cursor.fetchall()
        logger.info(result)

        if result:
            return f"LOGIN SUCCESS, user info is {result}!"
        else:
            return "Invalid credentials."
    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)
