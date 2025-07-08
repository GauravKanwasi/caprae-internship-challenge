# Caprae Lead Generator 🚀  
A tool to filter, visualize, and export high-quality SaaS/M&A leads from personal data.

---

## 📋 Table of Contents  
| Section | Description |  
|---------|-------------|  
| [About](#about) | Project summary and goals |  
| [Features](#features) | Key functionalities and enhancements |  
| [Installation](#installation) | Setup instructions |  
| [Usage](#usage) | How to run the app and use filters |  
| [File Structure](#file-structure) | Project organization |  
| [Evaluation Criteria Alignment](#evaluation-criteria-alignment) | How this meets Caprae’s requirements |  
| [Screenshots](#screenshots) | Visual examples of the UI |  
| [Contributing](#contributing) | Guidelines for contributions |  
| [License](#license) | MIT License |  
| [Contact](#contact) | Reach out for questions |

---

## 🔍 About  
This tool transforms raw personal data into actionable SaaS/M&A leads by:  
- **Mapping job titles to industries** (e.g., "Biomedical Engineer" → "HealthTech")  
- **Calculating age** from DOB for demographic insights  
- **Visualizing industry distribution and age trends**  
- **Exporting filtered leads** to CSV/Excel  

**Built with**:  
- **Streamlit** for interactive UI  
- **Pandas** for data manipulation  
- **Seaborn/Matplotlib** for visualizations  

---

## 🧠 Features  
| Feature | Description |  
|--------|-------------|  
| **Industry Mapping** | Maps job titles to SaaS/M&A-relevant industries (e.g., "Data Scientist" → "SaaS") |  
| **Age Calculation** | Derives age dynamically from DOB [[3]](https://github.com/GauravKanwasi/caprae-internship-challenge/blob/main/scraper/data_enrichment.py#L58) |  
| **Visualizations** | Interactive charts for industry distribution and age insights [[4]]( https://github.com/GauravKanwasi/caprae-internship-challenge/blob/main/app/app.py#L63) |  
| **Export Options** | Export filtered leads to CSV/Excel for CRM integration [[5]]( https://github.com/GauravKanwasi/caprae-internship-challenge/blob/main/app/app.py#L94) |  
| **Dark Mode** | Enhanced readability with `.streamlit/config.toml` [[6]]( https://github.com/GauravKanwasi/caprae-internship-challenge/blob/main/.streamlit/config.toml ) |  

---

## 🛠️ Installation  
### Prerequisites  
- Python 3.8+  
- Streamlit, Pandas, Matplotlib, Seaborn, XlsxWriter  

### Steps  
```bash
# Clone the repo  
git clone https://github.com/GauravKanwasi/caprae-internship-challenge.git   
cd caprae-internship-challenge  

# Install dependencies  
pip install -r requirements.txt  


# Generate enriched leads with age calculation  
cd scraper  
python data_enrichment.py  
