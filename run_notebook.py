"""Execute RAG_Assignment.ipynb top to bottom and save it with outputs.
The Gemini key is read with a hidden prompt (or from GEMINI_API_KEY) and only passed to the kernel's environment."""
import os, getpass, nbformat
from nbclient import NotebookClient
if "gemini" in open("RAG_Assignment.ipynb").read().split("LLM_BACKEND")[1][:60] and not os.environ.get("GEMINI_API_KEY"):
    os.environ["GEMINI_API_KEY"] = getpass.getpass("Paste your GEMINI_API_KEY (hidden): ").strip()
nb = nbformat.read("RAG_Assignment.ipynb", as_version=4)
NotebookClient(nb, timeout=1800, kernel_name="python3", resources={"metadata": {"path": "."}}).execute()
nbformat.write(nb, "RAG_Assignment.ipynb")
print("Done: RAG_Assignment.ipynb saved with outputs; tables in results/")
