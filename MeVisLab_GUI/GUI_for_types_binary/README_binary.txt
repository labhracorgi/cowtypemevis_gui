---- README ----

MeVisLab GUI: BINARY

This folder should contain:
	- (Functional) / gui_nameing_binary_types.mlab / A MeVisLab GUI used to select 
		the types/configurations.
	- (Functional) / pandas_collecter_binary.py / A Python script for collecting and 
		translating to notation. Possibly it could be enough to have a script that 
		collects them to pandas format.
	- (Functional) /chemical_horikoshi_parser_binary.py / A Python script that uses 
		the results from "pandas_collecter.py" to parse them 
		into a single type only represented by a string.	
	- (Functional) / to_horikoshi2002_parser_binary.py / A Python script to convert raw 
		binary arrays to a format which is comparable with the classification used by 
		Horikoshi (2002).
	- (Functional) / to_krabbehartkamp1998_parser_binary.py / A Python script to convert
		raw binary arrays to a format which is compatible with the classification
		used by Krabbe-Hartkamp 1998.
	- (Not created) / type_comparison_binary.py / A Python script for comparing 
		with automatic traces (D. Robben's algorithm).
		It could base itself on a lot of loading syntax from the parser;
		except that two different collective csvs will be loaded.