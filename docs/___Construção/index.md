# Construção

> Objetivo: Construir o sistema com base na arquitetura definida.

## Visão Geral do Processo de Construção

<p align="justify">
A fase de construção consistiu no desenvolvimento prático do sistema, transformando os modelos e planejamentos definidos na fase de elaboração em código funcional. As atividades foram realizadas de forma colaborativa pela equipe, priorizando a entrega incremental de funcionalidades, com testes constantes e validações junto aos membros da Associação de Moradores da Ilha Primeira.
</p>

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework Backend:** Django
- **Banco de Dados:** SQLite (para desenvolvimento) — possibilidade de migração para PostgreSQL em produção
- **Interface de Administração:** Django Admin
- **Documentação:** MkDocs
- **Controle de Versão:** Git e GitHub

## Principais Atividades

- Implementação dos modelos de dados (Django Models) representando os moradores, domicílios e informações demográficas.
- Desenvolvimento das interfaces de administração e gerenciamento de dados.
- Criação de funcionalidades para cadastro, atualização, consulta e exclusão de registros.
- Testes de funcionalidade e testes manuais para validação dos fluxos principais.
- Ajustes de interface e experiência do usuário na administração do sistema.
- Desenvolvimento da documentação técnica utilizando MkDocs.

## Funcionalidades Desenvolvidas

- **Cadastro de Moradores:**
  Permite adicionar informações pessoais e demográficas dos moradores, como nome, CPF, idade, gênero, endereço e outros dados.

- **Cadastro de Domicílios:**
  Cadastro de características dos domicílios, como tipo, quantidade de cômodos, acesso a serviços básicos (água, energia, esgoto, internet, lixo, etc.).

- **Cadastro de Indicadores:**
  Cadastro de informações relevantes sobre a Ilha, mas que não se encaixam como Morador ou Domicílio, geralmente perguntas de resposta única sobre a comunidade.

- **Gerenciamento de Dados:**
  Interface que possibilita visualizar, editar e excluir dados de forma simples e rápida é o Django Admin.

- **Relacionamento Morador-Domicílio:**
  Cada domicílio possui um proprietário (morador), e é possível visualizar quem está vinculado a qual domicílio.

- **Filtros e Pesquisas:**
  Ferramentas dentro da interface administrativa que permitem buscas rápidas por CPF, nome, endereço e outros critérios.


## Testes Realizados

- **Testes de funcionalidade:**
  Cada funcionalidade foi testada manualmente no ambiente de desenvolvimento, validando os fluxos de cadastro, atualização, consulta e exclusão.

- **Testes de integração:**
  Verificação dos relacionamentos entre os modelos, como a correta associação entre moradores e domicílios.

- **Testes de usabilidade:**
  Testes realizados com os membros da própria equipe e feedbacks do professor responsável pela disciplina para garantir que o sistema seja simples e fácil de usar.

- **Validações específicas:**
  - Validação de CPF com exatamente 11 dígitos.
  - Restrições em campos obrigatórios.

## Produto Gerado

- Sistema funcional desenvolvido em Django.
- Interface administrativa amigável, acessível e configurada para os usuários da associação.
- Documentação técnica hospedada no MkDocs, facilitando o entendimento e uso do sistema.

## Considerações Finais da Fase

<p align="justify">
A fase de construção permitiu transformar o planejamento em um sistema operacional, com as funcionalidades esperadas pela Associação de Moradores da Ilha Primeira. A colaboração da equipe, aliada aos testes constantes, garantiu que o produto fosse adequado às necessidades da comunidade, estando pronto para a próxima fase de transição e implantação.
</p>
