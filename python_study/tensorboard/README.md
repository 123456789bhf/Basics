### 参考链接

#### 模型框架可视化
https://datawhalechina.github.io/thorough-pytorch/%E7%AC%AC%E4%B8%83%E7%AB%A0/7.3%20%E4%BD%BF%E7%94%A8TensorBoard%E5%8F%AF%E8%A7%86%E5%8C%96%E8%AE%AD%E7%BB%83%E8%BF%87%E7%A8%8B.html

##### 实验记录
https://blog.csdn.net/deephub/article/details/123086159

### 在运行程序之前先运行下面命令
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python




##### 损失函数可视化

nohup bash lss_vis_train.sh 2□ > 2.log 1>&1

在终端运行
tensorboard --logdir=logs/fit
其中logs/fit是模型输出文件的路径
