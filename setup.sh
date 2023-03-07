#!/usr/bin/env bash

for m in praw numericalunits pylint black coverage; do 
  /usr/bin/env python3 -m pip install --upgrade $m
done

./test.sh &&
   echo "All tests OK" &&
   echo 'setup done, run `nohup ./bot.py`'
