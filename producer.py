#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiuBo
import pika

hostname = "10.43.166.63"
port = 5672
username = "guest"
password = "guest"
queues_key = "消息队列1"  # 测试队列名称
count = 10  # 生产者发送消息数目

# 创建凭证，使用rabbitmq用户密码登录
credentials = pika.PlainCredentials(username, password)
# 新建连接到服务器ip
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, credentials=credentials))
# 创建频道
channel = connection.channel()
# 声明一个队列，用于接收消息，队列名字叫上面“填写的变量”,其中durable=True为开启消息持久化,为False或者不加此参数则不持久化
channel.queue_declare(queue=queues_key, durable=True)

start = 0
while start < count:
    start = start + 1
    # 注意在rabbitmq中，消息想要发送给队列，必须经过交换(exchange)，初学可以使用空字符串交换(exchange='')，它允许我们精确的指定发送给哪个队列(routing_key=''),参数body值发送的数据
    channel.basic_publish(exchange='',
                          routing_key=queues_key,
                          body=f'\n新消息: {start}\n')
    print(f"消息队列1已经发送了 {start} 条消息")

# 程序退出前，确保刷新网络缓冲以及消息发送给rabbitmq，需要关闭本次连接
connection.close()
