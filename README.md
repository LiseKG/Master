# Master

This setup involves:
* The measurement setup (RAPL)
* The interfaces used to generate the files.
* The ChatGPT prompt and setup
* The files used (Dataset)
* The turnoff script used before running the experiment

````
| <ChatGPT-env>
    | FileForGenerating
        | #Example scripts
        | README.md on how to setup (env and files)
    | Scripts 
        | Scripts 
            | # the scripts used to generate the files
    | prompt.md #The prompts used
| Dataset # The files used
| Interfaces # The interfaces used
| <RAPL-code>
    | <m-types> #measurement types
    | <RAPL> #RAPL setup
    README.md # README from Green Software Lab
    ...

````

** The folder names were changed from the original setup to make the setup easier to understand.