# TimesJobs Web Scraper 🚀

A Python-based web scraping tool that automatically searches for Python developer jobs on TimesJobs.com and filters them based on your skill preferences.

## 📋 Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Output Format](#output-format)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- **Automated Job Scraping**: Continuously scrapes Python job postings from TimesJobs.com
- **Smart Filtering**: Filters out jobs that require skills you're not familiar with
- **Fresh Job Posts**: Only saves jobs posted more than "a few hours ago" or "today" (focuses on older, more stable postings)
- **Detailed Information**: Extracts company name, required skills, experience level, posting time, and job links
- **Continuous Monitoring**: Runs in a loop, checking for new jobs every 10 minutes
- **Local Storage**: Saves each job posting as a separate text file for easy review

## 🔧 How It Works

1. **User Input**: Prompts you to enter a skill you're not familiar with (e.g., "Django", "React", "Node.js")
2. **Web Scraping**: Fetches job listings from TimesJobs mobile site using Python keywords
3. **Data Extraction**: Parses HTML to extract:
   - Company name
   - Required skills
   - Experience level
   - Posting time
   - Job details link
4. **Smart Filtering**: 
   - Excludes very recent posts ("few hours ago", "today")
   - Filters out jobs requiring your unfamiliar skill
5. **Data Storage**: Saves qualifying jobs as numbered text files in the `posts/` directory
6. **Continuous Loop**: Waits 10 minutes and repeats the process

## 🚀 Installation

### Prerequisites

Make sure you have Python 3.6+ installed on your system.

### Clone the Repository

```bash
git clone https://github.com/falcon0124/WebScrape_timesJov.git
cd WebScrape_timesJov
```

### Install Required Packages

```bash
pip install beautifulsoup4 requests lxml
```

## 🎯 Usage

1. **Run the Script**:
   ```bash
   python main.py
   ```

2. **Enter Your Unfamiliar Skill**:
   ```
   Put skill you are not familiar with: 
   > django
   ```

3. **Monitor the Output**:
   The script will display messages like:
   ```
   You are not familiar with "django"
   Job post saved to posts/1.txt
   Job post saved to posts/5.txt
   Job post saved to posts/7.txt
   Waiting for 10 minutes before the next search...
   ```

4. **Stop the Script**:
   Press `Ctrl+C` to stop the continuous monitoring

## 📄 Output Format

Each job posting is saved as a numbered text file in the `posts/` directory with the following format:

```
company: IQVIA
skills: full stack development, python programming, scalable architecture, data processing pipelines, cloud platforms, c, orchestration, docker, sql, security, git, system architecture
experience: 3 - 6  Years
posting time: 2 days ago
more info: https://m.timesjobs.com/mobile/job-detail/python-developer-iqvia-bengaluru-bangalore-3-to-6-yrs-jobid-2DFKS0eGVfxzpSvf__PLUS__uAgZw==&bc=+&sequence=2
```

## 📁 Project Structure

```
WebScrape_timesJov/
│
├── main.py           # Main scraping script
├── posts/            # Directory containing scraped job data
│   ├── 0.txt
│   ├── 1.txt
│   ├── 5.txt
│   └── ...
└── README.md         # Project documentation
```

## 📦 Requirements

- **Python 3.6+**
- **beautifulsoup4**: For HTML parsing
- **requests**: For making HTTP requests
- **lxml**: XML and HTML parser (used by BeautifulSoup)
- **time**: For delays between requests (built-in)
- **os**: For file operations (built-in)

### Install all dependencies:

```bash
pip install beautifulsoup4 requests lxml
```

## ⚙️ Configuration

You can modify the following parameters in `main.py`:

- **Search Keywords**: Change the URL to search for different skills
- **Wait Time**: Modify `time_wait = 10` to change the interval between searches (in minutes)
- **Posting Time Filters**: Adjust the conditions in the posting time filter
- **Output Format**: Customize the information saved to each file

## 🎯 Use Cases

- **Job Market Research**: Analyze trends in Python job requirements
- **Skill Gap Analysis**: Identify commonly required skills you might want to learn
- **Automated Job Monitoring**: Stay updated on new opportunities without manual searching
- **Recruitment Analysis**: Study job posting patterns and requirements

## ⚠️ Important Notes

- **Rate Limiting**: The script includes a 10-minute delay between requests to be respectful to the server
- **Mobile Site**: Uses TimesJobs mobile site for better parsing reliability
- **Encoding**: Saves files with UTF-8 encoding to handle special characters
- **Error Handling**: Includes basic error handling for missing HTML elements

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📧 Contact

**Falcon0124** - [GitHub Profile](https://github.com/falcon0124)

Project Link: [https://github.com/falcon0124/WebScrape_timesJov](https://github.com/falcon0124/WebScrape_timesJov)

---

**⭐ Star this repository if you find it helpful!**
