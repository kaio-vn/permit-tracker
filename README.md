# 🏗️ Permit Tracker

Sistema de linha de comando (CLI) para gerenciar permits de construção, desenvolvido em Python com MySQL.


## 📋 Sobre o projeto

Este projeto simula o fluxo real de acompanhamento de permits de construção nos EUA, incluindo cadastro, atualização de status, atribuição de número oficial do permit, e cancelamento (soft delete).


## 🤖 Metodologia de desenvolvimento

Saber usar IA como ferramenta de engenharia é, hoje, uma competência técnica requisitada pelo mercado de trabalho. Este projeto foi construído com apoio de inteligência artificial (Claude, da Anthropic, e ChatGPT, da OpenAI), aplicada da mesma forma que profissionais de desenvolvimento já utilizam no mercado: para acelerar implementação e aprofundar entendimento técnico, nunca para substituí-lo.

A abordagem foi hands-on: em vez de estudar sintaxe e conceitos isolados sem aplicação prática, aprendi Python e SQL construindo um sistema real, modelado a partir da minha experiência prévia na área de permits de construção nos EUA (Flórida). A cada etapa, a IA propunha implementações e explicava o porquê de cada decisão técnica. Eu avaliava se a sugestão fazia sentido para o contexto de negócio real que conheço (sem expor aqui detalhes confidenciais do trabalho), testava, entendia o funcionamento e só então seguia adiante, nunca copiei sem compreender.

Existe uma crítica legítima a esse método: aprender sob demanda pode deixar lacunas na fundação teórica, comparado a estudar cada tópico exaustivamente antes de aplicá-lo. Por isso, complementei o processo consultando documentação oficial das tecnologias envolvidas sempre que a IA introduzia um conceito novo,garantindo que o entendimento não ficasse raso. O resultado é uma prática de estudo que simula um ambiente real de produção: aprender o que resolve o problema à frente, e aprofundar esse conhecimento durante a própria construção.

O histórico de commits deste repositório é a prova disso — cada etapa documenta uma decisão técnica discutida, testada e ajustada, não um projeto entregue pronto sem participação real de quem o construiu.


## 🛠️ Tecnologias

- Python 3
- MySQL 8
- Bibliotecas: `mysql-connector-python`, `python-dotenv`

## ✅ Funcionalidades

- Cadastrar novo permit (endereço, parcel ID, tipo)
- Visualizar todos os permits cadastrados
- Atualizar permit (permit number, aprovação, data de expiração, notas do inspetor)
- Cancelar permit (soft delete — o registro nunca é apagado, apenas marcado como `cancelled`)

## 🚀 Como rodar o projeto

1. Clone o repositório:

git clone https://github.com/kaio-vn/permit-tracker.git
cd permit-tracker


2. Crie e ative um ambiente virtual:

python -m venv venv
.\venv\Scripts\Activate


3. Instale as dependências:

pip install -r requirements.txt


4. Crie um arquivo `.env` na raiz do projeto com suas credenciais do MySQL:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=permit_tracker


5. Execute o `schema.sql` no MySQL Workbench (ou via terminal) para criar o banco e a tabela.

6. Rode o programa:

python main.py

## 🧠 Decisões técnicas

- **`permit_number` é opcional no cadastro**: no fluxo real de trabalho, o número oficial do permit só é atribuído após aplicação no condado, não no momento do cadastro inicial. Por isso a coluna aceita `NULL` e é preenchida depois via atualização.
- **Soft delete em vez de exclusão real**: permits nunca são apagados do banco, uma vez que podemos necessitar no futuro. Cancelamentos mudam o `status` para `'cancelled'`, preservando histórico completo — reflete como esse tipo de dado é tratado na prática.
- **Uso de parâmetros (`%s`) em todas as queries**: previne SQL Injection, nunca concatenando valores diretamente nas strings SQL.
- **Validação de status antes de atualizações**: um permit cancelado não pode ser atualizado novamente, evitando inconsistência nos dados.

## 🗄️ Estrutura do banco

Ver `schema.sql` para o histórico completo de criação e alterações da tabela `permits`.