# XTXForecastingChallenge

My attempt at 
https://challenge.xtxmarkets.com/

Learned and tested Regression, Gradient Boosted Tree Regression, LSTM/GRU/RNNs, 1D Convnets, DNN approaches

Most successful approaches were simple Linear regression/GBT regression on the shape of the order book, order book volumes only 

This likely works as order book volume is slightly stationary; some mean reversion factor inferred from the
regression coefficients k(Ask-Bid Volume), k >0 . This implies that if there are more sell orders than buy (signalling price will fall), the price will mean revert in the given time frame

Most effective deep learning approach was 1D Convnets; in retrospect shouldve tested using more hidden layers and larger layer sizes
