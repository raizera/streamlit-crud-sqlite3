
import datetime

import streamlit as st

import controller.userController as usrc


def main():

    menu = ["Home", "Cadastrar", "Consultar", "Alterar", "Deletar"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("CRUD com Python + Streamlit")
        st.subheader("Navegue pelo menu lateral.")

    elif choice == "Cadastrar":
        st.subheader("Adicionar usuário")

        col1, col2 = st.columns(2)

        with col1:
            nome = st.text_input(label="NOME")
            sexo = st.selectbox(
                "SEXO", ['', 'Masculino', 'Feminino', 'Prefiro não responder'], format_func=lambda x: 'Selecione o sexo' if x == '' else x)
            profissao = st.text_input(label="PROFISSÃO")

        with col2:
            email = st.text_input(label="E-mail")
            idade = st.date_input(
                "DATA DE NASCIMENTO (AAAA/MM/DD)")
            estado = st.selectbox("ESTADO",
                                  ['', 'AC', 'AL', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                                   'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], format_func=lambda x: 'Selecionar estado' if x == '' else x)

        if st.button("cadastrar"):
            if nome == '':
                st.warning('Você esqueceu de preencher o nome.', icon="⚠️")
            elif sexo == '':
                st.warning('Você esqueceu de preencher o sexo.', icon="⚠️")
            elif profissao == '':
                st.warning(
                    'Você esqueceu de preencher a profissão.', icon="⚠️")
            elif email == '':
                st.warning('Você esqueceu de preencher o e-mail.', icon="⚠️")
            elif idade == 0:
                st.warning('Você esqueceu de preencher a idade.', icon="⚠️")
            elif estado == '':
                st.warning('Você esqueceu de preencher o estado.', icon="⚠️")
            else:
                usrc.create_table()
                usrc.add_data(
                    nome, email, profissao, sexo, idade, estado
                )  # essa ordem é importante estar correta
                st.success("cadastrado com sucesso!")

    elif choice == "Consultar":
        st.subheader("Consultar usuário")
        with st.expander("ver tabela de cadastrados"):
            tabela = usrc.read()
            st.dataframe(tabela)

        with st.expander("ver cadastrados (JSON)"):
            st.write(tabela)  # dados json

    elif choice == "Alterar":

        st.subheader("Atualizar usuário")

        nome = [i[0] for i in usrc.read()]
        alterar = st.selectbox("Nome", nome)
        resultado = usrc.get_task(alterar)
        st.write(resultado)

        if resultado:
            nome = resultado[0][0]
            email = resultado[0][1]
            profissao = resultado[0][2]
            sexo = resultado[0][3]
            idade = resultado[0][4]
            estado = resultado[0][5]

            # tabela = usrc.read()

            col1, col2 = st.columns(2)

            with col1:
                novo_nome = st.text_input('NOME', nome)
                nova_profissao = st.text_input('PROFISSÃO', profissao)
                novo_sexo = st.selectbox('SEXO', ['{}'.format(sexo), 'Masculino', 'Feminino', 'Prefiro não responder'],
                                         format_func=lambda x: 'Selecione o sexo' if x == '' else x)
            with col2:
                novo_email = st.text_input('E-mail', email)
                nova_idade = st.date_input(
                    label='IDADE')
                novo_estado = st.selectbox('ESTADO',
                                           ['{}'.format(estado), 'AC', 'AL', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                                            'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'], format_func=lambda x: 'Selecionar estado' if x == '' else x)

                # usrc.update(nome, email, profissao, sexo, idade, estado) #esta linha está gerando erro...

            if st.button("Alterar"):
                if novo_nome == '':
                    st.warning('Você esqueceu de preencher o nome.', icon="⚠️")
                elif novo_sexo == '':
                    st.warning('Você esqueceu de preencher o sexo.', icon="⚠️")
                elif nova_profissao == '':
                    st.warning(
                        'Você esqueceu de preencher a profissão.', icon="⚠️")
                elif novo_email == '':
                    st.warning(
                        'Você esqueceu de preencher o e-mail.', icon="⚠️")
                elif nova_idade == 0:
                    st.warning(
                        'Você esqueceu de preencher a idade.', icon="⚠️")
                elif novo_estado == '':
                    st.warning(
                        'Você esqueceu de preencher o estado.', icon="⚠️")
                else:
                    # essa ordem é importante estar correta
                    usrc.update(novo_nome, novo_email, nova_profissao,
                                novo_sexo, nova_idade, novo_estado, nome, email, profissao, sexo, idade, estado)
                    st.success("alterado com sucesso!")

        # usrc.List()

    elif choice == "Deletar":
        st.subheader("Deletar usuário")

        nome = [i[0] for i in usrc.read()]
        delete_nome = st.selectbox("Nome", nome)

        if st.button("Delete"):
            usrc.delete(delete_nome)
            st.warning("{} foi deleteado!".format(delete_nome))

    else:
        st.subheader("Home")


if __name__ == '__main__':
    main()
