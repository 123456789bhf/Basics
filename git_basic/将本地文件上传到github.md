### 步骤
1. git add .
2. git commit -m "first"
3. git remote add origin "" 
4. gt push -u origin master
### 注意事项
https://blog.csdn.net/erhuobuer/article/details/89343380

如果报错就

//取消http代理

git config --global --unset http.proxy

//取消https代理

git config --global --unset https.proxy

然后再git commit 或git clone

https://blog.csdn.net/good_good_xiu/article/details/118567249
