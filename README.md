# AI Requirements Analyzer using LangChain LCEL

## Overview

This project implements an intelligent software requirements analysis system using **LangChain Expression Language (LCEL)**.

The system is designed for a technology consulting company where clients submit software ideas as unstructured text. The application processes the client's project description through a multi-stage prompt chain to analyze the request, classify the project, identify missing requirements, and generate an initial project assessment.

The workflow follows:

---

## Features

The application performs five sequential analysis stages:

### 1. Interpret Project Request
Analyzes the client's description to identify:

- Business objective
- Problem being solved
- Requested solution
- Project summary

---

### 2. Identify Possible Project Categories

Suggests possible categories from the available options:

- Web Application
- Mobile Application
- API / Backend Service
- Data Analytics Platform
- AI / Machine Learning System
- E-Commerce Platform
- Enterprise Management System
- System Integration
- DevOps / Infrastructure Automation
- General Software Project

---

### 3. Select Best Category

Uses the previous analysis to select the most appropriate project category.

---

### 4. Extract Missing Requirements

Identifies important information required before development begins, including:

- Target users
- Platform requirements
- Authentication requirements
- Integration requirements
- Data storage requirements
- Security requirements
- Performance requirements
- Scalability requirements

---

### 5. Generate Initial Assessment

Produces a final project assessment containing:

- Selected category
- Summary of client request
- Missing information
- Recommended next steps

---

# Technology Stack

- Python
- LangChain
- LangChain Expression Language (LCEL)
- OpenRouter API
- Python-dotenv

---

# Project Structure
AI-Requirements-Analyzer

│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
│
└── prompts
├── prompt1_interpret_request.txt
├── prompt2_identify_categories.txt
├── prompt3_select_category.txt
├── prompt4_extract_missing_requirements.txt
└── prompt5_generate_assessment.txt
---

# Installation

Clone the repository:

```bash
git clone <repository-url>

Navigate into the project:
cd AI-Requirements-Analyzer

Create a virtual environment:
python -m venv venv

Activate the environment:
venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Environment Configuration

Create a .env file in the same directory as main.py.

Add:

OPENROUTER_API_KEY=your_api_key
MODEL_NAME=your_model_name

Example:

OPENROUTER_API_KEY=sk-or-xxxxxxxx
MODEL_NAME=openai/gpt-4o-mini

The .env file should not be committed to GitHub.

Running the Application

The application accepts the client project description as a command-line argument.

Example:

python main.py "I want to build an AI chatbot for customer support using company documents"

The system will display:

STAGE 1
Project interpretation

STAGE 2
Possible categories

STAGE 3
Selected category

STAGE 4
Missing requirements

FINAL PROJECT ASSESSMENT
Complete project analysis
LCEL Implementation

The application uses LangChain Expression Language composition:

prompt | llm | output_parser

Each stage is implemented as an independent LCEL chain:

Prompt Template
        |
        v
        LLM
        |
        v
String Output Parser

The output from each stage is passed into the next stage, creating a sequential reasoning workflow.

Security

Sensitive information such as API keys is stored using environment variables.

The following files are excluded from version control:

.env
venv/
__pycache__/
Author

Developed as part of the KodeCamp AI for Developers Task 3:
Prompt Chaining using LangChain LCEL


After creating it, save with:

```text
Ctrl + S