# Image to Text using Amazon Rekognition
Use AWS Rekognition to extract text from images, parse output using jq and combine text output into a CSV file. Using the AWS CLI.

## Usage
1. Create a bucket to work with your application
```sh
aws s3 mb s3://angelo-itt
```
2. Upload a sample photo. I got this screenshot from AWS' website. Copyright AWS
```sh
aws s3 cp .\sample-image.png s3://angelo-itt/sample-image.png
```

3. Install the [jq](https://stedolan.github.io/jq/) tool
4. Run the following command using the AWS CLI to extract text to the command line
```sh
aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}"
```