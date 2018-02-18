This document is to help create a rule in AWS IoT to insert a received MQTT message to the DynamoDB

## Precondition
- Has an AWS account
- AWS IoT is able to receive MQTT message from device

## Getting start with DynamoDB and AWS IoT

### Create a table

- Longin AWS console, Service>DynamoDB
- In the left navigation panel, choose 'Dashboard'
- Click on the "Create table" button
- Named your table, "MyDevice" for example
- Choose the device ID as the 'Partition key', click the 'Add sort key', and use timestamp as the 'sort key'. 
Select 'Stirng' type for both of the keys
- Click on 'Create'
- Close the browser table and then login back the AWS console

### Create a rule

- Service>AWS IoT
- In the left navigation panel, choose 'Act', click on the 'Create' button
- Named the rule and write description
- In the 'Message source' part, type "*" in the 'Attribute' field; type the topic you used for publishing the mesage
in the 'Topic filter' filter
- Scroll down to the 'Set one or more actions' part, click on the 'add action button'. Select the 'Insert a message into
a DynamoDB table'. Click on 'Configure action'
- Select the table you created before for the Tbale name
- Type "${DeviceID}" for the Hash key value, and "${timestamp}" for the Range key value. The "${}" instruction takes the
value of the attribute, which you put in the braces, from MQTT message and write it into the partition key column 
in the DynamoDB table.
- For the 'IAM role name', click on 'Create a new role', named your role.
- Click on the 'Add action' button


For more information: https://docs.aws.amazon.com/iot/latest/developerguide/iot-ddb-rule.html
