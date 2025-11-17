# PLN / Machine Learning Completo

Este repositório contém um **Jupyter Notebook** com exemplo completo de **Processamento de Linguagem Natural (PLN)** usando *machine learning*. O notebook cobre desde a preparação de dados, vetorização, até o treinamento e avaliação de modelos.

## 🔍 Conteúdo

- Introdução ao PLN  
- Pré-processamento de texto: tokenização, limpeza, remoção de stopwords  
- Vetorização: Bag of Words, TF-IDF  
- Redução de dimensionalidade (se aplicada)  
- Modelos de Machine Learning: regressão, classificação, outros  
- Avaliação de modelos: métricas (acurácia, F1, recall, precision, etc.)  
- Visualização de resultados  

## 🧪 Tecnologias e Dependências

Para executar o notebook, você vai precisar de:

- Python 3.x  
- Bibliotecas:  
  - `nltk` (para tokenização, stopwords, etc.)  
  - `scikit-learn` (modelos, vetorizadores, métricas)  
  - `pandas` (manipulação de dados)  
  - `numpy`  
  - (outras que você usou no notebook)

Você pode instalar as dependências usando:

```bash
pip install nltk scikit-learn pandas numpy

#Também é recomendado baixar alguns recursos do NLTK (ex: stopwords, punkt):

import nltk
nltk.download('punkt')
nltk.download('stopwords')