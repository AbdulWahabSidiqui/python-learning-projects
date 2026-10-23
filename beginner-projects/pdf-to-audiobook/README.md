# PDF to Audiobook 🎧

A simple Python command-line application that extracts text from a PDF file and converts it into an audiobook using text-to-speech.

## 📌 About the Project

This project takes a PDF file provided by the user, extracts the text from its pages, and converts the extracted text into speech.

The audiobook is saved as an MP3 file that can be played using any standard audio player.

This project was created as part of my Python learning journey and portfolio projects.

## ✨ Features

* 📄 Accepts a PDF file path from the user
* 📖 Extracts text from all PDF pages
* 🗣️ Converts extracted text into speech
* 🎙️ Supports available system voices through `pyttsx3`
* ⚡ Allows control over speaking speed
* 🔊 Allows control over speech volume
* 🎧 Saves the generated audiobook as an MP3 file
* 💻 Runs directly from the command line

## 🛠️ Technologies Used

* **Python**
* **pypdf** — PDF text extraction
* **pyttsx3** — Text-to-speech conversion

## 📂 Project Structure

```text
PDF_to_Audiobook/
│
├── main.py
├── sample.pdf
├── requirements.txt
├── README.md
└── output/
    └── audiobook.mp3
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-to-audiobook.git
```

### 2. Navigate to the project directory

```bash
cd pdf-to-audiobook
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

## ▶️ How to Use

Run the program:

```bash
python main.py
```

The program will ask for the path of the PDF file:

```text
Enter the path of the pdf file:
```

Enter the path to your PDF file, for example:

```text
C:\Users\YourName\Documents\book.pdf
```

The program will extract the text and convert it into speech.

The generated audiobook will be saved as:

```text
audiobook.mp3
```

## 🔊 Voice and Speed

The project uses `pyttsx3`, which allows the program to use voices installed on the user's computer.

The speaking speed can be controlled using:

```python
engine.setProperty("rate", 180)
```

The volume can be controlled using:

```python
engine.setProperty("volume", 1.0)
```

Available voices can be accessed through:

```python
voices = engine.getProperty("voices")
```

## 📚 What I Learned

Through this project, I practiced:

* Working with PDF files in Python
* Extracting text from documents
* Using third-party Python libraries
* Working with text-to-speech technology
* Handling file paths
* Creating reusable functions
* Working with Python virtual environments
* Building command-line applications

## 🚀 Future Improvements

Possible improvements for future versions include:

* Add progress indicators while processing the PDF
* Automatically create an `output` directory
* Generate an output filename based on the PDF name
* Add better error handling
* Allow users to select from available voices
* Allow users to choose speaking speed from the command line
* Support large PDFs by processing them in smaller sections
* Add a graphical user interface in a future version

## 👨‍💻 Author

**Abdul Wahab Sidiqui**

This project is part of my journey toward becoming a **Data Scientist / Machine Learning Engineer** and building a practical Python portfolio.

## 📄 License

This project is for educational and portfolio purposes.
