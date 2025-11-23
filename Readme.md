# DeepScan 🔍

**AI-Powered Vulnerability Scanner**  
*Made by Pwimawy*

DeepScan is a powerful CLI tool that uses DeepSeek AI to scan your code for security vulnerabilities like SQL injection, XSS, command injection, and more across multiple programming languages.

## 🚀 Features

- **Multi-Language Support**: PHP, HTML, JavaScript, Java, Python, C/C++, C#, Ruby, Go, Rust, and more
- **Comprehensive Vulnerability Detection**: 
  - SQL Injection (SQLi)
  - Cross-Site Scripting (XSS)
  - Command Injection
  - Path Traversal
  - Authentication Issues
  - Sensitive Data Exposure
  - CSRF Vulnerabilities
  - XXE Attacks
  - And many more...
- **AI-Powered Analysis**: Uses DeepSeek AI for intelligent code analysis
- **Batch Scanning**: Scan single files or entire directories
- **Detailed Reports**: Structured vulnerability reports with severity levels and fix recommendations

## 📋 Requirements

- Python 3.6+
- DeepSeek API key (Free)

## 🔧 Installation

### 1. Clone the Repository (Recommended)

Use `git` to clone the repository to your local machine:

```bash
# Clone the repository
git clone https://github.com/Pwimawy/Deepscan.git

# Navigate into the project directory
cd deepscan
```

### 2. Manual Download

If you prefer not to use Git, you can download the single file directly. To do this, navigate to the `deepscan.py` file on GitHub, click the **"Raw"** button, and then right-click on the page to select **"Save As..."** to save the file to your desired location.

### 3. Install Dependencies

```bash
pip3 install requests
```

### 4. Configure API Key

- Get your free DeepSeek API key from: [https://platform.deepseek.com/api_keys](https://platform.deepseek.com/api_keys)
- Open `deepscan.py` and replace the default API key:
```python
# Change this line in the script to your actual API key:
self.api_key = "sk-your-deepseek-api-key-here"
```

## 🎯 Usage

### Basic File Scan
```bash
python3 deepscan.py target.php
```

### Scan Directory
```bash
python3 deepscan.py /path/to/your/code
```

### Custom Output File
```bash
python3 deepscan.py target.php -o security_report.txt
```

### Verbose Output
```bash
python3 deepscan.py target.php -v
```

## 📝 Examples

### Scan a PHP file:
```bash
python3 deepscan.py example.php
```

### Scan a JavaScript project:
```bash
python3 deepscan.py /path/to/javascript/project -o js_security_report.txt
```

### Scan multiple file types:
```bash
python3 deepscan.py /project/src
```

## 🔍 Supported File Types

- **Web**: `.php`, `.html`, `.htm`, `.asp`, `.aspx`, `.jsp`
- **JavaScript**: `.js`, `.ts`, `.jsx`, `.tsx`, `.vue`
- **Backend**: `.java`, `.py`, `.rb`, `.go`, `.rs`
- **Systems**: `.c`, `.cpp`, `.cs`

## 📊 Sample Output

```
==============================================
SCAN RESULTS: example.php
==============================================
SECURITY ASSESSMENT:
- Overall risk level: High
- Summary: Found SQL injection and XSS vulnerabilities

VULNERABILITIES FOUND:
- Type: SQL Injection
- Location: Line 15
- Severity: Critical
- Description: Direct user input concatenated into SQL query
- Risk: Full database compromise
- Recommendation: Use prepared statements
- Code snippet: $query = "SELECT * FROM users WHERE id = " . $_GET['id'];

- Type: Cross-Site Scripting (XSS)
- Location: Line 22
- Severity: High
- Description: Unescaped user output in HTML context
- Risk: Session hijacking, credential theft
- Recommendation: Use htmlspecialchars() or output encoding
- Code snippet: echo $_POST['comment'];
```

## 🛠️ How It Works

1. **Code Reading**: Reads your source code files
2. **AI Analysis**: Sends code to DeepSeek AI for security analysis
3. **Vulnerability Detection**: Identifies security issues with detailed explanations
4. **Reporting**: Generates comprehensive reports with fix recommendations

## ⚙️ Configuration

The tool is configured with these default settings:

- **API Model**: `deepseek-coder` (optimized for code analysis)
- **Temperature**: 0.1 (for consistent results)
- **Max Tokens**: 4000 (sufficient for detailed analysis)

## 🤝 Contributing

Feel free to contribute by:
- Reporting bugs
- Suggesting new features
- Adding support for more languages
- Improving the documentation

## ⚠️ Disclaimer

This tool is for educational and professional security assessment purposes only. Always ensure you have proper authorization before scanning systems that you don't own.

## 📄 License

MIT License © 2025 

## 🆘 Support

If you encounter any issues:
1. Check your API key is correctly set
2. Ensure you have an active internet connection
3. Verify the target file/directory exists
4. Check that you have read permissions for the files

---

**Made with ❤️ by Pwimawy**

*Stay secure! 🔒*