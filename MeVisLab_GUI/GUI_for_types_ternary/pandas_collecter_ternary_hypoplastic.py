#Pandas collecter:
#	Output should be usable with "chemical_horikoshie_parser.py".

#Uses codes and ideas from "output_decoder.py" and "chemical_horikoshi_parser.py".

#Imports
import os
import glob
import pandas
import numpy
import sys #Assume that this is to be run in a terminal python call!

#The order should not be tampered with...
artery_labels = ["ICA-L","ICA-R","MCA1-L","MCA1-R",
"ACA1-L","ACA1-R","AComA",
"PComA-L","PComA-R","PCA1-L","PCA1-R",
"VBA"]

#Constant paths:
csv_output_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_ternary_csv/cow_manual_hypo.csv"

base_path = "/Volumes/LaCie/to_be_traced/photometry/"

###Anything below here should not require modifications once it's complete!###

numpy_array_csv_paths = glob.glob(os.path.join(base_path,"*/3D_TOF/raw_ternary_hypo.csv"))

n_artery_labels = len(artery_labels)
n_csv_paths = len(numpy_array_csv_paths)
n_ids = n_csv_paths

#Matrix to convert to pandas format: (empty at the start)
type_matrix = numpy.zeros((n_ids,n_artery_labels))

#IDs that need to be in the same order as the paths are appended to the matrix.
ID_labels_part_1 = [w.replace("/3D_TOF/raw_ternary_hypo.csv", "") for w in numpy_array_csv_paths] 
ID_labels = [w.replace(base_path, "") for w in ID_labels_part_1] 

#Checks.
if (len(ID_labels) == n_ids):
	print "Same length, ok!"
else:
	print "Something is wrong with the labels...!"
	sys.exit("Exiting as a result...")

print "="*10
print "All the working paths are:"
print numpy_array_csv_paths
print "="*2
print "All the IDs are:"
print ID_labels
print "="*10

print "*** Starting the loop ***"
#Starts path loop.
id_counter = 0
for i in numpy_array_csv_paths:
	print "="*10
	print "Current working path is: " + i
	print "Current ID is: " + ID_labels[id_counter]
	
	#Extract relevant type:
	current_array = numpy.loadtxt(i).astype(int)
	
	#Add "current_array" to row number "id_counter":
	type_matrix[id_counter] = current_array
	
	id_counter = id_counter + 1
	print "Finished with this individual."
	#End of path loop.
print "*** Ending the loop ***"
#Collect it all and put it into a dataframe:
df_output = pandas.DataFrame(type_matrix.astype(int),
columns = artery_labels,index = ID_labels)
#Export to csv:
df_output.to_csv(csv_output_path)

print("Done...")