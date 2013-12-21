ec2-checkpoint
==============
EC2 checkpoint script to modify security groups.
```
usage:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  'authorize' or 'revoke'
  -r REGION, --region REGION
                        AWS region to use, e.g. 'us-west-1'
  --sg SG               Security group name to modify, e.g. 'default'
  --protocol PROTOCOL   Protocol type, e.g. 'tcp'
  --port PORT           Port to authorize/revoke, e.g. '22'
  --ip IP               IP to authorize/revoke, e.g. '127.0.0.1'
  --accessKey ACCESSKEY
                        AWS access key if not specified in ~/.boto [optional]
  --secretKey SECRETKEY
                        AWS secret key if not specified in ~/.boto [optional]
  --log LOG             Logging level - DEBUG|INFO|WARNING|ERROR|CRITICAL
                        [optional]
```
