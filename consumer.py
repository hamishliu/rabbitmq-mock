#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: LiuBo
import pika

hostname = "10.43.166.63"
port = 5672
username = "guest"
password = "guest"
queues_key = "消息队列1"  # 测试队列名称

# 建立与rabbitmq的连接
credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port, credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue=queues_key)


# 定义一个处理消息的回调函数
def callback(ch, method, properties, body):
    print("消费者接收到了数据：%r" % body.decode("utf8"))


# 有消息来临，立即执行callbak，没有消息则夯住，等待消息
channel.basic_consume(queue=queues_key, on_message_callback=callback, auto_ack=True)
# 开始消费，接收消息
channel.start_consuming()
