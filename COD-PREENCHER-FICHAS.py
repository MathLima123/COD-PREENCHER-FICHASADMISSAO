import fitz
import os
import glob

# =====================================================
# CRIA PASTA SAIDA
# =====================================================

os.makedirs("saida", exist_ok=True)

# =====================================================
# FUNÇÃO ESCREVER
# =====================================================

def escrever(doc, pagina, x, y, texto, tamanho=9):

    if texto is None:
        return

    texto = str(texto).strip()

    if texto == "":
        return

    page = doc[pagina]

    page.insert_text(

        (x, y),

        texto,

        fontsize=tamanho,

        fontname="helv",

        color=(0, 0, 0)

    )

# =====================================================
# FUNÇÃO MARCAR X
# =====================================================

def marcar_x(doc, pagina, x, y):

    page = doc[pagina]

    page.insert_text(

        (x, y),

        "X",

        fontsize=12,

        fontname="helv",

        color=(0, 0, 0)

    )

# =====================================================
# PROCURA TODOS TXT
# =====================================================

arquivos_txt = glob.glob("*.txt")

if len(arquivos_txt) == 0:

    print("")
    print("===================================")
    print("NENHUM ARQUIVO TXT ENCONTRADO")
    print("===================================")
    print("")

    exit()

# =====================================================
# PROCESSA TODOS OS TXT
# =====================================================

