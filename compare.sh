#! /bin/bash

read -p "Enter the first string: " str1
read -p "Enter the second string: " str2

if [[ ${#str1} -gt ${#str2} ]]
then echo The first string is longer
elif [[ ${#str1} -lt ${#str2} ]]
	then echo The first string is shorter
	else
		echo Both strings have the same length
fi
	
