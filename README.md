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

Navigate to the `backend` directory and install the required Python packages:

```bash
cd backend
pip install -r requirements.txt
```

### Step 3: Set Up SWI-Prolog

Ensure SWI-Prolog is installed on your system. Test the installation by running:

```bash
swipl
```

### Step 4: Configure Gemini API

Create a `.env` file in the `backend` directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### Step 5: Run the Backend Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

### Step 6: Install Frontend Dependencies

Navigate to the `frontend` directory and install the dependencies:

```bash
cd ../frontend
npm install
```

### Step 7: Run the Frontend

Start the Svelte development server:

```bash
npm run dev
```

The frontend should now be accessible at `http://localhost:5000`.

## Usage

1. Open the frontend in your browser.
2. Input a natural language query (e.g., "What are three numbers that add up to 15?").
3. The query is processed by the backend:
   - Gemini converts it to Prolog syntax.
   - The Prolog engine evaluates the query.
   - The result is returned in natural language.
4. View the output directly on the frontend.

## Example Query

**Input:** "What are three numbers where the first is twice the second, the third is one less than the first, and their sum is 15?"

**Backend Process:**

- Gemini translates the query into Prolog rules.
- Prolog evaluates:
  ```prolog
  solve(X, Y, Z) :- X + Y + Z =:= 15, X =:= 2 * Y, Z =:= X - 1.
  ```
- Result: `X=8, Y=4, Z=7`

**Output:** "The three numbers are 8, 4, and 7."

## Testing

### Unit Tests

Run the unit tests for the backend:

```bash
pytest tests/
```

### Integration Tests

Ensure the frontend and backend are running. Test the complete pipeline by entering sample queries into the frontend.

## Future Enhancements

- Expand Prolog knowledge bases for domain-specific applications.
- Improve error handling for ambiguous or invalid queries.
- Add visualizations for Prolog logic and reasoning on the frontend.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Google Gemini API for NLP capabilities.
- PySwip library for Prolog integration.
- Svelte and FastAPI communities for their excellent frameworks.

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

Navigate to the `backend` directory and install the required Python packages:

```bash
cd backend
pip install -r requirements.txt
```

### Step 3: Set Up SWI-Prolog

Ensure SWI-Prolog is installed on your system. Test the installation by running:

```bash
swipl
```

### Step 4: Configure Gemini API

Create a `.env` file in the `backend` directory and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

### Step 5: Run the Backend Server

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

To run the code in terminal instead:
```bash
python main.py
```

### Step 6: Install Frontend Dependencies

Navigate to the `frontend` directory and install the dependencies:

```bash
cd ../frontend/svelte-frontend
npm install
```

### Step 7: Run the Frontend

Start the Svelte development server:

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
  ```

number(A, B, C, D) :-
digit(A), digit(B), digit(C), digit(D),
A > B, B > C, C > D,
D mod 2 =\= 0, % Rightmost digit not divisible by 2
A + B + C + D =:= 20,
(A =:= 4 _ B ; A =:= 4 _ C ; A =:= 4 _ D ;
B =:= 4 _ C ; B =:= 4 _ D ;
C =:= 4 _ D),
B - C > 3.

````
- Result: {'A': 9, 'B': 8, 'C': 2, 'D': 1}

**Output:** "The results are A = 9, B = 8, C = 2, and D = 1."

## Errors
- Gemini API only allows two queries per minute. Please wait after each query.
- If frontend or backend is not working, try running in terminal

## Future Enhancements

- Expand Prolog knowledge bases for domain-specific applications.
- Improve error handling for ambiguous or invalid queries.
- Add visualizations for Prolog logic and reasoning on the frontend.


