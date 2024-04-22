---
title : "Dọn dẹp tài nguyên"
date :  "`r Sys.Date()`" 
weight : 4
chapter : false
pre : " <b> 4. </b> "
---
1. Xoá bảng trong DynamoDB
- Mở bảng điều khiển của [DynamoDB](https://ap-southeast-2.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-2#dashboard)
- Chọn **Tables** ở menu phía bên trái
- Chọn bảng **Books**
- Ấn **Delete**
- Nhập **delete** và ấn **Delete table**
2. Xoá S3 bucket
- Mở bảng điều khiển của [S3](https://s3.console.aws.amazon.com/s3/buckets?region=ap-southeast-2)
- Chọn bucket **book-image-resize-store**
- Ấn nút **Empty**
- Nhập **permanently delete** và ấn **Empty**
- Chọn bucket **book-image-resize-store**
- Ấn nút **Delete**
- Nhập **book-image-resize-store** và ấn **Delete**
- Chọn bucket **book-image-store**
- Ấn nút **Delete**
- Nhập **book-image-store** và ấn **Delete**
3. Xoá Lambda function
- Mở bảng điều khiển của [AWS Lambda](https://ap-southeast-2.console.aws.amazon.com/lambda/home?region=ap-southeast-2#/functions)
- Chọn **book_create** function
- Ấn **Actions**
- Chọn **Delete**
- Nhập **delete** và ấn **Delete**
- Tương tự với **resize_image** function
{{% notice note %}}
Nếu bạn tiếp tục với bài số 2 của series thì có thể bỏ qua bước xoá Lambda function.
{{% /notice %}}