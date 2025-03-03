from time import perf_counter
import gc
from recursion.recursive_floyd import recursive_floyd
from iterative.iterative_floyd import iterative_floyd

def performance_test(name, function_handle, runs=5):
    """
    Measures the average execution time of a function over multiple runs.

    Parameters:
    function_handle -> The function being tested. Must take no parameters.
    runs -> The number of times the function is executed for an accurate average time.
    """
    times = []

    # Warm-up run (ensures bytecode is optimized and CPU caching is used)
    function_handle()

    for _ in range(runs):
        gc.collect()  # Ensure memory is clean before each run
        gc.disable()  # Disable garbage collection during timing

        start_time = perf_counter()
        function_handle()
        end_time = perf_counter()

        times.append(end_time - start_time)
        gc.enable()  # Re-enable garbage collection after run

    avg_time = sum(times) / runs
    print(f"{name} - Average Execution Time: {avg_time:.6f} seconds")

def main():
    """Runs performance tests for Floyd-Warshall implementations."""
    print("Benchmarking Floyd-Warshall Implementations")
    performance_test("recursive_floyd", lambda: recursive_floyd(0, 0, 0))
    performance_test("iterative_floyd", iterative_floyd)


if __name__ == "__main__":
    main()
