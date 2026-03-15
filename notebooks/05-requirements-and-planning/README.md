# Chapter 5: AI-Assisted Requirements & Planning Notebook

This folder contains a runnable Jupyter Notebook demonstrating the concepts from **Chapter 5**, using the **GlobalBank Corporate Onboarding** case study.

## What's Inside

1. `chapter05_case_study.ipynb`: The main notebook. It uses `langchain` and OpenAI to demonstrate:
    - Stakeholder Discovery
    - Requirements Elicitation (EARS)
    - User Story Generation (CPFC)
    - Specification Analysis & Gap Detection
    - Epic Decomposition

2. `data/`: Contains mock input data used by the notebook:
    - `stakeholder_transcript.txt`: A transcribed kickoff meeting about the new onboarding platform.
    - `onboarding_epic.md`: A raw epic description for entity resolution.

## How to Run

1. Clone the repository and navigate to this folder.
2. Ensure you have Jupyter installed (`pip install jupyter`).
3. Launch the notebook: `jupyter notebook chapter05_case_study.ipynb`.
4. Run the first cell to install dependencies (`langchain`, `langchain-openai`).
5. You will be prompted to enter your `OPENAI_API_KEY`. The notebook is configured to use `gpt-4o-mini`.

*Note: You can easily swap the `ChatOpenAI` module for `ChatAnthropic` or `ChatBedrock` if you prefer to test with Claude or AWS models.*
