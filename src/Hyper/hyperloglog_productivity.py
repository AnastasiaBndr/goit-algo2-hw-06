import time
from .HyperLogLog import HyperLogLog

def hyperloglog_productivity(data):
    hll=HyperLogLog(p=14)

    for i in data:
        hll.add(i)
    
    start_time = time.perf_counter()
    estimated_cardinality=hll.count()
    end_time = time.perf_counter()

    return{"unique":estimated_cardinality, "time":end_time-start_time}