for arquivo_txt in arquivos_txt:

    print("")
    print("===================================")
    print(f"PROCESSANDO: {arquivo_txt}")
    print("===================================")

    # =====================================================
    # LÊ DADOS
    # =====================================================

    dados = {}

    with open(arquivo_txt, "r", encoding="utf-8") as arquivo:

        for linha in arquivo:

            linha = linha.strip()

            if linha == "":
                continue

            if "=" in linha:

                chave, valor = linha.split("=", 1)

                dados[chave.strip().lower()] = valor.strip()

    # =====================================================
    # CARGO
    # =====================================================

    cargo = dados.get("cargo", "").lower()

    pdf_entrada = ""

    # =====================================================
    # SERVENTE LIMPEZA
    # =====================================================

    if cargo == "servente de limpeza 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO SERVENTE LIMP 40H.pdf"

    elif cargo == "servente de limpeza 20h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO SERVENTE LIMP 20H.pdf"

    # =====================================================
    # MERENDEIRA
    # =====================================================

    elif cargo == "merendeira 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO MERENDEIRA 40H.pdf"

    elif cargo == "merendeira 20h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO MERENDEIRA 20H.pdf"

    # =====================================================
    # APOIO ESCOLAR
    # =====================================================

    elif cargo == "apoio escolar 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO APOIO 40H.pdf"

    elif cargo == "apoio escolar 20h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO APOIO 20H.pdf"

    # =====================================================
    # ASSISTENTE ADM
    # =====================================================

    elif cargo == "assistente administrativo 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO ASSISTENTE ADM 40H.pdf"

    elif cargo == "assistente administrativo 20h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO ASSISTENTE ADM 20H.pdf"

    # =====================================================
    # COPEIRO
    # =====================================================

    elif cargo == "copeiro(a) 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO COPEIRO (A) 40H.pdf"

    # =====================================================
    # ENCARREGADO
    # =====================================================

    elif cargo == "encarregado(a) 40h":

        pdf_entrada = "FICHAS/FICHA DE ADMISSÃO ENCARREGADO 40H.pdf"

    # =====================================================
    # ERRO
    # =====================================================

    else:

        print("")
        print("===================================")
        print(f"CARGO NÃO ENCONTRADO NO ARQUIVO: {arquivo_txt}")
        print("===================================")
        print("")

        continue

    # =====================================================
    # VERIFICA PDF
    # =====================================================

    if not os.path.exists(pdf_entrada):

        print("")
        print("===================================")
        print(f"PDF NÃO ENCONTRADO:")
        print(pdf_entrada)
        print("===================================")
        print("")

        continue

    # =====================================================
    # ABRE PDF
    # =====================================================

    doc = fitz.open(pdf_entrada)

    # =====================================================
    # VARIAVEIS
    # =====================================================

    dependentes = dados.get("dependentes_menores", "").lower()

    seguro = dados.get("seguro_desemprego", "").lower()

    vale = dados.get("vale_transporte", "").lower()

    operacao = dados.get("operacao", "").lower()

    # =====================================================
    # COORDENADAS PERSONALIZADAS PAGINA 4
    # =====================================================

    X_NOME_P4 = 320
    Y_NOME_P4 = 130

    X_CPF_P4 = 355
    Y_CPF_P4 = 147

    X_LOCAL_P4 = 590
    Y_LOCAL_P4 = 147

    # =====================================================
    # PAGINA 1
    # =====================================================

    escrever(doc, 0, 60, 80, dados.get("nome"))

    escrever(doc, 0, 480, 80, dados.get("data_nascimento"))

    escrever(doc, 0, 177, 105, dados.get("telefone_celular"))

    escrever(doc, 0, 50, 150, dados.get("cpf"))

    escrever(doc, 0, 240, 150, dados.get("rg"))

    escrever(doc, 0, 435, 150, dados.get("pis"))

    escrever(doc, 0, 270, 175, dados.get("estado_civil"))

    escrever(doc, 0, 60, 200, dados.get("email"))

    escrever(doc, 0, 400, 200, dados.get("escolaridade"))

    escrever(doc, 0, 80, 220, dados.get("naturalidade"))

    escrever(doc, 0, 260, 220, dados.get("cor_raca"))

    escrever(doc, 0, 44, 255, dados.get("banco"))

    escrever(doc, 0, 285, 255, dados.get("agencia"))

    escrever(doc, 0, 450, 255, dados.get("conta"))

    # =====================================================
    # MARCACOES PAGINA 1
    # =====================================================

    if seguro == "sim":

        marcar_x(doc, 0, 485, 175)

    else:

        marcar_x(doc, 0, 509, 175)

    if dependentes == "sim":

        marcar_x(doc, 0, 454, 218)

    else:

        marcar_x(doc, 0, 475, 218)

    if vale == "sim":

        marcar_x(doc, 0, 93, 298)

    else:

        marcar_x(doc, 0, 93, 318)

    if operacao == "corrente":

        marcar_x(doc, 0, 115, 279)

    elif operacao == "poupança":

        marcar_x(doc, 0, 243, 279)

    # =====================================================
    # PAGINA 2
    # =====================================================

    escrever(doc, 1, 180, 205, dados.get("nome"))

    escrever(doc, 1, 80, 247, dados.get("endereco"))

    escrever(doc, 1, 160, 290, dados.get("nome_proprietario"))

    escrever(doc, 1, 120, 330, "PROPRIETÁRIA DO IMÓVEL")

    # =====================================================
    # PAGINA 3
    # =====================================================

    escrever(doc, 2, 145, 145, dados.get("nome"))

    escrever(doc, 2, 145, 163, dados.get("cpf"))

    escrever(doc, 2, 145, 197, dados.get("data_admissao"))

    escrever(doc, 2, 145, 215, dados.get("local_trabalho"))

    # =====================================================
    # SERVENTE LIMPEZA
    # =====================================================

    if cargo in [

        "servente de limpeza 40h",
        "servente de limpeza 20h"

    ]:

        escrever(doc, 2, 450, 490, dados.get("bata"))

        escrever(doc, 2, 450, 510, dados.get("sapato"))

        escrever(doc, 2, 450, 530, dados.get("luva_azul"))

        escrever(doc, 2, 450, 550, dados.get("luva_amarela"))

        escrever(doc, 2, 450, 570, dados.get("mascara"))

    # =====================================================
    # APOIO ESCOLAR
    # =====================================================

    elif cargo in [

        "apoio escolar 20h",
        "apoio escolar 40h"

    ]:

        escrever(doc, 2, 450, 490, dados.get("jaleco"))

        escrever(doc, 2, 450, 510, dados.get("mascara"))

        escrever(doc, 2, 450, 530, dados.get("camiseta"))

    # =====================================================
    # ASSISTENTE ADM
    # =====================================================

    elif cargo in [

        "assistente administrativo 20h",
        "assistente administrativo 40h"

    ]:

        escrever(doc, 2, 450, 490, dados.get("jaleco"))

        escrever(doc, 2, 450, 510, dados.get("mascara"))

        escrever(doc, 2, 450, 530, dados.get("camiseta"))

    # =====================================================
    # COPEIRO
    # =====================================================

    elif cargo == "copeiro(a) 40h":

        escrever(doc, 2, 450, 490, dados.get("camiseta"))

        escrever(doc, 2, 450, 510, dados.get("calca"))

        escrever(doc, 2, 450, 530, dados.get("bata"))

        escrever(doc, 2, 450, 550, dados.get("sapato"))

        escrever(doc, 2, 450, 570, dados.get("rede_cabelo"))

    # =====================================================
    # ENCARREGADO
    # =====================================================

    elif cargo == "encarregado(a) 40h":

        escrever(doc, 2, 450, 490, dados.get("camiseta_dry"))

        escrever(doc, 2, 450, 510, dados.get("camiseta_social"))

        escrever(doc, 2, 450, 530, dados.get("mascara"))

        escrever(doc, 2, 450, 550, dados.get("sapato"))

    # =====================================================
    # MERENDEIRA
    # =====================================================

    elif cargo in [

        "merendeira 20h",
        "merendeira 40h"

    ]:

        escrever(doc, 2, 450, 490, dados.get("camiseta"))

        escrever(doc, 2, 450, 510, dados.get("calca"))

        escrever(doc, 2, 450, 530, dados.get("avental"))

        escrever(doc, 2, 450, 550, dados.get("spup"))

        escrever(doc, 2, 450, 570, dados.get("mascara"))

        escrever(doc, 2, 450, 595, dados.get("touca"))

    # =====================================================
    # PAGINA 4
    # =====================================================

    if cargo in [

        "encarregado(a) 40h",
        "apoio escolar 20h",
        "apoio escolar 40h",
        "assistente administrativo 20h",
        "assistente administrativo 40h"
        "merendeira 20h",
        "merendeira 40h"

    ]:

        escrever(doc, 3, X_NOME_P4, Y_NOME_P4, dados.get("nome"))

        escrever(doc, 3, X_CPF_P4, Y_CPF_P4, dados.get("cpf"))

        escrever(doc, 3, X_LOCAL_P4, Y_LOCAL_P4, dados.get("local_trabalho"))

    else:

        escrever(doc, 3, 320, 118, dados.get("nome"))

        escrever(doc, 3, 355, 134, dados.get("cpf"))

        escrever(doc, 3, 590, 134, dados.get("local_trabalho"))

    # =====================================================
    # PAGINA 6
    # =====================================================

    escrever(doc, 5, 154, 144, dados.get("nome"))

    escrever(doc, 5, 154, 163, dados.get("cpf"))

    escrever(doc, 5, 154, 200, dados.get("data_admissao"))

    escrever(doc, 5, 154, 217, dados.get("local_trabalho"))

    # =====================================================
    # PAGINA 8
    # =====================================================

    escrever(doc, 7, 50, 116, dados.get("nome"))

    escrever(doc, 7, 50, 144, dados.get("data_admissao"))

    escrever(doc, 7, 230, 144, dados.get("cpf"))

    escrever(doc, 7, 400, 144, dados.get("local_trabalho"))

    escrever(doc, 7, 50, 171, dados.get("endereco"))

    escrever(doc, 7, 50, 197, dados.get("cep"))

    escrever(doc, 7, 160, 197, dados.get("bairro"))

    escrever(doc, 7, 280, 197, dados.get("municipio"))

    escrever(doc, 7, 400, 197, dados.get("uf"))

    if vale == "sim":

        marcar_x(doc, 7, 50, 246)

        escrever(doc, 7, 81, 457, dados.get("linha_ida"))

        escrever(doc, 7, 477, 457, dados.get("tarifa_ida"))

        escrever(doc, 7, 81, 472, dados.get("linha2_ida"))

        escrever(doc, 7, 477, 472, dados.get("tarifa2_ida"))

        escrever(doc, 7, 81, 528, dados.get("linha_volta"))

        escrever(doc, 7, 477, 528, dados.get("tarifa_volta"))

        escrever(doc, 7, 81, 542, dados.get("linha2_volta"))

        escrever(doc, 7, 477, 542, dados.get("tarifa2_volta"))

    else:

        marcar_x(doc, 7, 50, 258)

    # =====================================================
    # PAGINA 9
    # =====================================================

    escrever(doc, 8, 70, 390, dados.get("nome"))

    # =====================================================
    # PAGINA 10
    # =====================================================

    escrever(doc, 9, 120, 130, dados.get("nome"))

    escrever(doc, 9, 180, 156, dados.get("cpf"))

    if dependentes == "sim":

        escrever(doc, 9, 105, 270, dados.get("dependente1"))

        escrever(doc, 9, 105, 318, dados.get("dependente2"))

        escrever(doc, 9, 105, 360, dados.get("dependente3"))

        escrever(doc, 9, 105, 410, dados.get("dependente4"))

        escrever(doc, 9, 105, 453, dados.get("dependente5"))

    # =====================================================
    # SALVA PDF
    # =====================================================

    nome_pdf = dados.get("nome", "SEM_NOME").upper()

    saida = f"saida/{nome_pdf} - FICHA DE ADMISSÃO.pdf"

    doc.save(saida)

    doc.close()

    # =====================================================
    # FINAL
    # =====================================================

    print("")
    print("===================================")
    print("FICHA PREENCHIDA COM SUCESSO")
    print("===================================")
    print(saida)
    print("===================================")

print("")
print("===================================")
print("TODOS OS ARQUIVOS FINALIZADOS")
print("===================================")
