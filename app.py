#!/usr/bin/env python3

from aws_cdk import core

from load_json_to_dynamodb_cdk.load_json_to_dynamodb_cdk_stack import LoadJsonToDynamodbCdkStack


app = core.App()
LoadJsonToDynamodbCdkStack(app, "load-json-to-dynamodb-cdk",env={'region': 'ap-south-1'})

app.synth()
