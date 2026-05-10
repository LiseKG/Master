for file in "run_x/"*; do
	#echo "Processing: $file"
	
	
	if python3 "$file" > /dev/null; then
		echo $file "runnable"
		continue
	else
		echo $file "not runnable" #>> "$logfile"
	#python3 $file
	fi
	done
