#!/bin/bash
# Bash script for POST request, send variable to URL, display body of response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
