#automatic_manual_comparison.py

###Imports:
import pandas
import numpy

###Initialised constants:
base_manual_path = "/Volumes/LaCie/to_be_traced/photometry_other/photometry_ternary_csv/"
input_csv_manual_path = base_manual_path + "cow_manual_reduced_string.csv"

base_automatic_path = "/Volumes/LaCie/pkl_output/out_csv/"
input_csv_automatic_path = base_automatic_path + "cow_type_automatic_string.csv"

output_information_csv_path = base_manual_path + "results_cow_comparison.csv"
output_successratio_csv_path = base_manual_path + "results_success_ratio.csv"

###Main code:

print "Loading..."

df_manual = pandas.DataFrame.from_csv(input_csv_manual_path,parse_dates = False)
df_automatic = pandas.DataFrame.from_csv(input_csv_automatic_path,parse_dates = False)

#Do a test to check the properties of the datasets, matching IDs/index and column(s).

ids_manual = list(df_manual.index)
label_manual = list(df_manual.columns)

ids_automatic = list(df_automatic.index)
label_automatic = list(df_automatic.columns)

n_ids_manual = len(ids_manual)
n_labels_manual = len(label_manual)

n_ids_automatic = len(ids_automatic)
n_labels_automatic = len(label_automatic)

if(n_labels_manual == 1 and n_labels_automatic == 1):
	print "The labels are both of length 1, good!"
else:
	error("...")

if(n_ids_manual == n_ids_automatic):
	print "There are an equal number of IDs!"
	n_ids_difference = 0
	more_manual = 0
else:
	if(n_ids_manual > n_ids_automatic):
		print "There are more manual IDs than automatic IDs."
		more_manual = True
		n_ids_difference = n_ids_manual - n_ids_automatic
	if(n_ids_manual < n_ids_automatic):
		print "There are more automatic IDs than manual IDs."
		more_manual = False
		n_ids_difference = n_ids_automatic - n_ids_manual

#Ad-hoc quick fix, to difference...: 
dummy_ids_manual = [str(x) for x in ids_manual]
if(sorted(dummy_ids_manual) == sorted(ids_automatic)):
	print "The index/IDs are all matching!"
else:
	print "Not all index/IDs are matching, further information will be provided..."

if(sorted(label_manual) == sorted(label_automatic)):
	print "All the labels/columns are matching!"
else:
	print "Not all the labels are matching... THEY HAVE TO BE!"
	error("...")

included_id = [""]*min(n_ids_manual,n_ids_automatic)
garbage_id = [""]*100 #Assume no more than a 100 that has to be removed for comparison.
garbage_count = 0
included_count = 0
#Matching TYPE:
if(more_manual or more_manual == 0):
	print "The manual dataframe is used to look at the automatic dataframe."
	
	outer_loop_list_ids = ids_manual
	inner_loop_list_labels = label_manual
	
	df_source = df_manual
	df_lookup = df_automatic
	
	df_matching = df_manual #To ensure same size as "df_source".
	
	max_matches = min(n_ids_manual,n_ids_automatic)
	print "Maximum matches is: " + str(max_matches)
	
	#Check how many of the
	for k in outer_loop_list_ids:
		this_count = ids_automatic.count(str(k))
		if(this_count != 1):
			print "Clean up your data, multiple instances of an ID was found!"
			print str(k)
			garbage_id[garbage_count] = str(k)
			garbage_count = garbage_count + 1
		else:
			included_id[included_count] = str(k)
			included_count = included_count + 1	
else:
	print "The automatic dataframe is used to look at the manual dataframe."
	
	outer_loop_list_ids = ids_automatic
	inner_loop_list_labels = label_automatic
	
	df_source = df_automatic
	df_lookup = df_manual
	
	df_matching = df_automatic #To ensure same size as "df_source".
	
	max_matches = min(n_ids_manual,n_ids_automatic)
	print "Maximum matches is: " + str(max_matches)	
	
	for k in outer_loop_list_ids:
		this_count = ids_manual.count(int(k))
		if(this_count != 1):
			print "Clean up your data, multiple instances of an ID was found!"
			print str(k)
			garbage_id[garbage_count] = str(k)
			garbage_count = garbage_count + 1
		else:
			included_id[included_count] = str(k)
			included_count = included_count + 1	
	
if(included_count == max_matches):
	print "Every ID in the source dataframe is included in the lookup dataframe!"
else:
	print "Not all IDs in the source dataframe is in the lookup dataframe...!!!!!!!!!!"
	print "Now things might go wrong... Hopefully this shall not happen..."
	print garbage_id
	print "Saving it by using only the included ones."
	outer_loop_list_ids = included_id
	max_matches = len(included_id)
	print "A new list of IDs have been created together with a new maximum of possible matches."
	#Ideally this part of the code should not be activated if the other "limits" are strong enough.
	#"garbage_id" should be able to skip certain ids. But let us leave it at this.

print "*** Staring double-loop ***"

matches_count = 0
id_iter_count = 0
for i in outer_loop_list_ids:
	print "="*10
	print "Current ID: " + str(i) #This should make it evident which IDs are possibly causing error!
	print i
	
	for j in inner_loop_list_labels:
	##Pandas problemer, automatic har ID i "str", mens manual har i "numpy.int64"...
	#If one does go back to change anything the code might just become messed up...
	#Ad-hoc Quick-Fix of different index types...
		if(more_manual or more_manual == 0):
			current_source = df_source.loc[i].loc[j]
			current_lookup = df_lookup.loc[str(i)].loc[j] #What if "i", "j" does not exist in lookup?
		else:
			current_source = df_source.loc[i].loc[j]
			current_lookup = df_lookup.loc[int(i)].loc[j]
		
		if(current_source == current_lookup):
			matches_count = matches_count + 1
			current_match_status = "Match"
		else:
			current_match_status = "Not"
		print str(matches_count)
		df_matching.at[i,j] = current_match_status
		df_matching.at[i,"SOURCE"] = current_source
		df_matching.at[i,"LOOKUP"] = current_lookup
	#End inner label loop.
	
	id_iter_count = id_iter_count + 1
	print "="*10
	#End outer index loop.

print "*** Ending double-loop ***"

#Creating the success ratio and making it ready for csv.
success_ratio = numpy.float32(matches_count)/max_matches
print success_ratio
print "Success Ratio is: " + str(success_ratio)

df_sr = pandas.DataFrame(index = ["isr"],columns = ["csr"])
df_sr = df_sr.fillna(0)
df_sr.at["isr","csr"] = success_ratio

print "Saving..."

df_matching.to_csv(output_information_csv_path)

df_sr.to_csv(output_successratio_csv_path)

print "Done..."