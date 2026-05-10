compile:
	@echo "Nothing to compile for stress-ng cpu"
	
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "stress-ng --class cpu --timeout 20s" stress-ng cpu 

run:
	stress-ng --class cpu --timeout 20s

mem:
	/usr/bin/time -v stress-ng --class cpu --timeout 20s
