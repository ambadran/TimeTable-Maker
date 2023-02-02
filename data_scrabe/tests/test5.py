import pickle


with open('test.pkl', 'rb') as f:
    print(pickle.load(f))
