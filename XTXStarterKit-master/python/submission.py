import subprocess, sys, os
from core import Submission

sys.stdout = open(os.devnull, 'w')  # do NOT remove this code, place logic & imports below this line

"""
PYTHON submission

Implement the model below

##################################################### OVERVIEW ######################################################

1. Use get_next_data_as_string() OR get_next_data_as_list() OR get_next_data_as_numpy_array() to recieve the next row of data
2. Use the predict method to write the prediction logic, and return a float representing your prediction
3. Submit a prediction using self.submit_prediction(...)

################################################# OVERVIEW OF DATA ##################################################

1. get_next_data_as_string() accepts no input and returns a String representing a row of data extracted from data.csv
     Example output: '1619.5,1620.0,1621.0,,,,,,,,,,,,,1.0,10.0,24.0,,,,,,,,,,,,,1615.0,1614.0,1613.0,1612.0,1611.0,
     1610.0,1607.0,1606.0,1605.0,1604.0,1603.0,1602.0,1601.5,1601.0,1600.0,7.0,10.0,1.0,10.0,20.0,3.0,20.0,27.0,11.0,
     14.0,35.0,10.0,1.0,10.0,13.0'

2. get_next_data_as_list() accepts no input and returns a List representing a row of data extracted from data.csv,
   missing data is represented as NaN (math.nan)
     Example output: [1619.5, 1620.0, 1621.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1.0, 10.0,
     24.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 1615.0, 1614.0, 1613.0, 1612.0, 1611.0, 1610.0,
     1607.0, 1606.0, 1605.0, 1604.0, 1603.0, 1602.0, 1601.5, 1601.0, 1600.0, 7.0, 10.0, 1.0, 10.0, 20.0, 3.0, 20.0,
     27.0, 11.0, 14.0, 35.0, 10.0, 1.0, 10.0, 13.0]

3. get_next_data_as_numpy_array() accepts no input and returns a Numpy Array representing a row of data extracted from
   data.csv, missing data is represented as NaN (math.nan)
   Example output: [1.6195e+03 1.6200e+03 1.6210e+03 nan nan nan nan nan nan nan nan nan nan nan nan 1.0000e+00
    1.0000e+01 2.4000e+01 nan nan nan nan nan nan nan nan nan nan nan nan 1.6150e+03 1.6140e+03 1.6130e+03 1.6120e+03
     1.6110e+03 1.6100e+03 1.6070e+03 1.6060e+03 1.6050e+03 1.6040e+03 1.6030e+03 1.6020e+03 1.6015e+03 1.6010e+03
      1.6000e+03 7.0000e+00 1.0000e+01 1.0000e+00 1.0000e+01 2.0000e+01 3.0000e+00 2.0000e+01 2.7000e+01 1.1000e+01
       1.4000e+01 3.5000e+01 1.0000e+01 1.0000e+00 1.0000e+01 1.3000e+01]

##################################################### IMPORTANT ######################################################

1. One of the methods get_next_data_as_string(), get_next_data_as_list(), or get_next_data_as_numpy_array() MUST be used and
   _prediction(pred) MUST be used to submit below in the solution implementation for the submission to work correctly.
2. get_next_data_as_string(), get_next_data_as_list(), or get_next_data_as_numpy_array() CANNOT be called more then once in a
   row without calling self.submit_prediction(pred).
3. In order to debug by printing do NOT call the default method `print(...)`, rather call self.debug_print(...)

"""


