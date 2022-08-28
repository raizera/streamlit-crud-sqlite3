import sqlite3

import models.cadastro as cadastro
import pandas as pd

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


#----------end READ----------#


#----------UPDATE----------#

def update():
    c.execute('')

#----------end UPDATE----------#
