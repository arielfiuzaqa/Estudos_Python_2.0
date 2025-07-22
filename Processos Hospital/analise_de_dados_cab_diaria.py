import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Configuração inicial da página Streamlit
st.set_page_config(layout="wide", page_title="Analisador Simples de Planilhas")

st.title("📊 Analisador Simples de Planilhas para SACs")
st.markdown("""
    Carregue suas planilhas (CSV ou Excel) para filtrar dados de SACs,
    visualizar demandas brutas, porcentagens e gráficos.
    **Ideal para analisar dados semelhantes de várias fontes!**
""")

# --- Carregamento de Arquivo ---
st.sidebar.header("1. Carregar Planilhas")
uploaded_files = st.sidebar.file_uploader("Escolha arquivos CSV ou Excel", type=["csv", "xlsx"], accept_multiple_files=True)

dataframes = {}
if uploaded_files:
    for uploaded_file in uploaded_files:
        try:
            if uploaded_file.name.endswith('.csv'):
                df_temp = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                # pandas.read_excel utiliza openpyxl internamente para arquivos .xlsx
                df_temp = pd.read_excel(uploaded_file)
            dataframes[uploaded_file.name] = df_temp
            st.sidebar.success(f"'{uploaded_file.name}' carregado!")
        except Exception as e:
            st.sidebar.error(f"Erro ao carregar '{uploaded_file.name}': {e}")

df = None
selected_analysis_name = None

if dataframes:
    # Opção para combinar todas as planilhas
    combine_sheets = st.sidebar.checkbox(
        "Combinar todas as planilhas para análise conjunta",
        value=True # Padrão para combinado para simplificar a análise de "pasta base"
    )

    if combine_sheets:
        if dataframes:
            try:
                df = pd.concat(dataframes.values(), ignore_index=True)
                selected_analysis_name = "Todos os Dados Combinados"
                st.sidebar.success("Planilhas combinadas!")
            except Exception as e:
                st.sidebar.error(f"Erro ao combinar planilhas. Verifique se as colunas são semelhantes: {e}")
                df = None
        else:
            st.sidebar.info("Nenhuma planilha carregada para combinar.")
    else:
        selected_file_name = st.sidebar.selectbox(
            "Ou selecione uma planilha individual",
            list(dataframes.keys())
        )
        if selected_file_name:
            df = dataframes[selected_file_name]
            selected_analysis_name = selected_file_name

