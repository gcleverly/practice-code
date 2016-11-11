## 2. Ensemble models ##

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import roc_auc_score

columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
clf.fit(train[columns], train["high_income"])

clf2 = DecisionTreeClassifier(random_state=1, max_depth=5)
clf2.fit(train[columns], train["high_income"])
predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

predictions = clf2.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

## 3. Combining our predictions ##

predictions = clf.predict_proba(test[columns])[:,1]
predictions2 = clf2.predict_proba(test[columns])[:,1]
combined = (predictions + predictions2) / 2
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))

## 5. Bagging ##

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows.
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every loop.
    # That would make all of our trees the same.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])
combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))

## 7. Random subsets in scikit-learn ##

# We'll build 10 trees
tree_count = 10

# Each "bag" will have 60% of the number of original rows.
bag_proportion = .6

predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every time.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2)
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))
predictions = []
for i in range(tree_count):
    # We select 60% of the rows from train, sampling with replacement.
    # We set a random state to ensure we'll be able to replicate our results.
    # We set it to i instead of a fixed value so we don't get the same sample every time.
    bag = train.sample(frac=bag_proportion, replace=True, random_state=i)
    
    # Fit a decision tree model to the "bag".
    clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=2, splitter="random", max_features="auto")
    clf.fit(bag[columns], bag["high_income"])
    
    # Using the model, make predictions on the test data.
    predictions.append(clf.predict_proba(test[columns])[:,1])

combined = numpy.sum(predictions, axis=0) / 10
rounded = numpy.round(combined)

print(roc_auc_score(test["high_income"], rounded))

## 8. Putting it all together ##

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_leaf=2)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

## 9. Parameter tweaking ##

from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=5, random_state=1, min_samples_leaf=2)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))
clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=2)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

## 10. Reducing overfitting ##

clf = DecisionTreeClassifier(random_state=1, min_samples_leaf=5)

clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))

clf = RandomForestClassifier(n_estimators=150, random_state=1, min_samples_leaf=5)
clf.fit(train[columns], train["high_income"])

predictions = clf.predict(train[columns])
print(roc_auc_score(train["high_income"], predictions))

predictions = clf.predict(test[columns])
print(roc_auc_score(test["high_income"], predictions))