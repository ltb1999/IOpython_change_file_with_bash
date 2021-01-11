#!/usr/bin/env python3
import sys
import subprocess

file_name = sys.argv[1]
list_command = []
with open(file_name) as file:
 for line in file:
  line = line.strip('\n')
  new = line.replace('jane', 'jdoe')
  #print('mv /home/student-00-8d461feffe6d' + line + ' /home/student-00-8d461feffe6d' +new)
  subprocess.run(["mv",".."+line,".."+new])
file.close()
