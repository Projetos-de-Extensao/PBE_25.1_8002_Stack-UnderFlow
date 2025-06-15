---
id: documento_de_visao
title: Documento de Visão
---

## Introdução

<p align="justify">
O presente documento tem como objetivo fornecer uma visão geral do projeto <b>Stack-UnderFlow</b>, desenvolvido pelos alunos do Ibmec no período 2025.1. Este projeto tem aplicação prática, sendo desenvolvido para atender às necessidades da <b>Associação de Moradores da Ilha Primeira</b>. O sistema busca auxiliar na organização, coleta e gestão dos dados demográficos da comunidade, além de servir como uma ferramenta de apoio para planejamento e tomada de decisões.
</p>

## Descrição do Problema

<p align="justify">
A Associação de Moradores da Ilha Primeira enfrenta desafios para realizar o levantamento e a gestão de dados sobre os moradores e os domicílios da região. A ausência de um sistema estruturado dificulta o acompanhamento das condições habitacionais, sociais e de infraestrutura da comunidade, impactando diretamente a capacidade de planejar ações, solicitar serviços públicos e implementar melhorias locais.
</p>

### Problema

Dificuldade na coleta, organização e gestão dos dados demográficos e habitacionais da Ilha Primeira.

### Impactados

- Associação de Moradores da Ilha Primeira.
- Lideranças comunitárias.
- Moradores da Ilha Primeira.
- Órgãos públicos e parceiros que utilizem os dados para apoiar a comunidade.

### Consequência

- Falta de dados organizados sobre a população e as moradias.
- Dificuldade em realizar diagnósticos precisos sobre as necessidades da comunidade.
- Limitações na comunicação com órgãos públicos e na solicitação de melhorias para a região.

### Solução

Desenvolvimento de um sistema web, utilizando o framework Django, que permita:
- Cadastrar moradores e domicílios de forma estruturada.
- Consultar, atualizar e remover registros.
- Gerar relatórios e ter acesso rápido às informações da comunidade.
- Apoiar a tomada de decisões e o planejamento da associação.

## Objetivos

<p align="justify">
O objetivo principal é fornecer uma ferramenta tecnológica que permita à Associação de Moradores da Ilha Primeira manter um cadastro atualizado dos moradores, domicílios e características da comunidade. Isso facilitará o diagnóstico das condições locais, a organização interna da associação e a interlocução com autoridades públicas, além de apoiar projetos sociais e comunitários.
</p>

## Recursos do Produto

### Cadastro de Domicílios

<p align="justify">
Permite o registro de informações detalhadas sobre os domicílios da Ilha Primeira, incluindo localização (UF, município, setor, distrito, subdistrito), tipo de moradia, quantidade de cômodos, disponibilidade de serviços básicos (água, esgoto, energia elétrica, internet, coleta de lixo) e outras características relevantes.
</p>

### Cadastro de Moradores

<p align="justify">
Permite cadastrar moradores vinculados a domicílios, com informações como nome, CPF, idade, gênero, situação ocupacional, escolaridade e outras informações sociodemográficas necessárias para a gestão da comunidade.
</p>

### Cadastro de Indicadores

<p align="justify">
Permite cadastrar indicadores relevantes que não poderiam ser associados à tabelas com dados específicos, como Morador e Domicílio. Esse cadastro inclui uma pergunta, uma resposta a essa pergunta, e uma descrição relacionada.
</p>

### Pesquisa e Gerenciamento

<p align="justify">
Permite pesquisar registros de moradores e domicílios, realizar filtros, acessar detalhes e gerar relatórios. Inclui funcionalidades para atualização e exclusão dos dados.
</p>

### Interface Administrativa

<p align="justify">
A interface administrativa do Django permite um gerenciamento completo, sendo adaptada para atender às necessidades da associação, garantindo facilidade de uso, segurança e eficiência no controle dos dados.
</p>

## Restrições

- O banco de dados utilizado inicialmente é SQLite para facilitar a instalação local, mas pode ser migrado para PostgreSQL ou outro SGBD para produção.
- O sistema requer acesso à internet local para funcionamento em rede, mas pode ser configurado para uso offline, dependendo da infraestrutura disponível.

## Referências Bibliográficas

> Django Documentation. Disponível em: https://docs.djangoproject.com/
> MkDocs Documentation. Disponível em: https://www.mkdocs.org/
> IBGE — Instituto Brasileiro de Geografia e Estatística. Disponível em: https://www.ibge.gov.br/
> Documentação de Visão — Engenharia de Software Moderna. Disponível em: https://engsoftmoderna.info/
