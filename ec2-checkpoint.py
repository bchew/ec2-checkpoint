#!/usr/bin/env python
import argparse, logging, boto.ec2

LOG_LEVEL = "INFO"
MODE_AUTHORIZE = "authorize"
MODE_REVOKE = "revoke"

def get_ec2_sg(conn, sg_name):
  sgs = conn.get_all_security_groups()
  sg = None
  for i in sgs:
    if i.name == sg_name:
      sg = i

  return sg

# parse args
parser = argparse.ArgumentParser(description="EC2 checkpoint script to modify security groups.")
parser.add_argument("-m", "--mode", help="'" + MODE_AUTHORIZE + "' or '" + MODE_REVOKE + "'")
parser.add_argument("-r", "--region", help="AWS region to use, e.g. 'us-west-1'")
parser.add_argument("--sg", help="Security group name to modify, e.g. 'default'")
parser.add_argument("--protocol", help="Protocol type, e.g. 'tcp'")
parser.add_argument("--port", help="Port to authorize/revoke, e.g. '22'")
parser.add_argument("--ip", help="IP to authorize/revoke, e.g. '127.0.0.1'")
parser.add_argument("--accessKey", help="AWS access key if not specified in ~/.boto [optional]")
parser.add_argument("--secretKey", help="AWS secret key if not specified in ~/.boto [optional]")
parser.add_argument("--log", help="Logging level - DEBUG|INFO|WARNING|ERROR|CRITICAL [optional]")
args = parser.parse_args()

# set log level
log_level = LOG_LEVEL
if args.log != None:
  log_level = args.log.upper()
logging.basicConfig(level=getattr(logging, log_level))

# instantiate connection
ec2_conn = boto.ec2.connect_to_region(args.region, aws_access_key_id=args.accessKey, aws_secret_access_key=args.secretKey)

# get sg
sg = get_ec2_sg(ec2_conn, args.sg)

if args.mode == MODE_AUTHORIZE:
  is_successful = sg.authorize(ip_protocol=args.protocol, 
                               from_port=int(args.port), 
                               to_port=int(args.port), 
                               cidr_ip=args.ip + "/32")
elif args.mode == MODE_REVOKE:
  is_successful = sg.revoke(ip_protocol=args.protocol, 
                         from_port=int(args.port), 
                         to_port=int(args.port), 
                         cidr_ip=args.ip + "/32")

if is_successful:
  logging.info(args.ip + " access to " + args.protocol + " " + args.port + " successfully " + args.mode + "d in " + args.sg + " security group!")
