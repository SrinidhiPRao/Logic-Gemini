# Logic-Gemini: Augmenting Logical Reasoning with Natural Language Processing

## Introduction

Large Language Models (LLMs) like Google Gemini excel in natural language processing and code generation, but they struggle with complex logic and reasoning tasks. This project bridges that gap by integrating Gemini's NLP capabilities with Prolog’s powerful logical reasoning capabilities. Users can input natural language queries, which are translated into Prolog code, executed for logical problem-solving, and returned as understandable responses.

## Features

1. **Natural Language to Prolog Conversion**
   - Translates user queries into Prolog facts, rules, and queries via Gemini API.
2. **Prolog Logic Engine**
   - Processes and solves logical problems using Prolog's deductive reasoning.
3. **FastAPI Backend**
   - Handles API requests and integrates Prolog and Gemini functionality.
4. **Svelte Frontend**
   - Provides a clean and user-friendly interface for input and output.
5. **Seamless End-to-End Pipeline**
   - Connects all components to enable natural language query handling.

## Tech Stack

- **Google Gemini API**: For natural language processing.
- **Python**: For backend logic and Gemini API integration.
- **PySwip**: For interfacing with the Prolog logic engine.
- **Prolog**: For logical reasoning and query execution.
- **FastAPI**: For creating RESTful API endpoints.
- **Svelte**: For building the frontend interface.

## Installation Instructions

### Prerequisites

Ensure the following are installed on your system:

- Python 3.8+
- SWI-Prolog
- Node.js (for the Svelte frontend)

### Step 1: Clone the Repository

```bash
git clone https://github.com/SrinidhiPRao/Logic-Gemini.git
cd Logic-Gemini
```

### Step 2: Install Backend Dependencies

Install the required Python packages:

```bash

pip install -r requirements.txt
```

### Step 3: Set Up SWI-Prolog

Ensure SWI-Prolog is installed on your system. Test the installation by running:

```bash
swipl
```
Or download from https://www.swi-prolog.org/

### Step 4: Configure Gemini API

Create a `.env` file in the directory if it doesn't exist already and add your Gemini API key:

```
API_KEY=your_api_key_here
```
Or follow the steps in [Gemini API Docs](https://ai.google.dev/gemini-api/docs/api-key) to get an API Key.

### Step 5: Run the Backend Server

Start the FastAPI server:

```bash
fastapi dev server.py
```

### Step 6: Install Frontend Dependencies

Navigate to the `frontend` directory and install the dependencies:

```bash
cd .\frontend\svelte-frontend\
npm install
```

### Step 7: Run the Frontend

Start the Svelte server:

```bash
npm run dev
```

The frontend should now be accessible at `http://localhost:5173`.

## Usage

1. Open the frontend in your browser.
2. Input a natural language query (e.g., "What are three numbers that add up to 15?").
3. The query is processed by the backend:
   - Gemini converts it to Prolog syntax.
   - The Prolog engine evaluates the query.
   - The result is returned in natural language.
4. View the output directly on the frontend.

## Example Query

**Input:** "I am a 4 digit number. My rightmost digit is not divisible by 2. The sum of my digits is 20, and all my digits are in strictly decreasing order from left to right. One of my digits is 4 times one of my other digits, and the difference between my 2 middle digits is more than 3. What number am I?"

**Backend Process:**

- Gemini translates the query into Prolog rules.
- Prolog evaluates:
  ```prolog
   digit(0).
   digit(1).
   digit(2).
   digit(3).
   digit(4).
   digit(5).
   digit(6).
   digit(7).
   digit(8).
   digit(9).

   number(A, B, C, D) :-
    digit(A), digit(B), digit(C), digit(D),
    A > B, B > C, C > D,
    D mod 2 =\= 0,
    A + B + C + D =:= 20,
    (A =:= 4 * B ; A =:= 4 * C ; A =:= 4 * D ;
     B =:= 4 * C ; B =:= 4 * D ;
     C =:= 4 * D),
    B - C > 3.

  ```
**Output:** "The results are 9, 8, 2, and 1."
