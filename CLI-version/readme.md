# Image to Text using Amazon Rekognition
Use [AWS Rekognition](https://aws.amazon.com/rekognition/) to extract text from images, parse output using [jq](https://stedolan.github.io/jq/) and combine text output into a CSV file. Using the [AWS CLI](https://aws.amazon.com/cli/). 

These commands were run in a VSCode powershell terminal.

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
```ps
#initialize csv file
echo '"Question","Option 1","Option 2","Option 3","Option 4","Option 5","Correct Answer","Time","Image Link"' > output.csv

#Windows: escape the double quote in a windows powershell terminal (VSCode)
$result = aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" | jq '.TextDetections | map(select(.Type ==\"LINE\").DetectedText) | join(\" \")' 

#format extracted text to csv format
$result = "$result,,,,,,,"

#save to file
echo $result >> output.csv



#unix: no escape needed
#aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" | jq '.TextDetections | map(select(.Type =="LINE").DetectedText) | join(" ")' >> output.csv

```

5. Open the file with excel. In the `Data` menu, choose `From Text/CSV` and choose delimiter `comma` and `use first row as header`. 


## References: 
- Researching JQ combine results: https://stedolan.github.io/jq/manual/
- https://programminghistorian.org/en/lessons/json-and-jq
- https://unix.stackexchange.com/questions/610461/how-to-merge-arrays-from-multiple-json-files-with-jq
- https://stackoverflow.com/questions/42011086/merge-arrays-of-json
- JQ join: https://unix.stackexchange.com/questions/312697/merge-jq-output-into-a-comma-separated-string