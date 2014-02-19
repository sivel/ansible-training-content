import os
import sys

try:
    import yaml
except ImportError:
    raise SystemExit('PyYAML python module is missing')

# Allow specification of a path to look for YAML files
# Fallback to dirname of this script itself
try:
    path = sys.argv[1]
except IndexError:
    path = os.path.dirname(os.path.abspath(__file__))

allfiles = os.listdir(path)

# Find all YAML chapter files.  Files should have "chapter" in the name
chapter_files = []
for f in allfiles:
    root, ext = os.path.splitext(f)
    if ('chapter' in root.lower() and 'template' not in root.lower() and
            ext.lower() in ['.yml', '.yaml']):
        chapter_files.append(f)

chapter_files.sort()

# Open the root.yml file that is the root of the slides
try:
    with open(os.path.join(path, 'root.yml')) as f:
        root = yaml.load(f)
except:
    raise SystemExit('root.yml file not found')

if 'slides' not in root:
    root['slides'] = []

errors = []
for chapter_file in chapter_files:
    try:
        with open(os.path.join(path, chapter_file)) as f:
            chapter = yaml.load(f)
    except:
        errors.append('*** Could not load/parse %s ***\n' % chapter_file)
    else:
        try:
            root['slides'].extend(chapter['slides'])
        except:
            errors.append('*** Could not find slides in %s ***\n' % chapter_file)

print yaml.dump(root, indent=4, allow_unicode=True, default_flow_style=False)

if errors:
    sys.stderr.write('\n'.join(errors))
    sys.exit(len(errors))

sys.exit(0)
