#!/bin/bash

url="https://api.reporter.nih.gov/v2/publications/search"
head1="accept: application/json"
head2="Content-Type: application/json"

COUNTER=0
# projects_to_curl.txt contains the core project name to be downloaded
# one line for one core project number
# each project is read as an variable "proj"
while IFS= read -r proj;do
	let COUNTER=COUNTER+1
	flag=`expr $COUNTER % 500`
	if [[ $flag == 0 ]]; then
		echo "$COUNTER processed at `date`"
		break
	fi

	curl -X POST $url -H "$head1" -H "$head2" -d "{\"criteria\":{\"pmids\":[0],\"applIds\":[0],\"coreProjectNums\":[\"string\"]},\"offset\":0,\"limit\":0,\"sortField\":\"string\",\"sortOrder\":\"string\"}" -o $proj.json --silent
	sleep 1

done < /path/projects_to_curl.txt
# using Curl to collect all publications associated with a project
# results are stored in a json file named with the project number
