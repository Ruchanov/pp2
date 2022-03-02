import json

with open('sample-data.json','r') as f:
    x=f.read()
dd = json.loads(x) 
print('Interface Status','='*74,sep='\n')
print('DN', ' '*40,'Description',' '*11,'Speed',' ','MTU',' '*2)
print('-'*43,'-'*23,'-'*6,'-'*6)

arr = dd['imdata']
for dic in arr:
    if len(dic["l1PhysIf"]['attributes']["dn"])==41:
        print(dic["l1PhysIf"]['attributes']["dn"],' '*25,dic["l1PhysIf"]['attributes']["speed"],' '*3,dic["l1PhysIf"]['attributes']["mtu"])
    else:
        print(dic["l1PhysIf"]['attributes']["dn"],' '*24,dic["l1PhysIf"]['attributes']["speed"],' '*3,dic["l1PhysIf"]['attributes']["mtu"])

