##################################### 7th practical ###############################################
# Load necessary library (optional for visualization)
library(ggplot2)
#1. Create a dataset
# Independent variables
# Predictor 1
age <- c(25, 30, 35, 40, 45, 50, 55, 60, 65, 70)
#Predictor 2
income <- c(40, 50, 60, 65, 70, 75, 80, 85, 90, 95)
# Dependent variable
spending_score<-c(20, 25, 30, 35, 40, 45, 50, 55, 60, 65) # Response variable
# Combine into a data frame
data<-data.frame(age, income, spending_score)
#2. Perform Multiple Regression
# Fit a model: spending_score age + income
multiple_model <- lm(spending_score~age+income, data = data)
# Display the summary of the regression model
cat("Multiple Regression Summary:\n")
print(summary (multiple_model))
#3. Extract Coefficients
intercept <- coef (multiple_model) [1]
age_coeff <-coef (multiple_model) [2]
income_coeff<- coef (multiple_model) [3]
cat("\nIntercept (80):", intercept,
    "\nCoefficient for Age (B1):", age_coeff,
    "\nCoefficient for Income (B2):", income_coeff, "\n\n")
#4. Make Predictions
# Predict using the regression model
predicted_scores <- predict(multiple_model)
# Add predictions to the dataset
data$Predicted <- predicted_scores
# Display the dataset with predictions
cat("Data with Predicted Spending Scores:\n")
print(data)
#5. Visualization (Scatterplot with regression prediction plane)
cat("Plotting Age vs. Spending Score...\n")
ggplot(data, aes (x = age, y = spending_score)) +
  geom_point(color ="blue", size = 3) + # Actual points 35
  geom_line (aes (y = Predicted), color="red", size = 1) + # Predicted line 36
  labs (title = "Multiple Regression: Spending Score vs. Age + Income", 
        x = "Age",
        y = "Spending Score") +
  theme_minimal()

################################################### 8th practical ##############################################
################################################### 8th practical ##############################################
################################################### 8th practical ##############################################
#Load ggplot2 library
if(!require("ggplot2")) install.packages("ggplot2", dependencies = TRUE)
library(ggplot2)

# 1.Bar chart
# create a data frame for a bar chart 
bar_data <- data.frame(
  category = c("A", "B", "C", "D"),
  values = c(10, 25, 18, 35)
)

# Plot a bar chart 
ggplot(bar_data, aes(x = category, y = values, fill = Category))+
   geom_bar(stat = "identity", width = 0.6) +
   labs(title = "Bar Chart Example", x = "Category", y = "Values") +
   theme_minimal()

# 2.Histogram
# Generate random data for histogram
set.seed (123) # For reproducibility
hist_data <- rnorm(1000, mean = 50, sd = 10) # 1000random points

# Plot a Histogram
ggplot(data.frame(hist_data), aes (x = hist_data)) +
  geom_histogram(binwidth=5, color = 'black', fill = "blue", alpha = 0.7) +
  labs (title = "Histogram Example", x = "Values", y = "Frequency") +
  theme_minimal()

# 3. Scatter Plot
# Create a data frame for scatter plot
scatter_data <- data.frame(
  X = rnorm(100, mean = 50, sd = 10), # Random X values
  Y= rnorm(100, mean = 60, sd = 15)   #Random Y values
)

# Plot a Scatter Plot
ggplot (scatter_data, aes (x = X, y = Y)) +
  geom_point(color="darkred", size = 3, alpha = 0.6) +
  labs (title = "Scatter Plot Example", x = "x-axis", y = "Y-axis") +
  theme_minimal()

