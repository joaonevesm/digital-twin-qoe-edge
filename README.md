# Digital Twin para Monitoramento de QoE em Dispositivos Edge

<p align="center">

Framework para monitoramento em tempo real de dispositivos Edge utilizando Raspberry Pi, com suporte a Digital Twin para avaliação da Qualidade de Experiência (QoE).

</p>

---

## 📖 Sobre o Projeto

Este projeto apresenta uma arquitetura baseada em **Digital Twin** para monitoramento em tempo real de dispositivos Edge.

A solução realiza a coleta contínua de métricas de rede e recursos computacionais da Raspberry Pi, permitindo a construção de uma representação virtual do dispositivo físico e fornecendo suporte à avaliação da Qualidade de Experiência (QoE).

O sistema foi desenvolvido utilizando **Python**, **Streamlit** e **Raspberry Pi**, sendo destinado a experimentos relacionados à Computação em Borda (Edge Computing), Redes 5G/6G e Inteligência Artificial.

---

## 🎯 Objetivos

- Monitorar continuamente métricas do dispositivo Edge;
- Construir um Digital Twin do ambiente monitorado;
- Avaliar a Qualidade de Experiência (QoE);
- Auxiliar estudos sobre Edge AI e Redes Inteligentes.

---

## 🏗 Arquitetura

```
                 Raspberry Pi
                      │
                      ▼
           Coleta de Métricas
                      │
                      ▼
          Processamento dos Dados
                      │
                      ▼
               Digital Twin
                      │
                      ▼
               Motor de QoE
                      │
                      ▼
            Dashboard Streamlit
```

---

## 📊 Métricas Monitoradas

### Rede

- RSSI
- RTT
- Jitter
- Throughput
- Perda de Pacotes

### Sistema

- Uso de CPU
- Memória RAM
- Temperatura
- Uso de Disco

---

## 📂 Estrutura do Projeto

```
digital-twin-qoe-edge
│
├── assets/
├── data/
├── docs/
│
├── src/
│   ├── backend/
│   ├── config/
│   ├── core/
│   └── frontend/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Instalação

Clone o repositório

```bash
git clone https://github.com/joaonevesm/digital-twin-qoe-edge.git
```

Entre na pasta

```bash
cd digital-twin-qoe-edge
```

Crie o ambiente virtual

Windows

```bash
python -m venv .venv
```

Ative

```bash
.venv\Scripts\activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando

Inicie o Dashboard

```bash
streamlit run src/frontend/app.py
```

---

## 🧠 Tecnologias Utilizadas

- Python
- Streamlit
- Pandas
- Plotly
- PySerial
- Raspberry Pi
- Git
- GitHub

---

## 📌 Aplicações

O projeto pode ser utilizado em pesquisas envolvendo:

- Computação em Borda (Edge Computing)
- Digital Twins
- Monitoramento de Redes
- Internet das Coisas (IoT)
- Inteligência Artificial
- QoE
- Redes 5G e 6G
