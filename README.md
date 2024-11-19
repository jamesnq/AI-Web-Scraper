# AI Web Scraper

An intelligent web scraping tool that combines modern web scraping capabilities with AI-powered content parsing. This tool allows you to extract specific information from any website using natural language instructions.

## 🌟 Features

- 🌐 Web scraping with Selenium for dynamic content support
- 🤖 AI-powered content parsing using Ollama
- 📝 Natural language instructions for data extraction
- 🎯 Precise content targeting and cleaning
- 💻 User-friendly Streamlit interface

## 🛠️ Technology Stack

- **Python 3.9+**
- **Streamlit**: Web interface
- **Selenium**: Web scraping
- **BeautifulSoup4**: HTML parsing
- **Langchain**: LLM integration
- **Ollama**: Local LLM for content parsing

## 📁 Project Structure

```
ai-scraper/
├── main.py           # Main Streamlit application
├── scrape.py         # Web scraping functionality
├── parse.py          # AI parsing functionality
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## 🚀 Getting Started

### Prerequisites

1. Install Python 3.9 or higher
2. Install Ollama 3.2
3. Install Chrome/Chromium browser

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jamesnq/AI-Web-Scraper.git
cd ai-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv ai
source ai/bin/activate  # On Windows: .\ai\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Ollama model:
```bash
ollama pull llama3.2
```

### Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Enter a URL in the input field
3. Click "Scrape" to fetch the content
4. Enter your parsing instructions in natural language
5. Click "Parse" to extract specific information

## 🔍 How It Works

1. **Web Scraping**: Uses Selenium to handle dynamic content and JavaScript-rendered pages
2. **Content Cleaning**: Removes unnecessary HTML, scripts, and formatting
3. **AI Processing**: Leverages Ollama's LLM to understand and extract specific information based on natural language instructions
4. **Result Presentation**: Displays cleaned and parsed results through a Streamlit interface

## 📝 Example Usage

```python
# Example parsing instructions:
"Extract all product prices from the page"
"Find all mentioned dates in the article"
"List all contact email addresses"
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Ollama team for providing the local LLM capabilities
- Streamlit team for the excellent web interface framework
- Selenium and BeautifulSoup4 maintainers for robust web scraping tools
