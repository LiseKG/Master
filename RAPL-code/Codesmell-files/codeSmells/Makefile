ifndef FILE
$(error FILE not set)
endif

compile:
	@echo "Nothing to compile for python codesmell"
	
measure:
	sudo modprobe msr
	sudo ../../RAPL/main "python3 $(FILE)" codesmell $(FILE) 

run:
	python3 $(FILE)

mem:
	/usr/bin/time -v python3 $(FILE)
