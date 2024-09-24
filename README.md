# Classificador de Dígitos com K-Nearest Neighbors (KNN)

Este projeto implementa um classificador de dígitos baseado no algoritmo supervisionado **K-Nearest Neighbors (KNN)**. O classificador foi treinado utilizando o dataset MNIST, que contém imagens de dígitos escritos à mão. O objetivo do projeto é identificar corretamente os dígitos de 0 a 9 a partir das características fornecidas pelas imagens.

## Status do Projeto
🚀 Concluído

## Descrição

O classificador utiliza o algoritmo KNN para prever os dígitos em imagens do dataset MNIST. A classificação é feita a partir de instâncias de treino e teste, com as features sendo escaladas usando `StandardScaler`. Após o treinamento, o modelo é salvo usando `joblib` para reutilização futura.

## Funcionalidades

- Classificação de dígitos escritos à mão (de 0 a 9) usando o algoritmo K-Nearest Neighbors.
- Normalização dos dados com `StandardScaler` para melhorar a precisão do modelo.
- Geração de relatório de classificação com métricas como precisão, recall e f1-score.
- Salvamento do modelo treinado e do scaler para inferência futura.

## Tecnologias Utilizadas

- **Python 3.8+**
- **Scikit-learn**: Biblioteca para algoritmos de Machine Learning.
- **Pandas**: Utilizada para manipulação e leitura dos dados CSV.
- **NumPy**: Biblioteca para operações numéricas e manipulação de arrays.
- **Joblib**: Utilizado para salvar o modelo e o scaler em disco.

## Estrutura dos Arquivos

```bash
├── scr
│   ├── MNIST_csv_zip
│   │   └── mnist_csv.zip      # Conjunto de dados usado no modelo
│   └── main.py                # Código do classificador
└── README.md                  # Documentação do projeto
```
## Modelo Salvo
O modelo treinado pode ser baixado do Google Drive através do seguinte link:

[Download do Modelo KNN](https://drive.google.com/file/d/16JgrPJgGcJtHybvMvKQdWOD6NY6gF41A/view?usp=sharing)

