import sqlite3

import streamlit as st

import models.cadastro as cadastro

conn = sqlite3.connect('data.db', check_same_thread=False)
c = conn.cursor()


# CREATE TABLE


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS cadastro(nome VARCHAR(20) NOT NULL, email VARCHAR(15) NOT NULL, profissao VARCHAR(15) NOT NULL, sexo CHAR(21) NOT NULL, idade INTEGER NOT NULL, estado CHAR(2) NOT NULL)')

# ----------CREATE----------#


def add_data(nome, email, profissao, sexo, idade, estado):
    c.execute('INSERT INTO cadastro (nome, email, profissao, sexo, idade, estado) VALUES (?, ?, ?, ?, ?, ?)',
              (nome, email, profissao, sexo, idade, estado))
    conn.commit()
# ----------end CREATE----------#

# -------------READ-------------#


def read():
    c.execute('SELECT * FROM cadastro')
    data = c.fetchall()
    return data
# ----------end READ----------#


# -----------UPDATE-----------#

def update(novo_nome, novo_email, nova_profissao, novo_sexo, nova_idade, novo_estado, nome, email, profissao, sexo, idade, estado):
    c.execute(
        "UPDATE cadastro SET nome=?, email=?, profissao=?, sexo=?, idade=?, estado=? WHERE nome=? and email=? and profissao=? and sexo=? and idade=? and estado=?", (novo_nome, novo_email, nova_profissao, novo_sexo, nova_idade, novo_estado, nome, email, profissao, sexo, idade, estado))
    conn.commit()
    data = c.fetchall()
    return data


# ---------end UPDATE---------#

# ---------DELETE---------#


def delete(nome):
    c.execute('DELETE FROM cadastro WHERE nome = "{}"'.format(nome))
    conn.commit()

    # ---------end DELETE---------#


def get_task(nome):
    c.execute('SELECT * FROM cadastro WHERE nome = "{}"'.format(nome))
    data = c.fetchall()
    return data


def selecionarTodos():
    c.execute("SELECT * FROM cadastro")
    costumerList = []

    for row in c.fetchall():
        costumerList.append(cadastro.Cadastro(
            row[0], row[1], row[2], row[3], row[4], row[5]))
    return costumerList


def List():
    colms = st.columns((1, 1, 1, 1, 1, 1, 1))
    campos = ['nome', 'email', 'profissão',
              'sexo', 'idade', 'estado', 'ação']

    for col, campo in zip(colms, campos):
        col.write(campo)

    for item in selecionarTodos():
        col1, col2, col3, col4, col5, col6, col7 = st.columns(
            (1, 1, 1, 1, 1, 1, 1))

        col1.write(item.nome)
        col2.write(item.email)
        col3.write(item.profissao)
        col4.write(item.sexo)
        col5.write(item.idade)
        col6.write(item.estado)

        button_space = col7.empty()

        on_click = button_space.button(
            'alterar', 'btnAlterar' + str(item.nome))

        if on_click:
            st.write("botao pressionado")
