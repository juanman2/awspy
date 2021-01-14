# awspy
A Python repository to access AWS APIs

## Prerequisites

* I highly recommend using venv, see (https://realpython.com/python-virtual-environments-a-primer/)
* Python 3.8.6. Other versions of Python 3 should work but have not been tested.
* AWS S3 account.  This is not designed as a generic S3 interface.

## References

* https://aws.amazon.com/sdk-for-python/

## Installation

Using Python 3.8.6, Boto3 1.16.54 for development.  

```
 pip3 install boto3
``` 

## AWS Credentials

Setup AWS credentials.  Download aws cli from:

https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html

```
 aws configure 
```
Alternatively the aws creds file can be setup by hand it has the following format. You can obtain your
access_key_id and secret from aws console. 

```
[default]
aws_access_key_id = 
aws_secret_access_key = 

```

## Setup Test Buckets

The following was my procedure for manual testing.  I used aws to create test buckets, then s3ls
was tested against those buckets.

```
aws s3 sync `pwd` s3://telleztec-fpl --region us-west-1
aws s3 sync `pwd` s3://telleztec-archive --region us-west-1
```
## Package Creation

The following program was used to create a package:

```
python3 setup.py sdist bdist_wheel 
```

## Usage

The tool has three commands,  space, files and buckets. Space prints all the buckets with aggregate
usage in b, kb, mb, or gb, and it displays the last time it was touched.  Buckets displays the names 
of the buckets and the creation date.  files, lists all the files in each bucket. 

```
$ python s3ls.py --region 'us-west-1' --unit g space
telleztec-archive              2021-01-13 20:32:12+00:00 2021-01-14 02:50:16+00:00             0.00
telleztec-fpl                  2021-01-13 20:31:28+00:00 2021-01-13 23:57:37+00:00             0.05
```
Buckets:

```
$ python s3ls.py buckets
telleztec-archive                                        2021-01-13 20:32:12+00:00
telleztec-fpl                                            2021-01-13 20:31:28+00:00
```

List files:

```
python s3ls.py files
telleztec-archive                                        2021-01-14 00:00:40+00:00 1957.000000
telleztec-archive                                        2021-01-14 00:00:40+00:00 17541.000000
telleztec-archive                                        2021-01-14 00:00:40+00:00 2067.000000
telleztec-archive                                        2021-01-14 02:50:16+00:00   0.000000
telleztec-fpl                                            2021-01-13 23:55:41+00:00 40665.000000
telleztec-fpl                                            2021-01-13 23:55:41+00:00 92699.000000
...
```

## TODO

* Top - An option to get the top 10 space users in the buckets
* Unit Tests
