# Image to Text using Amazon Rekognition
Serverless application using [AWS Rekognition](https://aws.amazon.com/rekognition/) to extract text from images in an S3 bucket and saving them in a DynamoDB database. The text is later compiled into a single CSV file. 

There is also an alternate solution using the AWS CLI and JQ. See the [CLI-version](CLI-version/readme.md) for that solution. 

## Process
process: end user upload images to s3 > s3 lambda trigger > call rekognition for each image > store text in ddb > compile into csv > notify requester

## Open issues
- how to combine all text into csv. table scan save
- how to know all done processing? step fxn? potential process flow: drop files