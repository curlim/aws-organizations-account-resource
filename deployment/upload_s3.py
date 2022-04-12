import os
import boto3

BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

if __name__ == '__main__':
	ref = os.getenv("GITHUB_REF").split('/')
	if ref[1] != 'tags':
		print("non tagged ref")
		version = ref[2]
		env = "dev"
	else:
		print("tagged ref")
		version = ref[2]
		env = "release"
	print(f"upload version {version} s3")
	s3_client = boto3.client("s3")
	s3 = boto3.resource("s3")
	bucket = s3.Bucket(BUCKET_NAME)
	prefix = "aws-organizations-account-resource"
	key = f"{env}/{prefix}/{version}.zip"
	bucket.upload_file(
		Filename="proserve-organizations-account.zip",
		Key=key
	)

	bucket.upload_file(
		Filename="quickstart/cfn-provider-registration.yaml",
		Key=f"release/{prefix}/cfn-provider-registration.yaml"
	)

