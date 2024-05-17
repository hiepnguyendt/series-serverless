---
title : "Kiểm tra hoạt động"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---
Bạn có thể tải tệp ảnh ở đây để thêm dữ liệu để kiểm tra hoạt động của các dịch vụ

{{%attachments title="Images" pattern=".*\.(jpg|png)$"/%}}

1. Mở tệp **config.js** trong thư mục source code của front-end
    - Bỏ comment dòng số 4, sau đó thay giá trị băng email mà bạn đã đăng ký tài khoản cũng là email là bạn đăng ký nhận thông báo
![UpdateSource](/images/4-test-operation/4-test-operation-1.png?featherlight=false&width=90pc)

2. Mở tệp **Login.js** trong thư mục **source/component/Authen/**
- Bỏ comment dòng số 39 và 41
![UpdateSource](/images/4-test-operation/4-test-operation-2.png?featherlight=false&width=90pc)

3. Chạy các lệnh dưới đây để build và tải lên S3 bucket
    ```
    yarn build
    aws s3 cp build s3://fcj-book-store --recursive
    ```

4. Mở bảng điều khiển của [Amazon S3](https://s3.console.aws.amazon.com/s3/buckets?region=ap-southeast-1)
    - Ấn vào bucket **fcj-book-store**
![AccessWeb](/images/1/22.png?width=90pc)

5. Ấn chọn tab **Properties**
![AccessWeb](/images/1/23.png?width=90pc)

    - Kéo xuống cuối trang, ấn vào endpoint của website
![AccessWeb](/images/1/24.png?width=90pc)

6. Ấn **Register**
![AccessWeb](/images/1/25.png?width=90pc)
7. Kiểm tra email để lấy code xác nhận
![AccessWeb](/images/1/26.png?width=90pc)
7. Nhấn login
    - Nhập tài khoản mà bạn đã đăng kí ở bước trước
    - Ấn **Submit**
    ![AccessWeb](/images/1/27.png?width=90pc)

7. Ấn **Create new book**
![AccessWeb](/images/1/28.png?width=90pc)

8. Nhập thông tin sách
    - Nhập ID: `1`
    - Nhập tên sách: `Java`
    - Nhập tác giả: `Jame Patternson`
    - Nhập thể loại: `IT`
    - Nhập giá: `10.98`
    - Nhập mô tả: `A beginner's guide to learning the basic of Java`
    - Ấn **Choose File** và chọn tệp ảnh **Java.jpg** mà bạn vừa tải về
    - Ấn **Create**
    - Ấn **OK**
![AccessWeb](/images/1/29.png?width=90pc)

10. Ấn **Create new book**
    - Nhập ID: `2`
    - Nhập tên sách: `Let's Go`
    - Nhập tác giả: `Alex Edwards`
    - Nhập thể loại: `IT`
    - Nhập giá: `15.8`
    - Nhập mô tả: `A step-by-step guide to creating fast, secure web with Go`
    - Ấn **Choose File** và chọn tệp ảnh **LetGoBook.png** mà bạn vừa tải về
    - Ấn **Create**
![AccessWeb](/images/1/30.png?width=90pc)

12. Ấn **Add to cart** lần lượt từng sản phẩm
![AccessWeb](/images/1/32.png?width=90pc)
13. Ấn vào biểu tượng cart ở góc trên bên phải.
    - Ấn **Checkout**
    - Ấn **Ok**
![AccessWeb](/images/1/32.1.png?width=90pc)

15. Quay lại với bảng điều khiển của Amazon SQS
    - Ấn **Send and receive messages**
![AccessWeb](/images/1/32.2.png?width=90pc)

16. Ấn **Poll messages**
![AccessWeb](/images/1/32.3.png?width=90pc)

17. Ấn vào message đang hiển thị
![AccessWeb](/images/1/32.4.png?width=90pc)

18. Xem nội dung của đơn hàng, ấn **Done**
![AccessWeb](/images/1/32.5.png?width=90pc)

19. Mở email mà bạn đã đăng ký nhận thông báo

![CreateRecord](/images/4-test-operation/4-test-operation-20.png?featherlight=false&width=90pc)

20. Quay trở lại với màn hình của ứng dụng
- Ấn **Orders**, các đơn hàng được hiện thị
![AccessWeb](/images/1/32.6.png?width=90pc)

21. Lặp lại bước 12 đến bước 14 để thêm một vài đơn hàng tuỳ ý bạn
22. Ấn **Orders**
    - Ấn **Handle**
![AccessWeb](/images/1/32.7.png?width=90pc)

23. Ấn **OK**
![AccessWeb](/images/1/32.8.png?width=90pc)

24. Đơn hàng đã được xử lý chuyển trạng thái sang thành **Processed** và không hiện các nút xoá và xử lý
    - Ấn **Delete**

25. Mở bảng điều khiển của [Amazon DynamoDB](https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#dashboard), ấn **Explore items** ở menu phía bên trái
    - Chọn **Orders**, dữ liệu đơn hàng đã được đưa vào bảng
![AccessWeb](/images/1/32.9.png?width=90pc)

24. Quay trở lại với màn hình của ứng dụng
    - Ấn **Delete**
    - Ấn **OK**
![AccessWeb](/images/1/33.png?width=90pc)

    - Đơn hàng bị xoá không còn hiện thị
![AccessWeb](/images/1/34.png?width=90pc)pc)

Chúng ta đã hoàn thành workshop, đã biết cách làm việc với Amazon SQS và Amazon SNS. Bài tiếp theo chúng ta sẽ sử dụng CodePipeline để triển khai ứng dụng.