"""
Corpus Ingestion Script:
Scans backend/app/data/corpus/ for documents, extracts metadata (effective_dates,
versions, superseding relationships), and populates vector index & catalog.
"""
import os
import json
from pathlib import Path

CORPUS_ROOT = Path(__file__).resolve().parent.parent / "backend" / "app" / "data" / "corpus"

def load_all_documents():
    print(f"Scanning corpus directory: {CORPUS_ROOT}")
    documents = []
    for json_file in CORPUS_ROOT.rglob("*.json"):
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            documents.append(data)
            print(f"Loaded: {data.get('id')} - {data.get('title')} (Effective: {data.get('effective_date')})")
    print(f"Total documents loaded: {len(documents)}")
    return documents

if __name__ == "__main__":
    load_all_documents()
