# pdf_to_audio

## PDF Summarization and Text-to-Speech

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
## Introduction
This Python script converts a PDF document into an audio summary. It utilizes various libraries to achieve this, including text extraction from PDF files and text summarization using OpenAI's ai model.

## Features

- Extract text from a PDF document.
- Split the extracted text into manageable chunks.
- Generate concise summaries of each text chunk using OpenAI's ai model.
- Convert the generated summaries into speech using text-to-speech technology.

## Dependencies

Before running the script, make sure to install the following Python libraries:

- `PyPDF2`: Used for extracting text from PDF files.
- `openai`  Utilized for text summarization.(davinci)
- `pyttsx3`: Used for text-to-speech conversion.


## Author
- Name: `cython boy`
- Gmail:`gaenshnikhil124@gmail.com`

## Prerequisites
  #python verson >= 3.10
  
## Dependencis
You can install these libraries using `pip`:
```bash
pip install -r requirements.txt
python3 main.py 


