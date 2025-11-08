##################################################### 3rd practical ##################################
# 1. String Concatenation
string1<- "Hello"
string2<- "World"
# Concatenating strings with a space
result_concat <- paste(stringl, string2)
cat("Concatenated String:\n", result_concat, "\n\n")

# 2. Substring Extraction
# Extract characters from 2nd to 4th position in a string
substring_result <- substr(string1, 2, 4)
cat("Substring from 'Hello' (2nd to 4th position):\n", substring_result, "\n\n")

# 3. Changing Case
uppercase <- toupper(stringl) # Convert to uppercase
lowercase <- tolower(string2)
cat("Uppercase:\n", uppercase, "\nLowercase:\n", lowercase, "\n\n")

# 4. String Length
length_stringl <- nchar(string1)
length_string2 <- nchar(string2)
cat("Length of 'Hello':", length_string1, "\n")
cat("Length of 'World':", length_string2, "\n\n")

# 5. String Replacement
text <- "R is a great programming language"
replaced_text <- sub("great", "fantastic", text) # Replace the first occurrence
cat("Original Text:\n", text, "\n")
cat("After Replacement:\n", replaced_text, "\n\n")

# 6. Splitting Strings
sentence <- "R is powerful for data science"
split_result <- strsplit(sentence, " ") # Split by space
cat("Splitting the sentence into words:\n")
print(split_result)

# 7. Joining Strings from a Vector
words <- c("Data", "Science", "is", "fun")
joined_string <- paste(words, collapse ="-")
cat("\nJoined String:\n", joined_string, "\n\n")

# 8. Detecting Patterns
pattern <- "data"
is_present <- grepl(pattern, sentence, ignore.case = TRUE) # Case-insensitive search
cat("Is 'data' present in the sentence ?: ", is_present, "\n\n")

# 9. Finding and Replacing Patterns
pattern_replacement <- gsub("data", "information", sentence, ignore.case = TRUE)
cat("After Pattern Replacement:\n", pattern_replacement, "\n\n")

# 10. Trimming whites paces
string_with_spaces <- " Trim me "
trimmed_string <- trimws(string_with_spaces)
cat("Original String with spaces:\n'", string_with_spaces, "'\n", sep = "")
cat("Trimmed String:\n'", trimmed_string, "'\n", sep = "")

########################################### 4th practical ################################################
########################################### 4th practical ################################################
########################################### 4th practical ################################################


# Sample data
data <- c(12, 15, 20, 22, 18, 15, 15, 17, 19, 22, 24)

# 1. Mean
mean_value <- mean(data)
cat("Mean of the data:\n", mean_value, "\n\n")

# 2. Median
median_value <- median(data)
cat("Median of the data:\n", median_value, "\n\n")

# 3. Mode
# Defining a custom function to calculate mode
calculate_mode <- function(x) {
  freq_table <- table(x) # Frequency of each value
  mode_values <- as.numeric(names(freq_table[freq_table == max(freq_table)]))
  return(mode_values)
}
  
  mode_value <- calculate_mode(data)
  cat("Mode of the data:\n", mode_value, "\n\n")
  
  # 4. Variance
  variance_value <- var(data)
  cat("Variance of the data:\n", variance_value, "\n\n")
  
  # 5. Standard Deviation
  std_dev_value <- sd(data)
  cat("Standard Deviation of the data:\n", std_dev_value, "\n\n")
  
  # 6. Summary of data (Optional)
  cat("Summary of the data: \n")
  print (summary(data))




