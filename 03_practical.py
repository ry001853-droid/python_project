######################################## 5th practical ########################################
# Load necessary library
library(ggplot2)

# 1. Create a dataset

# Independent variable (predictor)
x <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Dependent variable (response)
y <- c(3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Combine into a data frame
data <- data.frame(x, y)
View(data)

# 2. Perform Linear Regression

# Fit a linear model: y = β0 + β1*x
linear_model <- lm(y ~ x)
View(linear_model)

# Display the summary of the model
cat("Linear Regression Summary:\n")
print(summary(linear_model))


# 3. Extract Coefficients
intercept <- coef(linear_model)[1]
slope <- coef(linear_model)[2]
cat("\nIntercept (β0):", intercept, "\nSlope (β1):", slope, "\n\n")


# 4. Predict values using the model
predicted_values <- predict(linear_model)

# Add predictions to the data frame
data$Predicted <- predicted_values


# 5. Visualization
# Scatter plot with regression line
cat("Plotting the regression line...\n")
ggplot(data, aes(x = x, y = y)) +
  geom_point(color = "blue", size = 3) +   # Scatter plot
  geom_line(aes(y = Predicted), color = "red", size = 1) +  # Regression line
  labs(title = "Linear Regression: y ~ x",
       x = "Independent Variable (x)",
       y = "Dependent Variable (y)") +
  theme_minimal()

##################################################### 6th practical ######################################
##################################################### 6th practical ######################################
##################################################### 6th practical ######################################
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

   


