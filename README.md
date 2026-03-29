# Dario Bellicoso - Personal Website

This repository contains the source code for my personal academic and research portfolio, built using the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## 🚀 How to preview locally

If you want to preview your changes before pushing them live, you can build and serve the website locally.

**Prerequisites:** You need to have a modern user-space Ruby (via `rbenv`) and Node.js installed.

> [!WARNING]
> **Apple Silicon (M1/M2/M3) Mac Users:** DO NOT use the default macOS System Ruby (it will throw `GemNotFoundException` permission errors). Instead, install a modern user-space Ruby using [Homebrew](https://brew.sh/):
> ```bash
> # 1. Install Homebrew (if you haven't already)
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
> 
> # 2. Install rbenv to manage Ruby versions
> brew install rbenv ruby-build node
> 
> # 3. Setup rbenv in your shell (run these and restart your terminal)
> echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
> source ~/.zshrc
> 
> # 4. Install a modern version of Ruby and set it as globally active
> rbenv install 3.2.2
> rbenv global 3.2.2
> ```

1. **Install dependencies:**
   Open a terminal in this directory and run. First, node modules for the theme styling tools:
   ```bash
   npm install
   ```
   Then the Ruby dependencies:
   ```bash
   gem install bundler
   bundle install
   ```

2. **Start the local server:**
   ```bash
   bundle exec jekyll serve --lsi
   ```
   This will start a local web server (Jekyll will generate the HTML files into the `_site` directory).

3. **View the website:**
   Open your browser and navigate to `http://127.0.0.1:4000/`. As you edit your markdown files, the site will automatically rebuild. Simply refresh your browser to see the updates!

## 📝 How to update content

Updating the content on your website operates entirely on markdown and standard configuration files:

* **Bio / Homepage (`_pages/about.md`)**: The main homepage. Update your biography text here.
* **Publications (`_bibliography/papers.bib`)**: Just paste your standard BibTeX citations into this file. The theme automatically parses them and generates a beautiful publications page!
* **Research Projects (`_projects/`)**: Each project is an individual Markdown file. Add new ones here to expand your project grid.
* **Global Config (`_config.yml`)**: Global site configuration (e.g., links, colors, features).

## 🚢 Publishing your changes

Because `al-folio` is slightly more complex than a standard Jekyll site, pushing it to GitHub Pages handles the build automatically via a backend GitHub action bundled with the theme.

1. **Stage your changes:**
   ```bash
   git add .
   ```
2. **Commit your updates:**
   ```bash
   git commit -m "Update profile description"
   ```
3. **Push to go live:**
   ```bash
   git push origin master
   ```

Within a minute or two, your changes will be built and live at `https://dbellicoso.github.io/`.
