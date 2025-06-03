### 1. 使用https上传步骤
1. git add .
2. git commit -m "first"
3. git remote add origin "https的github上的连接" 
4. gt push -u origin master
### 2. 使用ssh上传步骤
1. 检查本地是否有ssh key:
     - cd ~/.ssh
     - ls
   看是否存在
1. git remote add origin "ssh的github链接"
2. git add .
3. git commit -m "first"
4. git push -u origin master
### 注意事项
https://blog.csdn.net/erhuobuer/article/details/89343380

1.出现警告解决方式
![{C7BFC21E-6FAC-4433-B73C-297E64F3F6FE}](https://github.com/user-attachments/assets/5abb6964-13ab-4b77-9ee5-3f5da8ab7210)

git pull --rebase origin master

git push -u origin master

2. 如果报错就

//取消http代理

git config --global --unset http.proxy


git config --global http.proxy 127.0.0.1:7897（7897是clash的端口号）

//取消https代理

git config --global --unset https.proxy

git config --global https.proxy 127.0.0.1:7897（7897是clash的端口号）

然后再git commit 或git clone

https://blog.csdn.net/good_good_xiu/article/details/118567249
