# F5 Home Assignment - PyTest in GitLab CI/CD

Two PyTest tests for [the-internet.herokuapp.com/context_menu](https://the-internet.herokuapp.com/context_menu), run automatically by a GitLab CI/CD pipeline.

## Tests

- `test_instructions_text_is_on_page`: checks that the page contains "Right-click in the box below to see one called 'the-internet'". Expected to pass.
- `test_alibaba_is_on_page`: checks that the page contains "Alibaba". Expected to fail.

## Project structure

```
.gitlab-ci.yml        # CI/CD pipeline
requirements.txt      # pytest + requests
test_main.py          # the tests
```

## How it works

1. A `page` fixture downloads the page once and shares it with both tests.
2. Each test is a single `assert`: is the text in the page's HTML?
3. On every push, GitLab runs `pytest` inside a `python:3.14-slim` Docker container.

The pipeline ends as failed (1 passed, 1 failed). This is expected, because the second test is designed to fail.

## Run locally

```bash
pip install -r requirements.txt
pytest -v
```
