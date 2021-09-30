# SonarProject

### How to download the repository: 
- git clone [https://github.com/anmancuso/SonarProject](https://github.com/anmancuso/SonarProject)

### Required Packages: 
- numpy
- pandas
- seaborn
- matplotlib
- sklearn

(The code has been developed with python3.8)

### How to run the project:

The project is composed by three notebooks:

1. [Exploring_the_dataset.ipynb](https://github.com/anmancuso/SonarProject/blob/main/Exploring_the_Dataset.ipynb) -> Data Visualization
2. [Rock_vs_Mine_binary_classification_without_feature_reduction.ipynb](https://github.com/anmancuso/SonarProject/blob/main/Rock_vs_Mine_binary_classification_without_feature_reduction.ipynb) -> ML without any data pre-processing
3. [Rock_vs_Mine_binary_classification_with_feature_reduction.ipynb](https://github.com/anmancuso/SonarProject/blob/main/Rock_vs_Mine_binary_classification_with_feature_reduction.ipynb) -> ML with feature selection and data pre-processing **This is the main script!**

Then there are two additional .py scripts to plot and to print the results.

------
# Description of the Project


The dataset under study is a storic dataset used by Gorman, R. P., and Sejnowski, T. J. (1988) in their “Analysis of Hidden Units in a Layered Network Trained to Classify Sonar Targets” in Neural Networks, Vol. 1, pp. 75–89.
As the name suggests, the aim of this project is to use the data provided by a sonar to distinguish between rocks and metal objects such as mines. 
The dataset is made of 60 features (strenght of bouncing signals at 60 different angles) with 208 observations.
For each observation we know the outcome as a Rock "R" or a Mine "M".

In the [Exploring_the_dataset.ipynb](https://github.com/anmancuso/SonarProject/blob/main/Exploring_the_Dataset.ipynb) notebook, the data studied by visualizing the  box plots to check the precesence of possible outliers and to understand the general trend of the data. 
Of course here the data under studied are only the train-data obtained with a train test split with size 0.2 (20% of the dataset is used to test the learning). 
From this check, no particular evidences can be pointed out. 

In this first attempt to face the classification problem [first attempt](https://github.com/anmancuso/SonarProject/blob/main/Rock_vs_Mine_binary_classification_without_feature_reduction.ipynb), the data have not been processed (except for the initial Encoding of the result of the observation : "R" is the class 1 and "M" is the class 0).

The algorithm used here for the train are: 

1. [Logistic Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html);
2. [linear Support Vector Classifier (SVC)](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html);
3. [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html);
 
I have decided to use different algorithms in order to compare the results in terms of Accuracy, Precision, AUC and Training Time. 
In particular from the Accuracy shown in the following figure:
![alt text](https://github.com/anmancuso/SonarProject/blob/main/plots/comparison_wo_featuresel.png?raw=true)

one can conclude that even without Data Pre-processing the results of the prediction are acceptable (higher than 80%) with the SVC algorithm.

Of course by looking at the results obtained by facing  the classification problem [with feature selection and data preparation](https://github.com/anmancuso/SonarProject/blob/main/Rock_vs_Mine_binary_classification_with_feature_reduction.ipynb), one realize that the performaces considerably improve.
The Data Preparation consist of the standardization of the observation (that is to have a dataset of Mean 0 and STD 1). 
For the feature selection instead the algorithm used are: 
1. [Univariate Selection with SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html);
2. [Recursive Feature Elimination](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html);
3. [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html);

After a first check of the distribution of the importance of the feature to optimize the number of feature to keep, I have implemented the train by means of Pipelines built with two steps: 
1. Data Processing
2. Training fit

By doing so for all the Algorithm chosen and for all the Feature selection functions, I have compared all the results, which can be summarized in the following plots:

![alt text](https://github.com/anmancuso/SonarProject/blob/main/plots/Accuracy_total.png?raw=true)


![alt text](https://github.com/anmancuso/SonarProject/blob/main/plots/AUC_total.png?raw=true)



![alt text](https://github.com/anmancuso/SonarProject/blob/main/plots/ROC_total.png?raw=true)

Among the Algorithm Tested, for sure the linear Support Vector Classifier with a Feature Reduction or with a Data Standardization, give the best results in terms of Accuracy and AUC. 



