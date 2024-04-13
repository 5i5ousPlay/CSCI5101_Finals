import unittest
from scheduler import Scheduler


class TestScheduler(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def _get_avg_waiting_time_sjf(self, programs: list[list]):
        for i in range(len(programs)):
            self.scheduler.add_process(i+1, programs[i][0], programs[i][1])
        completed_processes = self.scheduler._sjf_preemptive_algo(self.scheduler.processes)
        avg_waiting_time = self.scheduler._get_avg_waiting_time(completed_processes)

        self.scheduler.clear_processes()

        return avg_waiting_time

    def _get_avg_waiting_time_round_robin(self, programs: list[list], time_quantum):
        for i in range(len(programs)):
            self.scheduler.add_process(i+1, programs[i][0], programs[i][1])
        completed_processes = self.scheduler._round_robin_algo(self.scheduler.processes, time_quantum)
        avg_waiting_time = self.scheduler._get_avg_waiting_time(completed_processes)

        self.scheduler.clear_processes()

        return avg_waiting_time

    def test_avg_waiting_time_sjf(self):
        test_1 = [[0, 4], [1, 3], [2, 2], [3, 1]]
        test_2 = [[0, 3], [1, 1], [2, 2], [3, 4]]
        test_3 = [[0, 2], [1, 2], [2, 2], [3, 2]]
        test_4 = [[0, 1], [1, 3], [2, 2], [3, 4]]
        test_5 = [[0, 5], [1, 2], [2, 3], [3, 1]]
        test_6 = [[0, 5], [1, 3], [2, 6], [3, 7]]

        test_1_waiting_time = self._get_avg_waiting_time_sjf(test_1)
        self.assertEqual(test_1_waiting_time, 2.5)

        test_2_waiting_time = self._get_avg_waiting_time_sjf(test_2)
        self.assertEqual(test_2_waiting_time, 1.5)

        test_3_waiting_time = self._get_avg_waiting_time_sjf(test_3)
        self.assertEqual(test_3_waiting_time, 1.5)

        test_4_waiting_time = self._get_avg_waiting_time_sjf(test_4)
        self.assertEqual(test_4_waiting_time, 1.25)

        test_5_waiting_time = self._get_avg_waiting_time_sjf(test_5)
        self.assertEqual(test_5_waiting_time, 2)

        test_6_waiting_time = self._get_avg_waiting_time_sjf(test_6)
        self.assertEqual(test_6_waiting_time, 5)

    def test_avg_waiting_time_round_robin(self):
        test_1 = [[0, 5], [1, 3], [2, 8], [3, 6], [4, 4]]
        test_2 = [[0, 4], [1, 5], [2, 3], [3, 7], [4, 2]]
        test_3 = [[0, 2], [1, 7], [2, 4], [3, 6], [4, 3]]
        test_4 = [[0, 3], [1, 4], [2, 6], [3, 2], [4, 5]]
        test_5 = [[0, 6], [1, 2], [2, 5], [3, 3], [4, 4]]
        test_6 = [[0, 5], [1, 3], [2, 6], [3, 7]]

        time_quanta = [2, 3, 4, 5, 6]

        test_1_waiting_time = self._get_avg_waiting_time_round_robin(test_1, time_quanta[0])
        self.assertEqual(test_1_waiting_time, 12.6)

        test_2_waiting_time = self._get_avg_waiting_time_round_robin(test_2, time_quanta[1])
        self.assertEqual(test_2_waiting_time, 8.8)

        test_3_waiting_time = self._get_avg_waiting_time_round_robin(test_3, time_quanta[2])
        self.assertEqual(test_3_waiting_time, 7.8)

        test_4_waiting_time = self._get_avg_waiting_time_round_robin(test_4, time_quanta[3])
        self.assertEqual(test_4_waiting_time, 6.6)

        test_5_waiting_time = self._get_avg_waiting_time_round_robin(test_5, time_quanta[4])
        self.assertEqual(test_5_waiting_time, 6.6)

        test_6_waiting_time = self._get_avg_waiting_time_round_robin(test_6, time_quanta[1])
        self.assertEqual(test_6_waiting_time, 7.75)


if __name__ == '__main__':
    unittest.main()
