import psutil
import time
import os

def monitor_system_resources(interval=2, duration=None):
    """
    Monitors CPU and memory usage of the system.

    Args:
        interval (int): The time interval in seconds between each monitoring check.
                        Default is 2 seconds.
        duration (int, optional): The total duration in seconds for monitoring.
                                  If None, it will monitor indefinitely.
    """
    print(f"--- Starting System Resource Monitor ---")
    print(f"Monitoring every {interval} second(s). Press Ctrl+C to stop.")

    start_time = time.time()
    iteration = 0

    try:
        while True:
            iteration += 1
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            # --- CPU Usage ---
            # psutil.cpu_percent() provides system-wide CPU utilization as a percentage.
            # interval=1 argument in cpu_percent means it will block for 1 second to
            # calculate the CPU usage since the last call.
            cpu_usage = psutil.cpu_percent(interval=1)

            # --- Memory Usage ---
            # psutil.virtual_memory() returns a named tuple with various memory stats.
            memory_info = psutil.virtual_memory()
            total_memory_gb = memory_info.total / (1024**3) # Convert bytes to GB
            available_memory_gb = memory_info.available / (1024**3)
            used_memory_gb = memory_info.used / (1024**3)
            memory_percent = memory_info.percent # Percentage of memory used

            # --- Print Results ---
            print(f"\n[{current_time}] Iteration {iteration}:")
            print(f"  CPU Usage: {cpu_usage:.2f}%")
            print(f"  Memory Usage: {memory_percent:.2f}% (Used: {used_memory_gb:.2f} GB / Total: {total_memory_gb:.2f} GB)")

            # Check if duration limit is reached
            if duration is not None and (time.time() - start_time) >= duration:
                print(f"\n--- Monitoring finished after {duration} seconds ---")
                break

            # Wait for the next interval
            time.sleep(interval - 1) # Subtracting 1 because cpu_percent already waited for 1 second

    except KeyboardInterrupt:
        print("\n--- Monitoring stopped by user (Ctrl+C) ---")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    # Ensure psutil is installed:
    # pip install psutil

    # Example usage:
    # Monitor indefinitely with 2-second intervals
    monitor_system_resources(interval=2)

    # Monitor for 30 seconds with 5-second intervals
    # monitor_system_resources(interval=5, duration=30)
