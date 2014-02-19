import sys
import yaml

for yml in sys.argv[1:]:
    try:
        with open(yml) as f:
            yaml.load(f)
    except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
        print '********\n%s\n********' % e
    else:
        print '%s: Syntax OK' % yml
