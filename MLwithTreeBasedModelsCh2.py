# DecisionTreeRegressor class was imported from sklearn.tree
from sklearn.tree import DecisionTreeRegressor

# Imported train_test_split from sklearn.model_selection
from sklearn.model_selection import train_test_split

#imported cross_val_score from sklearn.model_selection
from sklearn.model_selection import cross_val_score

# Imported mean_squared_error from sklearn.metrics as MSE
from sklearn.metrics import mean_squared_error as MSE

# read X -> Matrix of input variables
# read y -> Array of output variable

# Set SEED for reproducibility
SEED = 1

# Split the data into train and  test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Instantiated a DecisionTreeRegressor dt
dt = DecisionTreeRegressor(max_depth=4, min_samples_leaf=0.26, random_state=SEED)

# Computed the array containing the 10-folds CV MSEs
MSE_CV_scores = - cross_val_score(dt, X_train, y_train, cv=10, 
                                  scoring='neg_mean_squared_error', 
                                  n_jobs=-1) 

# Compute the 10-folds CV RMSE
RMSE_CV = (MSE_CV_scores.mean())**(1/2)

# Print RMSE_CV
print('CV RMSE: {:.2f}'.format(RMSE_CV))

# Fit dt to the training set
dt.fit(X_train, y_train)

# Predict the labels of the training set
y_pred_train = dt.predict(X_train)

# Evaluate the training set RMSE of dt
RMSE_train = (MSE(y_train, y_pred_train))**(1/2)

# Print RMSE_train
print('Train RMSE: {:.2f}'.format(RMSE_train))