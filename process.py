

class Process:
    # initialize process
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.history = []
        self.completion_time = 0
        self.waiting_time = 0

    # function used by heap to arrange processes according to remaining time
    def __lt__(self, other):
        return self.remaining_time < other.remaining_time
