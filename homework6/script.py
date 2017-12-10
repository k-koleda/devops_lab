import yaml
import sys
import json
import subprocess
data = [subprocess.getoutput("python --version"),subprocess.getoutput("pyenv version-name")\
    ,sys.executable,subprocess.getoutput("which pip"),
        sys.exec_prefix,subprocess.getoutput("pip freeze").strip().split('\n'),
        subprocess.getoutput("python -m site --user-site")]
names=['version','name (alias)/virtual env','python executable location','pip location','PYTHONPATH'
    ,'installed packages:','site-packages location']
output=dict(zip(names, data))
with open('result.json', 'w') as fp:
    json.dump(output, fp)
with open('result.yml', 'w') as outfile:
    yaml.dump(output, outfile, default_flow_style=False)
