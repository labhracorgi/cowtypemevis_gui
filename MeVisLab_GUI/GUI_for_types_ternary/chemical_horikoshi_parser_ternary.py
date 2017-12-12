#Parser for chemical Horikoshi CoW notation formula:

####Imports
import pandas

#####Initialised constants:

base_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_ternary_csv/"
input_csv_path = base_path + "cow_manual_joint.csv"
output_csv_string_path = base_path + "cow_manual_joint_string.csv"

#The order is strictly important and necessary to keep.
label_parser_dict = {"ICA-L":"Il","ICA-R":"Ir",
					"MCA1-L":"Ml","MCA1-R":"Mr",
					"ACA1-L":"Al","ACA1-R":"Ar",
					"AComA":"Ac","PComA-L":"Pcl","PComA-R":"Pcr",
					"PCA1-L":"Pl","PCA1-R":"Pr",
					"VBA":"V"}

label_parser_dict_hypo = {"ICA-L":"Ilh","ICA-R":"Irh",
					"MCA1-L":"Mlh","MCA1-R":"Mrh",
					"ACA1-L":"Alh","ACA1-R":"Arh",
					"AComA":"Ach","PComA-L":"Pclh","PComA-R":"Pcrh",
					"PCA1-L":"Plh","PCA1-R":"Prh",
					"VBA":"Vh"}

####Main --- Naive ternary parser ---

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
		if (boolean_var == -1): #This should indicate that it is hypoplastic
			description_string = description_string + label_parser_dict_hypo[current_label]
			#End if.
		#End label loop.
	
	#Show and collect the string together with the ID.
	print(description_string)
	
	description_string = description_string.replace("IlIr","2I")
	description_string = description_string.replace("IlhIr","2hI")
	
	description_string = description_string.replace("MlMr","2M")
	description_string = description_string.replace("MlhMr","2hM")
	
	description_string = description_string.replace("AlAr","2A")
	description_string = description_string.replace("AlhAr","2hA")
	
	description_string = description_string.replace("PclPcr","2Pc")
	description_string = description_string.replace("PclhPcr","2hPc")
	
	description_string = description_string.replace("PlPr","2P")
	description_string = description_string.replace("PlhPr","2hP")
	
	#As such, an "h" before the capitalised label will indicate hypoplastic left side,
	# while an "h" after the capitalised label will indicate hypoplastic right side.
	# The alternative would be to remove this shorthand notation to differentiate. If
	# that is desired then just comment out this .replace functions.
	
	
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


