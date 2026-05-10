Partly forked from https://github.uio.no/gunnab/uio-gpt-hello-world-python/blob/develop/README.md

# function_*codesmellname* files
This read me explain the setup of the files for generating code smells.

There are two examples, one for codex models and one for 4o-mini models.
They all use the same process to setup the enviorment:

1. Update the bash shell with the required api key and deployment names, four in total. I'm used ~/.zshrc file. 

You will have to get the API key and deployment name and API version from someone. The syntax will look like this:
```
export UIO_SE_GROUP_GPT_API_KEY="<your api-key goes here>"
export UIO_SE_GROUP_GPT_RESOURCE_NAME="gpt-ifi-prog-eksperimenter-swe1"
export UIO_SE_GROUP_GPT_DEPLOYMENT_NAME="<your deployed model>"
# For example, "api-version=2025-01-01-preview"
export UIO_SE_GROUP_API_VERSION="<the version of your deployed model>"
```
Refresh the environment before proceeding (a restart of terminal will do). 

2. First time only: Create a virtual environment for python (MacOS)

```python3 -m venv chatgpt-env```

3. Activate the environment

```source chatgpt-env/bin/activate```

4. First time only: install ´requests´ dependency in the virtual environment

```pip install requests```

5. Run the python script

```python3 filename.py```


## Prompts.
The 3 different prompts are provided in the text file prompts.txt. These must be copy pasted into the example files before running.

My generating python prompt files were called:
- function_FE
- function_LM
- function_GC

You can either use  ```bash main_gen_smelly.sh``` or the script alone by doing ```python3 filename.py```

