import pandas as pd
import streamlit as st

import controller.userController as usrc


def main():
    st.title("CRUD with Streamlit")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Adicionar usuário")

        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input(label="nome")
            sexo = st.selectbox(
                "sexo", ['Masculino', 'Feminino', 'Prefiro não responder'])
            profissao = st.text_input(label="profissão")

        with col2:
            email = st.text_input(label="e-mail")
            idade = st.number_input("idade", format="%d", step=1)
            estado = st.selectbox("estado",
                                  ['AC', 'AL', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                                   'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'])

        if st.button("cadastrar"):
            usrc.create_table()
            usrc.create(
                nome, email, profissao, sexo, idade, estado
            )  # essa ordem é importante estar correta
            st.success("cadastrado com sucesso!")

    elif choice == "Read":
        st.subheader("Consultar usuário")
        tabela_ = usrc.read_()
        st.table(df)
        # st.write(tabela_)

    elif choice == "Update":

        st.subheader("Atualizar usuário")

    elif choice == "Delete":
        st.subheader("Deletar usuário")

    else:
        st.subheader("Sobre")


# gerando a lista com pandas
read_list = []

for item in usrc.read():
    read_list.append([item.nome, item.email, item.profissao,
                     item.sexo, item.idade, item.estado])

df = pd.DataFrame(
    read_list,
    columns=['nome', 'email', 'profissao', 'sexo', 'idade', 'estado']
)

if __name__ == '__main__':
    main()
