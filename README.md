# Proyecto de Gradient Boosting para Detectar el Consumo de Carbono

Este proyecto utiliza un modelo de **Gradient Boosting** para predecir el consumo de carbono de una persona en función de diversas características como su tipo de cuerpo, hábitos de transporte, reciclaje, entre otros. Los datos fueron obtenidos de Kaggle y se pueden acceder [aqui](https://www.kaggle.com/datasets/dumanmesut/individual-carbon-footprint-calculation)

## Estructura del proyecto 

- `data/` : Contiene los datos utilizados para entrenar y evaluar el modelo (disponible en kaggle)
- `models/` : El modelo entrenado esta en formato '.joblib'
- `notebooks/` : Notebooks de Jupyter con explicaciones paso a paso del entrenamiento y evaluación del modelo.
- `scripts/`: Código en Python para entrenar y evaluar el modelo.

## Requisitos
Para instalar las dependencias del proyecto, ejecuta:

```bash
pip install -r requirements.txt
