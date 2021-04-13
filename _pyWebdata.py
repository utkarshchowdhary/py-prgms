## Regular Expressions ##
# In computing, a regular expression also referred to as "regex" or "regexp", provides a concise and flexible
# means for matching strings of text such as particular characters, words, or patterns of characters.

# Before you can use regular expressions in your program, you must import the library using "import re"
# You can use re.search() to see if a string matches a regular expression
# Returns True/False depending on whether the string matches the regular expression

# You can use re.findall() to extract portions of a string that match your regular expression

# eg. ^X.*:
# X-Sieve:
# X-DSPAM-Result:
# X-DSPAM-Confidence:
# X-Content-Type-Message-Body:

# eg. ^X-\S+:

# ^	 Matches the beginning of a line
# $	 Matches the end of the line
# .	 Matches any character
# \s Matches whitespace
# \S Matches any non-whitespace character
# *	 Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# +	 Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou]  Matches a single character in the listed set
# [^XYZ]   Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# (	Indicates where string extraction is to start
# )	Indicates where string extraction is to end
"""
import re

x = "My 2 favorite numbers are 21 and 45"
y = re.findall("[0-9]+", x)
print(y)  ## ['2', '21', '45']

y = re.findall("[AEIOU]+", x)
print(y)  ## []
"""
# The repeat characters (* and +) push outwards in both directions (greedy) to match the largest possible string
r"""
import re

x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)  ## ['From: Using the :']

y = re.findall("^F.+?:", x)  ## ['From:']
print(y)

x = "From stephen.marquard@uct.ac.az Sat Jan  5 09:14:16 2008"
y = re.findall(r"\S+@\S+", x)
print(y)  ## ['stephen.marquard@uct.ac.az']

# Parentheses are not part of the match - but they tell where to start and stop what string to extract
y = re.findall(r"^From (\S+@\S+)", x)
print(y)  ## ['stephen.marquard@uct.ac.az']

y = re.findall(r"@([^ ]*)", x)
y = re.findall(r"^From .*@([^ ]*)", x)
print(y)  ## ['uct.ac.az']

x = "X-DSPAM-Confidence: 0.8475"
y = re.findall(r"^X-DSPAM-Confidence: ([0-9.]+)", x)
print(y)  ## ['0.8475]

# If you want a special regular expression character to just behave normally
# you prefix it with blackslash '\'
x = "We just received $10.00 for cookies"
y = re.findall(r"\$[0-9.]+", x)
print(y)  ## ['$10.00']
"""
# The extend() extends the list by adding all items of a list (passed as an argument) to the end
"""
with open("regex_sum.txt", "r") as f:
    filedata = f.readlines()
lst = list()
# Reading Line by Line
for line in filedata:
    line = line.strip()
    numlst = re.findall(r"[0-9]+", line)
    if len(numlst) != 0:
        lst.extend(numlst)
lst = [int(i) for i in lst]
print(sum(lst))  ## 336025
"""
# Network Technology
# In computer network an internet socket or network socket is an endpoint of a bi-directional inter-process
# communication flow accross internet Protocol-based computer network, such as internet

# A port is an application-specfic or process-specific software communication endpoint
# It allows multiple networked applications to coexist on the same server

# Python has built-in support for TCP Sockets

# The encode() method encodes the string, using the specified encoding. If no encoding is specified,
# UTF-8 will be used
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80))  # mysock.connect(("host", port))
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()
"""
# HTTP
# The Hyper Text Transfer Protocol is the set of rules to allow browsers to retrive
# web documents from the server over the internet

# ASCII American Standard Code for Information Interchange
# The ord() function tells us the numeric value of a simple ASCII character
"""
print(ord("H"))
print(ord("\n"))
"""
# In Python 3, all strings internally are UNICODE
# When we talk to a network resource using sockets or talk to a database we have to encode and decode data
# (usually to UTF-8)

# When we talk to an external resource like a network socket we send bytes, so we need to encode
# Python 3 strings into a given character encoding
# When we read data from an external resource, we must decode it based on the character set so it is properly
# represented inPython 3 as a string

# Urllib module is the URL handling module for python. It is used to fetch URLs (Uniform Resource Locators)
"""
from urllib.request import urlopen

fhand = urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())
"""
# Web Scraping
# When a program or script pretends to be a browser and retrives web pages, looks at those web pages, extract
# information, and then look at more web pages

# Beautiful Soup
# Beautiful Soup is a Python library for getting data out of HTML, XML, and other markup languages
# Beautiful Soup helps you pull particular content from a webpage, remove the HTML markup, and
# save the information
# It is a tool for web scraping that helps you clean up and parse the documents
# you have pulled down from the web
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url- ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrive all the anchor tags
tags = soup("a")
for tag in tags:
    print("TAG:", tag)
    print("URL:", tag.get("href", None))
    print("Contents:", tag.contents[0])
    print("Attrs:", tag.attrs)
"""
# Parsing XML
'''
import xml.etree.ElementTree as ET

data = """<person>
    <name>Jhon Doe</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
    </person>"""
    
data2 = """<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Jhon Doe</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>June</name>
        </user>
    </users>
</stuff>"""
tree = ET.fromstring(data)
print("Name: ", tree.find("name").text)
print("Attr: ", tree.find("email").get("hide"))
print()

stuff = ET.fromstring(data2)
lst = stuff.findall("users/user")
for item in lst:
    print("Name", item.find("name").text)
    print("Name", item.find("id").text)
    print("Name", item.get("x"))
    print()
'''
# Parsing JSON
# JSON represents data as nested "lists" and "dictionaries"
'''
import json

data = """{
    "name": "Jhon Doe",
    "phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
        },
    "email": {
        "hide": "yes"
    }
}"""
data2 = """[
    {
        "id": "001",
        "x": "2",
        "name": "Jhon Doe"
    } ,
    {
        "id": "002",
        "x": "7",
        "name": "June Summers"
    }
]"""
info = json.loads(data)
print("Name: ", info["name"])
print("Hide: ", info["email"]["hide"])
print()
stuff = json.loads(data2)
for item in stuff:
    print("Name: ", item["name"])
    print("Id: ", item["id"])
    print("Attribute: ", item["x"])
    print()
'''
