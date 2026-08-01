import streamlit as st

# 1. Configuração Inicial da Página (Foco em SEO básico e Design Minimalista)
st.set_page_config(
    page_title="Processamento de Dados e Automação | [Nome da Sua Empresa]",
    page_icon="📊",
    layout="centered", # 'centered' mantém o design minimalista e focado na leitura
    initial_sidebar_state="collapsed"
)

# Ocultar o menu padrão e o rodapé do Streamlit para dar aparência de site estático
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. Cabeçalho (Hero Section)
st.title("Otimize seu tempo com Automação e Processamento de Dados")
st.markdown("""
Ajudamos pequenas empresas a transformar dados desorganizados em informações valiosas. 
Foque no que realmente importa: **o crescimento do seu negócio**.
""")

st.divider() # Linha divisória sutil

# 3. Nossos Serviços (Com espaço para as 2 imagens)
st.header("Nossos Serviços")
st.markdown("Soluções sob medida para simplificar a sua rotina e aumentar a sua eficiência operional.")

# Utilizando colunas para alinhar lado a lado no desktop. 
# No mobile, o Streamlit automaticamente empilha as colunas (responsividade).
col1, col2 = st.columns(2)

with col1:
    # Substitua "caminho_imagem_1.jpg" pelo link ou arquivo da sua imagem
    # use_container_width=True garante que a imagem se ajuste perfeitamente ao tamanho da tela
    st.image("img.png", use_container_width=True)
    st.subheader("Processamento de Dados")
    st.write("Limpeza, organização e estruturação de bases de dados complexas para facilitar a sua tomada de decisão.")

with col2:
    # Substitua "caminho_imagem_2.jpg" pelo link ou arquivo da sua imagem
    st.image("img.png",use_container_width=True)
    st.subheader("Automação de Tarefas")
    st.write("Criação de rotinas automatizadas para eliminar trabalhos manuais e repetitivos, economizando horas da sua equipe.")

st.divider()

# 4. Seção de Contato
st.header("Fale Conosco")
st.markdown("Pronto para dar o próximo passo? Entre em contato e solicite um orçamento sem compromisso.")

# Exibição das informações de contato de forma limpa
st.markdown("""
* **Email:** contato@suaempresa.com.br
* **WhatsApp:** (11) 99999-9999
* **Endereço:** Rua Exemplo, 123 - Centro (Atendimento Online para todo o Brasil)
""")

# Botão para redirecionar para o WhatsApp (Exemplo prático de CTA)
whatsapp_link = "https://wa.me/5511999999999?text=Olá,%20gostaria%20de%20saber%20mais%20sobre%20os%20serviços%20de%20dados."
st.link_button("Falar com um Consultor no WhatsApp", whatsapp_link)