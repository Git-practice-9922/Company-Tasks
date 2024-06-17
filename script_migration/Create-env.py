import os
import json

#get the repo name and org name
with open("input.txt", "r") as file:
    for line in file:
        print(line.strip())
        line = line.strip().split("/")
        repo_name = line[-1]
        print(repo_name)
#Check if the repo present or not
def repo_exist():
    with open("environments_and_settings.json", "r") as file:
        data = json.loads(file)

    for keys, values in data.items():
        if keys == repo_name:
            print(values)

print(repo_exist())
#create the ENV 