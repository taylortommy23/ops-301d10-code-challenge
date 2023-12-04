#!/bin/bash

# Define backup directory and timestamp
bdir="/var/log/backups"
ts=$(date +"%Y%m%d%H%M%S")

# Function to compress and backup a log file
backup() {
    lf="$1"
    cf="$bdir/${lf##*/}-$ts.zip"

    orig_size=$(stat -c %s "$lf")
    echo "Original size of $lf: $orig_size bytes"

    gzip -c "$lf" > "$cf"

    comp_size=$(stat -c %s "$cf")
    echo "Compressed size of $cf: $comp_size bytes"

    > "$lf"
}

# List of log files to backup
logs=(
    "/var/log/syslog"
    "/var/log/wtmp"
)

# Loop through log files and perform backups
for lf in "${logs[@]}"; do
    if [ -e "$lf" ]; then
        echo "Backing up $lf..."
        backup "$lf"
    else
        echo "Log file $lf not found."
    fi
done

# Compare original sizes to compressed sizes
for lf in "${logs[@]}"; do
    if [ -e "$lf" ]; then
        orig_size=$(stat -c %s "$lf")
        cf="$bdir/${lf##*/}-$ts.zip"
        comp_size=$(stat -c %s "$cf")

        echo "Comparison for $lf:"
        echo "Original size: $orig_size bytes"
        echo "Compressed size: $comp_size bytes"

        if [ "$orig_size" -gt "$comp_size" ]; then
            echo "Original file is larger than compressed file."
        elif [ "$orig_size" -lt "$comp_size" ]; then
            echo "Original file is smaller than compressed file."
        else
            echo "Original file size is equal to compressed file size."
        fi
    fi
done
