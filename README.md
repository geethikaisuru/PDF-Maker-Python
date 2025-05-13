# PDF Maker using CSV 📄

This is a simple Python script that takes data from a CSV file and generates a formatted PDF document using the `FPDF` library. It reads topics from the CSV file and creates a PDF with each topic placed on a new page. The script also handles page numbers and custom footers for each page.

## Features ⚙️
- **Reads data from CSV**: The script processes topics from a CSV file where each row represents a topic and the number of pages it spans.
- **Generates PDF**: It generates a professional-looking PDF with custom headers and footers.
- **Customizable**: The layout can be easily adjusted by modifying the code, such as adding more styling, adjusting fonts, or spacing.
- **Simple to use**: Just place your `topics.csv` file in the same directory and run the script to create your PDF.

## Requirements 🛠
- Python 3.x
- `fpdf` library (Install via `pip install fpdf`)
- `pandas` library (Install via `pip install pandas`)

## Usage 🚀
1. Place your CSV file (named `topics.csv`) in the same directory as the script.
2. The CSV should contain the following columns:
    - `Topic`: The title of the topic.
    - `Pages`: The number of pages dedicated to that topic.
3. Run the script to generate `output.pdf`.

## Example CSV Format 📝

| Topic            | Pages |
|------------------|-------|
| Machine Learning | 5     |
| AI Algorithms    | 3     |
| Data Science     | 4     |

## Output 📑
The output will be a well-structured PDF with each topic displayed on its own page, followed by additional pages as specified in the CSV.

---

👨‍💻 About the Creator  
Hi! I'm Geethika Isuru, an AI Engineer & Entrepreneur who's trying to make a better world with AI.  
💼 LinkedIn Profile: [Geethika LinkedIn](https://www.linkedin.com/in/geethikaisuru/)  
📂 GitHub Profile: [Geethika GitHub](https://github.com/geethikaisuru)  
🛜 Website: [Geethika Website](https://geethikaisuru.me/)
