---
title : "Tạo Lambda function"
date :  "`r Sys.Date()`" 
weight : 1
chapter : false
pre : " <b> 3.1 </b> "
---
Trong bước này, chúng ta sẽ tạo một bảng DynamoDB mới để lưu dữ liệu đơn hàng đã được xử lý và bốn Lambda function để lưu đơn hàng, quản lý đơn hàng, xoá đơn hàng, xử lý đơn hàng bằng SAM template.

1. Mở tệp **template.yaml** của thư mục source code **fcj-book-shop-sam-ws6** đã tải về
     - Thêm đoạn script dưới đây để tạo một bảng **Orders** trong DynamoDB.
          ```
            OrdersTable:
              Type: AWS::Serverless::SimpleTable
              Properties:
                TableName: Orders
                PrimaryKey:
                  Name: id
                  Type: String
          ```
          ![CreateOrderTable](/images/1/15.png?width=90pc)

2. Chạy các lệnh dưới đây
    ```
    sam build
    sam deploy --guided
    ```
    ![CreateOrderTable](/images/1/16.png?width=90pc)
    - Mở bảng điều khiển của [AWS DynamDB](https://ap-southeast-1.console.aws.amazon.com/dynamodbv2/home?region=ap-southeast-1#tables) để kiểm tra


3. Thêm đoạn script dưới đây để tạo function **CheckOutOrder**
    ```
      CheckOutOrder:
        Type: AWS::Serverless::Function
        Properties:
          FunctionName: checkout_order
          CodeUri: fcj-book-shop/checkout_order
          Handler: checkout_order.lambda_handler
          Runtime: python3.9
          Architectures:
            - x86_64
          Policies:
            - Statement:
                - Sid: VisualEditor0
                  Effect: Allow
                  Action:
                    - sqs:*
                  Resource:
                    - !Sub arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:checkout-queue
                - Sid: VisualEditor1
                  Effect: Allow
                  Action:
                    - sns:Publish
                  Resource:
                    - !Sub arn:aws:sns:${AWS::Region}:${AWS::AccountId}:order-notice
          Environment:
            Variables:
              QUEUE_NAME: "checkout-queue"
    ```
    ![CreateOrderTable](/images/1/17.png?width=90pc)

- Thêm đoạn script dưới đây để tạo function **OrderManagement**
    ```
      OrderManagement:
        Type: AWS::Serverless::Function
        Properties:
          FunctionName: order_management
          CodeUri: fcj-book-shop/order_management
          Handler: order_management.lambda_handler
          Runtime: python3.9
          Architectures:
            - x86_64
          Policies:
            - Statement:
                - Sid: VisualEditor0
                  Effect: Allow
                  Action:
                    - sqs:*
                  Resource:
                    - !Sub arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:checkout-queue
                - Sid: VisualEditor1
                  Effect: Allow
                  Action:
                    - dynamodb:Query
                  Resource:
                    - !Sub arn:aws:dynamodb:${AWS::Region}:${AWS::AccountId}:table/Orders
          Environment:
            Variables:
              QUEUE_NAME: "checkout-queue"
    ```
    ![CreateOrderTable](/images/1/18.png?width=90pc)
- Thêm đoạn script dưới đây để tạo function **HandleOrder**
    ```
      HandleOrder:
        Type: AWS::Serverless::Function
        Properties:
          FunctionName: handle_order
          CodeUri: fcj-book-shop/handle_order
          Handler: handle_order.lambda_handler
          Runtime: python3.9
          Architectures:
            - x86_64
          Policies:
            - Statement:
                - Sid: VisualEditor0
                  Effect: Allow
                  Action:
                    - dynamodb:PutItem
                    - dynamodb:BatchWriteItem
                    - sqs:*
                  Resource:
                    - !Sub arn:aws:dynamodb:${AWS::Region}:${AWS::AccountId}:table/Orders
                    - !Sub arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:checkout-queue
          Environment:
            Variables:
              QUEUE_NAME: "checkout-queue"
    ```

- Thêm đoạn script dưới đây để tạo function **DeleteOrder**
    ```
      DeleteOrder:
        Type: AWS::Serverless::Function
        Properties:
          FunctionName: delete_order
          CodeUri: fcj-book-shop/delete_order
          Handler: delete_order.lambda_handler
          Runtime: python3.9
          Architectures:
            - x86_64
          Policies:
            - Statement:
                - Sid: VisualEditor0
                  Effect: Allow
                  Action:
                    - sqs:*
                    - dynamodb:DeleteItem
                  Resource:
                    - !Sub arn:aws:sqs:${AWS::Region}:${AWS::AccountId}:checkout-queue
                    - !Sub arn:aws:dynamodb:${AWS::Region}:${AWS::AccountId}:table/Orders
          Environment:
            Variables:
              QUEUE_NAME: "checkout-queue"
    ```
  ![CreateOrderTable](/images/1/19.png?width=90pc)

4. Thêm các thư mục và tệp source code cho các function. Cấu trúc thư mục như sau:
    ```
    fcj-book-shop-sam-ws6
    ├── fcj-book-shop
    │   ├── checkout_order
    │   │   └── checkout_order.py
    │   ├── order_management
    │   │   └── order_management.py
    │   ├── handle_order
    │   │   └── handle_order.py
    │   ├── delete_order
    │   │   └── delete_order.py
    │   ├── ....
    └── template.yaml
    ```
- Tạo thư mục tên **checkout_order** trong thư mục **fcj-book-shop-sam-ws6/fcj-book-shop**
- Tạo tệp **checkout_order.py** và sao chép đoạn code sau vào nó.
    ```
    import json
    import boto3
    import os

        
    def lambda_handler(event, context):
        client = boto3.client("sqs")
        sns = boto3.client('sns')
        queue_name = os.getenv("QUEUE_NAME")
        status = 200
        try:
            response = client.get_queue_url(
                QueueName=queue_name
            )
            
            send_response = client.send_message(
                QueueUrl=response['QueueUrl'], 
                MessageBody=event["body"]
            )
        except Exception as e:
            status = 400
        
        try:
            response1 = sns.publish(
                TopicArn=os.environ['SNS_ARN'],    
                Message="There is a new order. Please check it!",    
            )
        except Exception as e:
            status = 400
            print(e)

        return {
            'statusCode': status,
            'body': json.dumps(response["ResponseMetadata"]),
            'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
        }
    ```

- Tạo thư mục tên **order_management** trong thư mục **fcj-book-shop-sam-ws6/fcj-book-shop**
- Tạo 
 **order_management.py** và sao chép đoạn code sau vào nó.
    ```
    import boto3
    import json
    import os
    from boto3.dynamodb.types import TypeDeserializer

    # Create SQS client
    sqs_client = boto3.client('sqs')
    # Create DynamoDB client
    dynamodb_client = boto3.client('dynamodb')
    serializer = TypeDeserializer()


    def deserialize(data):
        if isinstance(data, list):
            return [deserialize(v) for v in data]

        if isinstance(data, dict):
            try:
                return serializer.deserialize(data)
            except TypeError:
                return {k: deserialize(v) for k, v in data.items()}
        else:
            return data


    def format_db_data(messages, db_data):
        if 'Items' in db_data:
            format_data = deserialize(db_data["Items"])
        price = 0
        for book_item in format_data:
            price = book_item['price']
            del book_item['price']
            del book_item['id']
        messages.append({
            "receiptHandle": "",
            "books": format_data,
            "price": price,
            "status": "Processed"
        })


    def get_order_from_dynamodb(messages):
        data = []
        i = 1
        while True:
            id = str(i)
            data = dynamodb_client.query(
                TableName="Orders", KeyConditionExpression="id = :id", ExpressionAttributeValues={":id": {"S": id}})
            if not data["Items"]:
                break
            format_db_data(messages, data)
            i += 1


    def get_order_from_sqs(messages):
        queue_name = os.getenv("QUEUE_NAME")
        queue = sqs_client.get_queue_url(QueueName=queue_name)
        queue_url = queue['QueueUrl']
        response = sqs_client.get_queue_attributes(
            QueueUrl=queue_url,
            AttributeNames=['ApproximateNumberOfMessages']
        )

        number_of_message = int(
            response['Attributes']['ApproximateNumberOfMessages'])
        print(number_of_message)
        i = 0
        while i < number_of_message:
            msg_list = sqs_client.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,
                WaitTimeSeconds=20,
                VisibilityTimeout=3
            )
            if 'Messages' in msg_list:
                for m in msg_list['Messages']:
                    print(json.loads(m["Body"]))
                    messages.append({
                        "receiptHandle": m["ReceiptHandle"],
                        "books": json.loads(m["Body"])['books'],
                        "price": json.loads(m["Body"])['price'],
                        "status": "Unprocessed"
                    })
                    i += 1


    def lambda_handler(event, context):
        messages = []

        get_order_from_dynamodb(messages)
        get_order_from_sqs(messages)
        print(messages)
        return{
            'statusCode': 200,
            'body': json.dumps(messages),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }

    ```
- Tạo thư mục tên **handle_order** trong thư mục **fcj-book-shop-sam-ws6/fcj-book-shop**
- Tạo 
 **handle_order.py** và sao chép đoạn code sau vào nó.
    ```
    import boto3
    import json
    import os

    dynamodb_client = boto3.resource('dynamodb')
    table = dynamodb_client.Table('Orders')
    sqs_client = boto3.client('sqs')


    def lambda_handler(event, context):
        order_item = json.loads(event["body"])
        products_infor = order_item['books']
        print(order_item)
        for book_item in products_infor:
            print(book_item)
            data = {
                "id": str(order_item['id']),
                "book_id": book_item['id'],
                "name": book_item['name'],
                "qty": str(book_item['qty']),
                "price": str(order_item['price'])
            }
            print(data)
            table.put_item(Item=data)

        queue_name = os.getenv("QUEUE_NAME")
        queue = sqs_client.get_queue_url(QueueName=queue_name)
        queue_url = queue['QueueUrl']
        response = sqs_client.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=order_item['receiptHandle']
        )

        response = {
            'statusCode': 200,
            'body': 'successfully handle order!',
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,X-Access-Token, XKey, Authorization",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS"
            },
        }
        return response

    ```
- Tạo thư mục tên **delete_order** trong thư mục **fcj-book-shop-sam-ws6/fcj-book-shop**
- Tạo tệp **delete_order.py** và sao chép đoạn code sau vào nó.
    ```
    import boto3
    import json
    import os

    dynamodb_client = boto3.client('dynamodb')
    sqs_client = boto3.client('sqs')


    def lambda_handler(event, context):
        order_item = json.loads(event["body"])
        if order_item['receiptHandle']:
            queue_name = os.getenv("QUEUE_NAME")
            queue = sqs_client.get_queue_url(QueueName=queue_name)
            queue_url = queue['QueueUrl']
            response = sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=order_item['receiptHandle']
            )

        response = {
            'statusCode': 200,
            'body': 'successfully handle order!',
            'headers': {
                'Content-Type': 'application/json',
                "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method,X-Access-Token, XKey, Authorization",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,OPTIONS"
            },
        }
        
        return response
    ```
5. Chạy các lệnh dưới đây
    ```
    sam build
    sam deploy --guided
    ```
    ![CreateOrderTable](/images/1/21.png?width=90pc)
6. Mở bảng điều khiển của [AWS Lambda](https://ap-southeast-1.console.aws.amazon.com/lambda/home?region=ap-southeast-1#/functions) để kiểm tra các function.
    ![CreateOrderTable](/images/1/22.png?width=90pc)