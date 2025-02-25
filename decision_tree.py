#-------------------------------------------------------------------------
# AUTHOR: Lewis Lui
# FILENAME: decision_tree.py
# SPECIFICATION: This program helps create a decision tree based on a given dataset.
# FOR: CS 4210- Assignment #1
# TIME SPENT: 30 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# X = 
reference = {}
reference['Young'] = 1
reference['Prepresbyopic'] = 2
reference['Presbyopic'] = 3
reference['Myope'] = 4
reference['Hypermetrope'] = 5
reference['Yes'] = 6
reference['No'] = 7
reference['Reduced'] = 8
reference['Normal'] = 9
for item in db:
    X.append([reference[thing] for thing in item[:-1]])
    

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
# Y =
for item in db:
    if item[-1] == 'No':
        Y.append(10)
    else:
        Y.append(11)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()