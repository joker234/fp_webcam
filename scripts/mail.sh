#!/bin/bash
if ! [ -f /tmp/ipmailsend ]; then
  ip a l dev eth0 | mail -s "IP Praktikumsraspi" joker@joker234.de,philip.bell@web.de
  touch /tmp/ipmailsend
fi
