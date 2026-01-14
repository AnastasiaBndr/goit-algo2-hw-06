import time

def set_productivity(data):
    start_time = time.perf_counter()
    unique = set(data)
    end_time = time.perf_counter()
    return {"unique": len(unique), "time": end_time-start_time}
    