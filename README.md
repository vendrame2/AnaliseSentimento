# 🌟 Sentiment Analysis App  

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)  
![Flask](https://img.shields.io/badge/flask-2.x-orange.svg)  

## 📖 Sobre o Projeto  
Esta aplicação interativa permite analisar sentimentos a partir de frases fornecidas. Ideal para quem deseja explorar o impacto emocional de suas palavras!  

### ✨ Funcionalidades  
- **Envio de Frases**: Insira uma frase e descubra o sentimento predominante.  
- **Visual Dinâmico**:  
  - **📊 Gráfico Interativo**: Exibe a porcentagem de sentimentos (positivo, neutro e negativo).  
  - **😃 Emojis**: Mostra o sentimento predominante de forma visual.  
- **Treinamento Personalizado**: Ajuste o modelo com seus próprios dados usando o notebook disponibilizado.
  - **😃 Dados Utilizados**: Frases específicas para suporte de TI.
  - **😃 Modelagens propostas**: Diversos ajustes de modelos foram feitos a título de conhecimentos: Ajustes na Tokenização, Kfold, Sistema de Votação.

---

## 🛠️ Tecnologias Utilizadas  

### Backend  
- 🐍 **Python**: Linguagem de programação principal.  
- 🌐 **Flask**: Framework para API e servidor web.  
- 🤖 **Scikit-learn**: Modelo de Machine Learning para análise de sentimentos.  

### Frontend  
- 🎨 **Bootstrap**: Para estilização e responsividade.  
- 📈 **Plotly**: Gráficos interativos dinâmicos.  

---

## 📂 Estrutura do Projeto  

```plaintext
flask-sentiment-analysis/
├── app/
│   ├── static/                # Arquivos estáticos (CSS, JS).
│   ├── templates/             # Templates HTML.
│   ├── api.py                 # Código da API Flask.
│   ├── __init__.py            # Inicialização da aplicação Flask.
├── model/
│   ├── sentiment_model.pkl    # Modelo treinado.
│   ├── vectorizer.pkl         # Vetorizador treinado.
├── data/
│   ├── training_data.csv      # Dados de treinamento.
├── notebooks/
│   ├── sentiment_training.ipynb  # Notebook para treinamento do modelo.
├── requirements.txt           # Dependências do projeto.
├── app.py                     # Arquivo principal para rodar o Flask.
```

---

## 🚀 Como Executar  

### Pré-requisitos  
- Python 3.8 ou superior  
- Ambiente virtual recomendado (`venv`)  

### Passos  

1. **Clone o repositório**:  
   ```bash
   git clone https://github.com/seu-usuario/flask-sentiment-analysis.git
   cd flask-sentiment-analysis
   ```

2. **Crie e ative o ambiente virtual**:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**:  
   ```bash
   python app.py
   ```

5. **Acesse no navegador**:  
   ```
   http://127.0.0.1:5000
   ```

---

## 🔧 Como Treinar o Modelo  

1. Navegue até o diretório `notebooks/`.  
2. Abra o notebook `sentiment_training.ipynb` em um ambiente Jupyter ou VSCode. 
3. Siga as instruções no notebook para treinar o modelo e salvar os arquivos necessários (`sentiment_model.pkl` e `vectorizer.pkl`).  

---

## 🤝 Contribuições  
Contribuições são bem-vindas! Se tiver sugestões ou encontrar problemas, sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.  

---

## 📜 Licença  
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.  

---

## 💻 Demonstração  

### Tela Inicial  
![Tela Inicial](https://via.placeholder.com/800x400?text=Tela+Inicial+da+Aplicação)  

### Resultado de Análise  
![Resultado de Emojis e Gráfico](https://via.placeholder.com/800x400?text=Gráfico+e+Emojis+Atualizados)  
```  

