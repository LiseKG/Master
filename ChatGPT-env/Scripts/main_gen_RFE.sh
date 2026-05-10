
VER="1"

echo $VER

python3 function_rf_fe.py featureenvy_"$VER"_s || exit 1
python3 dividefiles.py temp_fe.txt || exit 1
python3 function_rf_gc.py godclass_"$VER"_s || exit 1
python3 dividefiles.py temp_gc.txt || exit 1
python3 function_rf_lm.py longmethod_"$VER"_s || exit 1
python3 dividefiles.py temp_lm.txt || exit 1
python3 function_rf_energy.py godclass_"$VER"_s_RGC || exit 1
python3 dividefiles.py temp_e.txt || exit 1
python3 function_rf_energy.py featureenvy_"$VER"_s_RFE || exit 1
python3 dividefiles.py temp_e.txt || exit 1
python3 function_rf_energy.py longmethod_"$VER"_s_RLM || exit 1
python3 dividefiles.py temp_e.txt || exit 1


# 10 prompts per interface