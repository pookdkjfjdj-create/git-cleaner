<p align="center">
  <strong><code>git-cleaner</code></strong><br>
  <em>Interactive branch and tag cleanup -- list, dry-run, delete.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python_3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge&logo=opensourceinitiative" alt="License">
  <img src="https://img.shields.io/badge/Dependencies-None-ff69b4?style=for-the-badge" alt="Zero deps">
</p>

---

## What It Does

Lists and deletes merged branches and old tags from your git repository. Dry-run by default -- always preview before deleting.

## Quick Start

### List branches and tags

```bash
python -m git_cleaner list
```

```
Branches (merged, 12):
  feat/add-login
  fix/header-nav
  refactor/api-client

Tags (3):
  v0.1.0
  v0.2.0
  v0.3.0
```

### Dry-run delete

```bash
python -m git_cleaner delete --dry-run
```

### Actually delete

```bash
python -m git_cleaner delete
```

## Safety

- Never deletes main, master, or develop
- Safe delete only (git branch -d)
- Dry-run by default

## License

MIT

<p align="center">
  <a href="https://github.com/pookdkjfjdj-create">@pookdkjfjdj-create</a>
</p>
