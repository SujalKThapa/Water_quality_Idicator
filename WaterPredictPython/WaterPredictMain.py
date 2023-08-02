import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression


def PredictQuality(modelType, ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity):
    link = 'https://raw.githubusercontent.com/SujalKThapa/Water_quality_Idicator/main/data/water_potability.csv'
    data = pd.read_csv(link)
    # Split the data into features and target
    X = data.drop('Potability', axis=1)
    y = data['Potability']
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    # Oye, rf = random forest, kn = k nearest neighbour, svc = support vector component, aur lr = logistic regression
    if modelType == "rf":
        clf = RandomForestClassifier()
    elif modelType == "knn":
        clf = KNeighborsClassifier()
    elif modelType == "svc":
        clf = SVC()
    elif modelType == "svc":
        clf = SVC()
    else:
        clf = LogisticRegression()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy = clf.score(X_test, y_test)
    new_data = pd.DataFrame([[ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]],columns=X.columns)
    prediction = clf.predict(new_data)
    return prediction

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
