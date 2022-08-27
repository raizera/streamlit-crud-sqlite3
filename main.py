import readline
import sqlite3

import pandas as pd
import streamlit as st

import models.cadastro as cadastro

conn = sqlite3.connect('data.db')
c = conn.cursor()

# CREATE TABLE


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS cadastro (nome TEXT, email TEXT, profissao TEXT, sexo TEXT, idade INTEGER, '
        'estado TEXT)')

#----------CREATE----------#


def create(nome, email, profissao, sexo, idade, estado):
    c.execute('INSERT INTO cadastro (nome, email, profissao, sexo, idade, estado) VALUES (?, ?, ?, ?, ? ,?)',
              (nome, email, profissao, sexo, idade, estado)
              )
    conn.commit()

#----------end CREATE----------#

#----------READ----------#


def read_():
    c.execute('SELECT * FROM cadastro')
    data = c.fetchall()
    return data


def read():
    c.execute('SELECT * FROM cadastro')
    read_list = []

    for row in c.fetchall():
        read_list.append(cadastro.Cadastro(
            row[0], row[1], row[2], row[3], row[4], row[5]))
    return read_list


read_list = []

for item in read():
    read_list.append([item.nome, item.email, item.profissao,
                     item.sexo, item.idade, item.estado])

# gerando a lista com pandas
df = pd.DataFrame(
    read_list,
    columns=['nome', 'email', 'profissao', 'sexo', 'idade', 'estado']
)

#----------end READ----------#


#----------UPDATE----------#

def update():
    c.execute('')

#----------end UPDATE----------#


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
            create_table()
            create(
                nome, email, profissao, sexo, idade, estado
            )  # essa ordem é importante estar correta
            st.success("cadastrado com sucesso!")

    elif choice == "Read":
        st.subheader("Consultar usuário")
        tabela_ = read_()
        st.table(df)
        # st.write(tabela_)

    elif choice == "Update":

        st.subheader("Atualizar usuário")

    elif choice == "Delete":
        st.subheader("Deletar usuário")

    else:
        st.subheader("Sobre")


if __name__ == '__main__':
    main()
