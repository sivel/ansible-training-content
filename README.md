# yaml-slide-template

[![Build Status](https://travis-ci.org/sivel/yaml-slide-template.png)](https://travis-ci.org/sivel/yaml-slide-template)
Autobuilding on Jenkins [here](http://jenkins.onitato.com:8080/job/Slides/ws/output/index.html#/).

## Build Instructions

1. `git clone https://github.com/sivel/yaml-slide-template.git`
1. `cd yaml-slide-template`
1. Update root.yml with correct header information
1. Add chapters as standalone presentations, chapters are rendered in order, using the `.sort()` list method. Chapters must be named with "chapter" in the filename, ending with either `.yaml` or `.yml`.  Any yaml filename with the word `template` in it will be ignored.
1. `git clone https://github.com/mpdehaan/revelator.git`
1. `python build_single.py [optional-path] > whatever.yml`
1. `cd revelator`
1. `./write_it ../whatever.yml whatever/`
1. Open whatever/index.html in your browser


### Dependencies

* PyYAML

## Syntax Checking

```
python syntax_check.py *.yml
```
