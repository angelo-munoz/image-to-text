# Image to Text using Amazon Rekognition
Serverless application using [AWS Rekognition](https://aws.amazon.com/rekognition/) to extract text from images in an S3 bucket and saving them in a DynamoDB database. The text is later compiled into a single CSV file. 

There is also an alternate solution using the AWS CLI and JQ. See the [CLI-version](CLI-version/readme.md) for that solution. 

## Process
- option 1: end user upload images to s3 > s3 lambda trigger > call rekognition for each image > store text in ddb > compile into csv > notify requester
- option 2: on each lambda, get s3 item count, on the last one, notify downstream to compile all into one doc. Do we remove file or move to a subfolder to ensure an accurate count?


## Open issues
- how to combine all text into csv. table scan save
- how to know all done processing? step fxn? potential process flow: drop files. possibly ddb streams does table scan and compiles into 1 file in s3? but how to notify when the process is complete? 
- how to extract tags and other meta data? Each question will be a diff type. Should this be done manually post doc generation? Or try to capture on image file naming? 
