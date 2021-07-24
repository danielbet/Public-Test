#Script by Daniel
#Install python to use in windows
#Uncomment following line to use in linux  
#!/usr/bin/python3
#----prepairing objects---You can change Characters and length as you wish---
import random
char = ['A','B','C','D','E','F','G','H','J','K','M','N','P','Q','R','S','T','U','V','W','X','Y','Z',
        'a','b','c','d','e','f','g','h','j','k','m','n','p','q','r','s','t','u','v','w','x','y','z',
        '2','3','4','5','6','7','8','9','!','#']
length = 8
counter = 0
pas = []
#---------generating password------------------------------------------------
while counter < length :
    counter += 1
    pas.append(random.choice(char))
pas.append("#5")
print()
passtext = ("".join(pas))
print(passtext)
#---------copy to clipboard----------for windows only------------------------
import subprocess
def copy2clip(txt):
  cmd='echo '+txt.strip()+'|clip'
  return subprocess.check_call(cmd, shell=True)
copy2clip('%s'%(passtext))
print()
input('Press enter to quit...')