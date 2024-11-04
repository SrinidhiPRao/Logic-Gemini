<script>
  let query = '';
  let response = '';

  async function submitQuery() {
      try {
          const res = await fetch("http://127.0.0.1:8000/query", {
              method: "POST",
              headers: {
                  "Content-Type": "application/json",
              },
              body: JSON.stringify({ query })
          });
          const data = await res.json();
          response = data.response;
      } catch (error) {
          response = "Error connecting to the backend.";
          console.error("Error:", error);
      }
  }
</script>

<main>
  <h1>Query Interface</h1>

  <label for="query">Enter your query:</label>
  <input
      type="text"
      id="query"
      bind:value={query}
      placeholder="Type a question..."
  />
  <button on:click={submitQuery}>Submit</button>

  <h2>Response:</h2>
  <p>{response}</p>
</main>

<style>
  main {
      font-family: Arial, sans-serif;
      max-width: 500px;
      margin: 0 auto;
      padding: 2rem;
      text-align: center;
  }
  label, input, button, h1, h2, p {
      display: block;
      margin-bottom: 1rem;
  }
  input {
      width: 100%;
      padding: 0.5rem;
      font-size: 1rem;
  }
  button {
      padding: 0.5rem 1rem;
      font-size: 1rem;
      cursor: pointer;
  }
</style>
