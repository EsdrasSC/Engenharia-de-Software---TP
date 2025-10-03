# Documentação da Arquitetura - TP2

## 1. Escolha de Tecnologias
- **Frontend**: React (ou Angular/Vue) - interface do usuário
- **Backend**: FastAPI (Python) ou Express (Node.js) - lógica de negócio e API
- **Banco de Dados**: PostgreSQL - armazenamento de usuários, vagas e reservas
- **Infraestrutura**: Docker - facilitar execução local
- **(Opcional)**: Serviço de Notificação (e-mail/push)

## 2. Projeto Arquitetural
O sistema segue arquitetura em camadas:  
- O **usuário** acessa o **frontend web** (React).  
- O frontend comunica-se com o **Backend API** (FastAPI ou Node/Express).  
- O backend acessa o **banco de dados PostgreSQL** para registrar usuários, reservas e status de vagas.  
- O **administrador** acessa o painel de controle pela mesma aplicação web.  

### Diagramas
![Contexto](docs/diagrams/context.png)  
![Contêineres](docs/diagrams/containers.png)  
![Componentes](docs/diagrams/components.png)  
![Sequência](docs/diagrams/sequence-reserve.png)  

## 3. Justificativa do Modelo Escolhido
Foi escolhido o **C4 Model** porque ele permite descrever a arquitetura em diferentes níveis de detalhe:  
- **Contexto**: mostra os atores e como eles interagem com o sistema.  
- **Contêineres**: mostra os principais blocos de software (frontend, backend, banco).  
- **Componentes**: detalha os módulos internos do backend.  
- **Sequência**: descreve o fluxo principal de uma reserva.  

Esse modelo facilita a comunicação da arquitetura, torna o projeto mais compreensível e ajuda na manutenção futura.
