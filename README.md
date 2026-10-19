# RAG: Baseline (Bi-Encoder) vs. Re-Ranking (Cross-Encoder)

CL3410 Language Models and Agents, RAG assignment.

Two retrieval pipelines run over the same chunked corpus, the
*ICD-10-CM Official Guidelines for Coding and Reporting FY2026* (CMS/NCHS, public domain):

- **Pipeline 1:** `all-MiniLM-L6-v2` bi-encoder, cosine top-10, top-3 go to the LLM (Answer 1)
- **Pipeline 2:** the same top-10, re-scored by `cross-encoder/ms-marco-MiniLM-L-6-v2`, top-3 go to the LLM with the same prompt (Answer 2)

Everything is in **[`RAG_Assignment.ipynb`](RAG_Assignment.ipynb)**, saved with its outputs.

## Files

| Path | What it is |
|---|---|
| `RAG_Assignment.ipynb` | Full pipeline, failure-query scan, rank shifts, LLM answers, latency and scaling |
| `icd_10_cm_october_2025_guidelines_0.pdf` | Source document |
| `results/rank_shifts.csv` | Gold-chunk rank before and after re-ranking for each test query |
| `results/answers.md` | Answer 1 vs Answer 2 for each test query, with the expected answer |
| `results/answer_judgements.csv` | Each answer judged Correct / Partial / Wrong / No answer |
| `results/latency.csv` | Baseline vs re-rank latency (mean / std / p95) |
| `results/scaling.csv` | Cross-encoder cost per pair as N grows |
| `llm_cache.json` | Cached LLM responses, so a re-run gives the same answers without API calls |

## Running it

```bash
pip install -r requirements.txt
jupyter notebook RAG_Assignment.ipynb
```

The LLM is a local Qwen2.5-7B-Instruct (4-bit, MLX, Apple silicon); no API key is needed. Answers are cached in `llm_cache.json`.
`python run_notebook.py` runs the whole notebook headless and saves the outputs in place.
