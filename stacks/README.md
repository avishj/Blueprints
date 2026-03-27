# Stacks

Each stack is a [Copier](https://copier.readthedocs.io/) template. Scaffold a new project with:

```bash
git clone https://github.com/avishj/blueprints /tmp/blueprints
uvx copier copy /tmp/blueprints/stacks/<stack-name> my-project --trust
rm -rf /tmp/blueprints
```

Supported:

- [python-cli](./python-cli/): CLI tools, scripts and command-line applications built with Python.
- [ts-astro-react](./ts-astro-react/): Content-driven websites and apps using Astro with React islands and TypeScript.
