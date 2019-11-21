#!/bin/bash
while read LINE; do if [[ $LINE =~ (^\([0-9]{3}\)[[:blank:]][0-9]{3}-[0-9]{4}$)|(^[0-9]{3}-[0-9]{3}-[0-9]{4}$) ]]; then echo $LINE; fi; done < file.txt
