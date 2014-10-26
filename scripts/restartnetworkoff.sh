#!/bin/bash
ping 8.8.8.8 -c 3 2>&1 >/dev/null
if [[ $? == 0 ]]; then
  rm ~/restartundso/* -f
else
  if [[ ! -f ~/restartundso/first ]]; then
    touch ~/restartundso/first
    sudo shutdown -r 1
  fi
fi
