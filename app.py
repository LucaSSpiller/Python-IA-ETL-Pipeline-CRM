import streamlit as st
from datetime import datetime, time
import contrato

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow")
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da Venda", datetime.now())
    hora = st.time_input("Horário da Venda", value=time(9,0))
    valor = st.number_input("Valor da Venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de Produtos Vendidos", min_value=1, step=1)
    produto = st.selectbox("Produto", ["ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama 3.0"])

    if st.button("Salvar"):

        data_hora = datetime.combine(data, hora)
        st.write("**Dados da Venda:**")
        st.write(f"Email do Vendedor: {email}")
        st.write(f"Data e Hora da Compra: {data_hora}")
        st.write(f"Valor da Venda: R$ {valor:.2f}")
        st.write(f"Quantidade de Produtos: {quantidade}")
        st.write(f"Produto: {produto}")

if __name__ == "__main__":
    main()