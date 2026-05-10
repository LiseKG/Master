import re
from pathlib import Path
import sys

output_dir = "run_x"
input = sys.argv[1]

with open(input, "r", encoding="utf-8") as f:
     content = f.read().lstrip()
     
Path(output_dir).mkdir(exist_ok=True)

#File godclass smelly version: godclass_1.py
pattern = re.compile(r"File\s+(?P<smell_type>.+?[\w\-]+)\s+(?P<type>[\w\-]+)\s+version:\s*(?P<filename>[\w\-\.]+)\s*```(?:python)?\n(?P<code>.*?)```",
    re.DOTALL | re.IGNORECASE,
    )
pattern2 = re.compile(r"(?P<fence>`{3,5})(?:python)?\n#\s*File\s+(?P<smell_type>.+?[\w\-]+)\s+(?P<type>[\w\-]+)\s+version:\s*(?P<filename>[\w\-\.]+)\s*(?P<code>.*?)(?P=fence)",
    re.DOTALL | re.IGNORECASE,
    )

matches = pattern.findall(content)
matches2 = pattern2.findall(content)

if not matches and not matches2:
    print("could not find any mactes, check format")
    exit(1)
    

for smell, type, filename, code in matches:
    output_path = Path(output_dir) /filename
    print("code:\n",filename)
    with open(output_path,"w") as f:
        f.write(code)

    print("done")

for fence,smell, type, filename, code in matches2:
    output_path = Path(output_dir) /filename
    print("code:\n",filename)
    with open(output_path,"w") as f:
        f.write(code)

    print("done")



