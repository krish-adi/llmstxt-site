# llmstxt-site

This is a centralized directory of all /llms.txt files available online. The /llms.txt file is a proposed standard for websites to provide concise and structured information to help large language models (LLMs) efficiently use website content during inference time.

**Contributions are the backbone of this repository’s success. Let’s work together to build a comprehensive resource for /llms.txt files and advance the adoption of this standard for LLM-friendly content!**

## Purpose

The purpose of this project is to:

-   Curate a comprehensive list of /llms.txt files from various websites.
-   Provide a platform for contributors to share and update /llms.txt resources.
-   Support the adoption of /llms.txt as a standard for providing LLM-friendly content.

## What is /llms.txt?

/llms.txt is a file located in the root path of a website that provides a brief overview of the website and its purpose, lists key Markdown files containing detailed information for LLMs, uses Markdown to ensure human and LLM readability, and offers a structured approach to provide context for LLMs, facilitating easier access to relevant information.

For more details on the /llms.txt proposal, see the background and proposal documentation [here](https://llmstxt.org/).

## Contributing

We welcome contributions to this repository to expand the collection of /llms.txt files. Follow these steps to contribute:

1. Fork the Repository to your GitHub account.

2. Edit the data.json file located in the root directory of this repository. Each entry in the JSON file should contain:

You can leave the tokens fields empty: they'll be calculated automatically when your PR is merged.

If you don't have a full-txt file, you can leave the `llms-full-txt` and `llms-full-txt-tokens` fields empty.

Here is an example entry:

```json
// ...
{
    "product": "Anthropic",
    "website": "https://anthropic.com/",
    "llms-full-txt": "https://docs.anthropic.com/llms-full.txt",
    "llms-full-txt-tokens": 313919,
    "llms-txt": "https://docs.anthropic.com/llms.txt",
    "llms-txt-tokens": 159282
},
// ...
```

3. Submit a Pull Request (PR) with your changes. Please include a small description of the changes and ensure all the entries are accurate and follow the format provided.
