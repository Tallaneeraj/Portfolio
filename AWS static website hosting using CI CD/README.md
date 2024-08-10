
# AWS Cloud-based Web Application

## Overview
This project is a fully functional web application designed to demonstrate the integration of front-end technologies with AWS cloud services. The application showcases the use of HTML, CSS, and JavaScript for the frontend, and leverages several AWS services such as S3, CloudFront, DynamoDB, and Lambda for backend operations. GitHub Actions is utilized for continuous integration and continuous deployment (CI/CD).

## Features
- **Static Website**: Built using HTML, CSS, and JavaScript.
- **File Storage**: AWS S3 is used to store and serve static assets such as images, stylesheets, and scripts.
- **Content Delivery**: CloudFront is used for distributing the web application with low latency and high transfer speeds.
- **Data Storage**: DynamoDB is used to store application data in a NoSQL database.
- **Serverless Functions**: AWS Lambda functions are employed to interact with DynamoDB for retrieving and updating data.
- **CI/CD Pipeline**: GitHub Actions is configured to automate testing, building, and deployment of the application.

## Architecture
1. **Frontend**: The user interface is built using HTML, CSS, and JavaScript.
2. **AWS S3**: Stores all static files of the website.
3. **AWS CloudFront**: Distributes the content globally with low latency.
4. **AWS DynamoDB**: Acts as the database for storing and retrieving application data.
5. **AWS Lambda**: Serverless functions to handle backend logic and communicate with DynamoDB.
6. **GitHub Actions**: Automates the CI/CD pipeline to ensure the code is tested and deployed seamlessly.


