# Master

This setup involves:
* The experiment framework (RAPL)
* The interfaces used to generate the files.
* The ChatGPT prompt and setup
* The files used (Dataset)
* The turnoff script used before running the experiment

````
| <ChatGPT-env>
    | FileForGenerating
        | #Example sripts
        | README.md explaining how to setup (env and files)
    | Scripts 
        | Scripts 
            | # the scripts used to generate the files
    | prompt.md #All prompts used
| Dataset # The files used
| Interfaces # Interfaces used to generate files   
| <RAPL-code>
    | <m-types> #measurment types
    | <RAPL> #RAPL setup
    README.md # README from Green Software Lab
    ...

````

** The folder names were changed from the original setup to make the setup easier to understand.