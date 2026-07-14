# 📚 Mentoria Ada's Academy — Atividades Semanais

Bem-vinda ao repositório da mentoria! 🎉  
Aqui você vai organizar e entregar todas as atividades semanais propostas ao longo do programa.

---

## 📁 Estrutura do Repositório

O repositório está organizado em pastas por semana. Cada pasta corresponde a uma semana da mentoria:

```
mentoria_adas_dani/
├── semana1/
├── semana2/
├── semana3/
├── semana4/
├── semana5/
├── semana6/
├── semana7/
├── semana8/
├── semana9/
├── semana10/
└── README.md
```

---

## 📝 Como Entregar as Atividades

Siga o passo a passo abaixo para cada semana:

### 1. Clone o repositório (apenas na primeira vez)

```bash
git clone <URL_DO_REPOSITORIO>
cd mentoria_adas_dani
```

### 2. Atualize a branch `main` antes de começar

```bash
git checkout main
git pull origin main
```

### 3. Crie uma branch com o nome da semana

> ⚠️ **Importante:** O nome da branch deve seguir o padrão `semanaX` (ex: `semana1`, `semana2`...).

```bash
git checkout -b semana1
```

### 4. Adicione seus arquivos na pasta correspondente

Coloque seus códigos e exercícios dentro da pasta da semana. Por exemplo, para a semana 1:

```
semana1/
├── exercicio1.py
├── exercicio2.py
└── anotacoes.md
```

### 5. Faça o commit e envie para o repositório remoto

```bash
git add .
git commit -m "Atividades da semana 1"
git push origin semana1
```

### 6. Abra um Pull Request (PR)

1. Acesse o repositório no GitHub.
2. Clique em **"Compare & pull request"** para a branch que você acabou de enviar.
3. Adicione uma descrição breve sobre o que foi feito.
4. Clique em **"Create pull request"**.

> 💡 **Dica:** Aguarde o feedback da mentora antes de fazer o merge!

---

## ⚙️ Regras e Boas Práticas

- ✅ Sempre crie uma **branch nova** para cada semana — não suba os exercícios direto na `main`.
- ✅ Coloque os arquivos **dentro da pasta da semana correta**.
- ✅ Escreva **mensagens de commit claras** (ex: `"Exercício 1 - Listas em Python"`).
- ✅ Abra um **Pull Request** para cada entrega semanal.
- ❌ **Não** faça merge sem a revisão da mentora.
- ❌ **Não** altere arquivos de semanas anteriores sem autorização.

---

## 🚀 Vamos juntas!

Qualquer dúvida sobre o fluxo de entrega, é só chamar. Bora codar! 💜
