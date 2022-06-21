import numpy as np
import sys

benchmarkFile=""
try:
    benchmarkFile = sys.argv[1]
except:
    print("Command: python configWorkloads.py [benchmark ID]")
GD_ID=""
keysFile=""


if  benchmarkFile == "long":
    GD_ID="1zc90sD6Pze8UM_XYDmNjzPLqmKly8jKl"
    keysFile = "longitudes-200M.bin.data"
elif benchmarkFile == "longlat":
    GD_ID="1mH-y_PcLQ6p8kgAz9SB7ME4KeYAfRfmR"
    keysFile = "longlat-200M.bin.data"
elif benchmarkFile == "lognormal":
    GD_ID="1y-UBf8CuuFgAZkUg_2b_G8zh4iF_N-mq"
    keysFile = "lognormal-190M.bin.data"
elif benchmarkFile == "ycsb":
    GD_ID="1Q89-v4FJLEwIKL3YY3oCeOEs0VUuv5bD"
    keysFile = "ycsb-200M.bin.data"
else:
    print("Possible workloads:long, longlat, lognormal, ycsb" )



benchmark_db = np.load(keysFile)
np.sort(benchmark_db).tofile("sorted_"+keysFile)
