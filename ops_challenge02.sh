#!/bin/bash

# defining source and destination filenames
source_path="/var/log/syslog"
echo "/var/log/syslog"




# append the current date and time to file name 
date=$(date +"%m-%d-%Y")

destination_file="syslogfile_${date}"

cp "$source_path" "$destination_file"
