import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
from mlxtend.feature_selection import ExhaustiveFeatureSelector as EFS

#Get the data
df = pd.read_csv('airfares-1.csv')

'''preprocess data
1. Check for missing values (use viz)
2. Remove varibles that may be redundant or have many missing values'''

df.isnull()
df.isnull().sum()
df.drop(['S_CODE'],axis=1, inplace=True)
df.drop(['E_CODE'],axis=1, inplace=True)
df.drop(['S_CITY'],axis=1, inplace=True)
df.drop(['E_CITY'],axis=1, inplace=True)


'''Explore the numerical predictors and response (FARE) by creating a 
correlation table/heatmap and examining some scatterplots between FARE and those predictors.
 What seems to be the best single predictor of FARE?'''

sns.heatmap(df.corr())
df.corr()
sns.pairplot(df)

#Distance seems to be the best single predictor of FARE.

''' Explore the categorical predictors (excluding the first four)by computing the average
 fare in each category and using boxplots. Which categorical predictor seems best for predicting FARE?'''
 
df[['VACATION', 'SW', 'SLOT','GATE']].mean()

sns.boxplot(x='VACATION', y='FARE', data=df)
sns.boxplot(x='SW', y='FARE', data=df)
sns.boxplot(x='SLOT', y='FARE', data=df)
sns.boxplot(x='GATE', y='FARE', data=df)
# SW seems best for predicting FARE

'''Using all x-variables build a linear regression model to predict FARE
#partition the data into training (70%) and training (30%) sets
Use random state=1'''
x = df[['COUPON', 'NEW', 'VACATION', 'SW', 'HI', 'S_INCOME', 'E_INCOME',
       'S_POP', 'E_POP', 'SLOT', 'GATE', 'DISTANCE', 'PAX']]
y = df['FARE']
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)

lm = LinearRegression()
lm.fit(x_train,y_train)
predictions = lm.predict(x_test)

lm.coef_
lm.intercept_
from sklearn.metrics import mean_squared_error
mse =  mean_squared_error(y_test, predictions, squared=True)
rmse = mse**0.5

''' Using model above, predict the average fare on a route with the following 
characteristics: COUPON = 1.202, NEW = 3, VACATION = No, SW = No, HI = 4442.141, 
S_INCOME = 28,760, E_INCOME = 27,664, S_POP = 4,557,004, E_POP = 3,195,503, 
SLOT = Free, GATE = Free, PAX = 12,782, DISTANCE = 1976 miles.'''
lm.predict([[1.202,3,0,0,442.141,28760,27664,4557004,319503,0,0,1976,12782]])




'''Predict the reduction in average fare on the route above if Southwest
 decides to cover this route.'''

lm.predict([[1.202,3,0,1,442.141,28760,27664,4557004,319503,0,0,1976,12782]])

 
'''In reality, which of the factors will not be available for predicting 
 the average fare from a new airport (i.e., before ﬂights start operating on those
                                      routes)? Which ones can be estimated? How?'''
 
'''
 The COUPON for the toute will not be available for new airports. 
 
'''
 
 ###case contd.......

'''Select a model that includes only factors that you think are available before flights begin to operate on the new route. 
Use an exhaustive search to find such a model.'''
x = df[['NEW', 'VACATION', 'HI', 'S_INCOME', 'E_INCOME','S_POP', 'E_POP', 'SLOT', 'GATE', 'DISTANCE', 'PAX']]
y = df['FARE']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

lr = LinearRegression()

efs = EFS(lr, 
          min_features=1,
          max_features=11,
          scoring='neg_root_mean_squared_error',
          cv=10)

efs.fit(x_train, y_train)

##selected features
efs.best_feature_names_


X_train_efs = efs.transform(x_train)
X_test_efs = efs.transform(x_test)

# Fit the estimator using the new feature subset
# and make a prediction on the test data
lr.fit(X_train_efs, y_train)
y_pred = lr.predict(X_test_efs)



'''Report the RMSE of the above model on the test set'''
rmse = mean_squared_error(y_test, y_pred, squared=False)
print ("rmse is",rmse)

'''Use the model above to predict the average fare on a route with characteristics COUPON = 1.202, 
NEW = 3, VACATION = No, SW = No, HI = 4442.141, S_INCOME = $28,760, E_INCOME = $27,664, S_ POP = 4,557,004,
 E_POP = 3,195,503, SLOT = Free, GATE = Free, PAX = 12,782, DISTANCE = 1976 miles.'''
lr.predict([[0,4442.141,28760,27664,4557004,3195503,0,0,1976,12782]])

#Average fare on a route is $239.39 
 



