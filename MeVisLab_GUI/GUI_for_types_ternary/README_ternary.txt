---- README ----

MeVisLab GUI: TERNARY

This folder should contain:
	- (Functional) / gui_nameing_types_ternary.mlab / A MeVisLab GUI used to select 
		the types including hypo-plasticity.
	- (Functional) pandas_collecter_ternary_type.py / A Python script for collecting and 
		translating to notation. Possibly it could be enough to have a script that 
		collects them to pandas format. It has to take into account both "present" and 
		"hypoplastic" csv files.
	- (Functional) pandas_collecter_ternary_hypoplastic.py / A Python script for collecting
		 and translating to notation. Possibly it could be enough to have a script that 
		collects them to pandas format. It has to take into account both "present" and 
		"hypoplastic" csv files.
	- (Not created) / joint_collecter_ternary.py / A script to make a collective file
		of the type and hypoplastic, which is hoped to be easier to parse than two
		distinctive csvs.
		This script should also make a "reduced" binary case such that the hypoplastic and
		missing categories are merged and possible to compare with 3 other studies.
	- (Not created) /chemical_horikoshi_parser_ternary.py / A Python script that uses 
		the results from "joint_collecter_ternary.py" to parse them 
		into a single type only represented by a string.	
	- (Not created) / to_horikoshi2002_ternary_parser_ternary.py / A Python script to convert 
		raw ternary arrays to a format which is comparable with the classification used by 
		Horikoshi (2002).
	- (Not created) / to_krabbehartkamp1998_parser_ternary.py / A Python script to convert
		raw ternary arrays to a format which is compatible with the classification
		used by Krabbe-Hartkamp 1998.
	- (Not created) / type_comparison_ternary.py / A Python script for comparing 
		with automatic traces.
		It could base itself on a lot of loading syntax from the parser;
		except that two different collective csvs will be loaded.
