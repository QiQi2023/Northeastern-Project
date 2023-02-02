train_set <- read.csv("~/Downloads/train.csv", stringsAsFactors = FALSE)
View(train_set)
test_set <- read.csv("~/Downloads/test.csv", stringsAsFactors = FALSE)
View(test_set)

train_set$IsTrainSet <- TRUE
test_set$IsTrainSet <- FALSE

test_set$Survived <- NA
#Data Cleaning
Taitanic <- rbind(train_set,test_set)
Taitanic[Taitanic$Embarked == '', "Embarked"] <- 'S'
table(Taitanic$Embarked)
View(Taitanic)
median_age <- median(Taitanic$Age, na.rm = TRUE)
Taitanic[is.na(Taitanic$Age), "Age"] <- median_age
table(is.na(Taitanic$Age))
table(is.na(Taitanic$Fare))
median_fare <- median(Taitanic$Fare, na.rm = TRUE)
Taitanic[is.na(Taitanic$Fare), "Fare"] <- median_fare

Taitanic$Pclass <- as.factor(Taitanic$Pclass)
Taitanic$Sex<- as.factor(Taitanic$Sex)
Taitanic$Embarked<- as.factor(Taitanic$Embarked)
train_set <- Taitanic[Taitanic$IsTrainSet == TRUE,]
test_set <- Taitanic[Taitanic$IsTrainSet == FALSE,]

train_set$Survived <- as.factor(train_set$Survived)
#Predict
library(randomForest)

fit <- randomForest(Survived ~ Pclass+Sex+Age+SibSp+Parch+Fare+Embarked, 
                    data = train_set, ntree = 500, mtry=3,nodesize=0.01*nrow(test_set))
Survived <- predict(fit, test_set)
Survived
PassengerID <- test_set$PassengerId
output <- as.data.frame(PassengerID)
output$Survived <- Survived
write.csv(output, file = "kaggle_submission.csv", row.names = FALSE)


