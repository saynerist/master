__author__ = 'mranjan'

import requests
import json
import configparser
config=configparser.RawConfigParser()
config.read('file.properties')
IP=(config.get('LoginSection','IP'))
PORT=(config.get('LoginSection','PORT'))
sessions=requests.session()
url='http://'+IP+':'+PORT+'/bedrock-app/services/rest/login'
payload={"username":"admin","password":"admin","permissionNeeded":"true"}
headers = {'Content-type': 'application/json'}
response=sessions.post(url,json=payload)

#cookie=response.headers.get('Set-Cookie')
#print(cookie)


def CreateConnection(sessions):
    DB_PORT=(config.get('DatabaseProperties','databasePort'))
    DB_NAME=(config.get('DatabaseProperties','databaseName'))
    createDatabaseConUrl='http://'+IP+':'+PORT+'/bedrock-app/services/rest/ingestion/filesystems/internal/5/connections'
    databaseConJson={"connectionInstanceId":0,"connectionInstanceName":"MYSQLCon","description":"","fileSystemUri":"jdbc:mysql://"+IP+":"+DB_PORT+"/"+DB_NAME+"","fileSystemProperties":[{"connectionPropertyId":0,"fileSystemPropertyKey":"","fileSystemPropertyValue":""}],"dbType":"MYSQL","dbVersion":"","driverName":"com.mysql.jdbc.Driver","schemaName":"","leverageUsernamePassword":"true","userName":"bedrockdba","userPassword":"bedrockdba"}
    response=sessions.post(createDatabaseConUrl,json=databaseConJson)
    print(response.text)


CreateConnection(sessions)