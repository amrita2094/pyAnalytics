#Topic: DT - Diabetis Data Set
#-----------------------------
#libraries
#https://www.datacamp.com/community/tutorials/decision-tree-classification-python
# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
# Import Decision Tree Classifier
from sklearn.model_selection import train_test_split
# Import train_test_split function
from sklearn import metrics
#Import scikit-learn metrics module for accuracy calculation

#%%%% : Load Data
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/pima-indians-diabetes.csv'
# load dataset
pima = pd.read_csv(url, header=None, names=col_names)
pima.head()

#%%% : Feature Selection
#need to divide given columns into two types of variables dependent(or target variable) and independent variable(or feature variables).

#split dataset in features and target variable
feature_cols = ['pregnant', 'insulin', 'bmi', 'age', 'glucose', 'bp', 'pedigree']
X = pima[feature_cols] # Features
y = pima.label # Target variable

#%%% Splitting Data
#To understand model performance, dividing the dataset into a training set and a test set is a good strategy.
#Let's split the dataset by using function train_test_split(). You need to pass 3 parameters features, target, and test_set size.
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) 
# 70% training and 30% test

#%%%: Building Decision Tree Model :create a Decision Tree Model using Scikit-learn.

# Create Decision Tree classifer object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)
y_train
#Predict the response for test dataset
y_pred = clf.predict(X_test)

#%%% : Evaluating Model
# estimate, how accurately the classifier or model can predict the type of cultivars.# Accuracy can be computed by comparing actual test set values and predicted values.
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#classification rate of 67.53%, considered as good accuracy. You can improve this accuracy by tuning the parameters in the Decision Tree Algorithm.
#%%%
y_train
labels
graph = Source(tree.export_graphviz(clf, out_file=None, class_names=['0', '1']  , filled = True))
display(SVG(graph.pipe(format='svg')))

#%%%  Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
#classification rate increased to 77.05%, which is better accuracy than the previous model.

#%%% : Features
Decision trees are easy to interpret and visualize.
It can easily capture Non-linear patterns.
It requires fewer data preprocessing from the user, for example, there is no need to normalize columns.
It can be used for feature engineering such as predicting missing values, suitable for variable selection.
The decision tree has no assumptions about distribution because of the non-parametric nature of the algorithm
#%%% : Cons
Sensitive to noisy data. It can overfit noisy data.
The small variation(or variance) in data can result in the different decision tree. This can be reduced by bagging and boosting algorithms.
Decision trees are biased with imbalance dataset, so it is recommended that balance out the dataset before creating the decision tree.


#%%%
#%%% : Visualizing Decision Trees
#You can use Scikit-learn's export_graphviz function for display the tree within a Jupyter notebook. For plotting tree, you also need to install graphviz and pydotplus.
#pip install graphviz
#pip install pydotplus
#export_graphviz function converts decision tree classifier into dot file and pydotplus convert this dot file to png or displayable form

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data, filled=True, rounded=True, special_characters=True,feature_names = feature_cols, class_names=['0', '1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())

graph = Source(tree.export_graphviz(estimator, out_file=None   , feature_names=labels, class_names=['0', '1', '2']  , filled = True))
display(SVG(graph.pipe(format='svg')))