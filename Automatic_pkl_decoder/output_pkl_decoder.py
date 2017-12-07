#Output decoder of David Robben's algorithm:

#####Imports:
import pickle
import numpy
import pandas
import sys
import glob
import os

##########Constants initialised:
pickle_input_path = "/Volumes/LaCie/pkl_output/out/"
csv_output_path = "/Volumes/LaCie/pkl_output/out_csv/cow_type_automatic.csv"

matching_labels = ["ICA-L","ICA-R","MCA1-L","MCA1-R",
"ACA1-L","ACA1-R","AComA",
"PComA-L","PComA-R","PCA1-L","PCA1-R",
"VBA"]

os.chdir(pickle_input_path)
glob_string = "*/3d_tof.pkl"
all_ids = glob.glob(glob_string)

n_match_labels = len(matching_labels)
n_tot_id = len(all_ids)

type_matrix = numpy.zeros((n_tot_id,n_match_labels)) 
ID_labels = [w.replace("/3d_tof.pkl","") for w in all_ids]

individual_iter = 0 

##########Main code segment for iterating through individuals:
for id_label in all_ids:
	print "="*10
	print "ID: " + id_label
	print ID_labels[individual_iter]
	
	id_pickle_path = pickle_input_path + id_label
	f = open(id_pickle_path)
	
	current_person = pickle.load(f)
	
	all_node = current_person.nodes()
	all_edge_pairs = current_person.edges()
	
	n_node = len(all_node)
	n_edge_pairs = len(all_edge_pairs)
	
	all_labels = ["NaA"] * n_edge_pairs
	
	#Find all present labels:
	counter = 0
	for i in all_edge_pairs:
		
		first_key = i[0]
		second_key = i[1]
		
		this_edge_label = current_person.edge[first_key][second_key]["label"]
		
		all_labels[counter] = this_edge_label
		counter = counter + 1
		#End the label finding loop here.
	
	unique_labels = numpy.unique(all_labels)
	
	#Test if "unique_labels" have a "NaA" still
	if any(unique_labels == "NaA"):
		print("Warning: ___NaA___ still present in the unique label container.")
		error("Exiting due to possibly fatal error in decoding; see above.")
	else:
		print("Ok!")	
	
	#Match present labels with matching labels:
	type_array = [0]*n_match_labels
	######How to interpret the "type_array":
	##The order of the matching labels will correspond to which order
	## the arteries are denoted as present (=1) or missing (=0) in "type_array";
	## they are missing by default.
	
	counter = 0
	for j in matching_labels:
		
		if any(unique_labels == j):
			print "Match with: " + j
			type_array[counter] = 1
		else:
			print "No match with: " + j
		
		counter = counter + 1
		#End the label matching loop here.
	
	#Add the types before continuing to the next individual.
	print(type_array)
	type_matrix[individual_iter] = type_array
	individual_iter = individual_iter + 1
	print "This individual is done..."
	####END of iterative main

#Collect it all and put it into a dataframe:
df_output = pandas.DataFrame(type_matrix.astype(int),
							columns = matching_labels,index = ID_labels)
#Export to csv:
df_output.to_csv(csv_output_path)
