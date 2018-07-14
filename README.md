Used to forward requests from Slack bot to our application server, piercing our VPC.

See Makefile for options.

To deploy...
- run `make` to deploy
- you need to manually put the lambda function into the Tracebacks VPC and give it the 'talk to nodes' security group
- provide the env variable TODO
