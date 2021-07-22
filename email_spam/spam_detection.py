import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV

dataframe = pd.read_csv("spam.csv")
print(dataframe.head())

# splitting into train and test

x = dataframe["EmailText"]
y= dataframe["Label"]


x_train, y_train = x[0:4457],y[0:4457]
x_test, y_test = x[4458:],y[4458:]


cv = CountVectorizer()
features = cv.fit_transform(x_train)

model = svm.SVC()

model.fit(features,y_train)

features_test = cv.transform(x_test)

print("Accuracy is : ",model.score(features_test,y_test))



