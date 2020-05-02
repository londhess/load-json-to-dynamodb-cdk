
# Welcome to s3 to dynamodb CDK Python project!

The main funcationlity of this project is whenever json objects uploaded to aws s3 buckets, it will trigger the event and lambda function. Lambda functions reads the content from uploaded object and add entry to dynamodb table.

This will create the s3, lambda and dynamodb resources along with required policies and permissions.


To manually create a virtualenv on MacOS and Linux:

```
$ python -m venv .env
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .env/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .env\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

Deploy the code

```
$ cdk deploy
```

Destroy/ Cleanup resources 

```
$ cdk destroy
```

You need to manually delete s3 and dynamodb table. rest all the resources has been clean up by above command.