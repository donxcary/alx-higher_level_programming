#!/bin/bash
# Bash script that sends a header variable to URL displays body of the response
curl -s "$1" -H "X-School-User-Id: 98"
