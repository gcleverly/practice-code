## 4. Column split selection ##

def find_best_column(data, target_name, columns):
    # Fill in the logic here to automatically find the column in columns to split on.
    # data is a dataframe.
    # target_name is the name of the target variable.
    # columns is a list of potential columns to split on.
    information_gains = []
    for i in columns:
        information_gain = calc_information_gain(data,i,target_name)
        information_gains.append(information_gain)
    
    print(information_gains)
    highest_gain_index = information_gains.index(max(information_gains))
    highest_gain = columns[highest_gain_index]
    
    return highest_gain

# A list of columns to potentially split income with.
columns = ["age", "workclass", "education_num", "marital_status", "occupation", "relationship", "race", "sex", "hours_per_week", "native_country"]

income_split = find_best_column(income,"high_income",columns)


## 5. Creating a simple recursive algorithm ##

label_1s = []
label_0s = []

def id3(data, target, columns):
    unique_targets = pandas.unique(data[target])
    
    if len(unique_targets) == 1:
        if unique_targets == 1:
            label_1s.append(1)
        elif unique_targets == 0:
            label_0s.append(0)
        
        return
    
    # Find the best column to split on in our data.
    best_column = find_best_column(data, target, columns)
    # Find the median of the column.
    column_median = data[best_column].median()
    
    # Create the two splits.
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    
    # Loop through the splits and call id3 recursively.
    for split in [left_split, right_split]:
        id3(split, target, columns)
    
data = pandas.DataFrame([
    [0,20,0],
    [0,60,2],
    [0,40,1],
    [1,25,1],
    [1,35,2],
    [1,55,1]
    ])

data.columns = ["high_income", "age", "marital_status"]

id3(data, "high_income", ["age", "marital_status"])

## 6. Storing the tree ##

# Create a dictionary to hold the tree.  
tree = {}

# This list will let us number the nodes.
nodes = []

def id3(data, target, columns, tree):
    unique_targets = pandas.unique(data[target])
    
    # Assign the number key to the node dictionary.
    nodes.append(len(nodes) + 1)
    tree["number"] = nodes[-1]

    if len(unique_targets) == 1:
        if 1 in unique_targets:
            tree["label"] = 1
        elif 0 in unique_targets:
            tree["label"] = 0

        return
    
    best_column = find_best_column(data, target, columns)
    column_median = data[best_column].median()
    
    tree["column"] = best_column
    tree["median"] = column_median
    
    left_split = data[data[best_column] <= column_median]
    right_split = data[data[best_column] > column_median]
    split_dict = [["left", left_split], ["right", right_split]]
    
    for name, split in split_dict:
        tree[name] = {}
        id3(split, target, columns, tree[name])

id3(data, "high_income", ["age", "marital_status"], tree)

## 7. A prettier tree ##

def print_with_depth(string, depth):
    prefix = "    " * depth
    print("{0}{1}".format(prefix, string))
    
    
def print_node(tree, depth):
    # Check for the presence of label in the tree.
    if "label" in tree:
        # If there's a label, then this is a leaf, so print it and return.
        print_with_depth("Leaf: Label {0}".format(tree["label"]), depth)
        return
    # Print information about what the node is splitting on.
    print_with_depth("{0} > {1}".format(tree["column"], tree["median"]), depth)
    
    # Create a list of tree branches.
    branches = [tree["left"], tree["right"]]
        
    for i in branches:
        print_node(i,depth)
    
    depth += 1
    

print_node(tree, 0)

## 9. Automatic predictions ##

def predict(tree, row):
    if "label" in tree:
        return tree["label"]
    
    column = tree["column"]
    median = tree["median"]
    
    if row[column] <= median:
        return tree['left']
    if row[column] > median:
        return tree['right']

# Print the prediction for the first row in our data.
print(predict(tree, data.iloc[0]))

## 10. Making multiple predictions ##

new_data = pandas.DataFrame([
    [40,0],
    [20,2],
    [80,1],
    [15,1],
    [27,2],
    [38,1]
    ])
# Assign column names to the data.
new_data.columns = ["age", "marital_status"]

def batch_predict(tree, df):
    df = df.apply(lambda row:predict(tree,row), axis=1)
    # Insert your code here.
    pass
    return df

predictions = batch_predict(tree, new_data)