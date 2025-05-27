# Farmina Zendesk - Busca de Produtos para Pets

Aplicação web para agentes de atendimento consultarem produtos Farmina com base nas características dos pets dos clientes.

## Funcionalidades

- Filtros avançados para busca de produtos:
  - Tipo de alimento (seco ou molhado)
  - Tipo de pet (cão ou gato)
  - Gestação (sim ou não)
  - Lactação (sim ou não)
  - Fase da vida (filhote, adulto, sênior)
  - Cuidados especiais (carregados dinamicamente)
  
- Integração com as APIs Farmina:
  - Listagem de produtos
  - Listagem de cuidados especiais

- Exibição de resultados com:
  - Imagens dos produtos
  - Descrições completas
  - Formatos disponíveis e preços
  - Cuidados especiais associados

## Tecnologias Utilizadas

- Backend:
  - Python 3.x
  - Flask
  - Requests

- Frontend:
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

## Pré-requisitos

- Python 3.8+
- pip
- virtualenv (recomendado)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/farmina-zendesk.git
cd farmina-zendesk
```
## Crie e ative um ambiente virtual (recomendado):

```
python -m venv venv
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```
## Instale as dependências:

```
pip install -r requirements.txt
```

## Execução
```
python app.py
A aplicação estará disponível em: http://localhost:5000
```
## Estrututra do Projecto
```
farmina-zendesk/
├── app.py                # Aplicação principal Flask
├── requirements.txt      # Dependências Python
├── static/
│   └── style.css         # Estilos CSS
├── templates/
│   └── index.html        # Template HTML principal
├── README.md             # Este arquivo
└── LICENSE               # Licença (opcional)
```
## Configuração
```
A aplicação está configurada para usar as credenciais padrão da API Farmina:

python
API_BASE_URL = "https://gw-c.petgenius.info/wfservice/z1"
API_AUTH = HTTPBasicAuth('wsfarmina_zendesk', 'test')
O país padrão está definido como "MA" (Marrocos) conforme especificado no teste.

API Endpoints
A aplicação expõe dois endpoints principais:

POST /api/specialcares - Busca cuidados especiais

Parâmetros: species (dog/cat)

POST /api/products - Busca produtos

Parâmetros:

productType (dry/wet)

type (dog/cat)

lifeStage (opcional - puppy/adult/senior)

gestation (opcional - true/false)

lactation (opcional - true/false)

specialcares (opcional - array de IDs)
```
## adicionais 
``` python -m venv venv
.\venv\Scripts\activate
Instale o Flask :
2.3.3
pip install flask
 a versão do Werkzeug:
pip install werkzeug==2.3.7
 run:
python app.py
```
