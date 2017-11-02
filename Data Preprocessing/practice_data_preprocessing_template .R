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
dataset$Country =  factor(dataset$Country,c('France','Germany','Spain'),c(1,2,3))
dataset$Purchased = factor(dataset$Purchased,c('Yes','No'),c(1,0))