sampledata = read.csv('Salary_data.csv')
#install.packages("caTools")
library(caTools)
split = sample.split(sampledata$Salary, SplitRatio=0.66)
set.seed(123)
training_set = subset(sampledata, split== TRUE)
test_set = subset(sampledata, split== FALSE)

#Fitting Linear regression data to training set
regressor = lm(formula = Salary ~ YearsExperience, data = training_set)

#Prediction
y_pred = predict(regressor, newdata = test_set)

#Visualizition 
# install.packages('ggplot2')
library(ggplot2)
#Training set Visualization
ggplot()+
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary), colour ='red')+
  geom_line(aes(x= training_set$YearsExperience, y = predict(regressor, newdata = training_set)), colour='blue')+
  ggtitle('Salary vs Experience (Training Set)') +
  xlab('Years of Experience') + 
  ylab('Salary')
#Test set Visualization
