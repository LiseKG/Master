SOURCE_DIR="../../../../pythonenv/chatgpt-env/run5"

mapfile -t FILES < <(find "$SOURCE_DIR" -type f | sort)
target_temp=45000

temp() {
  cat /sys/class/thermal/thermal_zone3/temp
}

### Code written by Brage Isak Keiserås, and modified to use the right tempeture for the device.

wait_for_temp() {
    local start_time
    local last_log_time

    start_time=$(date +%s)
    last_log_time=$start_time

    while true; do
        temp=$(temp)
        if [ "$temp" -lt "$target_temp" ]; then
            break
        fi

        now=$(date +%s)
        if [ $((now - last_log_time)) -ge 60 ]; then
            echo "[$(date +'%T')] Waiting for temp to fall below $target_temp milli°C... (current: ${temp} milli°C)"
            last_log_time=$now
        fi

        sleep 1
    done
}
###

for fil in "${FILES[@]}"; do
	echo "$fil"
	echo "Warm up"
	for i in {0..1}; do
		python3 $fil
		#echo "Test $i"
		
	done

done


echo "Starting experiment"
temp
wait_for_temp

for fil in "${FILES[@]}"; do
   echo "running $fil"
   for i in {0..30}; do
	    temp
	    wait_for_temp
	    make measure FILE="$fil"
            done
done


