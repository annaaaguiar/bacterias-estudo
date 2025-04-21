import streamlit as st
import pandas as pd

csv_path = "bacterias.csv"

st.set_page_config(
    page_title="Estudo de Bactérias - Visualização Moderna",
    page_icon="🦠",
    layout="wide"
)
# Título
st.title("Estudo de Bactérias 🦠")

# Tenta carregar os dados
try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"Arquivo '{csv_path}' não encontrado. Verifique o caminho.")
    st.stop()

if not df.empty:
    # Filtros
    gram_options = df["GRAM"].dropna().unique().tolist()
    gram_selecionado = st.multiselect("Filtrar por coloração de Gram:", gram_options)

    morfologia_options = df["MORFOLOGIA"].dropna().unique().tolist()
    morfologia_selecionada = st.multiselect("Filtrar por morfologia:", morfologia_options)

    ver_todas = st.checkbox("Visualizar todas as bactérias (ignorar filtros)")

    # Define o DataFrame filtrado
    if ver_todas:
        df_filtrado = df.copy()
        st.info("Exibindo todas as bactérias, independentemente dos filtros.")
    
    elif gram_selecionado or morfologia_selecionada:
        df_filtrado = df.copy()
        if gram_selecionado:
            df_filtrado = df_filtrado[df_filtrado["GRAM"].isin(gram_selecionado)]
        if morfologia_selecionada:
            df_filtrado = df_filtrado[df_filtrado["MORFOLOGIA"].isin(morfologia_selecionada)]

        if df_filtrado.empty:
            st.warning("Nenhuma bactéria encontrada com os filtros selecionados.")
    
    else:
        df_filtrado = pd.DataFrame()
        st.info("Use os filtros ou marque a opção para visualizar todas as bactérias.")

    # Exibição dos cards se houver dados filtrados
    if not df_filtrado.empty:
        st.subheader("Bactérias Encontradas")
        col1, col2, col3 = st.columns(3)
        colunas = [col1, col2, col3]

        for i, (_, row) in enumerate(df_filtrado.iterrows()):
            with colunas[i % 3].expander(f"{row['BACTÉRIAS']}"):
                st.write(f"*Gram:* {row['GRAM']}")
                st.write(f"*Morfologia:* {row['MORFOLOGIA']}")
                st.write(f"*Patologias Associadas:* {row['PATOLOGIAS ASSOCIADAS']}")
                st.write(f"*Resposta Inflamatória:* {row['RESPOSTA INFLAMATÓRIA']}")
                st.write(f"*Resistência Microbiana:* {row['RESISTÊNCIA MICROBIANA']}")


# Seção de resumos
st.header("Resumos e Definições")
# Adicionar explicações em cards interativos

# Card sobre Gram
with st.expander("O que é a Coloração de Gram?"):
    st.write("""
    A coloração de Gram é uma técnica usada para classificar as bactérias em dois grupos principais:
    - **Gram-positivas**: possuem uma parede celular espessa de peptidoglicano que retém a coloração violeta.
        Cor após a coloração: Roxo 💜
             
    - **Gram-negativas**: têm uma parede celular mais fina, com uma camada de lipopolissacarídeos, que não retém a corante.
        Cor após a coloração: Rosa 🩷
    
    Esse teste é importante porque ajuda a escolher o antibiótico mais adequado para tratar infecções bacterianas.
    """)

# Card sobre o passo a passo da Coloração de Gram
with st.expander("Passo a Passo da Coloração de Gram"):
    st.write("""
    1. Aplicação do Cristal Violeta:
    O cristal violeta é o primeiro corante aplicado. Ele penetra nas células bacterianas e colore a parede celular de todas as bactérias, independentemente de sua estrutura. As células bacterianas ficam roxas após essa etapa.
    
    2. Aplicação do Lugol (Iodo):
    Após o cristal violeta, é aplicada uma solução de iodo, geralmente chamada de Lugol. O iodo forma complexos com o cristal violeta, criando uma ligação mais forte entre o corante e as estruturas da célula. Esse passo é crucial porque ajuda a fixar o cristal violeta nas células, tornando a coloração mais estável.

    3. Descoloração com Álcool ou Acetona:
    Este é o passo crítico que permite a diferenciação entre as bactérias Gram-positivas e Gram-negativas. O álcool ou acetona remove o cristal violeta das células Gram-negativas, que possuem uma parede celular mais fina, enquanto as células Gram-positivas, com uma parede celular mais espessa, retêm o corante. Após a descoloração, as células Gram-positivas continuam roxas, enquanto as Gram-negativas ficam incolores.

    4. Contracoloração com Safranina:
    Como as células Gram-negativas ficaram incolores após a descoloração, a safranina é aplicada como corante de contraste. Ela colore as células Gram-negativas de forma que fiquem rosas. As células Gram-positivas, já coloridas de roxo, não são afetadas pela safranina.
    
    Isso permite diferenciar as bactérias de acordo com a espessura da parede celular.
    """)

# Card sobre Resistência Microbiana
with st.expander("O que é Resistência Microbiana?"):
    st.write("""
    A resistência microbiana ocorre quando as bactérias ou outros microrganismos se tornam resistentes ao efeito de medicamentos (antibióticos).
    Isso pode ocorrer devido a mutações ou à transferência de genes de resistência entre bactérias.
    A resistência microbiana é um grande problema de saúde pública, pois torna as infecções mais difíceis de tratar.
    """)

# Card sobre as Bactérias AAR (Álcool-Ácido Resistentes)
with st.expander("O que são as Bactérias AAR (Álcool-Ácido Resistentes)?"):
    st.write("""
    As bactérias AAR são aquelas que possuem uma parede celular rica em lipídios, tornando-se resistentes ao tratamento com álcool ácido.
    A técnica de coloração de Ziehl-Neelsen é utilizada para identificar essas bactérias.
    """)

