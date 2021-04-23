# Image to Text using Amazon Rekognition
Use [AWS Rekognition](https://aws.amazon.com/rekognition/) to extract text from images, parse output using [jq](https://stedolan.github.io/jq/) and combine text output into a CSV file. Using the [AWS CLI](https://aws.amazon.com/cli/).

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

#Windows: escape the double quote in a windows powershell terminal (VSCode)
aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" | jq '.TextDetections | map(select(.Type ==\"LINE\").DetectedText) | join(\" \")'

#unix: no escape needed
aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" | jq '.TextDetections | map(select(.Type =="LINE").DetectedText) | join(" ")'

```

## References: 
- Researching JQ combine results: https://stedolan.github.io/jq/manual/
- https://programminghistorian.org/en/lessons/json-and-jq
- https://unix.stackexchange.com/questions/610461/how-to-merge-arrays-from-multiple-json-files-with-jq
- https://stackoverflow.com/questions/42011086/merge-arrays-of-json
- JQ join: https://unix.stackexchange.com/questions/312697/merge-jq-output-into-a-comma-separated-string