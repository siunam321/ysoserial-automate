# ysoserial automate

## Background

A python script that generates and send ysoserial tool's payload, which is an Java serialized object gadget chains.

> This python3 script is from my PortSwigger Labs' Insecure Deserialization lab 5.
>  
> Writeup: [https://siunam321.github.io/ctf/portswigger-labs/Insecure-Deserialization/deserial-5/](https://siunam321.github.io/ctf/portswigger-labs/Insecure-Deserialization/deserial-5/)

## Installation

```bash
wget https://raw.githubusercontent.com/siunam321/CVE-1999-1053-PoC/main/ysoserial-automate.py
```

## Usage

- `-j` or `--jar` to supply the absolute path of the ysoserial Jar file (Required)
- `-p` or `--payload` to supply the ysoserial payload (Required)
- `-c` or `--command` to supply the command you wanna execute (Required)
- `-u` or `--url` to supply the full URL of the target website

## Screenshots

![](https://github.com/siunam321/ysoserial-automate/blob/main/images/poc1.png)

![](https://github.com/siunam321/ysoserial-automate/blob/main/images/poc2.png)

![](https://github.com/siunam321/ysoserial-automate/blob/main/images/poc3.png)

![](https://github.com/siunam321/ysoserial-automate/blob/main/images/poc4.png)

![](https://github.com/siunam321/ysoserial-automate/blob/main/images/poc5.png)