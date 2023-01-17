from keyboard.output import autotype
from pynput.keyboard import Key
import json
import os
import sys
from format.conversion import *

def autofill(context,namespace,keys,command):
    if namespace not in context.keys():
        print(f"Namespace {namespace} not found")
    ns = context[namespace]
    at = autotype()
    for i in keys:
        if i not in ns["fields"].keys() and i not in reserved().keys() :
            print(f"{i} not found in {namespace}")
            return
        else:
            at.keys.append(i)
    at.start_with = ns["start_with"]
    at.end_with = ns["end_with"]
    at.between = ns["between"]
    at.fields = ns["fields"]
    at.command = command
    at.fill()

def addNameSpace(context,namespace,start_with,end_with,between):
    context[namespace] = dict()
    context[namespace]["start_with"] = start_with
    context[namespace]["end_with"] = end_with
    context[namespace]["between"] = between
    context[namespace]["fields"] = []

def addField(context,namespace,field,text):
    if namespace not in context.keys():
        print(f"Namespace {namespace} not found")
        return
    context[namespace]["fields"] = text

def askForFields(context,namespace):
    while True:
        field = input("Input field name ")
        if(field == ""):
            break
        elif(field == reserved().keys()):
            print(f'{field} is a reserved keyword')
            continue
        value = input(f"Input {field} value ")
        context[ns]["fields"][field] = value

if __name__ == "__main__":
    file = open(f'{os.path.dirname(__file__)}/context.json',"r")
    context = json.load(file)

    namespace = "default"
    command=[Key.ctrl,"1"] 
    keys = []

    try:
        if sys.argv[1] == "create":
            ns = sys.argv[2]
            addNameSpace(context,ns,[],[],'\t')
            askForFields(context,ns)
        elif sys.argv[1] == "add":
            ns = sys.argv[2] if len(sys.argv) > 2 else namespace
            askForFields(context,ns)
        else:
            i = 1
            while i < len(sys.argv):
                cmd = sys.argv[i]
                if cmd == "-ns":
                    i += 1
                    namespace = sys.argv[i]
                elif cmd == "-k":
                    for j in range(i+1,len(sys.argv)):
                        keys.append(sys.argv[j])
                    print("Press CTRL 1 to fill")
                    autofill(context,namespace,keys,command)
                    break
    except Exception as e:
        print(e)
    file.close()
    file = open(f'{os.path.dirname(__file__)}/context.json',"w")
    json.dump(context,file)