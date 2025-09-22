# Sword EU AI Act – Colab POC

This repo contains a free, no-install Proof of Concept to process the EU AI Act Excel workbook in **Google Colab**.

## What you get
- **Colab notebook** (`colab_ai_act_poc.ipynb`) – upload your Excel and get a Risk Classification preview.
- **Python helper** (`ai_act_loader.py`) – utilities to read the key sheets safely.
- **requirements.txt** – dependencies for local runs (optional).

## Quick start (Colab)
1. Open Google Colab.
2. Upload `colab_ai_act_poc.ipynb`.
3. Run the first cell to upload your Excel workbook.
4. The notebook will print sheet names and show preview tables for:
   - `Entity Demographics`
   - `Systems Description`
   - `Systems Verification`

> This is a POC: it **does not** replicate all rules yet. It demonstrates a safe, repeatable pipeline for reading your workbook end-to-end.
