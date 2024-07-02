
# Heart Disease Prediction

Heart disease prediction using machine learning involves building a predictive model that can accurately identify the likelihood of a person having heart disease or not based on various health metrics and risk factors.

## Steps Involved
- Data Collection
- Data Preprocessing
- EDA
- Scaling the Data Using MinMaxScalar
- Model building
- Model Evaluation
- Hyperparater Tuning (got 94.21% accuracy with RandomForestClassifier)
- Saving the model using pickle
- Created Streamlit app
- Uploaded to Github



## Installation

Install all project requirements to run this project locally

```bash
  pip install -r requirements.txt
```
    
Run the command to see the demo

```bash
  streamlit run app.py
```
## Authors

- [@Debopam-Pritam2014](https://www.github.com/Debopam-Pritam2014)


![Logo](https://www.cdc.gov/flu/images/freeresources/HeartDisease_690x388.gif)

## Lessons Learned

- **Data Preprocessing:** The importance of data cleaning and handling missing values. How to use MinMaxScaler for normalization to ensure that features contribute equally to the model performance.

- **Algorithm Selection:** Comparison of various machine learning algorithms to find the most suitable one for your dataset. Understanding the strengths and weaknesses of algorithms like Random Forest, SVM, and Logistic Regression.

- **Hyperparameter Tuning:** The impact of hyperparameters on the performance of the model.Techniques for hyperparameter tuning, such as GridSearchCV, to optimize model performance.

- **Model Evaluation:** Different metrics to evaluate the performance of the model, such as accuracy, precision, recall, and F1-score. The importance of cross-validation to ensure the robustness of the model.

- **Building Applications:** How to create a web application using Streamlit to make your model accessible to users. The basics of user interface design to create an intuitive and user-friendly application.

- **Version Control:** The importance of using GitHub for version control and collaboration. How to document your project and make it accessible to others.
### Challenges I Faced and How I Overcame Them

- **Feature Selection:** Identifying which features are most important for predicting heart disease. Used feature importance scores from the Random Forest model to select the most impactful features.
- **Model Overfitting:** The model performed well on training data but poorly on test data. Implemented cross-validation and regularization techniques to prevent overfitting.

- **Hyperparameter Tuning:** Finding the optimal hyperparameters was time-consuming. Automated the process using GridSearchCV to systematically search for the best parameters.

- **Deployment Issues:** Integrating the model into a Streamlit application and ensuring it runs smoothly. Iterative testing and debugging to resolve integration issues and ensure the application works seamlessly.


## Acknowledgements

 - [Dataset link kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
 - [EDA](https://www.kaggle.com/code/totoro29/heart-disease-eda-prediction)


## Feedback

If you have any feedback, please reach out to me at debopamdeycse19@gmail.com

