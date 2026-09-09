import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Calculadora 3D Pro", page_icon="🖨️", layout="centered")

st.title("🖨️ Calculadora de Custos - Impressão 3D")
st.write("Calcule o preço ideal das suas peças de forma rápida e automatizada.")

# --- BARRA LATERAL: CONFIGURAÇÕES GERAIS ---
st.sidebar.header("⚙️ Configurações da Máquina")
preco_rolo = st.sidebar.number_input("Preço do Rolo (R$)", value=70.00, step=1.00)
peso_rolo = st.sidebar.number_input("Peso do Rolo (g)", value=1000, step=100)
potencia = st.sidebar.number_input("Potência da Impressora (Watts)", value=300, step=10)
preco_kwh = st.sidebar.number_input("Preço do kWh (R$)", value=0.80, step=0.05)
valor_maquina = st.sidebar.number_input("Valor da Impressora (R$)", value=2000.00, step=100.00)
vida_util = st.sidebar.number_input("Vida Útil Estimada (Horas)", value=5000, step=500)

# --- CORPO PRINCIPAL: DADOS DA PEÇA ---
st.header("📦 Dados da Peça Atual")
col1, col2 = st.columns(2)

with col1:
    peso_peca = st.number_input("Peso da Peça (g)", value=20.0, step=1.0)
    tempo_peca = st.number_input("Tempo de Impressão (Horas)", value=0.6, step=0.1)

with col2:
    margem_lucro = st.number_input("Margem de Lucro Desejada (%)", value=925.0, step=10.0)

# --- CÁLCULOS AUTOMÁTICOS ---
custo_filamento = (peso_peca / peso_rolo) * preco_rolo
custo_energia = (potencia / 1000) * tempo_peca * preco_kwh
custo_depreciacao = (valor_maquina / vida_util) * tempo_peca
custo_total = custo_filamento + custo_energia + custo_depreciacao
preco_venda = custo_total * (1 + (margem_lucro / 100))
lucro_liquido = preco_venda - custo_total

# --- EXIBIÇÃO DOS RESULTADOS ---
st.divider()
st.header("📊 Detalhamento de Custos e Resultados")

m1, m2, m3 = st.columns(3)
m1.metric("Custo do Filamento", f"R$ {custo_filamento:.2f}")
m2.metric("Custo de Energia", f"R$ {custo_energia:.2f}")
m3.metric("Custo de Depreciação", f"R$ {custo_depreciacao:.2f}")

st.divider()

r1, r2, r3 = st.columns(3)
r1.metric("Custo Total", f"R$ {custo_total:.2f}")
r2.metric("Preço de Venda Sugerido", f"R$ {preco_venda:.2f}", delta=f"{margem_lucro}% Lucro")
r3.metric("Lucro Líquido", f"R$ {lucro_liquido:.2f}")