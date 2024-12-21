# Vulnerable Server Settings

## ENVIRONMENT

OpenResty

---

## PREPARING

```shell
docker compose up
```

---

## HOW TO USE

### Try Directory Listing

Go to [http://localhost:8080/list/](http://localhost:8080/list/)

![directory listing](./assets/directory_listing.png)

#### How to fix

delete settings at `nginx.conf`

```
            # FIXME: ディレクトリリスティング
            autoindex on;
            autoindex_exact_size off; # ファイルサイズを簡易表示
            autoindex_localtime on;   # ファイルのタイムスタンプをローカルタイムで表示
```

### Version information is exposed from Error Screen

Go to [http://localhost:8080/hoge](http://localhost:8080/hoge)

![404 error](./assets/404error.png)

#### How to fix

add settings at `nginx.conf`

```
        server_tokens off; # FIXME: エラーページ，レスポンスのServerヘッダにnginxのバージョンを表示しない
```

### Version information is exposed from Server Header

You can see `Server: openresty/1.21.4.1`

```shell
curl -v http://localhost:8080 2>&1 | grep '< '

< HTTP/1.1 200 OK
< Server: openresty/1.21.4.1
< Date: Sat, 21 Dec 2024 10:22:30 GMT
< Content-Type: text/html
< Content-Length: 601
< Last-Modified: Sat, 21 Dec 2024 10:14:57 GMT
< Connection: keep-alive
< ETag: "67669521-259"
< Accept-Ranges: bytes
```

#### How to fix

add settings at `nginx.conf`

```
        server_tokens off; # FIXME: エラーページ，レスポンスのServerヘッダにnginxのバージョンを表示しない
```

### Path information exposed by robots.txt (Just for your information)

Go to [http://localhost:8080/robots.txt](http://localhost:8080/robots.txt) and you can find `admin.html`
![robots.txt](./assets/robots.png)

#### How to fix

[Google検索セントラル](https://developers.google.com/search/docs/crawling-indexing/block-indexing?hl=ja)

- solution1: add meta at html

```html
<meta name="robots" content="noindex"> <!--robots.txtの代わり-->
```

- solution2: add `X-Robots-Tag: noindex` to Response

```
        location = /admin.html {
            add_header X-Robots-Tag "noindex";
        }
```

```shell
# check
curl -v http://localhost:8080/admin.html 2>&1 | grep '< '
< HTTP/1.1 200 OK
< Server: openresty/1.21.4.1
< Date: Sat, 21 Dec 2024 11:02:34 GMT
< Content-Type: text/html
< Content-Length: 93
< Last-Modified: Sat, 21 Dec 2024 10:52:36 GMT
< Connection: keep-alive
< ETag: "67669df4-5d"
< X-Robots-Tag: noindex
< Accept-Ranges: bytes
```
