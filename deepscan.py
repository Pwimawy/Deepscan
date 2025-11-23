import os
import sys
import argparse
import requests
from pathlib import Path
from typing import List, Dict, Any

BANNER = """
⣿⡅⠀⡀⠀⠀⠀⠀⡄⠀⠄⠀⠠⡁⡘⠀⠀⠀⠠⠀⠀⠤⠠⡎⠄⠀⠀⠀⡄⢂⡇⢀⡀⠀⠂⢦⠀⠐⠀⠁⡐⣀⡀⢀⠀⢘⢀⡠⠂⠀⡀⢀⡀⠀⠘⠋⢙⠀⠀⠁⠀⠁⠀⠠⠀
⣿⡇⠀⠄⠀⠀⠀⠐⡆⠀⠂⠀⠔⢨⡅⠀⠀⠃⠐⠇⠀⠀⠀⣽⣾⣶⠓⢶⡃⢌⠀⠀⠐⠀⠘⣂⠘⠀⠀⡇⠀⢿⢿⠾⠿⠿⠲⠂⡀⠀⡆⠀⣹⠖⠀⠐⠲⠆⠠⡇⠀⡐⠒⠒⠀
⣿⡁⠀⠁⠀⠀⠀⠀⡃⠀⠄⠀⡭⠀⣡⠤⠤⠀⠨⡖⠒⡆⢠⡼⠁⢏⠀⠀⡴⢾⡆⠀⠆⠀⠀⡇⢀⠀⠀⡀⠈⢏⠀⡐⠀⠀⢁⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⡀⠀⡀⠀⡆⠀⠐⠈
⣿⡇⠀⣀⠀⠀⠀⠀⠁⠀⠁⠀⠀⠄⠀⠀⠀⡀⢐⠁⠀⡄⠀⠙⡛⠛⠒⠛⣶⣌⣣⠀⠀⠀⠰⡡⡊⠀⠀⠀⢈⠌⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢿⠏⠉⡃⠀⠀⠀
⣿⠁⠀⠃⠀⠀⠀⠀⢀⠀⠄⠀⠐⠀⠐⠀⠀⠀⠀⠆⠀⠄⠀⢘⠄⠀⠀⠀⣾⢷⡇⠀⡆⠀⠀⢇⠀⡀⢀⡆⢀⠂⠀⠐⠀⠈⡀⠀⡁⠀⠀⠀⠅⠀⣰⠀⠀⡄⠈⡁⠀⠆⠀⠀⠀
⣿⡂⠀⠀⠀⠀⠀⠆⠈⠀⠂⠀⡀⠠⠀⠀⠀⠀⢈⡃⠀⠂⠀⠒⠄⠀⠀⠀⠀⠬⠁⠀⠁⠀⢀⡇⢀⠀⠀⢄⢀⡞⠀⠀⠀⠀⡁⠈⠁⠀⠀⠀⢄⠀⠀⠐⠠⡶⠶⡏⠙⢃⠀⣠⠀
⣧⡄⠀⠅⠀⢰⡶⢷⠀⠀⠂⠀⡂⠁⢀⠀⠀⠀⠠⡄⠀⡄⠀⡌⠂⠀⠀⠀⠒⡘⡄⠀⠀⠀⠸⠆⠀⡀⠀⠃⠀⡛⠀⠀⠠⠴⡀⠀⡇⠀⠁⠀⣺⠀⠘⠀⠠⡋⣈⡷⠶⢇⠀⡸⠀
⣿⡇⠀⠄⠀⠈⠡⠀⣄⡤⡄⠀⡇⠠⢃⠀⠀⠀⢐⡀⠀⣄⣀⠐⡃⣠⠤⠀⡄⡰⡇⠀⢃⢀⣀⢋⢀⠁⠀⠃⢀⣇⠀⠀⠀⠀⠄⠀⠁⠀⠁⠀⣺⣤⣌⠀⠀⠖⠀⠗⠲⡇⠀⠄⠀
⣿⠆⠀⠀⠀⠀⢀⣴⡿⠥⠳⠀⡆⡁⠀⠀⢀⡤⣦⠁⠀⡁⠀⢐⢠⣤⣄⡀⣧⣟⣿⣥⣼⣷⣾⣶⣶⣴⣶⣦⣬⣁⠠⠀⠀⠀⠦⠀⠀⠀⠆⠀⠀⠘⠙⠁⠈⡄⠠⡅⠀⡂⠀⠈⠀
⣿⠀⠀⠀⠀⢸⠘⠻⠀⠀⠀⠀⠇⠀⢠⠀⠈⠁⢁⣤⣠⣅⣶⣾⣿⣷⣿⣿⣿⡿⡿⠿⡿⠿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣽⣲⡡⡀⠀⠄⠀⡄⠀⠀⠀⠀⠀⠃⠃⠀⠀⠀⠐⠀
⣟⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⢿⠉⣡⣾⣶⣾⣿⣷⣿⣿⣮⣦⢫⡟⢿⣿⣿⣿⣿⣿⣿⣷⣧⣤⣦⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀⠘⠀
⣿⣄⡐⠁⠀⠀⠀⠀⠀⠀⠀⣠⣶⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠎⢰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦⡷⣎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣏⣷⡄⣀⠀⡄⠀⠀⠀⠁⠀⠀⠀
⣿⡷⡜⡎⡘⠀⣠⢦⢄⣤⣽⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⣼⣿⣼⣉⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣺⠾⣵⢦⣀⠀⠀⠀⢀⠀
⣿⢺⠽⡇⣾⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢬⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢳⡿⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣿⣿⣜⣆⠀⠀⢰⠠
⡿⠈⡀⠁⠀⠀⠉⠉⠉⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⡆⠚⢿⣿⣿⣿⢿⣿⣿⠻⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣏⠟⠉⠉⠀⠖⠀⢀⠘
⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠻⡿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣭⣢⡏⠀⠀⠈⢠⣛⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⡺⠁⠀⠉⠀⠀⡀⠀⡄⠀⠨⠀
⣿⠃⠀⠀⠀⠀⢀⠀⡀⠀⠀⠀⡂⠁⠀⠀⠀⠀⢡⠂⠀⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⡟⠀⠙⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⢠
⣿⠈⠀⠀⠀⠀⠀⡄⠀⠀⡄⠀⠃⠀⠀⠀⠀⠒⠠⡄⠀⠀⠀⢲⢈⠀⠈⠀⠃⢋⠛⠙⢿⠿⢻⡿⠿⡿⠿⠿⢿⣟⠋⠏⠀⠀⠉⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢸
⣿⠃⠀⠀⠀⠀⠠⣖⠀⠀⠀⠀⡀⠂⠀⠀⠀⡀⠠⡅⠀⠀⠠⡼⠀⠈⠀⠀⠀⢸⡀⠀⠀⠀⠌⡒⠀⠀⠀⣄⣈⡎⠀⣠⠤⢤⠈⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠸
⣿⠁⠀⠀⠀⠋⠐⠀⠂⠀⠀⠀⠁⠀⠀⠀⠀⠁⢀⠃⠀⠀⠀⠀⡅⠀⠀⠀⠀⡡⠟⠛⡻⠀⠠⡕⠀⠀⠀⠁⢀⠾⠁⡙⠚⠻⣀⢀⡆⠀⠀⠀⠙⠀⠀⠀⠀⡃⠀⠀⠀⢀⠀⢰⣈
⡧⠆⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⡀⠀⠀⠂⠠⠀⠀⠀⠀⠡⠄⠀⠀⢀⠀⢒⡀⠀⠇⠀⢰⡐⠀⠁⠀⡁⠐⡠⠀⠀⠀⠠⠡⠀⡄⠀⠀⠈⠎⠀⠁⠀⠂⠀⠀⠆⠀⠂⠀⢸⢠
⡟⠄⠀⠀⠀⢀⠀⠀⠀⠀⠔⠀⠈⡀⢰⠀⠀⠀⠠⠅⠀⣇⣀⡼⠀⠰⠀⠀⠿⢂⡅⠀⠄⠀⢀⠇⠀⡀⠀⠁⢀⡧⠀⠀⠀⠀⠄⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⢸⠠
⡯⠀⠀⠀⠀⠀⠀⠁⠀⠀⠄⠀⠅⡀⡀⠀⠀⠀⢐⠃⠀⠀⠀⠂⡁⠀⠀⠀⠀⠌⠆⠀⠃⠀⢀⡋⠀⠀⠀⠁⠠⢀⠀⠀⠀⠀⠆⠀⡅⠀⠁⠀⠀⠀⠀⠀⠀⡆⠀⡀⠀⠆⠀⢰⣻
⡗⠂⠀⠀⠀⠠⠸⠠⡅⠀⠀⠀⢅⠀⠓⠀⠀⠀⡈⠤⠀⠀⠀⠰⠴⢴⠀⠀⠄⢊⡅⠀⢁⠀⡰⡱⠀⡀⠀⡄⠈⠄⠀⢀⠀⢠⠔⠂⠆⠀⠀⠀⠊⠀⠀⠀⠠⠇⠀⠄⠀⡤⠀⣲⣾
░███████                                      ░██████                                    
░██   ░██                                    ░██   ░██                                   
░██    ░██  ░███████   ░███████  ░████████  ░██          ░███████   ░██████   ░████████  
░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██  ░████████  ░██    ░██       ░██  ░██    ░██ 
░██    ░██ ░█████████ ░█████████ ░██    ░██         ░██ ░██         ░███████  ░██    ░██ 
░██   ░██  ░██        ░██        ░███   ░██  ░██   ░██  ░██    ░██ ░██   ░██  ░██    ░██ 
░███████    ░███████   ░███████  ░██░█████    ░██████    ░███████   ░█████░██ ░██    ░██ 
                                 ░██                                                     
                                 ░██                                                     
                                                                                         
Made by Pwimawy
"""

