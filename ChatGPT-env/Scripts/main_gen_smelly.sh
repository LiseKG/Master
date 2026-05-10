
VER="1"

echo $VER
python3 function_FE.py $VER || exit 1
python3 dividefiles.py temp_feat.txt || exit 1
python3 function_GC.py $VER || exit 1
python3 dividefiles.py temp_gc.txt || exit 1
python3 function_LM.py $VER || exit 1
python3 dividefiles.py temp_lm.txt || exit 1
python3 function_testfiles.py $VER  || exit 1
python3 dividefiles.py temp_test.txt || exit 1