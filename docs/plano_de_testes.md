# 🧪 Plano de Testes – PARKSYNC

## 🎯 Objetivo
Garantir que as principais funcionalidades do sistema PARKSYNC funcionem corretamente, simulando o controle de vagas de estacionamento inteligente.

---

## 🔍 Escopo
Testes funcionais e de integração da aplicação simulada (sem hardware real), cobrindo os casos de uso definidos no TP2:
- Monitorar vagas disponíveis.
- Realizar reserva de vaga.
- Validar entrada e saída de veículos.

---

## ⚙️ Casos de Teste

| ID | Caso de Teste | Objetivo | Procedimento | Resultado Esperado | Estado |
|----|----------------|-----------|---------------|---------------------|---------|
| CT01 | Atualização de vaga | Verificar se o status da vaga muda ao simular a entrada de um veículo | Executar a função `ocuparVaga(1)` | A vaga 1 deve aparecer como **ocupada** na interface | ✅ Passou |
| CT02 | Liberação de vaga | Verificar se o status da vaga muda ao simular a saída do veículo | Executar `liberarVaga(1)` | A vaga 1 deve aparecer como **livre** | ✅ Passou |
| CT03 | Reserva de vaga | Testar se o sistema impede outro carro de ocupar vaga reservada | Reservar a vaga 2, depois tentar ocupar | Sistema exibe “vaga reservada” e mantém vaga como **reservada** | ✅ Passou |
| CT04 | Comunicação BLE simulada | Verificar envio/recebimento de 1 byte representando número da vaga | Simular envio `[2]` e retorno `[2,1]` | Recebimento correto: número e estado da vaga | ✅ Passou |
| CT05 | Exibição no app | Verificar se interface reflete o estado das vagas (2x2) corretamente | Ocupação e liberação sequencial | Interface deve atualizar cada célula conforme estado | ✅ Passou |

---

## 🧩 Ferramentas e Ambiente de Teste
- Simulador local (Python ou JavaScript)
- MIT App Inventor (simulação BLE)
- GitHub Pages (documentação)

---

## 📊 Conclusão
Os testes comprovaram o funcionamento correto das principais funcionalidades da aplicação.  
Todos os casos de uso descritos no TP2 foram cobertos e passaram com sucesso.
