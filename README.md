# 📚 Iniciação Científica — Processamento de Linguagem Natural (PLN) com Machine Learning

Repositório da Iniciação Científica focado em **Processamento de Linguagem Natural (PLN)** e **Inteligência Artificial**, com foco em **classificação de textos em português** usando modelos clássicos de Machine Learning e Contrastes Modernos (Transformers/Hugging Face).

O material desenvolvido neste repositório foi planejado para ser **altamente didático**: teoria concisa → exemplo prático → interpretação visual da saída e extração de métricas de avaliação.

---

## 🧭 Estrutura do Repositório

```text
PLN/
├── PLN_Machine_Learning.ipynb   ← Pipeline completo de Fundamentos e Pré-Proc de PLN
├── IA_Machine_Learning.ipynb    ← Fundamentos de IA, Classificação Linear/Probabilística e Transformers
└── NLTK_VADER/
    └── sentiment.py             ← App Streamlit Interativo de análise de sentimento (VADER)
```

---

## 📓 Resumo dos Notebooks

### 1. `PLN_Machine_Learning.ipynb` — *O Pipeline Clássico de PLN*

Cobre o fluxo de ponta a ponta focado em Processamento Numérico e Limpeza do Texto:

| Parte | Tópico | O que cobre |
|-------|--------|-------------|
| **1-2** | **Introdução e Setup** | O que é PLN, desafios da ambiguidade linguística, instalações com `nltk` e `spacy`. |
| **3** | **Tokenização** | Limpeza básica dividindo sentenças ou palavras, conversão usando `.lower()`. |
| **4** | **Stopwords** | Remoção de conectivos descartáveis vs. Construção de listas de remoção seguras (`não` perder negações). |
| **5-7** | **Bag of Words & TF-IDF** | Contagem de Ocorrências Absolutas (`CountVectorizer`) vs Frequência e Raridade Ponderada (`TfidfVectorizer`). |
| **8** | **Classificação de Sentimento** | Implementação de Multinomial Naive Bayes e Logistic Regression p/ detectar sentimentos positivos/negativos. |
| **9** | **Word Embeddings** | Visão conceitual usando `Word2Vec` (Gensim) para captar conexões e proximidade semântica (gatilho: Cachorro = Gato). |

### 2. `IA_Machine_Learning.ipynb` — *Modelos e Avaliações*

Cobre Inteligência Artificial aplicada, focado em Algoritmos (Clássicos vs Modernos) e Interpretação:

| Parte | Tópico | O que cobre |
|-------|--------|-------------|
| **1-3** | **Fundamentação de IA** | Abordagens de Machine Learning (Supervisionado, não-supervisionado) vs IA Simbólica. |
| **4-5** | **Ciência de Dados** | Matrizes e vetores no contexto de código, Overfitting, Underfitting e importância dos dados. |
| **6** | **Naive Bayes (Teórica)** | Intuição básica por trás do cálculo de Teorema de Bayes em eventos de texto probabilísticos. |
| **7** | **Modelos Práticos & Métricas** | Exemplo passo-a-passo e comentado explicitando a divisão entre Spam e Ham, incluindo relatórios reais de classificação e interpretação: **Precisão vs Recall vs F1-Score**. |
| **8** | **Modelos Clássicos vs Hugging Face** | O contraste de trabalhar codificando *Features Manuais* versus abstrair redes neurais e State of the Art via `pipelines("sentiment-analysis")` do pacote Transformer. |
| **9-10** | **Limitações e Referências** | Ética no ML, modelos de caixa preta, privacidade e referências literárias. |

---

## 🧪 Tecnologias Usadas

| Tecnologia | Função no Projeto |
|------------|------------------|
| **Python** 3.9+ | Linguagem core para todos os algoritmos. |
| **NLTK / SpaCy** | Pre-processamento de léxico, stopwords e VADER. |
| **Scikit-learn** | Geração de matrizes (`TF-IDF`), Classificadores (`NaiveBayes`/`LogisticRegression`) e Métricas Robustas. |
| **Hugging Face** | Instanciação de modelos de ponta baseados no ecossistema Transformer. |
| **Pandas / NumPy**| Manipulação avançada de tensores e Arrays Pandas para visualização de matriz de frequência. |
| **Streamlit** | UI reativa e hospedagem imediata de protótipos em Python. |

### Dependências p/ Uso:

```bash
# Instalador Geral de Pipeline Científico:
pip install -U nltk scikit-learn pandas numpy gensim spacy wordcloud

# Instalador de Interface Gráfica / NLP Moderno:
pip install -U streamlit transformers torch sentencepiece
```

---

## 🧠 Resultados Principais - O Que a IC Demonstrou

1. Percorrimos o **pipeline de maturidade NLP** partindo de *Bag Of Words* a *Deep Learning Pipelines*.
2. Conseguimos justificar porque a matemática do **TF-IDF supera Bag-of-Words** baseando-se em pesos de penalidade de *stopwords* indiretas.
3. Treinamos, validamos e metrificamos separadamente (usando F1-Score ao invés de apenas Acurácia) cenários estritos, como **Deteção de Spam**.
4. Demonstramos as facilidades e os atalhos tecnológicos criados pelos Models da **Hugging Face** para resolução imediata de Análise de Sentimentos.
5. Emersão final do código puro via Jupyter Notebook para uma GUI tangível e real gerada em **Streamlit**.

---

## 👤 Equipe e Autoria

- **Orientação:** Eliane De Bortoli Fávero
- **Alunos Envolvidos:** Gustavo (Aluno A) e Felipe (Aluno B)
- **Instituição:** UTFPR — Pato Branco
- **Período de Realização:** 2025

🔥 *Sinta-se livre para clonar o repositório, inspecionar cada modelo, brincar e injetar frases malucas no `IA_Machine_Learning.ipynb` para ver de que lado o Naive Bayes oscila nas previsões de Spam!*
