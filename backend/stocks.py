import numpy as np
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import *
from keras import Sequential
from keras.layers import LSTM ,Dense,Dropout



def stocks():
    dataset= pd.read_csv("AMZN.csv", index_col="Date",parse_dates=True) # read csv data using pandas
    dataset.head() # the first  5 rows in the data


    # data cleaning
    dataset.isna().any()  # to check if data is not applicable eg checking missi ng values
    dataset.info() # basic info of the data ie data type , columns and non-null values

    #####dataset['Open'].plot(figsize=(16,6))  #plot
    dataset.info()


      # convert the object data type to string
    dataset['Close']=dataset['Close'].astype(str).str.replace(',' , ' ').astype(float)
    dataset['Volume']=dataset["Volume"].astype(str).str.replace(',' , ' ').astype(float)

    #7 day rolling mean
    dataset.rolling(7).mean().head(20)
    ######dataset['Open'].plot(figsize=(16,6))
    ######dataset.rolling(window=30).mean()['Close'].plot()
    dataset['Close :30 Day Mean']=dataset['Close'].rolling(window=30).mean()
    ########dataset[['Close','Close :30 Day Mean']].plot(figsize=(16,6))

    #optimal specify minimum number of periods
    #########dataset['Close'].expanding(min_periods=1).mean().plot (figsize=(16,6))

    #training
    training_set=dataset["Open"]
    training_set=pd.DataFrame(training_set)

    # data cleaning
    dataset.isna().any()

    #feature scalling
    sc=MinMaxScaler(feature_range=(0,1))
    training_set_scaled=sc.fit_transform(training_set)

    #create a data structure  with 60 timestamps and and output
    x_train=[]
    y_train=[]
    for i in range (60,1256):
        x_train.append(training_set_scaled[i-60:i,0])
        y_train.append(training_set_scaled[i,0])
    x_train,y_train=np.array(x_train),np.array(y_train)


    # reshape the data
    x_train=np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))



    #initilizing RNN
    regressor= Sequential()


    # adding layers in LSTM
    regressor.add(LSTM(units =50,return_sequences=True,input_shape=(x_train.shape[1],1)))
    regressor.add(Dropout(0.2)) # dropout reducing over fitting
    regressor.add(LSTM(units=50,return_sequences=True))
    regressor.add(Dropout(0.2))
    regressor.add(LSTM(units=50))
    regressor.add(Dropout(0.2))

    # adding the outpt layer
    regressor.add(Dense(units=1))

    #compliling RNN
    regressor.compile(optimizer='adam',loss='mean_squared_error')

    #fitting the RNN to the trainging set
    regressor.fit(x_train,y_train,epochs=2,batch_size=32) #batch size - training examples utilized

    dataset_test=pd.read_csv("AMZN.csv", index_col="Date",parse_dates=True)
    real_stock_price=dataset_test.iloc[:,1:2].values # iloc - selecting rows and columns bt number in order that they appear on the data frame

    #dataset_test.head()
    #dataset_test.info()

    dataset_test["Volume"]= dataset_test["Volume"].astype(str).str.replace(',','').astype(float)
    test_set=dataset_test["Open"]
    test_set=pd.DataFrame(test_set)
    #test_set.info()

     #getting the predicted stlock price of 2017
    dataset_total=pd.concat((dataset['Open'],dataset_test['Open']),axis = 0)
    inputs = dataset_total[len(dataset_total)-len(dataset_test) - 60:].values
    inputs=inputs.reshape(-1,1)
    inputs=sc.transform(inputs)

    x_test=[]
    for i in range (60,1256):
        x_test.append(inputs[i-60:i,0])
    x_test=np.array(x_test)

    print(x_test)



    x=regressor.predict(x_test)
    qw=sc.inverse_transform(x)

    print(qw)
    print(real_stock_price)

    plt.plot(qw, color='blue', label="predicted google stock price")
    plt.plot(real_stock_price, color="red", label="Real Google Price")

    plt.title("google stock price prediction")
    plt.xlabel('time')
    plt.ylabel("google stock Price")
    plt.legend()
    plt.show()
    return qw, real_stock_price



if __name__=="__main__":
    stocks()

# visualising the results
