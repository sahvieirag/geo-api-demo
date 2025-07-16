# Memória do Projeto Geo-API Demo

Este documento contém as diretrizes e convenções para o projeto Geo-API.

## 1. Visão Geral da Arquitetura
- **Linguagem Principal:** Python 3
- **Framework:** Flask
- **Biblioteca Essencial:** `geopy` para todos os cálculos de geolocalização.
- **Estrutura:**
  - `app.py`: Contém apenas a camada de API (rotas e endpoints). **NÃO deve conter lógica de negócio.**
  - `services.py`: Onde toda a lógica de negócio e manipulação de dados deve residir.
  - `utils.py`: Para funções puras e reutilizáveis, como cálculos matemáticos.

## 2. Comandos Padrão
- **Para instalar dependências:** `pip install -r requirements.txt`
- **Para rodar a aplicação em modo de desenvolvimento:** `flask run`
- **Para executar a suíte de testes:** `pytest`

## 3. Convenções de Código
- **Documentação:** Todas as novas funções públicas devem ter uma docstring explicando seu propósito, argumentos (`Args:`) e o que retornam (`Returns:`).
- **Nomenclatura:** Variáveis e funções devem seguir o padrão `snake_case`.
- **Tratamento de Erros:** A camada de serviço (`services.py`) deve retornar uma tupla `(resultado, erro)`, onde `erro` é `None` em caso de sucesso. A camada da API (`app.py`) é responsável por transformar isso em uma resposta JSON com o código de status HTTP apropriado.
