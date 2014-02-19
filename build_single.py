import os
import sys

try:
    import yaml
except ImportError:
    raise SystemExit('PyYAML python module is missing')

try:
    path = sys.argv[1]
except IndexError:
    path = os.path.dirname(os.path.abspath(__file__))

allfiles = os.listdir(path)

chapter_files = []
for f in allfiles:
    root, ext = os.path.splitext(f)
    if ('chapter' in root.lower() and 'template' not in root.lower() and
            ext.lower() in ['.yml', '.yaml']):
        chapter_files.append(f)

chapter_files.sort()

try:
    with open(os.path.join(path, 'root.yml')) as f:
        root = yaml.load(f)
except:
    raise SystemExit('root.yml file not found')

if 'slides' not in root:
    root['slides'] = []

for chapter_file in chapter_files:
    try:
        with open(os.path.join(path, chapter_file)) as f:
            chapter = yaml.load(f)
    except:
        sys.stderr.write('*** Could not load/parse %s ***\n' % chapter_file)
    else:
        root['slides'].extend(chapter['slides'])

print yaml.dump(root, indent=4, allow_unicode=True, default_flow_style=False)
