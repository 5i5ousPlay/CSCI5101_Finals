from scheduler import Scheduler


def main():
    # Get number of processes from user
    while True:
        try:
            num_processes = int(input("Enter the number of processes: "))
            if num_processes > 0:
                break  # Exit the loop if a valid input is provided
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")

    scheduler = Scheduler()

    # Get arrival time and turnaround time for each process
    for i in range(num_processes):
        while True:
            try:
                arrival_time = int(input(f"Enter arrival time for process {i + 1}: "))
                if arrival_time >= 0:
                    break  # Exit the loop if a valid input is provided
                else:
                    print("Please enter a number greater than or equal to 0.")
            except ValueError:
                print("Please enter a valid integer.")

        while True:
            try:
                turnaround_time = int(input(f"Enter turnaround time for process {i + 1}: "))
                if turnaround_time >= 0:
                    break  # Exit the loop if a valid input is provided
                else:
                    print("Please enter a number greater than or equal to 0.")
            except ValueError:
                print("Please enter a valid integer.")

        scheduler.add_process(i+1, arrival_time, turnaround_time)

    # Get scheduling algorithm choice from user
    print("Choose a scheduling algorithm:")
    print("1. SJF Preemptive")
    print("2. Round Robin")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        scheduler.run_sjf_preemptive()
    elif choice == 2:
        time_quantum = int(input("Enter the time quantum for Round Robin: "))
        scheduler.run_round_robin(time_quantum)
    else:
        print("Invalid choice. Exiting.")
        return

    # clear / reset processes on scheduler
    scheduler.clear_processes()


if __name__ == "__main__":
    while True:
        main()

        try_again = input('Try Again (Y/N): ')
        if try_again == 'Y':
            continue
        elif try_again == 'N':
            break
        else:
            print("Invalid Input. Exiting.")
            break
