#!/usr/bin/env python3

#########################################################
# This is the database processing file. (aka. Models)
# It contains the DB connections, queries and functions.
# Uses principles of Models, Views, Controllers (MVC).
#########################################################

# Import modules required for app
import os
import boto3
import json
from werkzeug.utils import secure_filename
from config import ecs_test_drive

# Check if running in Pivotal Web Services with MongoDB service bound
#if 'VCAP_SERVICES' in os.environ:
#    VCAP_SERVICES = json.loads(os.environ['VCAP_SERVICES'])
#    MONGOCRED = VCAP_SERVICES["mlab"][0]["credentials"]
#    client = MongoClient(MONGOCRED["uri"])
#    DB_NAME = str(MONGOCRED["uri"].split("/")[-1])

# Remove any existing documents in photos collection
# db.photos.delete_many({})   # Comment this line if you don't want to remove documents each time you start the app

def upload_file(filename):
    # Get ECS credentials from external config file
    ecs_endpoint_url = ecs_test_drive['ecs_endpoint_url']
    ecs_access_key_id = ecs_test_drive['ecs_access_key_id']
    ecs_secret_key = ecs_test_drive['ecs_secret_key']
    ecs_bucket_name = ecs_test_drive['ecs_bucket_name']

    # Open a session with ECS using the S3 API
    session = boto3.resource(service_name='s3', aws_access_key_id=ecs_access_key_id, aws_secret_access_key=ecs_secret_key, endpoint_url=ecs_endpoint_url)

    ## Upload the original image to ECS
    session.Object(ecs_bucket_name, filename).put(Body=open(filename, 'rb'), ACL='public-read')
