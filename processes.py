class Process:
    def __init__(self,pid,arrival_time,burst_time,priority=0):
        self.pid= pid
        self.arrival_time = arrival_time
        self.burst_time= burst_time
        self.priority = priority

        self.remaining_time= burst_time
        self.waiting_time= 0
        self.turnaround_time = 0
        self.completion_time= 0

    def run_one_unit_of_cput(self):
            if self.remaining_time > 0:
                self.remaining_time-=1

    def is_finished(self):
            return self.remaining_time == 0
    
    def set_waiting_time(self,waiting_time):
          self.waiting_time= waiting_time

    def set_turnaround_time(self,turnaround_time):
          self.turnaround_time = turnaround_time