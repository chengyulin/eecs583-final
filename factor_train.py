import keras
import tensorflow as tf
from keras.layers import Input, Dropout, Embedding, merge, LSTM, Dense
from keras.layers.normalization import BatchNormalization
from keras.models import Model, Sequential, load_model
import numpy as np
from sklearn.model_selection import KFold
from sklearn.utils import shuffle

if __name__ == '__main__':
	x = np.load('case_b_input.npy')
	y = np.load('case_b_output_Fermi.npy')
	# kfold = KFold(n_splits=17, shuffle=True)
	# for i in range(5):
		# x, y = shuffle(x, y)
	model = Sequential([
	  Embedding(input_dim=129, input_length=1024,
                      output_dim=64, name="embedding"),
	  LSTM(64, return_sequences=True, implementation=1, name="lstm_1"),
	  LSTM(64, implementation=1, name="lstm_2"),
	  BatchNormalization(),
	  Dense(32, activation="relu"),
	  Dense(6, activation="softmax")
	])
	opt = keras.optimizers.Adam(lr=0.01)
	model.compile(optimizer=opt, loss="categorical_crossentropy", metrics=['accuracy'])

	model.fit(x, y, epochs=100, batch_size=4, verbose=1, shuffle=True)
	# print(type(x[16]))
	# tmp = np.reshape(x[16], (1,1024))
	# # print(type(tmp))
	# # print(tmp.shape)
	# out = model.predict(tmp)
	# # print(out.shape)
	# ind = np.argmax(out)
	# 	if y[0,ind] == 1:
	# 		print('validate accuracy:1.000')
	# 	else:
	# 		print('validate accuracy:0.000')