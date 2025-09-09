# Play LangGraph

Um projeto de playground para experimentar com LangGraph e Google Gemini AI.

## 📋 Pré-requisitos

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (gerenciador de dependências)
- Chave de API do Google Gemini

## 🚀 Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/luisfuturist/help-alura-agents
   cd help-alura-agents
   ```

2. **Instale as dependências:**
   ```bash
   uv sync
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` na raiz do projeto:
   ```bash
   GEMINI_API_KEY=sua_chave_api_aqui
   ```

## 🛠️ Comandos Disponíveis

O projeto inclui um `Makefile` com comandos úteis:

```bash
# Executar o projeto
make start

# Formatar e corrigir código automaticamente
make lintfix

# Verificar problemas de linting
make lint

# Verificar problemas de linting em modo watch
make lintwatch

# Verificar tipos com Pyright
make typecheck
```

## 📁 Estrutura do Projeto

```
play-langgraph/
├── src/
│   ├── main.py          # Ponto de entrada principal
│   └── config.py        # Configurações e variáveis de ambiente
├── .vscode/             # Configurações do VS Code
├── pyproject.toml       # Configuração do projeto e dependências
├── Makefile            # Comandos de desenvolvimento
└── README.md           # Este arquivo
```

## 🔧 Tecnologias Utilizadas

- **LangChain**: Framework para aplicações com LLM
- **LangGraph**: Biblioteca para construir aplicações com grafos de agentes
- **Google Gemini**: Modelo de IA generativa
- **Pydantic**: Validação de dados e configurações
- **Ruff**: Linter e formatador de código Python
- **Pyright**: Verificador de tipos estático

## 🎯 Como Usar

1. **Execute o projeto:**
   ```bash
   make start
   ```

2. **Desenvolva com qualidade:**
   - O código é formatado automaticamente ao salvar (VS Code)
   - Use `make lintfix` para corrigir problemas de linting
   - Use `make typecheck` para verificar tipos

## 🔑 Configuração do VS Code

O projeto inclui configurações recomendadas para VS Code:

- **Extensões recomendadas**: Python e Ruff
- **Formatação automática** ao salvar
- **Correção automática** de problemas de linting
- **Agrupamento de arquivos** relacionados no explorador

## 📝 Desenvolvimento

### Adicionando Novas Dependências

```bash
# Adicionar dependência de produção
uv add nome-do-pacote

# Adicionar dependência de desenvolvimento
uv add --dev nome-do-pacote
```

### Estrutura de Configuração

As configurações são gerenciadas através do arquivo `src/config.py` usando Pydantic Settings:

- Variáveis de ambiente são carregadas automaticamente do arquivo `.env`
- Configurações são cacheadas para melhor performance
- Validação automática de tipos

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feat/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Add new feature'`)
4. Push para a branch (`git push origin feat/nova-feature`)
5. Abra um Pull Request
