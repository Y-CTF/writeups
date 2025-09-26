# YCTF Writeups

This repository contains CTF writeups from the YCTF hacking club. These writeups are included as a git submodule in the main website [repo](https://github.com/y-ctf/y-ctf.github.io).

## Repository Structure

```
.
├── <ctf-name>/
│   ├── _index.md                    # CTF overview page
│   └── <challenge-name>/
│       ├── index.md                 # Challenge writeup
│       └── files/                   # Associated files
│           ├── <exploit-files>
│           ├── <challenge-files>
│           └── ...
└── ...
```

## Authoring Writeups

### Frontmatter Format

Each writeup must include TOML frontmatter with the following structure:

```toml
+++
title = "Challenge Name"
date = 2021-01-01
description = "Brief description of the challenge" # Optional
authors = ["Author 1", "Author 2"] # Optional

[taxonomies]
categories = ["category"]
+++
```

### Content Guidelines

#### Markdown Features

The website supports extended markdown features:

- **Math rendering** using [`typst`](https://typst.app) syntax:
  ```markdown
  $
  lim_(x->oo) (1 + 1/x)^x = e
  $
  ```

- **Callouts** (Obsidian-style):
  ```markdown
  > [!NOTE]
  > This is a note

  > [!WARNING]
  > This is a warning
  ```

- **Code block injection** from files:
  ~~~markdown
  ```python include=files/solution.py
  ```
  ~~~

- **Copy button** for code blocks:
  ~~~markdown
  ```python copy
  print("Hello, world!")
  ```
  ~~~

#### File Organization

- Place all challenge-related files in the `files/` subdirectory
- Use descriptive filenames (e.g., `exploit.py`, `challenge.bin`, `solution.sage`)
- Include both challenge files and your solution files when relevant

#### Writing Style

- **Clear structure**: Use headings to organize your writeup
- **Explain the approach**: Don't just show the solution, explain your thought process
- **Include references**: Link to useful tools, techniques, or related writeups
- **Code comments**: Comment your exploit code for clarity

## Contributing

We want **YOUR** writeups! Don't be intimidated, every solve is worth sharing, whether you're a beginner or an expert.

### Adding New Writeups

1. **Create the directory structure**:
   ```bash
   mkdir -p <ctf-name>/<challenge-name>/files
   ```

2. **Create the CTF index file** (if it doesn't exist):
   ```toml
   # <ctf-name>/_index.md
   +++
   title = "CTF Name"
   transparent = true
   template = "ctf.html"
   +++
   ```

3. **Get started with your writeup** following the format guidelines above

4. **Add associated files** to the `files/` directory

5. **Test locally** by running the website development server

## Submodule Usage

This repository is designed to be used as a git submodule in the main website repository. The content structure is consumed by the [Zola](https://github.com/cestef/zola) static site generator.
