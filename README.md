

# Teste técnico para vaga de Desenvolvedor Python/Django pela Data Stone

- Candidato: João Vitor Leal de Castro
- Email: joaoo.lealc@gmail.com
- GitHub: [@joaoleau](https://www.github.com/joaoleau)
- Linkedin: [Joao Vitor Leal](https://www.linkedin.com/in/joaolealc/)

## Destaques

- Endpoint para conversão de moedas
- Endpoint para verificar as moedas suportdas pela API
- Valores de cotações atualizados
- Banco de dados com Postgres a fim de no futuro possibilitar novos avanços
- API Rest com Django Rest Framework
- Contêiners com Docker para compatibilidade
- Testes Unitários com Pytest para aumentar a qualidade e segurança do código

## Observações

- O projeto é altamente dependente de dois endpoints da API CurrencyFreaks. Acredito que isto seja uma vulnerabilidade do sistema, pois caso a api externa seja comprometida, nossa aplicação também será. Faço uso da api externa a fim de pegar os valores das cotações atuais.

- Resolvi escolher por consumir uma api externa para os valores das cotações justamente para nossa aplicação fazer sentido, e responder com valores reais e atuais. 


## Rodando localmente

### Clone o projeto

```bash
  git clone https://github.com/joaoleau/django-teste-tecnico-datastone.git
```

### Entre no diretório do projeto

```bash
  cd django-teste-tecnico-datastone
```

### Inicie o projeto

```bash
  docker-compose up
```

## Ferramentas
Python, Django, Django Rest Framework, Pytest, Postgres, Git, Docker, Docker Compose

