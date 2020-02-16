from get_chuck import getChuck
from genFileName import randomFileName
import subprocess
import json
import os
import sys

#cwd = os.getcwd()
#print(os.path.dirname(os.path.abspath(__file__)))
#os.chdir(os.path.dirname(os.path.abspath(__file__)))
#os.chdir()
#print(cwd)

"""
/etc/gitconfig

~/.gitconfig or ~/.config/git/config 

config file in the Git directory (that is, .git/config) o
"""

def validJson(data):
    try: 
        json_object = json.loads(data) 
    except ValueError as e: 
        return False
    return True

def getConfig():
    if os.path.exists("config.json"):
        fd = open("config.json","r")
        data = fd.read()
        if validJson(data):
            jdata = json.loads(data)
            return jdata
        else:
            print("Config file is missing or corrupt...")
            return None
    else:
        return None

def localGitUserExists():
    try:
        user_name = subprocess.check_output(["git", "config" , "user.name"])
    except subprocess.CalledProcessError as e:
        user_name = ''
        
    try:
        user_email = subprocess.check_output(["git", "config" , "user.email"])
    except subprocess.CalledProcessError as e:
        user_email = ''

    # print(f"{user_name} {user_email}\n")
    # print((len(user_name),len(user_email)))
    
    if len(user_name) > 0 and len(user_email) > 0:
        return True
    else:
        return False

def addGitUser():
    jdata = getConfig()
    if not 'username' in jdata or not 'useremail' in jdata:
        print("Config file missing or corrupted....")
        sys.exit()
    
    print(f"Adding user: {jdata['username']} and email: {jdata['useremail']} to config...")
    subprocess.call(["git", "config" , "user.name",jdata['username']])
    subprocess.call(["git", "config" , "user.email",jdata['useremail']])

def saveCode(path,fname,data):
    if os.path.isdir(path):
        f = open(os.path.join(path,fname),"w")
        f.write(data)
        f.close()
    return os.path.isfile(os.path.join(path,fname))


if __name__=="__main__":
    if not localGitUserExists():
        print("No git config info found ...")
        addGitUser()
        jdata = getConfig()
        if not 'username' in jdata or not 'useremail' in jdata:
            print("Config file missing or corrupted....")
            sys.exit()
        else:
            addGitUser()
    else:
        file_data = getChuck()
        if not isinstance(file_data,dict):
            if validJson(file_data):
                file_data = json.loads(file_data) 
        
        base_path = './fake_files'
        
        file_name = randomFileName() + '.txt'


        print(base_path,file_name,file_data['value'])

        if saveCode(base_path,file_name,file_data['value']):
            print("File saved...")
        else:
            print("Error: something happened ..... ?!?!?!")

            
            

        


