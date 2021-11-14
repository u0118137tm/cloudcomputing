aws ec2 run-instances --image-id ami-09b49c48928db765c --count 1 --instance-type t2.micro --key-name default-ireland --security-groups default --user-data file://script.txt
pause