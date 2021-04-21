# Image to Text using Amazon Rekognition
Use AWS Rekognition to extract text from images, parse output using jq and combine text output into a CSV file. Using the AWS CLI.

## Usage
1. Upload jpg files to your S3 bucket
2. Install the [jq](https://stedolan.github.io/jq/) tool
3. Run the following command using the AWS CLI
```sh
aws rekognition detect-text --image "S3Bucket={Bucket=bucketname,Name=input.jpg}" | jq 
```

Open Issues: 
- todo: complete command