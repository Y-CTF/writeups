# YCTF Writeups

This repository contains CTF writeups from the YCTF hacking club. These writeups are included as a git submodule in the main website [repo](https://github.com/y-ctf/y-ctf.github.io).

## Repository Structure

```bash
.
├── <ctf-name>/
│   ├── _index.md                    # required by Zola
│   └── <challenge-name>/
│       ├── index.md                 # your writeup here
│       └── files/                   # associated files
│           ├── exploit.py
│           ├── challenge.bin
│           ├── screenshot.png
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
  ```
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

You are pretty much free to write however you want, but here are some tips:

- Start with a brief overview of the challenge
- Explain your thought process and approach
- Include code snippets and commands used
- Conclude with the final solution and any references you used / found helpful

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
