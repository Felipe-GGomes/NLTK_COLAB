# 🗣️ PLN com Machine Learning — Iniciação Científica

Repositório da IC em **Processamento de Linguagem Natural (PLN)** com foco em **classificação de textos em português** usando **modelos clássicos de Machine Learning** e representações de texto como **Bag of Words, TF‑IDF e Word Embeddings**.

O código foi pensado para ser **didático**: teoria curta → exemplo prático → interpretação da saída.

---

## 🧭 Arquivos desta pasta

```
PLN/
├── PLN_Machine_Learning.ipynb          ← Pipeline completo de PLN (10 partes)
├── IA_Machine_Learning.ipynb           ← Fundamentos de IA e ML (9 partes)
├── PLN_Machine.ipynb                   ← Versão anterior (referência)
├── PLN_Machine_Learning_Completo.ipynb ← Versão estendida (referência)
├── Sumario.md                          ← Sumário detalhado dos conteúdos
└── README.md                          ← Este arquivo
```

---

## 📓 Notebooks Principais

### `PLN_Machine_Learning.ipynb` — Pipeline de PLN

| Parte | Tópico | O que cobre |
|-------|--------|-------------|
| 1 | Introdução ao PLN | Definição, exemplos, desafios (ambiguidade, negação) |
| 2 | Setup | Instalação de dependências e imports |
| 3 | Tokenização | `word_tokenize`, `sent_tokenize`, normalização `.lower()` |
| 4 | Stopwords | Remoção padrão, riscos com negações, lista customizada |
| 5 | Bag of Words | `CountVectorizer` — matriz documento × palavra |
| 6 | TF-IDF | `TfidfVectorizer` — pesos inteligentes por raridade |
| 7 | BoW vs TF-IDF | Comparação lado a lado com o mesmo corpus |
| 8 | Classificação | Naive Bayes e Logistic Regression em reviews |
| 9 | Word Embeddings | Word2Vec com Gensim — similaridade semântica |
| 10 | Conclusão | Checklist, próximos passos e recursos |

### `IA_Machine_Learning.ipynb` — Fundamentos de IA

| Parte | Tópico | O que cobre |
|-------|--------|-------------|
| 1 | O que é IA | Definição, história (Turing → ChatGPT), tipos de IA |
| 2 | Abordagens | IA Simbólica vs Conectivista |
| 3 | Machine Learning | Supervisionado, não-supervisionado, reforço |
| 4 | Fundamentos Matemáticos | Vetores, matrizes, sigmoid, ReLU |
| 5 | Importância dos Dados | Overfitting, underfitting, regularização |
| 6 | Naive Bayes | Teorema de Bayes aplicado a texto (com código) |
| 7 | Logistic Regression e Prática | Sigmoid, gradient descent e Exemplo Prático de Spam vs Ham (Métricas: Precisão, Recall, F1) |
| 8 | Modelos de Ponta | Contraste de ML Clássico vs Transformers (Hugging Face via `pipeline`) |
| 9 | Limitações e Ética | Viés de dados, caixa preta, privacidade |
| 10 | Glossário e Recursos | Termos-chave e referências |

---

## 📚 O que você vai encontrar aqui

O conteúdo segue o pipeline completo de PLN:

1. **Introdução ao PLN**
   - O que é PLN, exemplos do dia a dia, desafios (ambiguidade, negação, variações)
   - Pipeline geral: texto bruto → tokens → limpeza → vetorização → modelo → predição

2. **Pré‑processamento de texto**
   - Tokenização com NLTK (`word_tokenize`, `sent_tokenize`)
   - Normalização (`.lower()`)
   - Stopwords em português (`nltk.corpus.stopwords`)
   - Lista customizada de stopwords para **não perder negações** como "não", "mas", "nunca"

3. **Representações clássicas de texto**
   - **Bag of Words (BoW)** com `CountVectorizer`
     - Criação de vocabulário, matriz documento × palavra
     - Interpretação de linhas/colunas e contagens
   - **TF‑IDF** com `TfidfVectorizer`
     - Intuição de TF, IDF e TF‑IDF (exemplos numéricos)
     - Matrizes TF‑IDF e palavras mais importantes por documento
   - **BoW vs TF‑IDF**
     - Comparação lado a lado com o mesmo corpus
     - Quando usar BoW, quando preferir TF‑IDF

