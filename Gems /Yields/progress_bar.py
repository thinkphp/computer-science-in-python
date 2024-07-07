import time
def progress_bar(total):
  """Yields progress updates for a long-running task with a specified total count.

  Args:
      total: The total number of steps in the task.

  Yields:
      A string representing the progress bar with percentage completion.
  """
  progress = 0
  while progress < total:
    progress += 1
    percent = int((progress / total) * 100)
    bar = "#" * int(percent / 5)  # Adjust character and division for desired granularity
    yield f"Progress: [{bar}{' ' * (20 - len(bar))}] {percent}%"

# Example usage with a simulated task
def long_running_task(n):
  for _ in range(n):
    # Simulate some work
    time.sleep(0.1)  # Adjust sleep time for desired duration

total_steps = 100

for update in progress_bar(total_steps):
  print(update)
  long_running_task(1)  # Adjust task size for desired granularity

print("Task completed!")
