from app import app  # app.pyからFlaskのインスタンスappをimport


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)  # default portを変更
