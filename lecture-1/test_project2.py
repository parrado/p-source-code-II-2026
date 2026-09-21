
from random import randint


users=[
    {'name':'Alex','role':'professor'},
    {'name':'Julian','role':'professor'},
    {'name':'Maria','role':'student'},
    {'name':'Juan','role':'student'},
    {'name':'Ana','role':'student'},
    {'name':'Pedro','role':'student'}
]

labs=('Voltage Divider','Current Divider','Mesh Analysis','Op Amp','Transient response')

professor=users[randint(0,1)]['name']
assigned_labs=[]
for user in users:
    if user['role']=='student':
        lab={'lab_names': set(),'professor': professor}
        while True:
            lab['lab_names'].add(labs[randint(0,4)])
            if len(lab['lab_names'])==2:
                break

        assigned_labs.append(lab)

print(assigned_labs)
