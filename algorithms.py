from collections import deque

def fcfs_s(processes):
      processes.sort(key = lambda p: p.arrival_time)

      current_time= 0

      for process in processes:
            if current_time < process.arrival_time:
                  current_time = process.arrival_time
            
            process.completion_time = current_time + process.burst_time
            # CT - AT
            process.turnaround_time = process.completion_time - process.arrival_time
            #TAT - BT
            process.waiting_time = process.turnaround_time - process.burst_time
            
            current_time = process.completion_time
      return processes


def sjf(processes):
      processes.sort(key= lambda p: p.arrival_time)
      current_time= 0
      completed_processes = []
      completed_count = 0
      n = len(processes)

      finished = [False] * n

      while completed_count < n:
            ready_queue = [processes[i] for i in range(n) if processes[i].arrival_time <= current_time and not finished[i]]

            if not ready_queue:
              current_time+= 1
              continue
            
            next_process = min(ready_queue, key = lambda p:p.remaining_time)

            current_time += next_process.remaining_time
            next_process.completion_time = current_time

            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.burst_time

        # Mark as finished
            finished[processes.index(next_process)] = True
            completed_count += 1
            completed_processes.append(next_process)

      return completed_processes

def priority_scheduling(processes):
    processes.sort(key=lambda p: p.arrival_time)  # sort by arrival time
    current_time = 0
    completed = []

    while len(completed) < len(processes):
        # Get processes that have arrived and are not completed
        ready_queue = [p for p in processes if p.arrival_time <= current_time and p not in completed]

        if not ready_queue:  # No process available, move time forward
            current_time += 1
            continue

        # Select process with highest priority (lowest number)
        process = min(ready_queue, key=lambda p: p.priority)

        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time

        current_time = process.completion_time
        completed.append(process)

    return processes


def round_robin(processes, time_quantum):
    processes.sort(key=lambda p: p.arrival_time)  # Sort by arrival time
    n = len(processes)
    current_time = 0
    completed = 0
    queue = deque()

    i = 0
    while completed < n:
        # Add newly arrived processes
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if not queue:
            current_time += 1
            continue

        process = queue.popleft()

        if process.remaining_time <= time_quantum:
            current_time += process.remaining_time
            process.completion_time = current_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time
            process.remaining_time = 0
            completed += 1
        else:
            current_time += time_quantum
            process.remaining_time -= time_quantum

            # Add new arrivals that came during this time slice
            while i < n and processes[i].arrival_time <= current_time:
                queue.append(processes[i])
                i += 1

            # Put the unfinished process back in the queue
            queue.append(process)

    return processes