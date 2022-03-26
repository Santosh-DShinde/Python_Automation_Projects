"""Automation script which accept file name. Extract all URL's from that file and connect to that URL's"""

from sys import *
import webbrowser
import re
from urllib.request import urlopen


def is_Connected():
    try:
        urlopen("https://www.google.com/", timeout=1)
        return True
    except Exception as err:
        return False


def Find(string):
    url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return url


def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str, new=2)


def main():
    print("Application name is : ", argv[0].split(".")[0])

    if len(argv) < 2 or len(argv) > 2:
        print("""Error : argument Error
For Help  : -h
For Usage : -u""")
        exit()

    if len(argv) == 2:
        if argv[1] == "-h" or argv[1] == "-H":
            print("""We are happy to help you. Please follow the below instructions for execution of script
This script accepts two command line arguments. first arguments is our application name and second file path
Expected syntax :  Application_Name.py  File_Path_Of_File_Which_Contains_URL's  """)
            exit()

        elif argv[1] == "-u" or argv[1] == "-U":
            print("Usage : The use of this script is open specified URL's by scripts automatically without human interaction")
            exit()

        try:
            if is_Connected():
                WebLauncher(argv[1]) # Call for WebLAuncher Function
            else:
                print("""Opps : Unable to connect to internet
Please check your internet connection""")

        except ValueError as Err:
            print("Error : Invalid datatype if input",Err)

        except Exception as obj:
            print("Error : Invalid input", obj)


if __name__ == "__main__":
    main()
