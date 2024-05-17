---
title : "Create SNS topic"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2. </b> "
---
1. Navigate [Amazon SNS console](https://ap-southeast-1.console.aws.amazon.com/sns/v3/home?region=ap-southeast-1#/dashboard)
    - Click **Topics** on the left menu
    - Click **Create topic**
![CreateSNS](/images/1/6.png?width=90pc)

3. Select **Stardard** for the topic type
    - Ente topic name: `order-notice`
![CreateSNS](/images/1/7.png?width=90pc)

4. Scroll down to bottom, click **Create topic**
![CreateSNS](/images/1/8.png?width=90pc)

5. Click on the topic you just created
![CreateSNS](/images/1/8.png?width=90pc)

6. Click **Create subscription**
![CreateSNS](/images/1/10.png?width=90pc)

8. On the **Create subscription** page  
    - Enter order-notice's topic arn
    - Select protocol type: **Email**
    - Enter the email with which you registered an account on Cognito and are admin
    - Click **Create subcription**
![CreateSNS](/images/1/11.png?width=90pc)

9. Then, status of subcription is pending confirmation
![CreateSNS](/images/1/12.png?width=90pc)

10. To confirm your email, open the registered email
    - Search mail sent from **no-reply@sns.amazonaws.com**, click to confrimation link
![CreateSNS](/images/1/13.png?width=90pc)

11. Back to SNS topic dashboard, subscription confirmed
![CreateSNS](/images/1/14.png?width=90pc)