if df is not None:
    st.subheader(f"Analisando: **{selected_analysis_name}**")

    # --- Filtros Dinâmicos ---
    st.sidebar.header("2. Aplicar Filtros")
    st.sidebar.markdown("Use os controles abaixo para filtrar os dados.")

    filtered_df = df.copy()

    for col in df.columns:
        col_type = df[col].dtype
        unique_values = df[col].unique()

        if pd.api.types.is_numeric_dtype(col_type):
            min_val = float(df[col].min())
            max_val = float(df[col].max())
            selected_range = st.sidebar.slider(
                f"Intervalo de {col}",
                min_value=min_val,
                max_value=max_val,
                value=(min_val, max_val)
            )
            filtered_df = filtered_df[
                (filtered_df[col] >= selected_range[0]) &
                (filtered_df[col] <= selected_range[1])
            ]
        elif pd.api.types.is_datetime64_any_dtype(col_type):
            df[col] = pd.to_datetime(df[col], errors='coerce')
            valid_dates = df[col].dropna()
            if not valid_dates.empty:
                min_date = valid_dates.min().date()
                max_date = valid_dates.max().date()
                selected_dates = st.sidebar.date_input(
                    f"Período de {col}",
                    value=(min_date, max_date),
                    min_value=min_date,
                    max_value=max_date
                )
                if len(selected_dates) == 2:
                    filtered_df = filtered_df[
                        (filtered_df[col].dt.date >= selected_dates[0]) &
                        (filtered_df[col].dt.date <= selected_dates[1])
                    ]
            else:
                st.sidebar.warning(f"Coluna '{col}' não contém datas válidas.")
        else: # Categórico (string, object)
            str_unique_values = [str(val) for val in unique_values if pd.notna(val)]
            selected_values = st.sidebar.multiselect(
                f"Selecionar {col}",
                options=str_unique_values,
                default=list(str_unique_values)
            )
            filtered_df = filtered_df[filtered_df[col].astype(str).isin(selected_values)]

    # --- Dados Brutos Filtrados ---
    st.header("Dados Brutos Filtrados")
    if not filtered_df.empty:
        st.dataframe(filtered_df)
        st.markdown(f"**Total de demandas filtradas:** {len(filtered_df)}")
    else:
        st.warning("Nenhum dado corresponde aos filtros selecionados.")

    # --- Análise de Frequência e Porcentagem ---
    st.header("Análise de Frequência e Porcentagem")
    categorical_cols = filtered_df.select_dtypes(include=['object', 'category']).columns.tolist()
    if categorical_cols:
        selected_cat_col = st.selectbox(
            "Selecione uma coluna para análise de frequência e porcentagem",
            categorical_cols
        )
        if selected_cat_col:
            frequency_df = filtered_df[selected_cat_col].value_counts().reset_index()
            frequency_df.columns = [selected_cat_col, 'Contagem']
            frequency_df['Porcentagem (%)'] = (frequency_df['Contagem'] / frequency_df['Contagem'].sum()) * 100
            st.dataframe(frequency_df.style.format({"Porcentagem (%)": "{:.2f}%"}))
    else:
        st.info("Não há colunas categóricas para análise de frequência e porcentagem.")

    # --- Tabela Dinâmica (Pivot Table) ---
    st.header("Tabela Dinâmica (Pivot Table)")
    st.markdown("Crie resumos de dados escolhendo linhas, colunas e valores para agregação.")

    all_cols = filtered_df.columns.tolist()
    if not all_cols:
        st.info("Nenhuma coluna disponível para criar uma Tabela Dinâmica.")
    else:
        # Seleção de colunas para a Tabela Dinâmica
        pivot_index = st.selectbox("Linhas (Índice)", ['Nenhum'] + all_cols, key='pivot_index')
        pivot_columns = st.selectbox("Colunas", ['Nenhum'] + all_cols, key='pivot_columns')

        # Seleção de valores e função de agregação
        numerical_cols_for_values = filtered_df.select_dtypes(include=['number']).columns.tolist()
        if not numerical_cols_for_values:
            numerical_cols_for_values = ['Contagem de Registros'] # Opção padrão se não houver numéricas

        pivot_values = st.selectbox("Valores", ['Nenhum'] + numerical_cols_for_values, key='pivot_values')

        aggregation_options = {
            'Contagem': 'size',
            'Soma': 'sum',
            'Média': 'mean',
            'Mínimo': 'min',
            'Máximo': 'max',
            'Mediana': 'median'
        }
        selected_agg_func_name = st.selectbox("Função de Agregação", list(aggregation_options.keys()), key='agg_func')
        agg_func = aggregation_options[selected_agg_func_name]

        if pivot_index != 'Nenhum' or pivot_columns != 'Nenhum' or pivot_values != 'Nenhum':
            try:
                # Prepare os parâmetros para a pivot_table
                index_param = pivot_index if pivot_index != 'Nenhum' else None
                columns_param = pivot_columns if pivot_columns != 'Nenhum' else None
                values_param = pivot_values if pivot_values != 'Nenhum' and pivot_values != 'Contagem de Registros' else None

                # Se 'Contagem de Registros' for selecionado como valor, use a função de agregação 'size'
                if pivot_values == 'Contagem de Registros':
                    pivot_table_df = pd.pivot_table(
                        filtered_df,
                        index=index_param,
                        columns=columns_param,
                        aggfunc='size' # size conta o número de linhas em cada grupo
                    )
                else:
                    pivot_table_df = pd.pivot_table(
                        filtered_df,
                        index=index_param,
                        columns=columns_param,
                        values=values_param,
                        aggfunc=agg_func
                    )
                st.dataframe(pivot_table_df)
            except Exception as e:
                st.warning(f"Não foi possível gerar a Tabela Dinâmica. Verifique suas seleções: {e}")
        else:
            st.info("Selecione pelo menos uma opção para Linhas, Colunas ou Valores para gerar a Tabela Dinâmica.")


    # --- Visualização de Dados (Gráfico) ---
    st.header("Visualização de Demandas")
    if not filtered_df.empty:
        plot_options = ["Nenhum", "Gráfico de Barras (Contagem Categórica)", "Histograma (Numérico)"]
        if len(filtered_df.select_dtypes(include=['number']).columns) >= 2:
            plot_options.append("Gráfico de Dispersão (Numérico)")
        
        plot_type = st.selectbox("Escolha o Tipo de Gráfico", plot_options)

        if plot_type == "Gráfico de Barras (Contagem Categórica)":
            categorical_cols_for_plot = filtered_df.select_dtypes(include=['object', 'category']).columns.tolist()
            if categorical_cols_for_plot:
                selected_col_bar = st.selectbox("Selecione a Coluna Categórica para o Gráfico de Barras", categorical_cols_for_plot, key='bar_plot_col')
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.countplot(y=selected_col_bar, data=filtered_df, order=filtered_df[selected_col_bar].value_counts().index, palette='viridis', ax=ax)
                ax.set_title(f"Contagem de Demandas por {selected_col_bar}", fontsize=16)
                ax.set_xlabel("Contagem", fontsize=12)
                ax.set_ylabel(selected_col_bar, fontsize=12)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Não há colunas categóricas para gerar um Gráfico de Barras.")

        elif plot_type == "Histograma (Numérico)":
            numerical_cols_for_plot = filtered_df.select_dtypes(include=['number']).columns.tolist()
            if numerical_cols_for_plot:
                selected_col_hist = st.selectbox("Selecione a Coluna Numérica para o Histograma", numerical_cols_for_plot, key='hist_plot_col')
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.histplot(filtered_df[selected_col_hist], kde=True, bins=20, palette='viridis', ax=ax)
                ax.set_title(f"Distribuição de {selected_col_hist}", fontsize=16)
                ax.set_xlabel(selected_col_hist, fontsize=12)
                ax.set_ylabel("Frequência", fontsize=12)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("Não há colunas numéricas para gerar um Histograma.")

        elif plot_type == "Gráfico de Dispersão (Numérico)":
            numerical_cols_for_plot = filtered_df.select_dtypes(include=['number']).columns.tolist()
            if len(numerical_cols_for_plot) >= 2:
                x_col_scatter = st.selectbox("Selecione a Coluna X", numerical_cols_for_plot, key='x_scatter_plot')
                y_col_scatter = st.selectbox("Selecione a Coluna Y", [col for col in numerical_cols_for_plot if col != x_col_scatter], key='y_scatter_plot')
                fig, ax = plt.subplots(figsize=(10, 6))
                sns.scatterplot(x=x_col_scatter, y=y_col_scatter, data=filtered_df, ax=ax)
                ax.set_title(f"Relação entre {x_col_scatter} e {y_col_scatter}", fontsize=16)
                ax.set_xlabel(x_col_scatter, fontsize=12)
                ax.set_ylabel(y_col_scatter, fontsize=12)
                plt.tight_layout()
                st.pyplot(fig)
            else:
                st.info("São necessárias pelo menos duas colunas numéricas para um Gráfico de Dispersão.")

    else:
        st.info("Nenhum dado para gerar visualizações. Carregue um arquivo e aplique os filtros.")

else:
    st.info("Por favor, carregue uma ou mais planilhas para começar a análise.")

st.sidebar.markdown("---")
st.sidebar.markdown("Desenvolvido com ❤️ por Gemini")
