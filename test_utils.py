from utils import gemini_response_to_prolog


gemini_response = """```json
{
  "facts": [
    {"subject": "john", "predicate": "parent", "object": "mary"},
    {"subject": "john", "predicate": "parent", "object": "tom"},
    {"subject": "mary", "predicate": "parent", "object": "ann"},
    {"subject": "mary", "predicate": "parent", "object": "lily"},
    {"subject": "tom", "predicate": "parent", "object": "sam"}
  ],
  "rules": [
    {
      "head": "grandparent(X, Y)",
      "body": ["parent(X, Z)", "parent(Z, Y)"]
    },
    {
      "head": "aunt(X, Y)",
      "body": ["sibling(X, Z)", "parent(Z, Y)"]
    },
    {
      "head": "uncle(X, Y)",
      "body": ["sibling(X, Z)", "parent(Z, Y)"]
    },
    {
      "head": "cousin(X, Y)",
      "body": ["parent(A, X)", "parent(B, Y)", "sibling(A, B)"]
    }
  ],
  "query": "grandparent(X, mary)"
}
```"""


print(gemini_response_to_prolog(gemini_response))


# Sample JSON input
json_data = {
    "facts": [
        {"subject": "john", "predicate": "parent", "object": "mary"},
        {"subject": "john", "predicate": "parent", "object": "tom"},
        {"subject": "mary", "predicate": "parent", "object": "ann"},
        {"subject": "mary", "predicate": "parent", "object": "lily"},
        {"subject": "tom", "predicate": "parent", "object": "sam"}
    ],
    "rules": [
        {
            "head": "grandparent(X, Y)",
            "body": ["parent(X, Z)", "parent(Z, Y)"]
        },
        {
            "head": "sibling(X, Y)",
            "body": ["parent(Z, X)", "parent(Z, Y)", "X \\= Y"]
        },
        {
            "head": "aunt(X, Y)",
            "body": ["sibling(X, Z)", "parent(Z, Y)"]
        },
        {
            "head": "uncle(X, Y)",
            "body": ["sibling(X, Z)", "parent(Z, Y)"]
        },
        {
            "head": "cousin(X, Y)",
            "body": ["parent(A, X)", "parent(B, Y)", "sibling(A, B)"]
        }
    ]
}