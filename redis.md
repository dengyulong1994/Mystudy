redis

* 读写分离
  * 一台 master 写操作   三台  slave(哪路)读取  实验
  * slaveof [IP]    ![img](file:///C:\Users\deng\AppData\Local\Temp\%W@GJ$ACOF(TYDYECOKVDYB.png)120.77.2.217 11223  给该IP 做slave
  * info replication  查看连接情况查看
  * 更改 config 文件   265 写入slaveof IP port  272   写入 master密码
  * cp myredis.config  更改端口可以在一个电脑上开多个redis服务器



* master 停止服务时 , 让其他的slave 扮演 master 
  * 让自动完成  哨兵   sentinel.config
    * 更改 sentinel.config     复制一份更改配置
      *  15 - bind 内网地址       绑定内网地址 ,访问用公网地址 
      *  17 -  protect-mode yes
      *  70 行sentinel monitor master + IP + port 2(票数) 开端口
      *  73 - 改名字和密码  master
    * 启动哨兵
      * redid-server sentinel.conf  --sentinel  -  
    * 脚本  - -LUA 定义新的命令    
    * 集群   --Cluster   分区操作, 将多个节点变为一个节点 , 轮转
      * yum install rubby