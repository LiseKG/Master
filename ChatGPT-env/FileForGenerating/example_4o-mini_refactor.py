#!/usr/bin/env python3
import os
import json
import requests
import sys
import re

# -------------------------
# Read environment variables
# -------------------------
uio_gpt_api_key = os.environ.get("UIO_SE_GROUP_GPT_API_KEY")
uio_gpt_resource_name = os.environ.get("UIO_SE_GROUP_GPT_RESOURCE_NAME", "[YOUR-RESOURCE-NAME, e.g., gpt-uio-mytest-01]")
uio_gpt_deployment_name = os.environ.get("UIO_SE_GROUP_GPT_DEPLOYMENT_NAME", "[YOUR-CHOSEN-DEPLOYMENT-NAME, e.g., hello-world-poem]")
uio_gpt_api_version = os.environ.get("UIO_SE_GROUP_API_VERSION", "[YOUR-API-VERSION-OF-DEPLYMENT, e.g., api-version=2025-01-01-preview]")

print("Deployment created in Azure for this script was: 'gpt-4o-mini'")
print("Not all deployment models and versions may be valid")

filename = sys.argv[1] # example godclass_1_s
print(filename)
dir = "run_x/"
match = re.match(r"^([a-zA-Z]+)_(\d+)", filename)


if match:
    name = match.group(1)
    version = match.group(2)
else:
    print("no matches in filename")
    exit(1)
      
try: 
	with open("interface_"+version+".py", "r") as file:
		int_content = file.read()
		#print(int_content)
		
except FileNotFoundError:
	print("file not found 2")
	exit()
	 
try: 
	with open(dir+"/"+filename+".py", "r") as file:
		scontent = file.read()
		#print(int_content)
		
except FileNotFoundError:
	print("file not found 3")
	exit()

content_prompt = f""" """

# -------------------------
# Prepare URL, headers, body
# -------------------------
endpoint_url = f"https://{uio_gpt_resource_name}.openai.azure.com/openai/deployments/{uio_gpt_deployment_name}/chat/completions?{uio_gpt_api_version}"

headers = {
    "api-key": uio_gpt_api_key,
    "Content-Type": "application/json"
}

body = {
    "messages": [
        {
            "role": "user",
            "content": content_prompt
        }
    ],
    "max_completion_tokens": 1000,
    "temperature": 1,
     "top_p": 1
}

# -------------------------
# Make the POST request
# -------------------------
response = requests.post(endpoint_url, headers=headers, data=json.dumps(body))
print(response)


# -------------------------
# Parse the response
# -------------------------
try:
    resp_json = response.json()
except json.JSONDecodeError:
    print("Error decoding JSON from API response:")
    print(response.text)
    exit(1)

if "error" in resp_json:
    print("API Error:")
    print(resp_json["error"])
else:
    # Print the content of the first choice
    msg = resp_json["choices"][0]["message"]["content"]
    
    ##Saving the files in text files
    with open("all_genGPT.txt","a") as f:
        f.write(msg)
    with open("temp_ERFE.txt","w") as f:
        f.write(msg)


    
