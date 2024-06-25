# Setup for Ubuntu

> One time setup for Ubuntu 22.04

## Compilers

```bash
sudo apt install build-essential
```

## pyenv

Install Python Dependencies:

```bash
sudo apt-get install libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev liblzma-dev
```

Install `pyenv`:

```bash
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
```

Enable:

```bash
source ~/.bashrc
```

## Python

Install via `pyenv`:

```bash
pyenv install 3.12.0
```

## Visual Studio Code

### Install via Snap Store (preferred):

```bash
sudo snap install --classic code
```
