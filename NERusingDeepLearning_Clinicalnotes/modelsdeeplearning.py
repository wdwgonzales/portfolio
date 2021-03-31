
## ---------- New

##model 1
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 2
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 3
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=40,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 4
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=40,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='sigmoid'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 5 (from model 3)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())



#model 6 (from model 5)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='sigmoid'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())

#model 7 (from model 5)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())

#model 8 (from model 7)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.4), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())

#model 9 (from model 8)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.5), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 10 (from model 8)
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.4), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="softmax"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())

#model 11 (from model 8)
reset_random_seeds(1)
model = Sequential()
model.add(glove_embedding_layer)
model.add(Bidirectional(LSTM(units=80,return_sequences=True,dropout=0.4), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())



#------------- OLD

###working
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=160,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=40,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


##Model 1
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=25,
    mask_zero=True))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 3
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=25,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=50,return_sequences=True,dropout=0.2), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())


#model 8

reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=25,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=50,return_sequences=True,dropout=0.4), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())




# model 10
reset_random_seeds(1)
model = Sequential()
model.add(Embedding(input_dim=len(word2idx.keys()),output_dim=20,input_length=25,
    mask_zero=True))
model.add(Bidirectional(LSTM(units=50,return_sequences=True,dropout=0.3), merge_mode = 'concat'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(40, activation='tanh'))
model.add(Dense(len(label2idx.keys()), activation="sigmoid"))
opt = tensorflow.keras.optimizers.Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
print(model.summary())





