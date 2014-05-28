#!/bin/bash
# Build script that should simplify Jenkins configuration.

# Exit if any command returns non-zero
set -e


if [ -d revelator ]; then
  echo "******** Checking for latest version of Revelator ********"
  cd revelator
  git pull
  cd ..
else
  echo "******** Downloading Revelator ********"
  git clone https://github.com/mpdehaan/revelator.git
  ln -fs revelator/reveal_js_261
fi

echo "******** Looping over folders ********"
for i in fundamentals operational advanced
  do
    echo "******** Syntax Check on $i ********"
    python $DRONE_BUILD_DIR/syntax_check.py $DRONE_BUILD_DIR/$i/*.yml
    echo "******** Creating output folder for $i ********"
    mkdir -p output/$i
    echo "******** Build Single on $i ********"
    python $DRONE_BUILD_DIR/build_single.py $DRONE_BUILD_DIR/$i > $i_comp.yml
    echo "******** Generating Slides on $i ********"
    python revelator/write_it $i_comp.yml output/$i
  done
