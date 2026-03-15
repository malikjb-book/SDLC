# Chapter 6: AI-Powered Design & Architecture Notebook

This directory contains a runnable Jupyter Notebook demonstrating the concepts from **Chapter 6**, using the **GlobalBank Corporate Onboarding** case study.

## What's Inside

1. `chapter06_architecture.ipynb`: The main notebook. It uses the raw `openai` Python SDK to demonstrate:
    - AI-Assisted Architecture Exploration (Trade-off Matrices)
    - Design Document Generation (ADR generation from a PR context)
    - Automated Diagramming (Mermaid C4 Container generation)
    - API Design (OpenAPI 3.1 YAML generation from requirements)
    - Data Modeling (Entity-Relationship generation and SQL migrations)

2. `data/`: Contains mock input data used by the notebook:
    - `system_context.txt`: System constraints for the Corporate Onboarding platform.
    - `event_broker_pr.txt`: A mock PR discussion weighing message broker options.
    - `api_requirements.txt`: The backend contract requirements for a Risk Decisioning API.
    - `data_model_reqs.txt`: Data tracking requirements for corporate entities and AML screening over time.

## How to Run

1. Clone the repository and navigate to this folder.
2. Ensure you have Jupyter and the OpenAI SDK installed (`pip install jupyter openai`).
3. Launch the notebook: `jupyter notebook chapter06_architecture.ipynb`.
4. Run the first cell to load your dependencies.
5. You will be prompted to enter your `OPENAI_API_KEY`. The notebook is configured to use `gpt-4o-mini`.
