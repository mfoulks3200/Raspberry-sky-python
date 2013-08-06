#!/usr/bin/python

import sys, getopt

def main(argv):
   launchtube = ''
   try:
      opts, args = getopt.getopt(argv,"hl:",["launchcode="])
   except getopt.GetoptError:
      print 'launchrocket.py -l <launch#>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'launchrocket.py -l <launch#>'
         sys.exit()
      elif opt in ("-l", "--launchcode"):
         launchtube = arg
   print 'Launch Rocket Tube - "', launchtube


if __name__ == "__main__":
   main(sys.argv[1:])
