#!/Users/juan/venv-3.8.6/bin/python3.8
# Copyright 2020 Telleztec.com, Juan Tellez, All Rights Reserved
#

import boto3
import datetime
import argparse

# convert bytes to kb, mb, and gb
def to_units(b, unit):
    if unit=='b':
        return b
    elif unit=='k':
        return round(b/1000, 2)
    elif unit=='m':
        return round(b/(1000*1000), 2)
    elif unit=='g':
        return round(b/(1000*1000*1000), 2)

# list_buckets prints the name of all buckets and the creation time 
def list_buckets(s3):
    for bucket in s3.buckets.all():
        d = bucket.creation_date
        print('{:<30s}{:>52s}'.format(
            bucket.name, d.isoformat(' ')))


# list_bucket_usage prints all buckets, date of the newst object and the total disk used        
def list_bucket_usage(s3, unit):
    totalSizeBytes = 0
    for bucket in s3.buckets.all():
        d = bucket.creation_date
        newest = datetime.datetime(datetime.MINYEAR,1,1,tzinfo=datetime.timezone.utc)
        for obj in bucket.objects.all():
            totalSizeBytes += obj.size
            if newest < obj.last_modified:
                newest = obj.last_modified
        print('{:<30s} {:s} {:s} {:>16.2f}'.format(bucket.name, d.isoformat(' '), newest.isoformat(' '),
                                                 to_units(totalSizeBytes, unit)))


# list_files prints all the objects in a bucket.        
def list_files(s3, unit):
    totalSizeBytes = 0
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
              d = obj.last_modified
              print('{:<30s}{:>52s} {:>10f}'.format(
                  bucket.name, d.isoformat(' '), to_units(obj.size, unit)))

def main():
    parser = argparse.ArgumentParser(prog='s3ls')
    parser.add_argument('--region', nargs=1, default='us-east-1', 
                        help='AWS region, e.g. us-east-1')
    parser.add_argument('--unit', choices=['b','k','m', 'g'], default='b',
                        help='Unit to display disk usage in: b, k, m or g')
    parser.add_argument('do', choices=['space', 'files', 'buckets'], default='space', 
                        help='Tells the tool what to do: Print space usage, list files or buckets')

    namespace = parser.parse_args()
    args = vars(namespace)

    region = args['region']
    unit = args['unit']
    
    session = boto3.session.Session()
    s3 = session.resource('s3', region[0])

    if args['do'] == 'space':
        list_bucket_usage(s3, unit)
    elif args['do'] == 'buckets':
        list_buckets(s3)
    elif args['do'] == 'files':
        list_files(s3, unit)

if __name__ == "__main__":
    main()
