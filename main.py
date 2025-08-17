from collections import deque
from processes import Process
from algorithms import *


def print_results(processes, algorithm_name):
    print(f"\nResults for {algorithm_name} Scheduling")
    print("PID  AT  BT  CT  WT  TAT")
    for p in processes:
        print(f"{p.pid:>3}  {p.arrival_time:>2}  {p.burst_time:>2}  {p.completion_time:>2}  {p.waiting_time:>2}  {p.turnaround_time:>3}")

    avg_wt = sum(p.waiting_time for p in processes) / len(processes)
    avg_tat = sum(p.turnaround_time for p in processes) / len(processes)

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")


def get_process_list():
    return [
        Process(pid=1, arrival_time=0, burst_time=5, priority=2),
        Process(pid=2, arrival_time=1, burst_time=3, priority=1),
        Process(pid=3, arrival_time=2, burst_time=8, priority=4),
        Process(pid=4, arrival_time=3, burst_time=6, priority=3),
    ]


processes_fcfs = get_process_list()
fcfs_s(processes_fcfs)
print_results(processes_fcfs, "FCFS")

processes_sjf = get_process_list()
sjf(processes_sjf)
print_results(processes_sjf, "SJF")

processes_pr_sch = get_process_list()
priority_scheduling(processes_pr_sch)
print_results(processes_pr_sch, "Priority Scheduling")

processes_rr = get_process_list()
round_robin(processes_rr, time_quantum=2)
print_results(processes_rr, "Round Robin")

