FROM python:3.12.8-slim-bullseye AS setup
# app.py or wsgi.py以外ならappオブジェクトを作成しているパスのexportが必須。
ENV FLASK_APP=app
WORKDIR /usr/local/flask_app

# library install
COPY ./requirements.txt /usr/local/flask_app/
RUN <<EOF bash -ex
python3 -m pip install --upgrade pip setuptools wheel --no-cache-dir
python3 -m pip install -r requirements.txt
EOF


FROM setup AS deploy
COPY . .
EXPOSE 8000
