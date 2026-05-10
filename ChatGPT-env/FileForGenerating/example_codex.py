#!/usr/bin/env python3
import os
import json
import requests
import sys

# -------------------------
# Read environment variables
# -------------------------
uio_gpt_api_key = os.environ.get("UIO_SE_GROUP_GPT_API_KEY")
uio_gpt_resource_name = os.environ.get("UIO_SE_GROUP_GPT_RESOURCE_NAME", "[YOUR-RESOURCE-NAME, e.g., gpt-uio-mytest-01]")
uio_gpt_deployment_name = os.environ.get("UIO_SE_GROUP_GPT_DEPLOYMENT_NAME", "[YOUR-CHOSEN-DEPLOYMENT-NAME, e.g., hello-world-poem]")
uio_gpt_api_version = os.environ.get("UIO_SE_GROUP_API_VERSION", "[YOUR-API-VERSION-OF-DEPLYMENT, e.g., api-version=2025-01-01-preview]")

print("Deployment created in Azure for this script was: 'Codex'")
print("Not all deployment models and versions may be valid")

version = sys.argv[1]
print("version",version)	
     
try: 
	with open("interface_"+version+".py", "r") as file:
		int_content = file.read()
		#print(int_content)
		
except FileNotFoundError:
	print("file not found 2")
	exit()


content_prompt = f""""""

# -------------------------
# Prepare URL, headers, body
# -------------------------
endpoint_url = f"https://{uio_gpt_resource_name}.openai.azure.com/openai/responses?{uio_gpt_api_version}"

headers = {
     "Content-Type": "application/json",
    "Authorization": f"Bearer {uio_gpt_api_key}",
    
}

body = {
    "input":content_prompt,
   "model":"",
   "max_output_tokens": 10000
}

# -------------------------
# Make the POST request
# -------------------------
response = requests.post(endpoint_url, headers=headers, json=body)
#response = responseRaw["output"][1]["content"][0]["text"]
print(response)

# -------------------------
# Parse the response
# -------------------------
## Saving the files into text files
try:
    resp_json = response.json()
    msg = resp_json["output"][1]["content"][0]["text"]
    print(msg)
    with open("all_genGPT.txt","a") as f:
        f.write(msg)
		
    with open("temp_feat.txt","w") as f2:
        f2.write(msg)
except json.JSONDecodeError:
    print("Error decoding JSON from API response:")
    print(response.text)
    exit(1)


