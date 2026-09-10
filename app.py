import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Calculadora 3D Pro", page_icon="🖨️", layout="centered")

st.title("🖨️ Calculadora de Custos - Impressão 3D")
st.write("Calcule o preço ideal das suas peças e lotes de forma rápida e automatizada.")

# --- BARRA LATERAL: CONFIGURAÇÕES GERAIS ---
st.sidebar.header("⚙️ Configurações da Máquina")
preco_rolo = st.sidebar.number_input("Preço do Rolo (R$)", value=70.00, step=1.00)
peso_rolo = st.sidebar.number_input("Peso do Rolo (g)", value=1000, step=100)
potencia = st.sidebar.number_input("Potência da Impressora (Watts)", value=300, step=10)
preco_kwh = st.sidebar.number_input("Preço do kWh (R$)", value=0.80, step=0.05)
valor_maquina = st.sidebar.number_input("Valor da Impressora (R$)", value=2000.00, step=100.00)
vida_util = st.sidebar.number_input("Vida Útil Estimada (Horas)", value=5000, step=500)

# --- CORPO PRINCIPAL: DADOS DA PEÇA ---
st.header("📦 Dados da Peça e Lote")
col1, col2 = st.columns(2)

with col1:
    peso_peca = st.number_input("Peso de 1 Peça (g)", value=20.0, step=1.0)
    tempo_peca = st.number_input("Tempo de Impressão de 1 Peça (Horas)", value=0.6, step=0.1)

with col2:
    quantidade_itens = st.number_input("Quantidade de Itens (Lote)", value=1, step=1, min_value=1)
    margem_lucro = st.number_input("Margem de Lucro Desejada (%)", value=925.0, step=10.0)

# --- CÁLCULOS AUTOMÁTICOS POR UNIDADE ---
custo_filamento_unit = (peso_peca / peso_rolo) * preco_rolo
custo_energia_unit = (potencia / 1000) * tempo_peca * preco_kwh
custo_depreciacao_unit = (valor_maquina / vida_util) * tempo_peca
custo_total_unit = custo_filamento_unit + custo_energia_unit + custo_depreciacao_unit
preco_venda_unit = custo_total_unit * (1 + (margem_lucro / 100))
lucro_liquido_unit = preco_venda_unit - custo_total_unit

# --- CÁLCULOS TOTAIS DO LOTE ---
custo_total_lote = custo_total_unit * quantidade_itens
preco_venda_lote = preco_venda_unit * quantidade_itens
lucro_liquido_lote = lucro_liquido_unit * quantidade_itens

# --- EXIBIÇÃO DOS RESULTADOS POR UNIDADE ---
st.divider()
st.header("📊 Custos por Unidade")

m1, m2, m3 = st.columns(3)
m1.metric("Filamento / Unidade", f"R$ {custo_filamento_unit:.2f}")
m2.metric("Energia / Unidade", f"R$ {custo_energia_unit:.2f}")
m3.metric("Depreciação / Unidade", f"R$ {custo_depreciacao_unit:.2f}")

u1, u2 = st.columns(2)
u1.metric("Custo Total por Unidade", f"R$ {custo_total_unit:.2f}")
u2.metric("Preço de Venda Unitário", f"R$ {preco_venda_unit:.2f}", delta=f"{margem_lucro}% Lucro")

# --- EXIBIÇÃO DOS RESULTADOS TOTAIS DO LOTE ---
st.divider()
st.header(f"📦 Resultados Totais para o Lote ({quantidade_itens} itens)")

l1, l2, l3 = st.columns(3)
l1.metric("Custo Total do Lote", f"R$ {custo_total_lote:.2f}")
l2.metric("Preço de Venda Total", f"R$ {preco_venda_lote:.2f}")
l3.metric("Lucro Líquido Total", f"R$ {lucro_liquido_lote:.2f}")