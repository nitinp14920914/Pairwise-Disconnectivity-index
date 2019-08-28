library(STRINGdb)
get_STRING_species(version="10", species_name=NULL)
cat("Enter ID: ")
a <- readLines(con="stdin", 1)
cat(a,"\n")
a <- as.numeric(a)
#n <- as.integer(readline(prompt = "Enter an species id : "))
string_db <- STRINGdb$new( version="10", species=a  ,score_threshold=0, input_directory="./out" )
string_db
