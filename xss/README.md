# XSS DEMO

## HOW TO USE

1. run docker container

  ```shell
  cd xss
  docker compose up
  ```
2. Go to [localhost:81/index.html](http://localhost:81/index.html)
3. Chose XSS Type
4. Try XSS e.g. `<img src=x onerror=alert('hoge')>`

![dom base xss](./assets/dom-based-xss.png)
![refrected](./assets/refrected-xss.png)

---

## Reference

- [my Qiita](https://qiita.com/sigma_devsecops/items/b45868019eca4f3880f0)
- [UBsecure Blog](https://www.ubsecure.jp/blog/cross-site-scripting)
