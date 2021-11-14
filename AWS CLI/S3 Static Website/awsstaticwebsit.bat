SET /P bucketname= Please enter bucket name:
CALL aws s3api create-bucket --bucket %bucketname% --region eu-west-1 --create-bucket-configuration LocationConstraint=eu-west-1
CALL aws s3 website s3://%bucketname%/ --index-document index.html --error-document error.html
CALL aws s3 cp index.html s3://%bucketname% --acl public-read
CALL aws s3 cp error.html s3://%bucketname% --acl public-read
CALL echo website url: http://%bucketname%.s3-website-eu-west-1.amazonaws.com
pause