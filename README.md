# Eureka

As a performance analyst I had to deal usually with experiments involving automated tasks with Bash, data generation and plotting.
I used to do all this manually but I was spending a lot of time dealing with file system related stuff.
This tool provides an higher level of abstraction setting the environment for a new experiment, running bash and gnuplot scripts directly from the its interface

### Architecture
This Python3 script makes use of ```os```, ```shutil``` and ```subprocess``` modules to interface with the file system and running external scripts
The programs does not create any additional file to keep track of the environment in order to not have any problems involving inconsistencies of the project setup

### Customization
The sample files that are copied in each new experiment are copied from the ```sample/``` directory in the root project folder. If a different starting point is desidered, edit 
```
samples/plot.gp
samples/script.sh
``` 

Installation
```
cd && git clone https://github.com/DanX3/eureka
```

Then create a symbolic link to the file ```eureka/src/main.py``` where your PATH is looking for. For example, I have a ```~/bin``` folder so I should do
```
cd ~/bin && ln -s ~/eureka/src/main.py eureka
```