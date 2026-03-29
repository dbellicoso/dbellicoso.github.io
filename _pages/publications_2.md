---
layout: page
permalink: /publications/
title: Publications
description:
nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<!-- Bibsearch Feature -->

{% include bib_search.liquid %}

## Academic Publications

<div class="publications">
{% bibliography -f papers --query @*[type!=patent] %}
</div>

<br>
<br>

## Patents

<div class="publications">
{% bibliography -f papers -q @patent %}
</div>
