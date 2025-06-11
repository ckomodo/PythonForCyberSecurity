#!/usr/bin/env python3
# Script that scans files using VirusTotal
# https://developers.virustotal.com/reference
# By CW

#import python modules
import requests
import configparser
import hashlib


#function to get API key
def get_api_key(key_name):
    config = configparser.ConfigParser()
    config.read("c:\\users\\student\\secrets.ini")
    api_key = config ["APIKeys"][key_name]
    return api_key
    

#function to get VT report

#function to submit file to be scanned

#main body of code - part of it from virus total

#Get API key
token = get_api_key("VirusTotal")

#Prompt user for the file/file pathway
target_file = input("File to scan ")

#Get file hash


#Get VT report

#IF report is not there, upload VT file
    #wait
    #get VT report
    