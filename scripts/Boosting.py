from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
import pandas as pd
import joblib

df = pd.read_csv('carbono.csv')

categorical_columns = [
    'Body Type', 'Diet', 'How Often Shower', 
    'Heating Energy Source', 'Transport', 'Vehicle Type', 
    'Social Activity', 'Frequency of Traveling by Air', 
    'Waste Bag Size', 'Energy efficiency', 'Recycling', 
    'Cooking_With'
]

numeric_columns = [
    'Monthly Grocery Bill', 'Vehicle Monthly Distance Km', 
    'Waste Bag Weekly Count', 'How Long TV PC Daily Hour', 
    'How Many New Clothes Monthly', 'How Long Internet Daily Hour'
]


onehotencoder = OneHotEncoder(sparse_output=False,drop='first')

scaler = MinMaxScaler(feature_range=(-1,1))

prepocesamiento = ColumnTransformer(
    transformers=[
        ('cat',onehotencoder,categorical_columns),
        ('num',scaler,numeric_columns)
    ]
)

df_transformer = prepocesamiento.fit_transform(df)

onehot_encoder_fitted = prepocesamiento.named_transformers_['cat']
cat_feature_names = onehot_encoder_fitted.get_feature_names_out(categorical_columns)
num_feature_names = numeric_columns
all_feature_names = list(cat_feature_names) + num_feature_names

df_transformer= pd.DataFrame(df_transformer,columns=all_feature_names)
target = df['CarbonEmission']

x_train, x_test, y_train, y_test = train_test_split(df_transformer, target, test_size=0.2, random_state=0)

#print(x_train,y_train)

gmb = GradientBoostingRegressor(n_estimators=100,learning_rate=0.1,max_depth=5)

gmb.fit(x_train,y_train)

y_predict = gmb.predict(x_test)

mse = mean_squared_error(y_test,y_predict)
mae =mean_absolute_error(y_test,y_predict)

r2 = r2_score(y_test,y_predict)
print(f'margen de error: {mse}')
print(f'margen de erro apsoluto: {mae}')
print(f'r2: {r2}')
features_importance = gmb.feature_importances_
print('feautere importans: ')
print(features_importance)

#joblib.dump(gmb,'Boosting.joblib')
#joblib.dump(prepocesamiento, 'prepocesamiento.joblib')
