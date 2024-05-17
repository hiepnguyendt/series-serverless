---
title : "Tạo hàng đợi"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 2.1. </b> "
---
1. Mở bảng điều khiển của [Amazon SQS](https://ap-southeast-1.console.aws.amazon.com/sqs/v2/home?region=ap-southeast-1#/homepage)
![CreateSQS](/images/1/3.png?width=90pc)

2. Ấn **Create queue**
![CreateSQS](/images/1/4.png?width=90pc)

3. Chọn **Stardard** cho kiểu của hàng đợi
    - Nhập tên cho hàng đợi: `checkout-queue`
    - Kéo xuống cuối, ấn **Create queue**
![CreateSQS](/images/1/5.png?width=90pc)

5. Ấn **Send and receive messages** 

6. Nhập nội dung message, ví dụ: `The first order`
    - Ấn **Send** để gửi message đến hàng đợi
![CreateSQS](/images/1/5.1.png?width=90pc)

7. Ấn **Poll message** để nhận toàn bộ message gửi đến hàng đợi
![CreateSQS](/images/1/5.2.png?width=90pc)

8. Ấn vào message đang hiện thị
![CreateSQS](/images/1/5.3.png?width=90pc)

9. Nội dung message được hiện thị
    - Ấn **Done**
![CreateSQS](/images/1/5.4.png?width=90pc)
10. Tích chọn message. Ấn **Delete**
    - Ấn **Delete** để xoá message
![CreateSQS](/images/1/5.5.png?width=90pc)

