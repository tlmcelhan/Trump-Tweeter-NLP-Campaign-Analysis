def remove_punctuation(s):
    import string
    s = ''.join([i for i in str(s) if i not in frozenset(string.punctuation)])
    return s

    
def plot_series(df, cols=None, title='Title', xlab=None, ylab=None):
    import matplotlib.pyplot as plt
    # Set figure size to be (18, 9).
    plt.figure(figsize=(18,9))
    
    # Iterate through each column name.
    for col in cols:
        
        # Generate a line plot of the column name.
        # You only have to specify Y, since our
        # index will be a datetime index.
        plt.plot(df[col])
        
    # Generate title and labels.
    plt.title(title, fontsize=26)
    plt.xlabel(xlab, fontsize=20)
    plt.ylabel(ylab, fontsize=20)
    
    # Enlarge tick marks.
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18);
    

def corr_heatmap(df, col, ascend):
    import seaborn as sns
    return sns.heatmap(df.corr()[[col]].sort_values(by=col,ascending=ascend).head(15), annot = True)

def plot_exp_var(LSA_model,n_components):
    import numpy as np
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(20,10))
    plt.bar(np.array(range(n_components))+1, 
            LSA_model.explained_variance_ratio_, 
            color='g', 
            label='explained variance')
    plt.plot(np.array(range(n_components))+1, 
             np.cumsum(LSA_model.explained_variance_ratio_), 
             label='cumulative explained variance')
    plt.legend(fontsize=16)
    plt.xlabel('component', fontsize=20)
    plt.ylabel('variance ratio', fontsize=20)
    plt.title('Explained variance by component', fontsize=36);
    

def error_scores(true_values,pred_values):
    import numpy as np
    import pandas as pd
    from sklearn.metrics import confusion_matrix
    tn, fp, fn, tp = confusion_matrix(true_values, pred_values).ravel()
    
    spec = tn / (tn + fp)
    sens = tp / (tp + fn)
    
    print(f'Specificity: {spec}')
    print(f'Sensitivity: {sens}')
