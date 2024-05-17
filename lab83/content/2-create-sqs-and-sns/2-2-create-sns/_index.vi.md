---
title : "Tạo SNS topic"
date :  "`r Sys.Date()`" 
weight : 2
chapter : false
pre : " <b> 2.2. </b> "
---
1. Mở bảng điều khiển của [Amazon SNS](https://ap-southeast-1.console.aws.amazon.com/sns/v3/home?region=ap-southeast-1#/dashboard)
    - Ấn **Topics** ở menu phía bên trái
    - Ấn **Create topic**
![CreateSNS](/images/1/6.png?width=90pc)

3. Chọn **Stardard** cho kiểu của topic
    - Nhập tên topic: `order-notic`
![CreateSNS](/images/1/7.png?width=90pc)

4. Kéo xuống cuối trang, ấn **Create topic**
![CreateSNS](/images/1/8.png?width=90pc)

5. Ấn vào topic mà bạn vừa tạo
![CreateSNS](/images/1/8.png?width=90pc)

6. Ấn **Create subscription**
![CreateSNS](/images/1/10.png?width=90pc)

7. Chọn **Protocol** là **Email**

![CreateSNS](/images/2-create-sqs-and-sns/2-2-create-sns-7.png?featherlight=false&width=90pc)

8. Tại trang **Create subscription**
    - Nhập arn của order-notice topic
    - Chọn protocol type: **Email**
    - Nhập email mà bạn đã đăng ký tài khoản trên Cognito và là admin
    - Ấn **Create subcription**
![CreateSNS](/images/1/11.png?width=90pc)

9. Sau đó, subcription sẽ ở trạng thái đang xử lý

![CreateSNS](/images/2-create-sqs-and-sns/2-2-create-sns-9.png?featherlight=false&width=90pc)

10. Để xác nhận email của bạn, mở email đã đăng ký
    - Tìm mail được gửi đến từ địa **no-reply@sns.amazonaws.com**, ấn vào link để xác nhận
![CreateSNS](/images/1/13.png?width=90pc)

11. Quay lại với sns topic, subcription đã được xác nhận
![CreateSNS](/images/1/14.png?width=90pc)
