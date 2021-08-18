from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score #Import scikit-learn metrics module for accuracy calculation

from sklearn.model_selection import KFold

import pandas as pd


tile_data = { # for 4 questions in form (fuel, news, traffic news, journey time, music, weather, stocks and speed)
    "detailed": [1, 1, 1, 0, 0, 1, 1, 0], # is there a lot to read?
    "numerical": [1, 0, 0, 1, 0, 1, 1, 1], # does selecting mean looking at numerical data on the whole
    "only_car": [1, 0, 1, 1, 0, 0, 0, 1], # is this category only needed whilst in the car
    "include": [1, 0, 1, 1, 1, 0, 0, 1] # the labels (to include = 1, not include = 0) (based on what the user chooses in the form on the destination selection page)
}

# load data into a DataFrame object:
df = pd.DataFrame(tile_data)

cols = ['detailed', 'numerical', 'only_car']
X = df[cols]
y = df['include']



#Implementing cross validation
k = 2 # similar idea to form where 4 questions are used in training and 4 questions are predicted (test)
kf = KFold(n_splits=k, shuffle=True, random_state=1)
clf = DecisionTreeClassifier(max_leaf_nodes=8, random_state=1)
 
acc_score = []
 
for train_index , test_index in kf.split(X):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
     
    clf.fit(X_train,y_train)
    pred_values = clf.predict(X_test)
     
    acc = accuracy_score(pred_values , y_test)
    acc_score.append(acc)

    print(pred_values)
    print(y_test)
     
avg_acc_score = sum(acc_score)/ k
 
print('Accuracy of each fold is', acc_score)
print('Average accuracy is {}%'.format(avg_acc_score*100))

