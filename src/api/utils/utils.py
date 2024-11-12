import pickle

def load_model() -> object | None: 
    try:
        with open('model_regression.pkl', 'rb') as f:
            model_regression = pickle.load(f)
            return model_regression
    except Exception as e:
        print(f"É preciso rodar as celular jupyter para carregar o modelo")
    return None