class DeepScan:
    def __init__(self):
        self.api_key = "sk-your-deepseek-api-key-here"
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        # Define vulnerability patterns to look for
        self.vulnerability_categories = {
            "sql_injection": "SQL Injection vulnerabilities",
            "xss": "Cross-Site Scripting (XSS) vulnerabilities",
            "command_injection": "Command Injection vulnerabilities",
            "path_traversal": "Path Traversal vulnerabilities",
            "auth_issues": "Authentication and Authorization issues",
            "sensitive_data": "Sensitive data exposure",
            "csrf": "CSRF vulnerabilities",
            "xxe": "XML External Entity (XXE) vulnerabilities",
            "deserialization": "Insecure deserialization",
            "buffer_overflow": "Buffer overflow risks"
        }

    def print_banner(self):
        print(BANNER)
        print("DeepScan - AI-Powered Vulnerability Scanner")
        print("=" * 50 + "\n")

    def read_file(self, file_path: str) -> str:
        """Read and return file content"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return ""

    def get_file_extension(self, file_path: str) -> str:
        """Get file extension for language-specific analysis"""
        return Path(file_path).suffix.lower()

    def generate_analysis_prompt(self, code: str, file_extension: str, filename: str) -> str:
        """Generate an analysis prompt for DeepSeek"""
        
        language_map = {
            '.php': 'PHP',
            '.html': 'HTML',
            '.js': 'JavaScript',
            '.java': 'Java',
            '.py': 'Python',
            '.c': 'C',
            '.cpp': 'C++',
            '.cs': 'C#',
            '.rb': 'Ruby',
            '.go': 'Go',
            '.rs': 'Rust'
        }
        
        language = language_map.get(file_extension, 'Unknown')
        
        prompt = f"""
        SECURITY CODE ANALYSIS REQUEST
        
        FILE: {filename}
        LANGUAGE: {language}
        
        Please perform a comprehensive security analysis of the following code. Look for these specific vulnerability types:
        
        1. SQL Injection
        2. Cross-Site Scripting (XSS)
        3. Command Injection
        4. Path Traversal
        5. Authentication/Authorization issues
        6. Sensitive data exposure
        7. CSRF vulnerabilities
        8. XXE vulnerabilities
        9. Insecure deserialization
        10. Buffer overflow risks
        11. Input validation issues
        12. Insecure cryptographic practices
        13. Security misconfigurations
        14. Insecure direct object references
        15. Server-side request forgery (SSRF)
        
        CODE TO ANALYZE:
        ```
        {code}
        ```
        
        Please provide your analysis in the following structured format:
        
        SECURITY ASSESSMENT:
        - Overall risk level: [Low/Medium/High/Critical]
        - Summary: [Brief overview of findings]
        
        VULNERABILITIES FOUND:
        [For each vulnerability found, provide:]
        - Type: [Vulnerability type]
        - Location: [Line numbers or code section]
        - Severity: [Low/Medium/High/Critical]
        - Description: [Detailed explanation]
        - Risk: [Potential impact]
        - Recommendation: [How to fix it]
        - Code snippet: [Relevant code section]
        
        SECURITY RECOMMENDATIONS:
        [List of general security improvements]
        
        If no vulnerabilities are found, please state that clearly.
        
        Be thorough and focus on practical, exploitable security issues.
        """
        
        return prompt

    def analyze_with_deepseek(self, prompt: str) -> str:
        """Send analysis request to DeepSeek API"""
        try:
            # Check if API key is still the default
            if self.api_key == "sk-your-deepseek-api-key-here":
                return "ERROR: Please update the API key in the script. Get your free API key from: https://platform.deepseek.com/api_keys"
            
            payload = {
                "model": "deepseek-coder",
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a senior security analyst with expertise in code security and vulnerability assessment. Provide detailed, accurate security analysis focusing on practical vulnerabilities."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "temperature": 0.1,
                "max_tokens": 4000
            }
            
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            return f"Error calling DeepSeek API: {e}"
        except KeyError as e:
            return f"Unexpected API response format: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"

    def scan_file(self, file_path: str) -> Dict[str, Any]:
        """Scan a single file for vulnerabilities"""
        print(f"🔍 Scanning: {file_path}")
        
        code = self.read_file(file_path)
        if not code:
            return {"error": f"Could not read file: {file_path}"}
        
        file_extension = self.get_file_extension(file_path)
        prompt = self.generate_analysis_prompt(code, file_extension, file_path)
        
        print("🤖 Analyzing with DeepSeek AI...")
        analysis_result = self.analyze_with_deepseek(prompt)
        
        return {
            "file_path": file_path,
            "analysis": analysis_result,
            "file_extension": file_extension
        }

    def scan_directory(self, directory: str) -> List[Dict[str, Any]]:
        """Scan all supported files in a directory recursively"""
        supported_extensions = {
            '.php', '.html', '.htm', '.js', '.java', '.py', 
            '.c', '.cpp', '.cs', '.rb', '.go', '.rs', '.ts',
            '.jsx', '.tsx', '.vue', '.asp', '.aspx', '.jsp'
        }
        
        results = []
        
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_ext = self.get_file_extension(file_path)
                
                if file_ext in supported_extensions:
                    result = self.scan_file(file_path)
                    results.append(result)
        
        return results

    def save_report(self, results: List[Dict[str, Any]], output_file: str = "deepscan_report.txt"):
        """Save scan results to a report file"""
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write("DEEPSCAN VULNERABILITY REPORT\n")
                f.write("Made by Pwimawy\n")
                f.write("=" * 80 + "\n\n")
                
                for result in results:
                    if "error" in result:
                        f.write(f"FILE: {result['file_path']}\n")
                        f.write(f"ERROR: {result['error']}\n")
                    else:
                        f.write(f"FILE: {result['file_path']}\n")
                        f.write(f"TYPE: {result['file_extension']}\n")
                        f.write("-" * 40 + "\n")
                        f.write(result['analysis'])
                        f.write("\n" + "=" * 80 + "\n\n")
            
            print(f"📄 Report saved to: {output_file}")
        except Exception as e:
            print(f"Error saving report: {e}")

    def print_analysis(self, result: Dict[str, Any]):
        """Print analysis results to console"""
        print("\n" + "=" * 80)
        print(f"SCAN RESULTS: {result['file_path']}")
        print("=" * 80)
        
        if "error" in result:
            print(f"ERROR: {result['error']}")
        else:
            print(result['analysis'])
        
        print("=" * 80)

def main():
    parser = argparse.ArgumentParser(description='DeepScan - AI-Powered Vulnerability Scanner')
    parser.add_argument('target', help='File or directory to scan')
    parser.add_argument('--output', '-o', help='Output report file (optional)')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    scanner = DeepScan()
    scanner.print_banner()
    
    # Check if API key needs to be updated
    if scanner.api_key == "sk-your-deepseek-api-key-here":
        print("⚠️  IMPORTANT: Please update the API key in the script!")
        print("Get your FREE DeepSeek API key from: https://platform.deepseek.com/api_keys")
        print("Then edit deepscan.py and replace 'sk-your-deepseek-api-key-here' with your actual API key")
        sys.exit(1)
    
    if not os.path.exists(args.target):
        print(f"❌ Error: Target '{args.target}' not found")
        sys.exit(1)
    
    if os.path.isfile(args.target):
        # Single file scan
        results = [scanner.scan_file(args.target)]
        scanner.print_analysis(results[0])
    elif os.path.isdir(args.target):
        # Directory scan
        print(f"📁 Scanning directory: {args.target}")
        results = scanner.scan_directory(args.target)
    else:
        print(f"❌ Error: Target '{args.target}' not found")
        sys.exit(1)
    
    # Save report if output specified
    if args.output:
        scanner.save_report(results, args.output)
    elif os.path.isdir(args.target):
        # Auto-save report for directory scans
        scanner.save_report(results)
    
    # Print summary
    print(f"\n✅ Scan completed!")
    print(f"📊 Files scanned: {len(results)}")
    if args.output or os.path.isdir(args.target):
        report_file = args.output if args.output else "deepscan_report.txt"
        print(f"💾 Report saved to: {report_file}")

if __name__ == "__main__":
    # Check if running without arguments
    if len(sys.argv) == 1:
        scanner = DeepScan()
        scanner.print_banner()
        print("Usage: python3 deepscan.py <file_or_directory>")
        print("\nExamples:")
        print("  python3 deepscan.py example.php")
        print("  python3 deepscan.py /path/to/code")
        print("  python3 deepscan.py /path/to/code -o custom_report.txt")
        print("\n⚠️  Remember to update the API key in the script first!")
        sys.exit(1)
    
    main()