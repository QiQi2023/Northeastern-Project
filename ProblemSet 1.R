library(MASS)
head(Boston)
pairs(Boston)

library(ggplot2)
ggplot(Boston, aes(crim, medv)) +
  geom_point()

#(c) correlation test
cor.test(Boston$crim, Boston$ptratio)
0.2899456^2 # --> multiple R-squared 0.08407.
fit <- lm(crim ~ ptratio, data = Boston)
summary(fit)
#(d)
ggplot(Boston , aes(crim)) +
  geom_histogram(aes(y=..density..)) +
  geom_function(fun = dnorm, args = list(mean = mean(Boston$crim), 
                                         sd = sd(Boston$crim)), color="red")
Boston$crimLog <- log(Boston$crim)
ggplot(Boston , aes(crimLog)) +
  geom_histogram(aes(y=..density..)) +
  geom_function(fun = dnorm, args = list(mean = mean(Boston$crimLog), 
                                         sd = sd(Boston$crimLog)), color="red")

#(e)
#glm
summary(glm(chas ~., Boston, family = binomial))
Boston$crimLog <- NULL

