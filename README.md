# Python 3 scripts template

This is a basic nix flake used for python3 development. If you want to write a
quick script that you'd inline in a CloudFormation template, or just want to
quickly invoke from CLI - then just pasting it here in script.py and opening it
in your favorite text editor with LSP is a great strategy.

Hoping you've got [nix installed](https://nixos.wiki/wiki/Nix_Installation_Guide#Single-user_install),
preferably with [direnv](https://github.com/nix-community/nix-direnv) support.

It may also come handy for exercises or just stuff you wanna quickly try out.
Just clone it somewhere, `cp script.py foo.py`, and get it going - `*.py` files
are gitignored.

**NOTE**: github actions are disabled by default.

## Text editor setup
### Helix
This goes to `~/.config/helix/languages.toml`.
It enables the pep8 checking, pylint, and a nice code coverage gutter on the left.
```
[[language]]
name = "python"
language-servers = ["pylsp"]
auto-format = true

[language-server.pylsp.config.pylsp.plugins]
flake8 = {enabled = true}
autopep8 = {enabled = true}
pycodestyle = {enabled = true}
pyflakes = {enabled = true}
pylint = {enabled = true}
ruff = { enabled = true, ignore = ["F401"], lineLength = 120 }
```
