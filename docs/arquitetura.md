# 🧱 Arquitetura do Sistema – PARKSYNC

## Visão Geral

O sistema PARKSYNC foi projetado utilizando uma arquitetura modular e escalável.  
Inicialmente, o projeto envolvia componentes físicos (ESP32, sensores ultrassônicos, servomotor e BLE).  
Nesta versão (TP4), a arquitetura foi mantida, porém com foco na **simulação lógica**.

---

## 🧩 Componentes Principais

1. **Módulo de Simulação**  
   - Substitui os sensores físicos.  
   - Gera estados de vagas aleatórios ou controlados via interface.

2. **Módulo de Comunicação BLE (Simulado)**  
   - Envia e recebe bytes representando o número e estado das vagas.  
   - Utilizado pelo App Inventor ou terminal de testes.

3. **Interface App Inventor (Simulada)**  
   - Mostra as vagas 2x2 e permite reservar/liberar vagas.

4. **Banco de Dados Simples (em memória)**  
   - Armazena os estados atuais das vagas.

---

## 🧭 Diagrama Lógico (Simplificado)

```
[Simulador de Vagas] ⇄ [Módulo BLE Simulado] ⇄ [App PARKSYNC]
       │                           │
       ▼                           ▼
 [Banco de Estados]          [Interface Gráfica]
```

---

## 🧠 Observação sobre o TP4

O foco deste sprint foi garantir o funcionamento completo da lógica principal sem dependência de hardware físico, além da criação de um plano de testes abrangente e da demonstração do projeto em vídeo.
