# Ultron Sentinel – Cyber Security Intelligent Agent  

Ultron Sentinel é um agente inteligente de cibersegurança em desenvolvimento, projetado para realizar **análise automatizada de logs**, detectar padrões de ataque, gerar alertas e evoluir para responder automaticamente a incidentes.  

O projeto combina fundamentos de **Python, Regex, arquitetura modular, análise de ameaças e automação**, servindo como base para integrações futuras com **IA, dashboards interativos e recursos avançados de resposta a incidentes (SOAR)**.

---

## Objetivos do Projeto

- Criar um agente autônomo para identificação de eventos suspeitos  
- Detectar ataques como brute force, SQL Injection, XSS, login inválido e acessos não autorizados  
- Manter uma arquitetura modular e escalável  
- Registrar alertas para histórico e análise posterior  
- Evoluir futuramente para usar Inteligência Artificial  
- Criar um painel (dashboard) para visualização dos eventos  
- Automatizar respostas (bloquear IPs, enviar alertas, etc.)

---

## Tecnologias Utilizadas

- **Python 3.14+**  
- **Regex (Expressões Regulares)**  
- **Arquitetura Modular**  
- **JSON (persistência inicial)**  
- **Git & GitHub**  
- **VS Code**  
- Futuro: **SQLite, FastAPI, React, Dash/Streamlit, IA/ML**

---

## Estrutura do Projeto

📁 Estrutura do Projeto
```Ultron Sentinel/
│
├── logs/                 # Arquivos de log para análise
│   └── example.log
│
├── sentinel_core/        # Núcleo do agente de segurança
│   ├── log_analyzer.py   # Motor de análise de padrões
│   ├── main.py           # Script principal
│   └── __init__.py
│
└── README.md
```

---

##  Como Funciona a Análise de Logs

O Ultron Sentinel identifica padrões de ataque usando:

- **regex avançado**
- análise de palavras-chave indicativas de ataque  
- extração de IP  
- contagem automática de tentativas maliciosas (ex: brute force)

Exemplos de padrões detectados:

- `failed password`
- `unauthorized`
- `invalid user`
- `sql injection`
- `xss attempt`
- `ssh.*failed`

Também é detectado:

- **Brute force** (com limite configurável de tentativas)  
- Falhas repetidas de login por IP  
- Erros severos e acessos negados  

---

## ▶️ Como Executar o Projeto

1. **Clone o repositório:**

`git clone https://github.com/lucascardoso1912/ultron-sentinel.git`

2. **Entre no diretório do projeto:**
   
`cd ultron-sentinel/sentinel_core`

3. **Execute o script principal:**

`python main.py`


4. Veja os alertas sendo exibidos em tempo real no terminal.

---

## 📊 Roadmap (Evolução do Projeto)

### 🔎 **Versão Atual – v1.0**
- [x] Estrutura inicial  
- [x] Análise básica de logs  
- [x] Detecção de brute force  
- [x] Padrões com regex  
- [x] Arquitetura modular  

### 📌 **Próximas Etapas**
#### **Persistência**
- [ ] Salvar alertas em JSON  
- [ ] Migrar para SQLite  
- [ ] Criar modelo de dados  

#### **Back-End**
- [ ] Criar API com FastAPI  
- [ ] Criar endpoint para receber logs externos  
- [ ] Criar sistema de autenticação básica  

#### **Front-End / Dashboard**
- [ ] Dashboard com Streamlit ou React  
- [ ] Gráficos em tempo real  
- [ ] Tabela de alertas  
- [ ] Filtros avançados  

#### **IA / Machine Learning**
- [ ] Classificação automática de ataques  
- [ ] Identificação de anomalias  
- [ ] Previsão de comportamento suspeito  

#### **Automação de Resposta (SOAR)**
- [ ] Bloqueio automático de IPs  
- [ ] Notificação em Telegram/Email  
- [ ] Geração automática de relatórios  

---

## 🧩 Por que este projeto é importante?

Este projeto representa a base para um sistema avançado de defesa cibernética, unindo:

- lógica de programação  
- análise de dados  
- fundamentos de segurança  
- arquitetura de software  
- automação  
- futura integração com IA  

É ideal para quem deseja ingressar nas áreas de:

- Desenvolvimento  
- Defesa Cibernética  
- Análise de Segurança  
- Engenharia de Software  
- Inteligência Artificial aplicada a Cyber  

---

## 👨‍💻 Autor

**Lucas Cardoso**  
Estudante de Defesa Cibernética  
Desenvolvedor em formação | Entusiasta da técnlogia, desenvolvimento e segurança  

---

## ⭐ Contribuições

Pull requests e sugestões são bem-vindas enquanto o projeto evolui.

---






