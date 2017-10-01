# SQS ping

First program to test SQS functionality.

# How to use

This repository contains different python scripts to create an SQS queue, send and receive messages from the queue.

As a first step one needs to create a queue. In this example we will create a queue and name it `test`.

## Create a queue

```
python3 createSQSqueue.py
```

At this point we can either start a software to poll the queue, called a consumer, or the script that sends messages to the queue. Let's start the sender first.

## Send a message to the queue

```
python3 senderSQS.py
```

Let's now poll the queue to retrieve the message.

## Poll the queue
```
python3 consumerSQSpolling.py
```
