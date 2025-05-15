# ========================
# 📦 IMPORTS
# ========================
import streamlit as st
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import pandas as pd
import plotly.express as px

# ========================
# 🗄️ CONFIGURAÇÃO DO BANCO
# ========================
engine = create_engine("sqlite:///gastos.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# ========================
# 📊 MODELO DA TABELA
# ========================
class Gasto(Base):
    __tablename__ = "gastos"
    id = Column(Integer, primary_key=True)
    pessoa = Column(String)
    descricao = Column(String)
    classificacao = Column(String)
    valor = Column(Float)
    data_compra = Column(DateTime, default=datetime.now)

Base.metadata.create_all(engine)

# ========================
# 🧾 CADASTRO DE GASTO
# ========================
def cadastrar_gasto():
    with st.form("form_gasto"):
        pessoa = st.text_input("Quem gastou?")
        descricao = st.text_input("O que comprou?")
        classificacao = st.selectbox("Classificação", ["Alimentação", "Transporte", "Lazer", "Outros"])
        valor = st.number_input("Valor (R$)", min_value=0.0, step=0.01)
        data_compra = st.date_input("Data da compra", value=datetime.today())
        enviado = st.form_submit_button("Salvar gasto")
        if enviado:
            novo = Gasto(pessoa=pessoa, descricao=descricao, classificacao=classificacao,
                         valor=valor, data_compra=datetime.combine(data_compra, datetime.min.time()))
            session.add(novo)
            session.commit()
            st.success("✅ Gasto registrado com sucesso!")

# ========================
# 🔍 VISUALIZAÇÃO E FILTROS
# ========================
def visualizar_gastos():
    st.subheader("🔎 Ver e filtrar gastos")
    todos = session.query(Gasto).all()
    df = pd.DataFrame([{
        "Pessoa": g.pessoa,
        "Descrição": g.descricao,
        "Classificação": g.classificacao,
        "Valor (R$)": g.valor,
        "Data": g.data_compra.date()
    } for g in todos])

    # Filtros
    pessoa_filtro = st.selectbox("Filtrar por pessoa", ["Todos"] + sorted(df["Pessoa"].unique()))
    classe_filtro = st.selectbox("Filtrar por classificação", ["Todos"] + sorted(df["Classificação"].unique()))
    data_ini = st.date_input("De:", value=datetime.today().replace(day=1))
    data_fim = st.date_input("Até:", value=datetime.today())

    if pessoa_filtro != "Todos":
        df = df[df["Pessoa"] == pessoa_filtro]
    if classe_filtro != "Todos":
        df = df[df["Classificação"] == classe_filtro]

    df = df[(df["Data"] >= data_ini) & (df["Data"] <= data_fim)]

    # Total
    total = df["Valor (R$)"].sum()
    st.metric("💰 Total filtrado", f"R$ {total:,.2f}")

    # Tabela
    st.dataframe(df)

    # Gráficos
    if not df.empty:
        fig_pizza = px.pie(df, names="Classificação", values="Valor (R$)", title="Gastos por classificação")
        fig_bar = px.bar(df, x="Pessoa", y="Valor (R$)", color="Classificação", title="Gastos por pessoa")
        st.plotly_chart(fig_pizza)
        st.plotly_chart(fig_bar)
    else:
        st.info("Nenhum gasto encontrado nesse filtro.")

# ========================
# ▶️ APP STREAMLIT
# ========================
st.title("📘 Registro de Gastos de Casa")

menu = st.sidebar.radio("Navegação", ["Cadastrar Gasto", "Visualizar Gastos"])
if menu == "Cadastrar Gasto":
    cadastrar_gasto()
else:
    visualizar_gastos()
# ========================