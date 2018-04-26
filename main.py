from flask import Flask, request
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/predict') 
def predict():
    #Loading Model
#    xgb_model=pickle.load(open("carsales_xgb.pickle.dat", "rb"))
##Loading Encoders
#    encoder_trans=pickle.load(open("encoder_trans.pickle.dat", "rb"))
#    encoder_wheels=pickle.load(open("encoder_wheels.pickle.dat", "rb"))
#    encoder_size=pickle.load(open("encoder_size.pickle.dat", "rb"))
#    encoder_make=pickle.load(open("encoder_make.pickle.dat", "rb"))
#    encoder_style=pickle.load(open("encoder_style.pickle.dat", "rb"))
##Loading scaler
#    scaler=pickle.load(open("scaler.pickle.dat", "rb"))
#    
#    
#    
#    
#    Engine_HP=request.args['Engine_HP']
#    Age=request.args['Age']
#    city_mpg=request.args['city_mpg']
#    city_mpg=np.log(int(city_mpg))
#    car_trans_type=request.args['car_trans_type']
#    car_driven_wheels=request.args['car_driven_wheels']
#    car_vehicle_size=request.args['car_vehicle_size']
#    car_vehicle_style=request.args['car_vehicle_style']
#    car_make=request.args['car_make']
#    numeric_columns_list=['Engine HP','Age','log_city mpg']
#    df = pd.DataFrame([[Engine_HP,Age,city_mpg]], columns=numeric_columns_list)
#    df_scaled=scaler.transform(df)
#    car_trans_1hot = encoder_trans.transform([car_trans_type])
#    df_scaled = np.concatenate((df_scaled,car_trans_1hot),axis=1)
#    car_drive_1hot = encoder_wheels.transform([car_driven_wheels])
#    df_scaled = np.concatenate((df_scaled,car_drive_1hot),axis=1)
#    car_size_1hot = encoder_size.transform([car_vehicle_size])
#    df_scaled = np.concatenate((df_scaled,car_size_1hot),axis=1)
#    car_style_1hot = encoder_style.transform([car_vehicle_style])
#    df_scaled = np.concatenate((df_scaled,car_style_1hot),axis=1)
#    car_make_1hot = encoder_make.transform([car_make])
#    df_scaled = np.concatenate((df_scaled,car_make_1hot),axis=1)
#    carSales_predictions = xgb_model.predict(df_scaled)
#    output = "Predicted Price: " + str(np.exp(carSales_predictions[0]))
    return "20000"

if __name__ == '__main__':
  app.run()
