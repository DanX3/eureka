import os

def cmd_has_name(line):
    words = line.split(' ')
    if len(words) <= 1:
        return []
    return words

def directory_exists(name):
    ls = os.scandir(os.getcwd())
    for direntry in ls:
        if name == direntry.name:
            return True
    return False

def is_experiment(name):
    if not directory_exists(name):
        return False
    os.chdir(name)
    ls = os.scandir(os.getcwd())
    scriptPresent = False
    plotPresent = False
    for innerdir in ls:
        if innerdir.name == "script.sh":
            scriptPresent = True
        if innerdir.name == "plot.gp":
            plotPresent = True
    os.chdir('../')
    if scriptPresent and plotPresent:
        return True
    return False


