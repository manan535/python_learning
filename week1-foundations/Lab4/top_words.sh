#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <filename> [count]"
    exit 1
fi

FILE=$1
COUNT=${2:-10}

tr '[:upper:]' '[:lower:]' < "$FILE" \
| tr -cs '[:alpha:]' '\n' \
| sort \
| uniq -c \
| sort -nr \
| head -n "$COUNT"
