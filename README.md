# Dario Bellicoso - Personal Website

This repository contains the source code for my personal academic and research portfolio, built using the [al-folio](https://github.com/alshedivat/al-folio) Jekyll theme.

## 🚀 How to preview locally

If you want to preview your changes before pushing them live, you can build and serve the website locally.

**Prerequisites:**

- Ruby 3.2.2 (the same version the GitHub deploy action uses), installed in user space via `rbenv`
- [ImageMagick](https://imagemagick.org/), used to generate responsive WebP images (`imagemagick.enabled: true` in `_config.yml`)
- Node.js (optional; only needed to run the Prettier formatter that CI checks)

> [!WARNING]
>
> **Apple Silicon (M1/M2/M3) Mac Users:** DO NOT use the default macOS System Ruby (it will throw `GemNotFoundException` permission errors). Instead, install a modern user-space Ruby using [Homebrew](https://brew.sh/):
>
> ```bash
> # 1. Install Homebrew (if you haven't already)
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
>
> # 2. Install rbenv to manage Ruby versions, plus ImageMagick and Node.js
> brew install rbenv ruby-build imagemagick node
>
> # 3. Setup rbenv in your shell
> echo 'eval "$(rbenv init - zsh)"' >> ~/.zshrc
> source ~/.zshrc
>
> # 4. Install a modern version of Ruby and set it as globally active
> rbenv install 3.2.2
> rbenv global 3.2.2
> ```

1. **Install dependencies:**
   Open a terminal in this directory and install the Ruby dependencies:

   ```bash
   gem install bundler
   bundle install
   ```

   Optionally, install the node modules for the Prettier formatter:

   ```bash
   npm install
   ```

2. **Start the local server:**

   ```bash
   bundle exec jekyll serve
   ```

   This will start a local web server (Jekyll will generate the HTML files into the `_site` directory).

3. **View the website:**
   Open your browser and navigate to `http://127.0.0.1:4000/`. As you edit your markdown files, the site will automatically rebuild. Simply refresh your browser to see the updates!
   Changes to `_config.yml` are **not** picked up automatically: stop the server (`Ctrl+C`) and start it again.

## 📝 How to update content

Updating the content on your website operates entirely on markdown and standard configuration files:

- **Bio / Homepage (`_pages/about.md`)**: The main homepage. Update your biography text here.
- **Publications (`_bibliography/papers.bib`)**: Just paste your standard BibTeX citations into this file. The theme automatically parses them and generates a beautiful publications page!
  To attach a PDF, put it in `assets/pdf/` and add `pdf = {filename.pdf}` to the entry (the file name only, without a folder).
- **Projects (`_pages/projects_3.md`)**: Hand-written HTML sections with embedded videos. Add a new `<h2>` block to add a project.
- **Media (`_pages/media_5.md`)** and **Music (`_pages/music_6.md`)**: Hand-written HTML sections. Images go in `assets/img/`.
- **CV (`assets/json/resume.json`)**: The CV page is generated from this [JSON Resume](https://jsonresume.org/) file. The downloadable PDF is `assets/pdf/cv_dario_bellicoso.pdf`.
- **Global Config (`_config.yml`)**: Global site configuration (e.g., links, colors, features).

The number at the end of each page file name (e.g. `_3`) is only a reminder of its position in the navigation bar; the actual order is set by `nav_order` in the page's front matter.

## 🚢 Publishing your changes

Because `al-folio` is slightly more complex than a standard Jekyll site, the site is built and deployed by the `Deploy site` GitHub Action (`.github/workflows/deploy.yml`) on every push to `master`.

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

The deploy action only runs when the push touches content files (`assets/`, `.md`, `.bib`, `.yml`, `.liquid`, `.html`, `.js`, `Gemfile`). If you only changed something else (e.g. `_sass/` or `_plugins/`), trigger it manually:

```bash
gh workflow run deploy.yml
```

A separate `Prettier code formatter` action checks the formatting of the source files. To fix formatting locally before pushing (requires `npm install`):

```bash
npx prettier --write .
```

## Troubleshooting

If:

```bash
dyld[97331]: Library not loaded: /opt/homebrew/opt/gmp/lib/libgmp.10.dylib
  Referenced from: <85CC2209-0AC2-3439-953D-1B0174069D90> /Users/dariobellicoso/.rbenv/versions/3.2.2/bin/ruby
  Reason: tried: '/opt/homebrew/opt/gmp/lib/libgmp.10.dylib' (no such file), '/System/Volumes/Preboot/Cryptexes/OS/opt/homebrew/opt/gmp/lib/libgmp.10.dylib' (no such file), '/opt/homebrew/opt/gmp/lib/libgmp.10.dylib' (no such file)
zsh: abort      bundle exec jekyll serve --lsi
```

reinstall:

```bash
# 1. Remove the broken Ruby build
rbenv uninstall 3.2.2

# 2. Reinstall it (this forces a fresh compilation against the new gmp)
rbenv install 3.2.2

# 3. Ensure it is set as your active version
rbenv global 3.2.2

# 4. Reinstall your project gems
gem install bundler
bundle install
```

If the build fails with:

```bash
Liquid Exception: invalid byte sequence in US-ASCII in _pages/publications_2.md
```

your shell has no UTF-8 locale set (the BibTeX file contains accented names). Set it and serve again:

```bash
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
bundle exec jekyll serve
```
