import sys
import yaml

exit = 0
for yml in sys.argv[1:]:
    try:
        with open(yml) as f:
            yaml.load(f)
    except (yaml.parser.ParserError, yaml.scanner.ScannerError) as e:
        print '********\n%s\n********' % e
        exit += 1
    else:
        print '%s: Syntax OK' % yml

sys.exit(exit)
