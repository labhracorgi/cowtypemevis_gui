---- README ----

MeVisLab GUI: TERNARY

This folder should contain:
	- (Functional) / GUI_for_types_ternary.mlab / A MeVisLab GUI used to select 
		the types including hypo-plasticity.
	- (Functional) pandas_collecter_ternary_type.py / A Python script for collecting and 
		translating to notation. Possibly it could be enough to have a script that 
		collects them to pandas format. It has to take into account both "present" and 
		"hypoplastic" csv files.
	- (Functional) pandas_collecter_ternary_hypoplastic.py / A Python script for collecting
		 and translating to notation. Possibly it could be enough to have a script that 
		collects them to pandas format. It has to take into account both "present" and 
		"hypoplastic" csv files.
	- (Functional) / joint_collecter_ternary.py / A script to make a collective file
		of the type and hypoplastic, which is hoped to be easier to parse than two
		distinctive csvs.
		This script should also make a "reduced" binary case such that the hypoplastic and
		missing categories are merged and possible to compare with 3 other studies.
	- (Functional) / chemical_horikoshi_parser_ternary.py / A Python script that uses 
		the "joint" output from "joint_collecter_ternary.py" to parse them 
		into a single ternary/joint type only represented by a string.
	- (Functional) / chemical_horikoshi_parser_ternary_reduced.py / A Python script that 
		uses the "reduced" output from "joint_collecter_ternary.py" to parse them into
		a single binary/reduced type only represented by a string.
	- (Functional) / to_horikoshi2002_parser_reduced.py / A Python script that parses the
		reduced/binary output from "joint_collecter_ternar.py" to a string type which is
		comparable with Horikoshi (2002) notation.
	- (Functional) / to_krabbehartkamp1998_parser_reduced.py / A Python script that parses 
		the reduced/binary output from "joint_collecter_ternar.py" to a string type which 
		is comparable with Krabbe-Hartkamp (1998) notation.
	- (Functional) / automatic_manual_comparison.py / A Python script for comparing 
		with automatic traces; it will base itself on "reduced" output type parsed or not.
		It could base itself on a lot of loading syntax from the parser;
		except that two different collective csvs will be loaded.
		Perhaps only the binary one is enough..?
		Definitely requires that the images that are not contained in the other, somehow,
		is "removed" when comparing as it just isnt possible...
		Do it with an intermediate "new" list of IDs.