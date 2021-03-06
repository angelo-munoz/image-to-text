# Image to Text using Amazon Rekognition
Serverless application using [AWS Rekognition](https://aws.amazon.com/rekognition/) to extract text from images in an [S3](https://aws.amazon.com/s3/) bucket and saving them in a [DynamoDB](https://aws.amazon.com/dynamodb) database. The text is later compiled into a single CSV file. 
Considering adding [terraform](https://www.terraform.io/) to the solution. 
There is also an alternate solution using the [AWS CLI](https://aws.amazon.com/cli/) and [JQ](https://stedolan.github.io/jq/). See the [CLI-version](CLI-version/readme.md) for that solution. 

Update: due to the 100 character extraction limit in Rekognition, I'll switch to another solution, perhaps an OCR API like [OCR space](https://ocr.space/ocrapi).
## Process
- option 1: end user upload images to s3 > s3 lambda trigger > call rekognition for each image > store text in ddb > compile into csv > notify requester
- option 2: on each lambda, get s3 item count, on the last one, notify downstream to compile all into one doc. Do we remove file or move to a subfolder to ensure an accurate count?

## OCR sample commend
```sh
#convert image to text
curl -H "apikey:helloworld" -F "file=@images/abcya.png" -F "OCREngine=2" https://api.ocr.space/parse/image

#convert, parse w JQ and send to text file output
curl -H "apikey:helloworld" -F "file=@images/scans/abcya.png" -F "OCREngine=2" https://api.ocr.space/parse/image | jq .ParsedResults[0].ParsedText >> extractedText.txt
```


## Open issues
- how to combine all text into csv. table scan save
- how to know all done processing? step fxn? potential process flow: drop files. possibly ddb streams does table scan and compiles into 1 file in s3? but how to notify when the process is complete? 
- how to extract tags and other meta data? Each question will be a diff type. Should this be done manually post doc generation? Or try to capture on image file naming? 
