# 📚 Iniciação Científica — PLN com Machine Learning

Repositório da Iniciação Científica em **Processamento de Linguagem Natural (PLN)** e **Inteligência Artificial**, com foco em **classificação de textos em português** usando modelos clássicos de Machine Learning.

Material **didático**: teoria curta → exemplo prático → interpretação da saída.

---

## 🧭 Estrutura do Repositório

```
IC/
├── PLN/
│   ├── PLN_Machine_Learning.ipynb   ← Pipeline completo de PLN (10 partes)
│   └── IA_Machine_Learning.ipynb    ← Fundamentos de IA e ML (9 partes)
│
├── NLTK_VADER/
│   └── sentiment.py                 ← App Streamlit de análise de sentimento
│
└── README.md
```

---

## � Notebooks

### `PLN_Machine_Learning.ipynb` — Pipeline de PLN

Cobre o pipeline completo de Processamento de Linguagem Natural:

| Parte | Tópico | O que faz |
|-------|--------|-----------|
| 1 | Introdução ao PLN | Definição, exemplos do dia a dia, desafios (ambiguidade, negação) |
| 2 | Setup | Instalação de dependências e imports |
| 3 | Tokenização | `word_tokenize`, `sent_tokenize` e normalização com `.lower()` |
| 4 | Stopwords | Remoção padrão, riscos com negações, lista customizada |
| 5 | Bag of Words | `CountVectorizer` — matriz documento × palavra |
| 6 | TF-IDF | `TfidfVectorizer` — pesos inteligentes por raridade |
| 7 | BoW vs TF-IDF | Comparação lado a lado com o mesmo corpus |
| 8 | Classificação | Naive Bayes e Logistic Regression em reviews |
| 9 | Word Embeddings | Word2Vec com Gensim — similaridade semântica |
| 10 | Conclusão | Checklist, próximos passos e recursos |

### `IA_Machine_Learning.ipynb` — Fundamentos de IA

Cobre a teoria e os primeiros modelos de Machine Learning:

| Parte | Tópico | O que cobre |
|-------|--------|-------------|
| 1 | O que é IA | Definição, história (Turing → ChatGPT), tipos de IA |
| 2 | Abordagens | IA Simbólica vs IA Conectivista |
| 3 | Machine Learning | Supervisionado, não-supervisionado, reforço |
| 4 | Fundamentos Matemáticos | Vetores, matrizes, sigmoid, ReLU |
| 5 | Importância dos Dados | Overfitting, underfitting, regularização |
| 6 | Naive Bayes | Teorema de Bayes aplicado a classificação de texto |
| 7 | Logistic Regression | Sigmoid, gradient descent, interpretação de pesos |
| 8 | Limitações e Ética | Viés de dados, caixa preta, privacidade |
| 9 | Glossário e Recursos | Termos-chave e referências |

### `NLTK_VADER/sentiment.py` — App de Sentimento

App web simples com **Streamlit** que usa o **VADER** (NLTK) para classificar feedback de clientes como positivo, negativo ou neutro em tempo real.

---

## 🧪 Tecnologias

| Tecnologia | Uso no projeto |
|------------|---------------|
| **Python** 3.9+ | Linguagem base |
| **NLTK** | Tokenização, stopwords, VADER |
| **Scikit-learn** | CountVectorizer, TfidfVectorizer, MultinomialNB, LogisticRegression |
| **Pandas / NumPy** | Manipulação de dados e visualização de matrizes |
| **Gensim** | Word2Vec (Word Embeddings) |
| **Streamlit** | Interface web para o app VADER |

### Instalação

```bash
# Notebooks
pip install -U nltk scikit-learn pandas numpy gensim

# App VADER
pip install -U streamlit
```

Download dos recursos NLTK (executar uma vez):

```python
import nltk
for recurso in ['punkt_tab', 'stopwords', 'wordnet', 'vader_lexicon']:
    nltk.download(recurso)
```

---

## 🚀 Como usar

1. **Clone o repositório** ou envie os notebooks para o Google Colab.

2. **Pipeline de PLN** → abra `PLN/PLN_Machine_Learning.ipynb` e execute na ordem (Partes 1–10).

3. **Fundamentos de IA** → abra `PLN/IA_Machine_Learning.ipynb` e execute na ordem (Partes 1–9).

4. **App de sentimento** → execute no terminal:
   ```bash
   cd NLTK_VADER
   streamlit run sentiment.py
   ```

---

## 🧠 O que você aprende

- Percorrer o **pipeline completo de PLN**: texto bruto → tokenização → limpeza → vetorização → modelo → predição.
- Entender **BoW vs TF-IDF** e quando usar cada um.
- Criar **listas customizadas de stopwords** para preservar negações.
- Treinar e interpretar **Naive Bayes** e **Logistic Regression** em texto.
- Entender os **fundamentos de IA/ML**: tipos de aprendizado, overfitting, sigmoid, gradient descent.
- Dar os primeiros passos com **Word Embeddings** e **VADER**.

---

## 👤 Autoria

- **Aluno:** Felipe Gomes
- **Orientação:** Eliane De Bortoli Fávero
- **Instituição:** UTFPR — Pato Branco
- **Período:** 2025

---

## 📖 Recursos Recomendados

- 📚 *Speech and Language Processing* — Jurafsky & Martin
- 🎓 Machine Learning (Andrew Ng — Coursera)
- 🐍 [NLTK](https://www.nltk.org/) · [Scikit-learn](https://scikit-learn.org/) · [Gensim](https://radimrehurek.com/gensim/)
- 🤗 [Hugging Face](https://huggingface.co/) — modelos de linguagem modernos

---

**Licença:** MIT — fique à vontade para reutilizar, citando a autoria.

Se este repositório foi útil, deixe uma ⭐ e abra issues com sugestões. Bons estudos! 🚀
