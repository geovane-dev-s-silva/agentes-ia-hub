# 🧠 Agentes IA - Hub de Inteligência com CSV

Este repositório é um projeto colaborativo de um grupo de estudos com foco na criação de **agentes de IA que respondem perguntas baseadas em arquivos CSV**.

Nosso objetivo é permitir que o usuário faça perguntas como:

- "Qual fornecedor teve maior montante recebido?"
- "Qual item teve o maior volume entregue?"
- "Quantas notas fiscais foram emitidas em janeiro?"

---

## 📌 Estrutura do Projeto

```
agentes-ia-hub/
├── .venv/               # Ambiente virtual (não incluído no Git, listado no .gitignore)
├── data/                # Arquivos CSV de entrada
├── src/                 # Código-fonte dos agentes
│   └── main.py          # Script principal
├── requirements.txt     # Dependências Python
└── README.md            # Documentação do projeto
```
.gitignore demais pastas rs 
---

## ✅ Como executar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/geovane-dev-s-silva/agentes-ia-hub.git
cd agentes-ia-hub
```

2. **Crie e ative um ambiente virtual:**

```bash
python -m venv .venv
.venv\Scriptsctivate  # No Windows
# ou
source .venv/bin/activate  # No Linux/macOS
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Execute o agente:**

```bash
python src/main.py
```

---

## 🗂️ Organização Scrum do grupo

| Nome | Responsável por | Status |
|---|---|---|
| Izaque Liborio | Integrador e Agente Principal.| 🔄 |
| Igor Araujo Mattos | Métodos Elaborados. | 🔄 |
| Tadeu| Implementar a extração de texto de
arquivos PDF. | 🔄 |
| Paula Monteiro | Salvar arquivos carregados em um local temporário.| 🔄 |
| Márcia | Converter os dados extraídos para o formato CSV. | 🔄 |
| Amanda | Simular o processo de upload de um arquivo. | 🔄 |
| Lu.uh Rodrigues | Formatar os dados extraídos para exibição na tela. | 🔄 |
| Geovane | Inferir o tipo de documento fiscal. | ✅ |

> _Status atual: Em desenvolvimento (Sprint até dia 18)._

---

## 🌐 Onde vamos expor o projeto online?

👉 **Nosso GitHub Pages:**
> Em breve: https://geovane-dev-s-silva.github.io/agentes-ia-hub/

**Outras sugestões:**  
- Google Colab (para notebooks demonstrativos)  

---

## 🚧 Status atual:

✅ Repositório criado  
✅ Estrutura de pastas inicial  
✅ Ambiente virtual configurado  
⬜️ Funções para leitura de CSVs  
⬜️ Mecanismo básico de perguntas e respostas  

---

## 📌 Próximas etapas

- [ ] Implementar leitura robusta dos arquivos CSV
- [ ] Criar interface de perguntas simples
- [ ] Testar casos de perguntas como: "Maior montante", "Maior quantidade"
- [ ] Documentar exemplos de perguntas e respostas

---

## 📄 Licença

Projeto com fins educacionais para estudo de agentes de IA com dados estruturados.  
Licença: MIT

---

Colabore, faça fork ou abra issues para contribuir!