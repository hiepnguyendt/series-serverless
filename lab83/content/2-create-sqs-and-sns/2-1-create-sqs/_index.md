---
title : "Create queue"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 2.1. </b> "
---
1. Open [Amazon SQS console](https://ap-southeast-1.console.aws.amazon.com/sqs/v2/home?region=ap-southeast-1#/homepage)
![CreateSQS](/images/1/3.png?width=90pc)

2. Click **Create queue**
![CreateSQS](/images/1/4.png?width=90pc)

3. Select **Stardard** for queue type. 
    - Enter queue name: `checkout-queue`
    - Then scroll down, click **Create queue**
![CreateSQS](/images/1/5.png?width=90pc)

5. Click **Send and receive messages**
6. Enter message content, such as: `The first order`
    - Click **Send** to send message to queue
![CreateSQS](/images/1/5.1.png?width=90pc)

7. Click **Poll message** to receive all message sent to queue 
![CreateSQS](/images/1/5.2.png?width=90pc)

8. Click to the message is showing
![CreateSQS](/images/1/5.3.png?width=90pc)

9. The message content is displayed
    - Click **Done**
![CreateSQS](/images/1/5.4.png?width=90pc)

10. Check to this message. Click **Delete**
    - Click **Delete** to delete message
![CreateSQS](/images/1/5.5.png?width=90pc)

