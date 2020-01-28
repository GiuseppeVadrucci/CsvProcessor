# CsvProcessor
A class to convert a table.dat in a table.csv, to perform differenze between two columns and to print the value with the minimum difference from a result column.


Usage:

Create a file .py for example test.py with the following code:

#########################################

import CsvProcessor as csp 					                                  
import sys  


p1 = csp.CsvProcessor(sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])              
p1.converter()             				                                          
p1.Result()   
#########################################

And launch from terminal:

python test.py weather.dat weather.csv MxT MnT Dy 

or 

python test.py football.dat football.csv F A Team
