# 🌟 README.md para `Calendario_Falhas_Transporte_Publico_SP` 🌟

## 📜 Descrição
O script `Processamento_Python.py` faz parte de um conjunto de ferramentas Python 🐍 destinadas a extrair, processar e visualizar dados 📊 relacionados ao funcionamento de linhas de trem/metrô 🚆. Este script gerencia o fluxo de trabalho desde a extração de dados HTML até a criação de imagens representativas 🖼️.

## 🧩 Módulos
O script utiliza os seguintes módulos personalizados:
- `ExtrairHTML` 🌐
- `TratamentoDados` 🔍
- `CriarImagem` 🎨
- `CriarImageTodosMeses` 📅

## ⚙️ Fluxo de Trabalho
1. **Seleção de Dados** 📋: O usuário insere as linhas e anos desejados.
2. **Validação** ✔️: Verifica se as entradas estão nas listas de linhas e anos válidos.
3. **Processamento** 🔄: Se as entradas forem válidas, o script segue para a extração de dados, tratamento e criação de imagens.

## 📚 Módulos Detalhados
### ExtrairHTML
- Utiliza `selenium` e `BeautifulSoup` para extrair dados HTML do site especificado 🌍.
- Salva os dados em uma pasta local `HTML_Salvos` 📁.

### TratamentoDados
- Processa os arquivos HTML salvos, usando expressões regulares para extrair informações relevantes 🕵️‍♂️.

### CriarImagem
- Gera imagens mensais indicando dias com falhas, usando a biblioteca `PIL` 📆.

### CriarImageTodosMeses
- Compila informações anuais em um arquivo HTML, personalizado com cores e informações específicas da linha de trem/metrô 🌈.
- Salva os resultados de HTML em uma pasta local `Resultado` 📁.

## 📋 Requisitos
- Python 3.x 🐍
- Ambiente virtual: `venv` 📦
- Bibliotecas: `selenium`, `bs4`, `PIL` 📚

## 🚀 Instalação e Inicialização do `Processamento_Python.py` 🚀

## 🐧 Para Linux e macOS

### 🌟 `1_PrimeiroUso_IniciarProjetoParaLinuxEMacOS.sh`

Este script facilita a instalação e execução do projeto em sistemas Linux e macOS. Siga estes passos para um início rápido:

1. **Abra um Terminal** 🖥️: Encontre e abra o terminal em seu sistema.
2. **Navegue até a Pasta do Projeto** 📁: Use o comando `cd` para chegar à pasta do script.
3. **Torne o Script Executável** 🔐: Torne-o executável com:
   ```bash
   chmod +x 1_PrimeiroUso_IniciarProjetoParaLinuxEMacOS.sh
   ```
4. **Execute o Script** 🚀: Execute com:
   ```bash
   ./1_PrimeiroUso_IniciarProjetoParaLinuxEMacOS.sh
   ```
O script vai:
- Criar um ambiente virtual Python 🐍.
- Ativar este ambiente virtual.
- Instalar dependências 🧰 (Pillow, Selenium, BeautifulSoup4).
- Executar `Processamento_Python.py`.
- Indicar onde os resultados foram salvos 📊 e esperar que você pressione Enter para finalizar.

## 🪟 Para Windows

### 🌟 `1_PrimeiroUso_IniciarProjetoParaWindows.bat`

Para usuários Windows, o processo é adaptado para este ambiente:

1. **Abra o Prompt de Comando** 💻: Pesquise "cmd" no menu Iniciar e abra-o.
2. **Navegue até a Pasta do Projeto** 📁: Use `cd` para chegar à pasta do projeto.
3. **Execute o Script** 🚀: Digite o nome do script e pressione Enter:
   ```cmd
   1_PrimeiroUso_IniciarProjetoParaWindows.bat
   ```
O script irá:
- Criar um ambiente virtual Python 🐍.
- Ativar este ambiente (ajustando políticas de execução, se necessário).
- Instalar dependências 🧰 (Pillow, Selenium, BeautifulSoup4).
- Executar `Processamento_Python.py`.
- Informar onde os resultados foram salvos 📊 e pausar para revisão.

## 📝 Notas Importantes

- **Python Instalado** 🐍: Certifique-se de ter o Python instalado.
- **Ajustes de Segurança no Windows** 🔒: Pode ser necessário ajustar configurações de segurança para executar scripts.
- **Localização dos Scripts** 📌: Os scripts devem estar na mesma pasta do projeto.

## 🖐️ Instalação Manual (Opcional)

Se preferir uma abordagem manual:

1. **Crie um Ambiente Virtual**:
   - Linux/macOS: `python3 -m venv .venv` / `source .venv/bin/activate`
   - Windows: `python -m venv .venv` / `.venv\Scripts\activate`
2. **Instale as Dependências**:
   ```bash
   pip install Pillow selenium bs4
   ```
3. **Execute o Script**:
   ```bash
   python Processamento_Python.py
   ```
4. **Verifique os Resultados** na pasta `Resultado`.

Assim, você terá total controle sobre cada etapa do processo! 🌈🛠️

## 🚀 Uso
1. Execute `Processamento_Python.py` 🖥️.
2. Insira as linhas e anos conforme solicitado ✏️.
3. O script processará os dados e gerará as saídas correspondentes 📈.]

## 📝 Nota
Assegure-se de ter os drivers adequados para o `selenium` e as fontes necessárias para a `PIL` 🛠️.
