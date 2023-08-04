# Text Summarization

This uses Neural Language Processing (NLP) library - SpaCy - to perform text summarization. It will read the content of a file that is called `text.txt`, processes it, and then prints the outcome.

## Prerequisites
- Python 3.10
- SpaCy
- en_core_web_sm model for SpaCy

## Installation
1. Install the required packages from `requirements.txt` mentioned in Prerequisites.
2. Download the `en_core_web_sm` model using the following command:
python -m spacy download en_core_web_sm```

## Usage
1. Place the text that you would like to summarize into a file called `text.txt`. The file should be in the same directory as the main script.
2. Execute the script, and within a couple of seconds, the summarized text will be printed in the terminal.

## Example output from exmaple input
```
Artificial Intelligence (AI) is the simulation of human intelligence in machines, enabling them to perform tasks that typically require human cognitive abilities, such as learning, problem-solving, decision-making, and perception.
```

### Notes
The original source code can be found at:
- [GitHub Repository](https://github.com/anoopsingh1996/Text_Summarization/tree/master)
- [Medium Article](https://medium.com/analytics-vidhya/text-summarization-using-nlp-3e85ad0c6349)
