# 365 Atividades STEM

Catálogo web das 365 atividades do livro "365 Atividades STEM".
Permite buscar atividades por nome ou tag, ver o número da página,
e adicionar/editar uma análise para cada atividade.

## Funcionalidades

- Busca por nome da atividade
- Filtro por tag (ciência, tecnologia, engenharia, matemática, arte)
- Filtro por status da análise (com análise / sem análise)
- Página individual para cada atividade
- Adicionar e editar análise textual
- Badges visuais indicando status da análise

## Como rodar

### Pré-requisitos

- Docker e Docker Compose

### Passos

```bash
# 1. Clone o repositório
git clone <url>
cd sumario

# 2. Crie o arquivo de ambiente
cp .env.example .env # Crie uma senha para o banco no .env


# 3. Suba os serviços
docker compose up -d

# 4. Acesse
http://localhost:8000
```

O banco é populado automaticamente com as 366 atividades do `sumario.csv`.
