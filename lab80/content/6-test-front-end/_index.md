---
title : "Test APIs with front-end"
date :  "`r Sys.Date()`" 
weight : 6
chapter : false
pre : " <b> 6. </b> "
---
After testing that the APIs work properly with Postman, we will test the APIs that are called with the front-end built from part 2.
1. Open **config.js** in **fcj-serverless-frontend** folder that downloaded from part 2
- Change value of **APP_API_URL** with your URL:

![CreateRestAPI](/images/6-test-front-end/6-test-front-end-0.png?featherlight=false&width=90pc)

![UpdateURL](/images/6-test-front-end/6-test-front-end-1.png?featherlight=false&width=90pc)

2. Open **App.js** in **fcj-serverless-frontend/src/**, change value of **isAdmin** with **true**
3. Run the command lines under here:
```
yarn build
aws s3 cp build s3://fcj-book-store --recursive
```
4. Paste the endpoint of S3 static web into your browser. The app already shows the book information, but still no pictures because we haven't uploaded the pictures yet.

![WebApp](/images/6-test-front-end/6-test-front-end-2.png?featherlight=false&width=90pc)

So the listing API is working properly

5. Test writing API
- Click **Management** tab
- Click **Update**

![WebApp](/images/6-test-front-end/6-test-front-end-3.png?featherlight=false&width=90pc)

- Edit whatever you want except **id**
- Click **Choose image**
- Upload the below image to the bucket:
{{%attachments title="Image" pattern=".*\.(jpeg)$"/%}}
- Click **Update**

![WebApp](/images/6-test-front-end/6-test-front-end-4.png?featherlight=false&width=90pc)

- Click **OK**

![WebApp](/images/6-test-front-end/6-test-front-end-5.png?featherlight=false&width=90pc)

- Image and information updated

![WebApp](/images/6-test-front-end/6-test-front-end-6.png?featherlight=false&width=90pc)

- Click on the **Create new book** tab to write new data to the database
- Enter id with `5`
- Enter name: `Amazon Web Services in Action`
- Enter the author: `Andreas Wittig`
- Enter category: `IT`
- Enter price: `59.99`
- Enter a description: `Amazon Web Services in Action, Second Edition is a comprehensive introduction to computing, storing, and networking in the AWS cloud. You'll find clear, relevant coverage of all the essential AWS services you to know, emphasizing best practices for security, high availability, and scalability.`

{{%attachments title="Image" pattern=".*\.(jpg)$"/%}}

- Press the **Choose File** button to upload the image
- Press the **Create** button

![WebApp](/images/6-test-front-end/6-test-front-end-7.png?featherlight=false&width=90pc)

- Click **OK**

![WebApp](/images/6-test-front-end/6-test-front-end-8.png?featherlight=false&width=90pc)

- Display newly created information

![WebApp](/images/6-test-front-end/6-test-front-end-9.png?featherlight=false&width=90pc)

6. Test the deleting API
- Click **Management** tab
- Click **Update**

![WebApp](/images/6-test-front-end/6-test-front-end-10.png?featherlight=false&width=90pc)

- Click **Delete**

![WebApp](/images/6-test-front-end/6-test-front-end-11.png?featherlight=false&width=90pc)

- Click **OK** to confirm delete

![WebApp](/images/6-test-front-end/6-test-front-end-12.png?featherlight=false&width=90pc)

- Click **OK**

![WebApp](/images/6-test-front-end/6-test-front-end-13.png?featherlight=false&width=90pc)

- View results after deleting: no appearing book information

![WebApp](/images/6-test-front-end/6-test-front-end-14.png?featherlight=false&width=90pc)

We have finished building a simple SAM-based web application following the serverless model.