#!/bin/bash
# Bash script that displays the size of the body of URL response
curl -sI "$1" | grep -i "content-length" | cut -d' ' -f2
