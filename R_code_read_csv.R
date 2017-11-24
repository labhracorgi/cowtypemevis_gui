####Base script to just be able to load the files nicelt into R for statistical purposes:

#To import the pandas' Python csv created file correctly:
path_to_string_csv = "example/path/to/pandas/python/file.csv"
manual_string = read.csv(path_to_string_csv,
                         header = TRUE,row.names = 1)

#To access rownames:
rownames(manual_string)

#To set up a frequency plot of factors/categories:
freq_tab = table(manual_string$TYPE)
barplot(freq_tab)