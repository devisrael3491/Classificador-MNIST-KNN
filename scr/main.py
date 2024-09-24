#importações necessárias

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import joblib

#tratamento de exceções
try:
    train_data = np.array(pd.read_csv('MNIST_csv/MNIST_train.csv'))
    test_data = np.array(pd.read_csv('MNIST_csv/MNIST_test.csv'))
except FileNotFoundError:
    print(f'E: Arquivo inexistente. Certifique-se de baixar todos os arquivos corretamente.')
except Exception as e:
    print(f'E: um erro inesperado ocorreu: {e}.')
else:
    scaler = StandardScaler() #criando uma instância do scaler para a padronização dos dados.

    #separando dados de teste e treino.

    X_train = train_data[:, 1:]
    X_test = test_data[:, 1:]
    y_train = train_data[:, 0]
    y_test = test_data[:, 0]

    #usando o scaler para padronizar as features.

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    #instanciando o classificador com k = 5.

    modelo = KNeighborsClassifier(n_neighbors=5)

    #treinamento do modelo.

    modelo.fit(X_train_scaled, y_train)

    #fase de testes, utilização do classification report para mapear os resultados.

    y_pred = modelo.predict(X_test_scaled)

    resultado = classification_report(y_test, y_pred)

    print(resultado)

    #pertinência do modelo em um arquivo para futuros usos.

    joblib.dump(modelo, 'KNN_MNIST.pkl')
    joblib.dump(scaler, 'SCALER_MNIST.pkl')

