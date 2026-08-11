#! /bin/bash

cnt=1
while [ $cnt -le 4 ]
do
	read -p "Choose between fruits: apple/banana/orange: " fruit
	case $fruit in
		"apple")
			echo -e "This is a red fruit\n"
			;;
		"banana")
			echo -e "This is a yellow fruit\n"
			;;
		"orange")
			echo -e "This is an orange fruit\n"
			;;
		*)
			echo -e "Unknown fruit\n"
	esac
	((cnt+=1))
done