# class MySubmission is the class that you will need to implement
class MySubmission(Submission):

    """
    get_prediction(data) expects a row of data from data.csv as input and should return a float that represents a
       prediction for the supplied row of data
    """
    # from sklearn.externals import joblib
    # model =joblib.load("model.pkl")
    
    import tensorflow as tf
    from tensorflow.keras.models import load_model
    from tensorflow.keras import backend as K
    
    def coeff_determination(y_true, y_pred):
        from keras import backend as K
        SS_res =  K.sum(K.square( y_true-y_pred ))
        SS_tot = K.sum(K.square(y_true))
        return ( 1 - SS_res/(SS_tot + K.epsilon()) )
    

    model = load_model("model.h5",custom_objects={'coeff_determination':coeff_determination})
    
    # from sklearn.externals import joblib
    # pca = joblib.load("pca.joblib") 

    # import xgboost as xgb
    # from xgboost import XGBRegressor
    # from sklearn.externals import joblib
    # model = joblib.load("model.joblib")

    def get_prediction(self, data):
        import numpy as np

        # weights = [-0.1493639 , -0.09890566, -0.07830242, -0.04830867,  0.00040121,
        # 0.00055115,  0.00052302,  0.00032139,  0.02560983, -0.02170808,
        # 0.01204431]
        # bias = 0.009333372633211108
        means = [16.118416706138902,15.547841849280616,14.464779154926385,13.944853314951105,12.043094347698116,6.749742249914084,7.251348417116139,13.252863084287695,16.04343201447734,16.58679452893151,18.50610483536828,18.92986730995577,1642.0246804248934]
        stds = [25.81653619582708,24.14784409606728,21.015679492101324,18.165416450841708,14.969962478611999,10.72717450193673,12.546854875872082,18.312426769134564,22.82668960588688,24.51113901536429,29.013517318266146,29.97927973196393,26.86899517770618]

        top = np.nan_to_num(data[-1])
        

        depth = 6



        # featureIndexes = list(range(29+depth,29,-1)) + list(range(0,depth)) + list(range(44+depth,44,-1)) + list(range(15,15+depth))
        # X = top[featureIndexes].reshape(12,)

        featuresIndexes = list(range(44+depth,44,-1)) + list(range(15,15+depth))
        X = top[featuresIndexes]

        for i in range(2*depth):
            X[i] -= means[i]
            X[i] /= stds[i]



        # X = X.reshape((1,2,16))
        
        pred = self.model.predict(X.reshape(1,12))
        return pred[0][0]
        # orderImbalances = []
        # levelImbalances = []
        # for i in range(4):
        #     orderImbalances += [(top[15+i] - top [45+i]) / (top[15+i] + top [45+i])]
        #     levelImbalances += [top[15+i] - top [45+i]]

        # priceMean = 0

        # if len(data) >= 10:
        #     for i in range(10,0,-1):
        #         priceMean += (data[-i][0] + data[-i][30])
        #     priceMean /= 20
        #     priceDiff10 = (data[-1][0] + data[-i][30])/2 - priceMean
        #     bought = (data[-1][0] >= data[-2][0])  * 1
        #     sold = (data[-1][30] <= data[-2][30])  * 1
           
        #     X  = orderImbalances + levelImbalances + [priceDiff10,bought,sold]
        # else:
        #     X = orderImbalances + levelImbalances + [0,0,0]

        # return np.dot(np.array(X),np.array(weights))+bias
        # orderImbalances = []
        # means = {'askSize0': 7.122326821015551,'bidSize0': 6.664690259333936,'askSize1': 13.105987624278661,'bidSize1': 11.942553477484994,'askSize2': 15.589880182623004,'bidSize2': 13.75408421979652,'askSize3': 16.361909198359175,'bidSize3': 14.32155044149343}
        # stds = {'askSize0': 12.199097015681906,'bidSize0': 10.519117143767081,'askSize1': 18.048612878792103,'bidSize1': 14.695585863698176,'askSize2': 21.87241884197138,'bidSize2': 17.83868081319584,'askSize3': 24.18229531433362,'bidSize3': 20.597330755364773}
        # for i in range(4):
        #     orderImbalances += [(data[15+i] - data[45+i]) / (data[15+i] + data[45+i])]

        # for i in range(4):
        #     data[15+i] = (data[15+i] - means['askSize'+str(i)])  / stds['askSize'+str(i)]
        #     data[45+i] = (data[45+i] - means['bidSize'+str(i)])  / stds['bidSize'+str(i)]

        # orderImbalances = np.array(list(data[15:19]) + list(data[45:49]) +orderImbalances).reshape(1,12)
        # self.debug_print(orderImbalances)
        # timestep = 1
        # data = data[-timestep:]

        
        # # if len(data) < timestep:
        # #     return 0

        # featureIndexes = list(range(45,55)) + list(range(15,25))

        # for i in range(timestep):
        #   data[i] = np.nan_to_num(data[i])
        #   data[i][featureIndexes] = self.pca.transform(data[i][featureIndexes].reshape(1,len(featureIndexes)))
        # data = np.array(data)
        
        


        
        
    
        # X = data[:,featureIndexes].reshape((1,timestep,len(featureIndexes)))

        # if len(data) < 20:
        #   x = data[-1][15:18] +  data[-1][45:48] + [np.nan]*8
        #   x = np.array(x)
        # else:
        #   x = data[-1][15:18] + data[-1][45:48]
        #   for i in range(15,18):
        #     x += [data[-1][i]-data[-20][i]]
        #   for i in range(45,48):
        #     x += [data[-1][i]-data[-20][i]] 
        #   x += [data[-1][0] - data[-20][0]] + [data[-1][30]-data[-20][30]]
        #   x = np.array(x) 
        # pred = self.model.predict(x.reshape(1,14))

        # if len(data) == 1:
        #   return 0

        # data = data[-1:]
        # X = []
        # timestep = 1
        # data  = data[-1]
        # askSizeScales = [404.0,405.0,405.0,455.0,571.0,621.0,668.0,668.0,667.0,674.0,674.0,674.0,674.0,674.0,672.0]
        # bidSizeScales = [385.0,385.0,380.0,377.0,394.0,394.0,539.0,548.0,546.0,545.0,537.0,602.0,533.0,483.0,483.0]
        # # featureIndexes = list(range(55,44,-1)) + list(range(15,26))
        # featureIndexes = list(range(15,25)) + list(range(45,55)) + [0] + [30]
        # for i in range(timestep):
        # #   temp = np.nan_to_num(data[i])
          
        #   temp = np.nan_to_num(data)
        #   for j in range(11):
        #     temp[15+j] /= askSizeScales[j]
        #     temp[45+j] /= bidSizeScales[j]
        #   temp[0] = (temp[0] - 1642.0) / 75.0
        #   temp[30] =(temp[30] - 1642.0) / 75.0


        #   X.append(temp[featureIndexes])


        # # # for i in range(1,15):
        # # #   if data[i] == 0:
        # # #     data[i] = data[i-1] + 0.5
        # # #   if data[30+i] == 0:
        # # #     data[30+i] = data[29+i] - 0.5
        


        # # # for i in range(15):
        # # #   data[i] = (data[i] - 1642.0) / 73.0
        # # #   data[30+i] = (data[30+i] - 1642.0) / 73.0
        # # #   data[15+i] /= askSizeScales[i]
        # # #   data[45+i] /= bidSizeScales[i]

        # X = np.array(X).reshape((1,timestep,len(featureIndexes)))
        # self.debug_print(X)


        
        # pred = self.model.predict(orderImbalances)
        # return pred[0][0]
        # return pred

    """
    run_submission() will iteratively fetch the next row of data in the format 
       specified (get_next_data_as_string, get_next_data_as_list, get_next_data_as_numpy_array)
       for every prediction submitted to self.submit_prediction()
    """
    def run_submission(self):

        self.debug_print("Use the print function `self.debug_print(...)` for debugging purposes, do NOT use the default `print(...)`")
        hist = []
        while(True):
            """
            NOTE: Only one of (get_next_data_as_string, get_next_data_as_list, get_next_data_as_numpy_array) can be used
            to get the row of data, please refer to the `OVERVIEW OF DATA` section above.

            Uncomment the one that will be used, and comment the others.
            """

            #data = self.get_next_data_as_list()
            
            data = self.get_next_data_as_numpy_array()
            hist += [data]
            #data = self.get_next_data_as_string()

            prediction = self.get_prediction(hist)

            """
            submit_prediction(prediction) MUST be used to submit your prediction for the current row of data
            """
            self.submit_prediction(prediction)


if __name__ == "__main__":
    MySubmission()
