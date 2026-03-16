# -*- coding: utf-8 -*-
import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# ==============================================================================
# CONFIGURAÇÕES INICIAIS
# ==============================================================================
# Garantir que o recurso necessário do NLTK esteja disponível
@st.cache_resource
def carregar_recursos():
    nltk.download('vader_lexicon', quiet=True)
    return SentimentIntensityAnalyzer()

satisfacao = carregar_recursos()

# ==============================================================================
# INTERFACE DO USUÁRIO (UI)
# ==============================================================================
st.set_page_config(page_title="Análise de Satisfação", page_icon="📊")

st.title("🤖 Análise de Satisfação do Cliente")
st.markdown("""
Esta ferramenta utiliza o algoritmo **VADER** para identificar a polaridade de feedbacks.
*Nota: O VADER é otimizado para Inglês, mas funciona com termos universais e emojis.*
""")

# Entrada de dados
feedback = st.text_area("Digite a avaliação do cliente:", placeholder="Ex: Adorei o atendimento, foi excelente! 😊")

# ==============================================================================
# LÓGICA DA MÁQUINA PREDITIVA
# ==============================================================================
if st.button("Analisar Sentimento"):
    if feedback.strip():
        # Cálculo da polaridade
        pontuacao = satisfacao.polarity_scores(feedback)
        score_composto = pontuacao['compound'] # O 'compound' é a métrica principal (-1 a 1)

        st.divider()
        st.subheader("Resultado da Análise")

        # Regras de refinamento baseadas no Score Composto (Padrão Acadêmico)
        if score_composto >= 0.05:
            st.success(f"### Sentimento: POSITIVO 😊")
            st.info(f"Grau de satisfação: {score_composto:.2f}")
            
        elif score_composto <= -0.05:
            st.error(f"### Sentimento: NEGATIVO 😞")
            st.info(f"Grau de insatisfação: {score_composto:.2f}")
            
        else:
            st.warning(f"### Sentimento: NEUTRO 😐")

        # Expansor com detalhes técnicos para a IC
        with st.expander("Ver detalhes técnicos da pontuação"):
            st.json(pontuacao)
    else:
        st.warning("Por favor, digite algo para analisar.")

# Instrução de execução
# No terminal: pip install streamlit nltk
# no terminal: cd NLTK_VADER
# No terminal: streamlit run sentiment.py