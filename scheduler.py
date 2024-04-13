from process import Process
from heapq import heappush, heappop
import matplotlib.pyplot as plt
from collections import deque


class Scheduler:
    processes = []

    def add_process(self, pid, arrival_time, burst_time):
        process = Process(pid, arrival_time, burst_time)
        self.processes.append(process)

    def clear_processes(self):
        self.processes.clear()

    @staticmethod
    def _sjf_preemptive_algo(processes: list[Process]):
        processes.sort(key=lambda x: x.arrival_time)
        ready_queue = []
        current_time = 0
        completed_processes = []

        # while there is a process to be executed continue
        while processes or ready_queue:

            # insert processes into the ready queue according to arrival time
            while processes and processes[0].arrival_time <= current_time:
                heappush(ready_queue, processes.pop(0))

            # increment time if ready queue is empty during cycle
            if not ready_queue:
                current_time += 1
                continue

            # execute process for a time unit
            process = heappop(ready_queue)
            process.remaining_time -= 1
            process.history.append(current_time)
            current_time += 1

            # calculate waiting time of process if finished,
            # otherwise return to heap to check next shortest remaining burst
            if process.remaining_time == 0:
                process.completion_time = current_time
                process.waiting_time = (process.completion_time - process.arrival_time) - process.burst_time
                completed_processes.append(process)
            else:
                heappush(ready_queue, process)

        return completed_processes

    @staticmethod
    def _get_avg_waiting_time(completed_processes: list[Process]):
        total_waiting_time = 0
        for process in completed_processes:
            total_waiting_time += process.waiting_time
        return total_waiting_time / len(completed_processes)

    def run_sjf_preemptive(self):
        completed_processes = self._sjf_preemptive_algo(self.processes)
        completed_processes.sort(key=lambda x: x.pid)
        avg_waiting_time = self._get_avg_waiting_time(completed_processes)

        fig, ax = plt.subplots()
        proc_intervals = []
        for p in completed_processes:
            intervals = [(start, 1) for start in p.history]
            proc_intervals.append(intervals)

        for proc in range(len(proc_intervals)):
            ax.broken_barh(proc_intervals[proc], (10 * proc, 10), facecolors='blue')

        ax.set_yticks([5 + (5 * 2 * i) for i in range(len(proc_intervals))])
        ax.set_yticklabels([f'P{p.pid}' for p in completed_processes])
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        ax.set_title(f'Process Execution Chart \nAvg Waiting Time: {avg_waiting_time}')
        ax.grid(True)
        plt.show()

        print(f"Average Waiting Time: {avg_waiting_time}")

    @staticmethod
    def _round_robin_algo(processes: list[Process], time_quantum: float):
        processes.sort(key=lambda x: x.arrival_time)

        ready_queue = deque()
        current_time = 0
        completed_processes = []
        i = 0

        while i < len(processes) or ready_queue:

            # simulate arrival on empty ready queue
            while i < len(processes) and processes[i].arrival_time <= current_time:
                ready_queue.append(processes[i])
                i += 1

            if not ready_queue:
                current_time = processes[i].arrival_time
                continue

            # execute process in time quanta
            process = ready_queue.popleft()
            prev_time = current_time

            if process.remaining_time <= time_quantum:
                current_time += process.remaining_time
                process.remaining_time = 0
                process.completion_time = current_time
                process.waiting_time = (process.completion_time - process.arrival_time) - process.burst_time
                completed_processes.append(process)
            else:
                current_time += time_quantum
                process.remaining_time -= time_quantum

                # simulate arrival while program is executing
                while i < len(processes) and processes[i].arrival_time <= current_time:
                    ready_queue.append(processes[i])
                    i += 1
                ready_queue.append(process)

            process.history.append((prev_time, current_time))

        return completed_processes

    def run_round_robin(self, time_quantum):
        completed_processes = self._round_robin_algo(self.processes, time_quantum)
        completed_processes.sort(key=lambda x: x.pid)
        avg_waiting_time = self._get_avg_waiting_time(completed_processes)

        fig, ax = plt.subplots()
        proc_intervals = []
        for p in completed_processes:
            intervals = [(round[0], round[1] - round[0]) for round in p.history]
            proc_intervals.append(intervals)

        for proc in range(len(proc_intervals)):
            ax.broken_barh(proc_intervals[proc], (10 * proc, 10), facecolors='blue')

        ax.set_yticks([5 + (5 * 2 * i) for i in range(len(completed_processes))])
        ax.set_yticklabels([f'P{p.pid}' for p in completed_processes])
        ax.set_xlabel('Time')
        ax.set_ylabel('Processes')
        ax.set_title(f'Process Execution Chart \nAvg Waiting Time: {avg_waiting_time}')
        ax.grid(True)
        plt.show()

        print(f"Average Waiting Time: {avg_waiting_time}")
