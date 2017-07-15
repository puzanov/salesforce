#! /usr/local/bin/python3
import os

from simple_salesforce import Salesforce
from time import sleep
from creds import *

# salesforce user account setup - actual vars are in creds.py
# salesforceusername = '';
# salesforcepassword = '';
# salesforcesecuritytoken = '';

# establish a connection to salesforce
sf = Salesforce(
 instance_url='https://cs17.salesforce.com', \
 username=salesforceusername, \
 password=salesforcepassword, \
 security_token=salesforcesecuritytoken, \
 sandbox = True)

#this is internal ID of Zentist doctor object
REFERRING_OFFICE_ID = '006g000000EsD2MAAV'
contact_result = sf.Contact.create({
            'FirstName':'Bill',
            'LastName':'Vahidov',
            'Phone':'123',
            'Email':'billyboy@chupakabra.net',
            'Lead_Type__c':'Community',
            'LeadSource':'Communities Portal'})

print(contact_result)

if contact_result['success']:
    scheduler_result = sf.Scheduler__c.create(
        {
            'Contact_ID__c':contact_result['id'],
            'Name__c':'Bill Vahidov',
            'Scan_Date_Time__c':'07-17-2017 3:30PM',
            'Scan_Office__c':'Oakland',
            'Account_ID__c':None,
            'Referring_Office_Scheduler__c':'Zentist',
            'Referring_Doctor_Scheduler__c':'API',
            'isCommunity__c':True})

print(scheduler_result)

#result = sf.query("""SELECT Id, Patient_Name__c, Stage__c, Account_ID__c, Name__c, Scan_Date_Time__c, Scan_Office__c, Referring_Office_Scheduler__c FROM Scheduler__c WHERE Scan_Office__c = 'San Jose' and Scan_Date_time__c like '07-11-2017%' ORDER BY Scan_Date_Time__c""")

# loop through the list of results
#for e in result["records"]:
    # print(e)
    # enforce a 7 second delay between each request to get round api restrictions when loading lots
    # sleep(0.7)
