#To Horikoshi 2002 notation, from raw arrays:
#	Direct copy from "chemical_horikoshi_parser.py" and just some slight modifications...	

####Imports
import pandas

#####Initialised constants:

base_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_csv/"
input_csv_path = base_path + "cow_manual_type.csv"
output_csv_string_path = base_path + "cow_manual_horikoshitype_string.csv"

#The order is strictly important and necessary to keep.
label_parser_dict = {"ICA-L":"","ICA-R":"",
					"MCA1-L":"","MCA1-R":"",
					"ACA1-L":"Al","ACA1-R":"Ar",
					"AComA":"","PComA-L":"","PComA-R":"",
					"PCA1-L":"Pl","PCA1-R":"Pr",
					"VBA":""} 
					#This parser does not take into account doubly missing arteries.
					#Though, the code down below can be customised to account for that.

####Main --- Naive parser ---

print "Loading..."
df = pandas.DataFrame.from_csv(input_csv_path,parse_dates = False)

#Use these to make a double for loop.
all_ids = list(df.index)
all_labels = list(df.columns)

n_ids = len(all_ids)
n_labels = len(all_labels)

result_string_list = [""]*n_ids

print "="*10
print "These are all the IDs: "
print all_ids
print "="*3
print "These are all the labels: "
print all_labels
print "="*10

print "*** Starting ID loop ***"
id_iter = 0
for i in all_ids:
	print "="*10
	print "ID: " + str(i)
	
	current_id = i
	description_string = ""
	
	for j in all_labels:
		current_label = j
		boolean_var = df.loc[[current_id],[j]].iloc[0][0]
		
		if (boolean_var == 0): #Change 0 to 1 if the opposite interpretation is needed.
			description_string = description_string + label_parser_dict[current_label]
			#End if.
		#End label loop.
	
	#Show and collect the string together with the ID.
	print(description_string)
	
	description_string = description_string.replace("Al","A")
	description_string = description_string.replace("Ar","A")
	description_string = description_string.replace("Pl","P")
	description_string = description_string.replace("Pr","P")
	
	if(description_string == ""):
		description_string = "O"
	
	print(description_string)
	result_string_list[id_iter] = description_string
	id_iter = id_iter + 1
	print "="*10
	#End id loop.
print "*** Ending ID loop ***"
####End main

print "Collecting..."
df_output_string = pandas.DataFrame(result_string_list,index = all_ids,columns = ["TYPE"])

print "Saving..."
df_output_string.to_csv(output_csv_string_path)

print "Done..."
