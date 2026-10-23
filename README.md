# java-to-python-service

License: MIT

I'm building the Python foundation for
enterprise AI systems — and documenting the journey through a Java lens.

This is **Week 1 of a 10-week AI Architect roadmap** (Python → LLM systems → RAG → agents →
guardrails → LLMOps, on Azure and AWS), where every week ships one working project.

## What this repo is

Two things, both written for experienced Java developers who are new to Python:

1. **Python fundamentals, translated** — exercises in [`/exercises`](exercises/) that pair every
   Python concept with its Java equivalent (and call out where the translation *breaks*).
2. **A FastAPI microservice** — a small REST service of the kind you'd normally build with
   Spring Boot, rebuilt idiomatically in Python: Pydantic validation (the Bean Validation
   equivalent), async endpoints, pytest tests, and a Docker image.

## The Java → Python cheat table (grows all week)

| Concept | Java | Python |
|---|---|---|
| Build / dependency tool | Maven / Gradle (`pom.xml`) | **uv** (`pyproject.toml`) |
| Add a dependency | `<dependency>` in pom | `uv add fastapi` |
| Isolated environment | — (one classpath per app) | virtualenv, managed by uv |
| Web framework | Spring Boot | **FastAPI** |
| Request validation | Bean Validation (`@Valid`, `@NotNull`) | **Pydantic** models |
| Data class | `record` / Lombok `@Data` | `@dataclass` / Pydantic `BaseModel` |
| Streams / map-filter | `stream().map(...).filter(...)` | comprehensions: `[f(x) for x in xs if p(x)]` |
| try-with-resources | `try (var r = ...)` | `with ... as r:` (context manager) |
| Annotation / AOP | `@Transactional`, custom annotations | decorators: `@decorator` |
| Unit tests | JUnit | **pytest** |
| Optional | `Optional<T>` | `T \| None` |
| Entry point | `public static void main` | `if __name__ == "__main__":` |

## Run it

Prerequisites: Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                 # install dependencies (creates the project environment)
uv run fastapi dev app/main.py   # start the service (Swagger UI at /docs)
uv run pytest           # run the test suite
docker build -t java-to-python-service . && docker run -p 8000:8000 java-to-python-service
```

## Project layout

```
exercises/     Python fundamentals, each file paired with Java notes
app/           The FastAPI service (endpoints, Pydantic models)
tests/         pytest suite
Dockerfile     Container image for the service
```

## Week 1 learning log

- **Day 1** — Setup (Python, VS Code, uv, this repo); variables, data types, strings
- **Day 2** — Lists/dicts/sets, comprehensions, functions with type hints
- **Day 3** — Classes the Python way, decorators, context managers; FastAPI basics
- **Day 4** — FastAPI + Pydantic service build
- **Day 5** — Async endpoints + pytest
- **Day 6** — Docker, this README, portfolio write-up
- **Day 7** — Review 

## Why Python, why now

The enterprise AI stack — LLM APIs, RAG, agents, evaluation — is Python-first. Architecture
judgment transfers; the implementation language had to change. This repo is the evidence.

*Part of a 10-week build-in-public series — follow along on LinkedIn.*
