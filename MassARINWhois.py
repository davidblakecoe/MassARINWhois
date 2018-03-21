#This script will take a file with IP addresses one per line and perform an ARIN whois lookup using the whois command built into most flavors of *nix
#There is minimum error handling, use at your own risk
import subprocess
import sys

if len(sys.argv) > 1: #ensure ip list is provided
  f=open(sys.argv[1], "r")
  for ip in f:
    if not ip.strip(): #skip blank lines
      continue
    else:
      try:
        output=subprocess.check_output("whois " + ip, shell=True) #run command line whois tool
      except:  #catch all error handling
        print("Whois Lookup Error on " + ip.strip())
      else:
        for line in output.splitlines(): #additional values can be added or removed to give you the details you need
          if "OrgName" in line:
            details = ip.strip() + ", " + line + ", "
          if "City" in line:
            details += line + ", "
          if "State" in line:
            details += line + ", "
          if "Country" in line:
            details += line
        print " ".join(details.split()) #remove annoying whitespaces and print results
else:
  print("Usage: MassWhois.py filname")
