# Projeto - Agendador de Processos Concorrentes (Tema C)

## 👥 Integrantes
- ANA ELISA OLIVEIRA SILVA
- SAMYRA LOBO

## 📖 Objetivo
O programa lê um grafo de incompatibilidades de processos a partir de um arquivo `.txt`, verifica se o grafo é **bipartido (2-colorível)** e informa se é possível agendar os processos em apenas **dois turnos**.  

## ⚙️ Funcionalidades
- Verificar adjacência entre dois processos
- Calcular grau de um processo
- Listar vizinhos
- Listar todas as arestas
- Testar bipartição (2-coloração)
- Visualizar o grafo colorido (turnos)

## 📂 Estrutura
- `main.py` → programa principal com menu
- `grafo.py` → leitura e operações básicas
- `biparticao.py` → algoritmo central (2-coloração)
- `visualizacao.py` → desenho do grafo
- `exemplos/` → arquivos de teste

## 🚀 Como executar
1. Instalar dependências:
   ```bash
   pip install -r requirements.txt

