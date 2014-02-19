import os
import sys
import yaml
import json


allfiles = os.listdir(os.path.dirname(os.path.abspath(__file__)))

chapter_files = []
for f in allfiles:
    root, ext = os.path.splitext(f)
    if ('chapter' in root.lower() and 'template' not in root.lower() and
            ext.lower() in ['.yml', '.yaml']):
        chapter_files.append(f)

chapter_files.sort()

try:
    with open('root.yml') as f:
        root = yaml.load(f)
except:
    raise SystemExit('root.yml file not found')

if 'slides' not in root:
    root['slides'] = []

for chapter_file in chapter_files:
    try:
        with open(chapter_file) as f:
            chapter = yaml.load(f)
    except:
        sys.stderr.write('Could not load/parse %s\n' % chapter_file)
    else:
        root['slides'].extend(chapter['slides'])

print yaml.dump(root, indent=4, allow_unicode=True, default_flow_style=False)
