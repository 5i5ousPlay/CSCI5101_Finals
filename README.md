# CSCI 51.01 - Lecture Finals Project (Implementation)

_Submitted by Raul Jarod Conanan (Section F) in partial fulfillment of the finals project for CSCI 51.01: Operating
Systems - Lecture_

# Running the Program

The following program can be exclusively ran with and through any command terminal whose system has
Python 3 installed. (Python 3.11 + recommended)

## Create Virtual Environment

Upon extracting the files, in the directory where the files are stored, open the command line and create a Python
virtual environment using the command `python -m venv <virtual_environment_name>`. If you do not have virtualenv 
installed, enter the command `pip install virtualenv` and then try creating the new virtual environment again.

## Installing Requirements

Provided alongside the files in project is a `requirements.txt` file containing all the necessary dependencies needed
for running the program. While in the same directory as the created virtual environment, use the terminal to make sure 
that the virtual environment is started by entering `<virtual_environment_name>\Scripts\activate`. When the virtual 
environment is active, enter `pip install -r requirements.txt` into the terminal to install the needed dependencies.

## Starting / Using the Program

To start and use the program, input `python main.py`. When the program is running it will ask for the number
of processes to run. It will then ask for the respective arrival and burst times (process durations). It will then
ask for the type of scheduling algorithm to simulate: Shortest Job First Preemptive [1] or Round Robin [2]. If 
Round Robin is selected, the user will be prompted to provide the time quantum for the Round Robin scheduler. A 
gantt chart will then be generated illustrating the execution of the different processes given the particular 
scheduling algorithm as well as displaying the average waiting time. The command line will also print out the average
waiting time of the given inputs. Exiting the window of the gantt chart will continue the program providing the user
with the prompt to try again (Y/N). If the user inputs 'Y' the process will repeat, else the program will exit.