4. **Classificação de Sentimentos**
   - Pipeline completo: texto → TF‑IDF → modelo → predição
   - **Naive Bayes (MultinomialNB)** como primeiro classificador probabilístico
   - **Logistic Regression** como classificador linear que retorna probabilidades
   - Predição em novas reviews, discussão sobre overfitting/dados pequenos

5. **Word Embeddings (introdução prática)**
   - Intuição: vetores densos que capturam semântica
   - Demonstração com **Word2Vec (Gensim)**
   - Palavras similares ("gato" ~ "cachorro", "python" ~ "java")
   - Diferença para BoW/TF‑IDF e quando vale a pena usar

6. **Conclusão e checklist**
   - Revisão do pipeline completo
   - O que você domina depois de passar pelos notebooks
   - Sugestões de próximos passos (Transformers, BERT/GPT, etc.)

---

## 🧪 Tecnologias e Dependências

| Tecnologia | Uso nos notebooks |
|------------|------------------|
| **Python** 3.9+ | Linguagem base |
| **NLTK** | Tokenização, stopwords |
| **Scikit‑learn** | Modelos (Naive Bayes, Logistic Regression), matrizes (TF-IDF, BoW) e Métricas de avaliação |
| **Hugging Face** | NLP moderno usando `transformers` e `pipeline` |
| **Pandas** | Visualização de matrizes BoW/TF‑IDF como `DataFrame` |
| **NumPy** | Operações numéricas com vetores |
| **Gensim** | Word2Vec (Word Embeddings) |

Instalação sugerida:

```bash
pip install -U nltk scikit-learn pandas numpy gensim transformers torch sentencepiece
```

Recursos do NLTK (baixar uma vez):

```python
import nltk
for recurso in ['punkt_tab', 'stopwords', 'wordnet']:
    nltk.download(recurso)
```

---

## 🚀 Como usar (local ou Colab)

1. Clone o repositório ou envie o notebook para o Google Colab.

2. Abra o notebook principal (`PLN_Machine_Learning.ipynb`).

3. Execute na ordem:
   - **Partes 1–3:** introdução, setup, tokenização/normalização
   - **Parte 4:** stopwords e stopwords customizadas
   - **Partes 5–7:** BoW, TF‑IDF e comparação
   - **Parte 8:** classificação de sentimentos (Naive Bayes e Logistic)
   - **Parte 9:** embeddings (opcional, mais avançado)

4. Em cada seção, teste com seus próprios textos (frases positivas/negativas, reviews, etc.).

5. Explore as células de análise (top palavras, pesos do modelo) para entender **por que** o modelo decide como decide.

6. Para fundamentos de IA/ML, abra `IA_Machine_Learning.ipynb` (Partes 1–9).

---

## 🧠 O que você aprende com este projeto

- Sair do **texto bruto** até um **classificador de sentimento funcional**.
- Entender as **diferenças práticas** entre BoW e TF‑IDF e quando escolher cada um.
- Criar **listas customizadas de stopwords** para não destruir a informação de negação.
- Treinar e interpretar **modelos clássicos de ML** em texto (Naive Bayes, Logistic Regression).
- Ler e extrair **métricas robustas** em cenários reais como Spam vs Ham (Acurácia, Precisão, Recall e F1-Score).
- Entender os **fundamentos de IA/ML**: tipos de aprendizado, overfitting, sigmoid, gradient descent.
- Dar os primeiros passos com **Word Embeddings** e similaridade semântica.
- Contrastar modelos clássicos com abordagens de ponta por meio do uso de **Transformers (Hugging Face pipelines)**.
- Ler e adaptar **pipelines de PLN** para seus próprios projetos em português.

---

## 👤 Autoria

- **Aluno:** Felipe Gomes
- **Orientação:** Eliane De Bortoli Fávero
- **Instituição:** UTFPR — Pato Branco
- **Tema:** Iniciação Científica em Processamento de Linguagem Natural com Machine Learning

Se este repositório te ajudou, considere deixar uma ⭐ e abrir issues com dúvidas ou sugestões.

---

## 📖 Leituras recomendadas

- 📚 *Speech and Language Processing* — Jurafsky & Martin
- 🎓 Curso de Natural Language Processing (Coursera / edX)
- 🐍 Documentação:
  - [NLTK](https://www.nltk.org/)
  - [Scikit‑learn](https://scikit-learn.org/)
  - [Gensim](https://radimrehurek.com/gensim/)
- 🤗 Comunidade: [Hugging Face](https://huggingface.co/) para modelos de linguagem modernos

---

**Licença:** MIT — fique à vontade para reutilizar os notebooks, citando a autoria.
