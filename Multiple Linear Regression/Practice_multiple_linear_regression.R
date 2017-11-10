#Multiple Linear regression
#install.packages('catools')
sampledata = read.csv('50_Startups.csv')

#Handling Catagorical Data
sampledata$State = factor(x = sampledata$State ,levels = c('New York','California','Florida'), labels = c(1,2,3))
  
#Splitting into Training and test data
library(caTools)
set.seed(123)
split = sample.split(sampledata$Profit,SplitRatio = 4/5)
training_set = subset(sampledata , split==TRUE)
test_set = subset(sampledata, split == FALSE)

