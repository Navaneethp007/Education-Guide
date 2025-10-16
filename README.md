# Education Guide

A command-line application that generates tailored educational roadmaps based on user input, using CrewAI and DeepSeek-R1 8B to orchestrate AI agents for parsing, researching, curriculum design, project suggestions, and output formatting.

## Features

- **Dynamic Input**: Users enter learning goals (e.g., "Learn Python for AI development as a beginner") via a command-line prompt.
- **Multi-Agent System**: Five AI agents powered by DeepSeek-R1 8B:
   - **Input Analyst**: Parses input into topic, level, and goal.
   - **Researcher**: Finds free online resources using DuckDuckGo Search.
   - **Curriculum Designer**: Creates a 4-week learning path.
   - **Project Idea Generator**: Suggests beginner-friendly projects.
   - **Formatter**: Outputs results as a markdown file (learning_path.md).
- **Fully Local**: Runs DeepSeek-R1 8B (~4-5 GB) via Ollama, requiring no external APIs or costs.

## Architecture

- **Main Script**: (`app.py`) orchestrates the workflow using CrewAI.
- **AI Model**: DeepSeek-R1 8B, hosted locally via Ollama for efficient inference.
- **Key Libraries**:
  - `crewai`: Manages multi-agent collaboration.
  - `langchain_ollama`: Interfaces with DeepSeek-R1 8B.
  - `langchain_community`:  Provides DuckDuckGo Search tool for resource discovery.
 



