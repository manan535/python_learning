import numpy as np
import time

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

print(arr.mean(axis=0))
print(arr.mean(axis=1))

print(arr.max(axis=0))
print(arr.min(axis=0))

column_min = arr.min(axis=0)
column_max = arr.max(axis=0)

normalized = (arr - column_min) / (column_max - column_min)

print(normalized)

column_means = arr.mean(axis=0)
centered = arr - column_means

print(centered)

large_arr = np.random.rand(1000000)

start = time.time()
vectorized = large_arr * 2
vectorized_time = time.time() - start

start = time.time()
loop_result = [x * 2 for x in large_arr]
loop_time = time.time() - start

print(vectorized_time)
print(loop_time)