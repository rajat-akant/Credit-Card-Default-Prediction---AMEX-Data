Credit default prediction is central to managing risk in a consumer lending business. Credit default prediction allows lenders to optimize lending decisions, which leads to a better customer experience and sound business economics.

Credit default prediction is central to managing risk in a consumer lending business. Credit default prediction allows lenders to optimize lending decisions, which leads to a better customer experience and sound business economics.

However, how do the card issuers be assured that the charged payment will be received back? That’s a complex problem with many existing solutions—and even more potential improvements, which has been the primary objective of this Project.

In this project, I have leveraged an industrial scale data set to build a machine learning model. Training and validation datasets include time-series behavioural data and anonymized customer profile information. Before arriving on the machine learning part, the following prerequisites have been performed:

1) Data Ingestion on MongoDB via Python
2) Sample Data Extraction from MongoDB using python.
- The Primary objective for using a NoSQL Database like MongoDB was to make the optimum use of dynamic data schema. The dataset is comparatively huge with 5.5 million rows and 190 columns. A document database will not only speed up the data manipulation but will also facilitate embedding of further data without the need of resource consuming joins and without any redundant information.

3) Exploratory Data Analysis using python.
- EDA was performed mainly to understand the data further. The data description phase helped us to understand the relation between the unique values and overall available data. The co-relation plots helped us with the features having high co-linearity, which further aided in dimensionality reduction measures. Density plots of different variables against the target was performed to observed the skewness and statistically infer the relations against the same.

4) Data Cleaning and Pre-processing.
- Data Cleaning was essential for this dataset because of high percentage of missing values. Around 25 columns were present with more than 70% missing values, which had to be removed. For rest of the columns, the missing values were less than 50% and an imputation was performed accordingly. For Numerical columns, imputation was done with median and for categorical columns with mode.
- Looking at the dataset naively, would certainly output the dataset as scaled, however with further looking at the mean and standard deviation of individual features, we understood that the dataset needed scaling for further processing.
- One_Hot_Encoding of categorical columns was performed to allow the ML model to infer the categorical columns information correctly.
- For the pre-processing part, the target values distribution observed from EDA was 75/25, which was highly imbalanced for a ML Model to be trained. Hence, the data was further balanced with SMOTE technique, which is done by generating synthetic samples of the less populated class in the target variable to balance the population of variables in target feature. 
- In order to overcome the curse of dimensionality, I further processed the data with Principal Components Analysis (PCA) technique, to bring out strong patterns in a dataset by supressing variations. PCA not only helped with identifying important features, but also reduced the risk of over-fitting.

5) Machine Learning Model Building on Training Data.
- As the dataset target variable suggested the problem statement as a binary classification problem, the initial training algorithm was Logistic Regression, However, the results were not satisfactory and led to further study into Light Gradient Boosting Method (LGBM) algorithm. With available feature importances and few parameters tuned, LGBM yielded the desired results with ROC_AUC of 0.97.

6) Validating the output against Validation Data Sets.
- The LGBM trained model was further tested and validated with two different validation sets. Each yielding a model accuracy of 0.87 and 0.89 respectively.

With more computing power and further data feeding, the model accuracy can be further improved.
Successful implementation of this model will help create a better customer experience for cardholders and improved risk management for card issuers.
