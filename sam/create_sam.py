#!/usr/bin/python

import sys
import yaml
import zipfile
from shutil import copyfile

yaml_file=str(sys.argv[1])

with open(yaml_file, 'r') as stream:
    try:
        data = yaml.load(stream)
        functions=data['lambda_functions']
        #print(data['lambda_functions'])
        #print(functions)
     
        dicta = {k:v for d in data['lambda_functions'] for k, v in d.items()}
        #print(dicta) 
        # In the event of multiple lambda functions in the file, would need to iterate here
        #for k, v in dicta.items():
        lambda_code = dicta['lambda_code']
        lambda_code_base = dicta['lambda_code_base']
        function_name = dicta['function_name']
        timeout = dicta['timeout']
        handler = dicta['handler']
        runtime = dicta['runtime']
        description = dicta['description']
        codeuri = dicta['uri']
        event = dicta['event']
        type = dicta['type']
        path = dicta['path']
        method = dicta['method']

    except yaml.YAMLError as exc:
        print(exc)

# Save in the event we later want to zip 
#zf = zipfile.ZipFile("bundle.zip", 'w')
#try:
#    zf.write(lambda_code)
#finally:
#    zf.close()

# Copy lambda_code to codeurl
destfile = lambda_code_base + lambda_code
copyfile(lambda_code, destfile)

file = open("template.yaml","w")
file.write("AWSTemplateFormatVersion : '2010-09-09'\n")
file.write("Transform: AWS::Serverless-2016-10-31\n")
# Would be ideal to split out boilerplate header stuff 
# With individual functions in the event of multiple
file.write("Description: " + description + "\n")
file.write("Globals: \n")
file.write("    Function: \n")
file.write("        Timeout: " + str(timeout) + "\n")
file.write("Resources: \n")
file.write("  " + function_name + ":\n")
file.write("    Type: AWS::Serverless::Function\n")
file.write("    Properties:\n")
file.write("        CodeUri: " + codeuri + "\n")
file.write("        Handler: " + handler + "\n")
file.write("        Runtime: " + runtime + "\n")
file.write("        Events: \n")
file.write("            " + event + ": \n")
file.write("                Type: " + type + "\n")
file.write("                Properties: \n")
file.write("                    Path: " + path + "\n")
file.write("                    Method: " + method + "\n")
file.close()
