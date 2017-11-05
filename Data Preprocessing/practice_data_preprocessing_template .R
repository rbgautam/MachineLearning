# Importing the dataset
dataset = read.csv('data.csv')

#Handling missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age,FUN = function(x) mean(x , na.rm = TRUE)),
                     dataset$Age )

dataset$Salary = ifelse(is.na(dataset$Salary),
                        ave(dataset$Salary,FUN= function(x) mean(x,na.rm = TRUE)),
                        dataset$Salary)

#Handling categories
dataset$Country =  factor(dataset$Country,c('France','Spain','Germany'),c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,c('No','Yes'),c(0,1))

#Splitting training and test set
#install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased,SplitRatio = 0.8)
training_set  = subset(dataset, split == TRUE)
test_set = subset(dataset,split == FALSE)