# Monthly report generator

Fetches PRs merged given month and generates the report based on the
[`template.html`](./template.html).

Usage:

```shell
python3 main.py <YEAR-MONTH>
```

for example `python3 main.py 2024-05`.

The report will be printed on standard output as HTML and ready for
copy&pasting it to Google docs or other text processing app.

Features:
- PR report:
  - fetches PRs and orders them based on the importance
  - the importance is computed based on the diff lines of code not considering
    go.sum, .svg, yarn.lock, Cargo.lock and similar files.
  - fetches both releases and tags published that month

If you encounter `403` rate limiting error on github, create Personal Access
token and export it as the `API_KEY` env variable before executing the report
generator.