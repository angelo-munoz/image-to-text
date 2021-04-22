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

aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" | jq '.TextDetections[].DetectedText' #works! 
#.TextDetections[] | select(.Type =="LINE").DetectedText #works in jqtester
echo "$json" | jq '.TextDetections[].DetectedText'
```

Open issues: 
- researching JQ combine results: https://stedolan.github.io/jq/manual/
- https://programminghistorian.org/en/lessons/json-and-jq
- https://unix.stackexchange.com/questions/610461/how-to-merge-arrays-from-multiple-json-files-with-jq
- https://stackoverflow.com/questions/42011086/merge-arrays-of-json

```js
//TextDetections[].DetectedText
{
    "TextDetections": [
        {
            "DetectedText": "Amazon Rekognition text detection can detect text in images and videos. It can then convert the detected text into machine-readable text.",
            "Type": "LINE",
            "Id": 0,
            "Confidence": 98.95492553710938,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.971509575843811,
                    "Height": 0.0804489329457283,
                    "Left": 0.006743445992469788,
                    "Top": 0.04250591993331909
                },
                "Polygon": [
                    {
                        "X": 0.006743445992469788,
                        "Y": 0.04455532506108284
                    },
                    {
                        "X": 0.9782436490058899,
                        "Y": 0.04250591993331909
                    },
                    {
                        "X": 0.9782530069351196,
                        "Y": 0.12090544402599335
                    },
                    {
                        "X": 0.006752857938408852,
                        "Y": 0.1229548528790474
                    }
                ]
            }
        },
        {
            "DetectedText": "You can Use the machine-readable text detection in images to implement solutions such as:",
            "Type": "LINE",
            "Id": 1,
            "Confidence": 98.58275604248047,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.6436870694160461,
                    "Height": 0.08108685165643692,
                    "Left": 0.005988156422972679,
                    "Top": 0.140477254986763
                },
                "Polygon": [
                    {
                        "X": 0.005988156422972679,
                        "Y": 0.14269687235355377
                    },
                    {
                        "X": 0.6496597528457642,
                        "Y": 0.140477254986763
                    },
                    {
                        "X": 0.6496752500534058,
                        "Y": 0.21934449672698975
                    },
                    {
                        "X": 0.006003634072840214,
                        "Y": 0.22156411409378052
                    }
                ]
            }
        },
        {
            "DetectedText": "Visual search. An example is retrieving and displaying images that contain the same text.",
            "Type": "LINE",
            "Id": 2,
            "Confidence": 98.81427001953125,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.6264359951019287,
                    "Height": 0.08459045737981796,
                    "Left": 0.03224177658557892,
                    "Top": 0.3036935329437256
                },
                "Polygon": [
                    {
                        "X": 0.03225833177566528,
                        "Y": 0.3036935329437256
                    },
                    {
                        "X": 0.6586777567863464,
                        "Y": 0.3059057593345642
                    },
                    {
                        "X": 0.6586611866950989,
                        "Y": 0.38828399777412415
                    },
                    {
                        "X": 0.03224177658557892,
                        "Y": 0.3860717713832855
                    }
                ]
            }
        },
        {
            "DetectedText": "Content",
            "Type": "LINE",
            "Id": 3,
            "Confidence": 96.96983337402344,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.06376594305038452,
                    "Height": 0.05974842607975006,
                    "Left": 0.03300825133919716,
                    "Top": 0.44025155901908875
                },
                "Polygon": [
                    {
                        "X": 0.03300825133919716,
                        "Y": 0.44025155901908875
                    },
                    {
                        "X": 0.09677419066429138,
                        "Y": 0.44025155901908875
                    },
                    {
                        "X": 0.09677419066429138,
                        "Y": 0.5
                    },
                    {
                        "X": 0.03300825133919716,
                        "Y": 0.5
                    }
                ]
            }
        },
        {
            "DetectedText": "Amazon",
            "Type": "WORD",
            "Id": 4,
            "ParentId": 0,
            "Confidence": 99.4904556274414,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.06151537969708443,
                    "Height": 0.0628930851817131,
                    "Left": 0.006751687731593847,
                    "Top": 0.050314463675022125
                },
                "Polygon": [
                    {
                        "X": 0.006751687731593847,
                        "Y": 0.050314463675022125
                    },
                    {
                        "X": 0.06826706975698471,
                        "Y": 0.050314463675022125
                    },
                    {
                        "X": 0.06826706975698471,
                        "Y": 0.11320754885673523
                    },
                    {
                        "X": 0.006751687731593847,
                        "Y": 0.11320754885673523
                    }
                ]
            }
        },
        {
            "DetectedText": "Rekognition",
            "Type": "WORD",
            "Id": 5,
            "ParentId": 0,
            "Confidence": 99.61886596679688,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.08627156913280487,
                    "Height": 0.07547169923782349,
                    "Left": 0.06901725381612778,
                    "Top": 0.04716981202363968
                },
                "Polygon": [
                    {
                        "X": 0.06901725381612778,
                        "Y": 0.04716981202363968
                    },
                    {
                        "X": 0.15528881549835205,
                        "Y": 0.04716981202363968
                    },
                    {
                        "X": 0.15528881549835205,
                        "Y": 0.12264151126146317
                    },
                    {
                        "X": 0.06901725381612778,
                        "Y": 0.12264151126146317
                    }
                ]
            }
        },
        {
            "DetectedText": "text",
            "Type": "WORD",
            "Id": 6,
            "ParentId": 0,
            "Confidence": 98.66462707519531,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.030757689848542213,
                    "Height": 0.05974842607975006,
                    "Left": 0.15753938257694244,
                    "Top": 0.050314463675022125
                },
                "Polygon": [
                    {
                        "X": 0.15753938257694244,
                        "Y": 0.050314463675022125
                    },
                    {
                        "X": 0.1882970780134201,
                        "Y": 0.050314463675022125
                    },
                    {
                        "X": 0.1882970780134201,
                        "Y": 0.11006288975477219
                    },
                    {
                        "X": 0.15753938257694244,
                        "Y": 0.11006288975477219
                    }
                ]
            }
        },
        {
            "DetectedText": "detection",
            "Type": "WORD",
            "Id": 7,
            "ParentId": 0,
            "Confidence": 99.54156494140625,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.06908885389566422,
                    "Height": 0.069182388484478,
                    "Left": 0.18904726207256317,
                    "Top": 0.04716981202363968
                },
                "Polygon": [
                    {
                        "X": 0.18904726207256317,
                        "Y": 0.04716981202363968
                    },
                    {
                        "X": 0.25806450843811035,
                        "Y": 0.044025156646966934
                    },
                    {
                        "X": 0.25806450843811035,
                        "Y": 0.11320754885673523
                    },
                    {
                        "X": 0.18904726207256317,
                        "Y": 0.11635220050811768
                    }
                ]
            }
        },
        {
            "DetectedText": "can",
            "Type": "WORD",
            "Id": 8,
            "ParentId": 0,
            "Confidence": 98.8798828125,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.027756938710808754,
                    "Height": 0.056603774428367615,
                    "Left": 0.2595648765563965,
                    "Top": 0.056603774428367615
                },
                "Polygon": [
                    {
                        "X": 0.2595648765563965,
                        "Y": 0.056603774428367615
                    },
                    {
                        "X": 0.2873218357563019,
                        "Y": 0.056603774428367615
                    },
                    {
                        "X": 0.2873218357563019,
                        "Y": 0.11320754885673523
                    },
                    {
                        "X": 0.2595648765563965,
                        "Y": 0.11320754885673523
                    }
                ]
            }
        {
            "DetectedText": "detect",
            "Type": "WORD",
            "Id": 9,
            "ParentId": 0,
            "Confidence": 99.44644165039062,
            "Geometry": {
                "BoundingBox": {
                    "Width": 0.046617813408374786,
                    "Height": 0.056603774428367615,
                    "Left": 0.288822203874588,
                    "Top": 0.05345911905169487
                },
                "Polygon": [
                    {
                        "X": 0.288822203874588,
                        "Y": 0.05345911905169487
                    },
                    {
                        "X": 0.33533382415771484,
                        "Y": 0.050314463675022125
                    },
```

```
aws rekognition detect-text --image "S3Object={Bucket=photo-collection,Name=photo.jpg}" --region us-east-1
```
