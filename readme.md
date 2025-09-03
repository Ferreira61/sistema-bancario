# 🏦 Sistema Bancário em Python

Este projeto é uma implementação simples de um **sistema bancário** em Python, feito para praticar conceitos básicos da linguagem, como:

- Estruturas condicionais (`if/elif/else`)
- Laços de repetição (`while`)
- Listas para armazenar informações
- Variáveis imutáveis e mutáveis
- Regras de negócio aplicadas a operações financeiras

---

## 📋 Regras do Sistema

O sistema permite **3 operações principais**: depósito, saque e extrato.

### 🔹 Depósito
- Deve ser maior que R$ 0,00.  
- O valor é adicionado ao saldo.  
- O depósito é registrado no extrato.  

### 🔹 Saque
- Até **3 saques diários**.  
- Limite de **R$ 500,00 por saque**.  
- Não pode ser maior que o saldo.  
- O saque é registrado no extrato.  

### 🔹 Extrato
- Lista todos os depósitos e saques realizados.  
- Mostra o **saldo atual** no final.  
- Caso não haja movimentações, exibe:  
  `"Não foram realizadas movimentações"`  

---

## 🚀 Como executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario.git
