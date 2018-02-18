# ConnectAWS
Publish message to AWS IoT from Pycom devices

## Environments
- macOS High Sierra Version 10.13.2
- LoPy1.0r (use os.uname() to check)

(sysname='LoPy', nodename='LoPy', release='1.9.2.b2', version='v1.8.6-796-g489fafa0 on 2017-10-15', machine='LoPy with ESP32', lorawan='1.0.0')

## Getting start with AWS IoT

- Create an AWS account and login to the console
- Services > AWS IoT

### Create a policy
- In the left navigation panel, choose Secure > Policies
- Click on the 'Create' button
- Name the policy. 

In the action part, choose"iot:Publish, iot:Subscribe, iot:Connect, iot:Receive". The Resource ARN part will then generated itself. Choose Allow on the Effect part.
- Click on the 'Create' button

### Register a device(Thing)

- In the left navigation panel, choose Manage > Things.
- Click on the 'Create' button
- Click on the'Create a single thing' button
- Name your thing, click on the 'Next' button
- Click on the 'Create certificate', download the generated certificate(xxx.cert.pem),your public key(xxx.public.key), private key(xxx.private.key) and a root CA(xxx.pem).
- Click on the 'Active' button and then click on the 'Attach a policy'
- Choose the policy you created
- Click on the 'Register Thing' button

## Setting up the LoPy
- Download the connectAWS folder, replace the root CA certificate, the clinet certificate and the private key in the cert folder
- Update the config.py with your WiFi configuration and your certificate path
- Connect your device via **ftp** and put main.py, config.py, AWSIoTPythonSDK folder and cert folder in the device flash
- Reboot your device

### Connect your device via FTP

1. FileZilla (could be downloaded from: https://filezilla-project.org)

- Connect your comupter wifi to the device hotpot, the username should be like 'lopy-wlan-xxxx', the password is 'www.pycom.io'
- Open FileZilla, click on the Site Manager
- Within the 'General' tab

  - fill '192.168.4.1' in the Host
  - select 'FTP - File Transfer Protocol' for the Protocol
  - select '**Only use plain FTP(insecure)**' for the Encryption
  - select 'Ask for password' for the Logon Type
  - User: 'micro', Password: 'python'

- Within the 'Transfer Settings' tab

  - select 'Passive' for the Transfer mode
  - tick the 'Limit number of simultaneous connections'
  - set the limitation as 1

- Click on the 'connect' button

Drag the file you need in our out to upload/download a file/folder.

## Troubleshooting

-  Error: "MemoryError: memory allocation failed, allocating 2048 bytes"

   Solution: Upgarde your firmware, reboot the device
   


