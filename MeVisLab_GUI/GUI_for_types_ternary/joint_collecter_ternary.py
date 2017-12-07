#joint_collecter_ternary.py
##	Script intended to merge the two separate csvs about "type" and "hypoplasticity" to
##	2 other csvs. One which extends the ternary classification and another
##	which reduces the ternary case to the binary case such that the earlier scripts
##	from the binary case can be used.

#Idea: Let us create two independent pandas matrices from the "type" csv, then use "hypo"
#	to modify the two matrices according to 2 different rules.

###Imports:
import pandas

###Initialised constants:
base_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_ternary_csv/"

input_csv_type_path = base_path + "cow_manual_type.csv"
input_csv_hypo_path = base_path + "cow_manual_hypo.csv"

output_csv_string_joint_path = base_path + "cow_manual_joint.csv"
output_csv_string_reduced_path = base_path + "cow_manual_reduced.csv"

###Main code:

print "Loading..."

df_joint = pandas.DataFrame.from_csv(input_csv_type_path,parse_dates = False)
df_reduced = pandas.DataFrame.from_csv(input_csv_type_path,parse_dates = False)

df_hypo_mod = pandas.DataFrame.from_csv(input_csv_hypo_path,parse_dates = False)


#Do a check between the "hypo" and "type" csv that the same elements actually exists...
all_ids = list(df_joint.index)
all_labels = list(df_joint.columns)

n_ids = len(all_ids)
n_labels = len(all_labels)

all_hypo_ids = list(df_hypo_mod.index)
all_hypo_labels = list(df_hypo_mod.columns)

n_hypo_ids = len(all_hypo_ids)
n_hypo_labels = len(all_hypo_labels)

if (n_ids == n_hypo_ids):
	print "Same number of IDs... OK!"
else:
	print "Not the same number of IDs... Aborting..."
	error("...")

if (n_labels == n_hypo_labels):
	print "Same number of labels... OK!"
else:
	print "Not the same number of labels... Aborting..."
	error("...")

if(sorted(all_ids) == sorted(all_hypo_ids)):
	print "The IDs are identical too!"
else:
	print "The IDs are not identical... Aborting"
	error("...")

if(sorted(all_labels) == sorted(all_hypo_labels)):
	print "The labels are identical too!"
else:
	print "The labels are not identical... Aborting..."
	error("...")


print "="*10
print "These are all the " + str(n_ids) + " IDs: "
print all_ids
print "="*3
print "These are all the " + str(n_labels) + " labels: "
print all_labels
print "="*10

print "*** Starting loop ***"

for i in all_ids:
	print "="*10
	print "ID: " + str(i)
	
	for j in all_labels:
		print "Label: " + str(j)
		
		type_value = df_joint.loc[[i],[j]].iloc[0][0]
		hypo_value = df_hypo_mod.loc[[i],[j]].iloc[0][0]
		
		#The case which changes values.
		if(type_value == 1 and hypo_value == 1):
			df_joint.at[i,j] = -1
			df_reduced.at[i,j] = 0
		
		#The case which is not allowed in joint mode.
		if(type_value == 0 and hypo_value == 1):
			print "Something went wrong, most likely in the classification GUI"
			print "Check this ID: " + str(i) + " and at this label: " + str(j)
			print "Aborting..."
			error("...")

	print "Finished with this ID..."
	print "="*10
	
print "*** Ending loop ***"
###End main code

print "Saving..."

df_joint.to_csv(output_csv_string_joint_path)
df_reduced.to_csv(output_csv_string_reduced_path)

print "Done..."
