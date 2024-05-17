---
title : "Test web operation"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---
You can download the image files here to add data to check the operation of the services

{{%attachments title="Images" pattern=".*\.(jpg|png)$"/%}}

1. Open **config.js** file in source code folder of front-end
    - Uncomment the line 4, then change value with email that you registered account as well as registered to receive notify    
![UpdateSource](/images/4-test-operation/4-test-operation-1.png?featherlight=false&width=90pc)

2. Open **Login.js** file in **source/component/Authen/** folder
    - Uncomment the lines 39 and 41
![UpdateSource](/images/4-test-operation/4-test-operation-2.png?featherlight=false&width=90pc)

3. Run the below command to build and upload to S3 bucket
    ```
    yarn build
    aws s3 cp build s3://fcj-book-shop --recursive
    ```

4. Navigate [Amazon S3 console](https://s3.console.aws.amazon.com/s3/buckets?region=ap-southeast-1)
    - Click to **fcj-book-shop** bucket
![AccessWeb](/images/1/22.png?width=90pc)

5. Click **Properties** tab
![AccessWeb](/images/1/23.png?width=90pc)
    - Scroll down to bottom, click to website endpoint
![AccessWeb](/images/1/24.png?width=90pc)

6. Click **Register**
![AccessWeb](/images/1/25.png?width=90pc)
7. Check your email to get code.
![AccessWeb](/images/1/26.png?width=90pc)
7. Click login
    - Enter your account has created previous step
    - Click **Submit**
![AccessWeb](/images/1/27.png?width=90pc)
8. Click **Create new book**
![AccessWeb](/images/1/28.png?width=90pc)

8. Enter the book information
    - Enter ID: `1`
    - Enter book name: `Java`
    - Enter author: `Jame Patternson`
    - Enter catagory `IT`
    - Enter price: `10.98`
    - Enter desciption: `A beginner's guide to learning the basic of Java`
    - Click **Choose File** và chọn tệp ảnh **Java.jpg** mà bạn vừa tải về
    - Click **Create**
    - Click **OK**
![AccessWeb](/images/1/29.png?width=90pc)


10. Ấn **Create new book**
    - Enter ID: `2`
    - Enter book name: `Let's Go`
    - Enter author: `Alex Edwards`
    - Enter catagory: `IT`
    - Enter price: `15.8`
    - Enter desciption: `A step-by-step guide to creating fast, secure web with Go`
    - Click **Choose File** và chọn tệp ảnh **LetGoBook.png** mà bạn vừa tải về
    - Click **Create**
![AccessWeb](/images/1/30.png?width=90pc)


12. Click **Add to cart** of each product
![AccessWeb](/images/1/32.png?width=90pc)

13. Click on the cart icon in the upper right corner. 
    - Click **Checkout**
    - Click **OK**
![AccessWeb](/images/1/32.1.png?width=90pc)


15. Back to Amazon SQS console
    - Click **Send and receive messages**
![AccessWeb](/images/1/32.2.png?width=90pc)

16. Click **Poll messages**
![AccessWeb](/images/1/32.3.png?width=90pc)

17. Click to the showing message
![AccessWeb](/images/1/32.4.png?width=90pc)

18. View the content of the order, Click **Done**
![AccessWeb](/images/1/32.5.png?width=90pc)

19. Open email that you have subscribed to receive notification

![CreateRecord](/images/4-test-operation/4-test-operation-20.png?featherlight=false&width=90pc)

20. Back to the application tab
    - Click **Orders**, orders are displayed
![AccessWeb](/images/1/32.6.png?width=90pc)

21. Repeat steps 12 to 14 to add as some orders as you like
22. Click **Orders**
    - Click **Handle**
![AccessWeb](/images/1/32.7.png?width=90pc)

23. Click **OK**
![AccessWeb](/images/1/32.8.png?width=90pc)

24. The order has been processed, the status is changed to **Processed** and delete and processing buttons aren't displayed
    - Click **Delete**

25. Open [Amazon DynamoDB console](https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#dashboard), Click **Explore items** on the left menu
    - Select **Orders**, processed order data has been entered into the table
![AccessWeb](/images/1/32.9.png?width=90pc)

24. Back to application tab
    - Click **Delete**
    - Click **OK**
![AccessWeb](/images/1/33.png?width=90pc)

    - Deleted orders are no longer displayed
![AccessWeb](/images/1/34.png?width=90pc)

We have completed the workshop, already know how to work with Amazon SQS and Amazon SNS. The next workshop we will use CodePipeline to deploy the application.