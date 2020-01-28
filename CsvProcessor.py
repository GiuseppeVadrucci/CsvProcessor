
import pandas as pd
import csv
import sys




class CsvProcessor:
 def __init__(self, fileToProcess, finalFile, column1, column2, column3):
  self.input = fileToProcess
  self.output = finalFile
  self.column1 = column1
  self.column2 = column2
  self.columnResult = column3
  self.result = 1					                                                   



 def converter(self):
  try:
   datContent = [i.strip().replace("*","").replace("-","").split() for i in open(self.input).readlines()]  

  except Exception as e:
   print("Error no file o input scorretto\n")
   print("Utilizzo: python fileprincipale.py <filedaprocessare> <nomefilerisultato>\n")
   exit(1)

  try:
   with open(self.output, "wb") as f:	 	                                                          
    writer = csv.writer(f)
    writer.writerows(datContent)

  except Exception as e:
    print("Errore nel file di output")

#metodo per fare la differenza tra le due colonne indicate
 def process(self, row):
  try:
    return float(row[self.column1]) - float(row[self.column2])                                             
  except:
    print("Problemi con il file in input, puo' essere un problema di nome delle colonne")


#metodo per restituire il risultato,  e inserisco la colonna con la differenza
 def Result(self):
  columns_to_keep = [self.columnResult, self.column1, self.column2]                                        
  dataframe = pd.read_csv(self.output, usecols=columns_to_keep)                                            
  dataframe['Result'] = dataframe.apply(self.process, axis=1)                                              
  self.result = dataframe.loc[dataframe['Result'].idxmin(), self.columnResult]                             
                                                                                                           						                                                                
  print ("\n\nLa differenza minima tra le colonne "+self.column1 +" e "+self.column2+ " corrisponde a "+self.columnResult +" "+ self.result+"\n\n")
