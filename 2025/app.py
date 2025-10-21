from flask import Flask, render_template
from pathlib import Path
import os
import json

app = Flask(__name__)

def load_snippets():
  snips_dir = Path("snippets")
  snippets = []
  for file in os.listdir(snips_dir):
    if file.endswith(".json"):
      with open(snips_dir / Path(file)) as f:
        snippets.append(json.load(f))
  return snippets
    

@app.route("/")
def index():
  snippets = load_snippets()
  return render_template("index.html", snippets=snippets)

@app.route("/snippet/<slug>.html")
def snippet(slug):
    path = os.path.join("snippets", f"{slug}.json")
    if not os.path.exists(path):
        return "Snippet not found", 404
    with open(path) as f:
        data = json.load(f)
    return render_template("snippet.html", snippet=data)

if __name__ == "__main__":
  app.run(debug=True)