#To Krabbe-Hartkamp 1998 notation:
#	Most of the code should be similar to the "chemical_horikoshi_parser.py"...

####Imports
import pandas

#####Initialised constants:

base_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_csv/"
input_csv_path = base_path + "cow_manual_type.csv"
output_csv_string_path = base_path + "cow_manual_krabbehartkamptype_string.csv"
output_csv_value_path = base_path + "cow_manual_krabbehartkamptype_value.csv"

#The order is strictly important and necessary to keep.
label_parser_dict = {"ICA-L":"A","ICA-R":"A",
					"MCA1-L":"A","MCA1-R":"A",
					"ACA1-L":"A","ACA1-R":"A",
					"AComA":"A","PComA-L":"P","PComA-R":"P",
					"PCA1-L":"P","PCA1-R":"P",
					"VBA":"P"} 
					#This parser only takes into account which part is anterior or posterior
					# according to Krabbe-Hartkamp 1998 to be able to classify correctly.
					
####Main --- Naive parser ---

print "Loading..."
df = pandas.DataFrame.from_csv(input_csv_path,parse_dates = False)

#Use these to make a double for loop.
all_ids = list(df.index)
all_labels = list(df.columns)

n_ids = len(all_ids)
n_labels = len(all_labels)

result_string_list = [""]*n_ids
result_value_list = [-1]*n_ids

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
	description_value = -1
	
	anterior_complete = True
	posterior_complete = True
	
	for j in all_labels:
		current_label = j
		boolean_var = df.loc[[current_id],[j]].iloc[0][0]
		
		if (boolean_var == 0): #Change 0 to 1 if the opposite interpretation is needed. Though this will wreck the upcoming code...
			description_string = description_string + label_parser_dict[current_label]
			#End if.				
		#End label loop.
	
	#Show and collect the string together with the ID.
	print(description_string)
	
	if(description_string.find("A") > -1):
		print "Found an A"
		anterior_complete = False
	if(description_string.find("P") > -1):
		print "Found a P"
		posterior_complete = False
	
	print "These are the two booleans: " 
	print "Anterior complete:"
	print anterior_complete
	print "Posterior complete:"
	print posterior_complete
	
	if(anterior_complete or posterior_complete):
		description_string = "partial"
		description_value = 2
	if(anterior_complete and posterior_complete):
		description_string = "complete"
		description_value = 3
	if((not anterior_complete) and (not posterior_complete)):
		description_string = "incomplete"
		description_value = 1
	
	print(description_string)
	result_string_list[id_iter] = description_string
	result_value_list[id_iter] = description_value
	id_iter = id_iter + 1
	print "="*10
	#End id loop.
print "*** Ending ID loop ***"
####End main

print "Collecting..."
df_output_string = pandas.DataFrame(result_string_list,index = all_ids,columns = ["TYPE"])
df_output_value = pandas.DataFrame(result_value_list,index = all_ids,columns = ["TYPE"])

print "Saving..."
df_output_string.to_csv(output_csv_string_path)
df_output_value.to_csv(output_csv_value_path)

print "Done..."


