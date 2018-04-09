import os
import shutil
import json
import subprocess
from utils import *

class main: 
    def __init__(self):
        self.EUREKA_HOME = os.path.dirname(os.path.abspath(__file__))[0:-3]
        while True:
            print("> ", end='')
            new_command = input()
            self.execute(new_command)

    def info(self):
        print("Eureka v 0.0.1")
        print("in", self.EUREKA_HOME)

    def environ(self):
        for key, value in os.environ.items():
            print(key, value)

    def print_help(self, command):
        if command == "exp":
            print("exp <experiment>")
        elif command == "plot":
            print("plot <experiment>")
        else:
            print("{:10s} : creates the environment for a new experiment".format("new | n"))
            print("{:10s} : prints basic information about the platform".format("info"))
            print("{:10s} : prints environment variables".format("environ"))
            print("{:10s} : quit the program".format("quit | q"))
            print("{:10s} : run the plot function for an experiment".format("plot"))
            print("{:10s} : prints this help message".format("help"))
            print("{:10s} : show current experiment set".format("exp | ls"))

    def create_experiment(self, command):
        words = cmd_has_name(command)
        if not words:
            print_help("new")
            return

        name = words[1]
        
        # Checking if a directory with the same name exists
        if directory_exists(name):
            print("Directory %s already exists. Skipping..." % name)
            return

        os.mkdir(os.getcwd() + '/' + name)
        os.chdir(name)
        shutil.copy(self.EUREKA_HOME + "/samples/plot.gp", os.getcwd())
        shutil.copy(self.EUREKA_HOME + "/samples/script.sh", os.getcwd())
        print("Created a project in", os.getcwd())
        os.chdir('../')


    def run_experiment(self, command):
        words = cmd_has_name(command)
        if not words:
            print_help("run")
            return

        name = words[1]
        if not directory_exists(name):
            print("{:s}: experiment does not exists".format(name))
            return
        os.chdir(name)
        subprocess.call("./script.sh")
        os.chdir('../')

    def initialize(self, command):
        if not cmd_has_name(command):
            print_help("init")
            return
        name = command.split(' ')[1]
        os.mkdir(os.getcwd() + "/" + name)
        os.chdir(name)

    def show_experiments(self):
        ls = os.scandir(os.getcwd())
        for direntry in ls:
            if direntry.is_file():
                continue
            if is_experiment(direntry.name):
                print(direntry.name)

    def plot_experiment(self, command):
        words = cmd_has_name(command)
        if not words:
            print_help("plot")
            return

        if directory_exists(words[1]):
            os.chdir(words[1])
            subprocess.call(['gnuplot', 'plot.gp'])
            os.chdir('../')


    def remove_experiment(self, command):
        words = cmd_has_name(command)
        if not words:
            print_help("remove")
            return
        if not is_experiment(words[1]):
            print("\"{:s}\" is not an experiment".format(words[1]))
            return

        confirm = input('Do you really want to delete experiment \"{:s}\" (y/N) '.format(words[1]))
        if confirm.lower() not in ['y', 'yes']:
            return
        os.chdir(words[1])
        ls = os.scandir(os.getcwd())
        for direntry in ls:
            os.remove(direntry.name)
        os.chdir('../')
        os.rmdir(words[1])
        print('Experiment \"{:s}\" has been deleted'.format(words[1]))


    def execute(self, line):
        command = line.split(' ')[0]
        if command == "info":
            self.info()
        elif command in ["quit", 'q']:
            exit()
        elif command == "environ":
            self.environ()
        elif command in ["new", "n"]:
            self.create_experiment(line)
        elif command in ["help", "h"]:
            self.print_help("")
        elif command == "run":
            self.run_experiment(line)
        elif command in ["exp", "ls"]:
            self.show_experiments()
        elif command == "plot":
            self.plot_experiment(line)
        elif command == "remove":
            self.remove_experiment(line)
        elif command == "":
            pass
        else:
            print("{:s}: command not found".format(command))

if __name__ == "__main__":
    instance = main()
