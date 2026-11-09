# Getting started: run your first project 🚀

Never run Python code from a terminal before? No problem. This guide takes you from nothing to a working project in about 10 minutes. You only need to do steps 1 and 2 once.

## 1. Install Python

You need **Python 3.9 or newer**.

- **Mac or Windows:** download it from [python.org/downloads](https://www.python.org/downloads/) and run the installer.
- **Windows only:** on the first screen of the installer, tick **"Add python.exe to PATH"**. This one box saves a lot of trouble later.

To check it worked, open a terminal (step 2) and type:

```bash
python3 --version        # Windows: python --version
```

You should see something like `Python 3.12.4`.

## 2. Open a terminal

A terminal is a window where you type commands instead of clicking.

- **Mac:** press `Cmd + Space`, type **Terminal** and press Enter.
- **Windows:** press the Windows key, type **PowerShell** and press Enter.
- **VS Code:** open the menu **Terminal > New Terminal**. This works on both.

## 3. Get the code

Pick one:

- **Download ZIP (easiest):** on the [repo page](https://github.com/RichelCode/tech-made-easy-code), click the green **Code** button, then **Download ZIP**. Unzip it somewhere easy to find, like your Desktop.
- **Git:** run `git clone https://github.com/RichelCode/tech-made-easy-code.git`

## 4. Move into a project folder

Use `cd` (change directory) to step into the folder. For example:

```bash
cd Desktop/tech-made-easy-code-main/01-time-series-forecasting
```

**Tip:** type `cd ` (with a space), then drag the folder from Finder or File Explorer into the terminal window. It fills in the path for you.

## 5. Make a virtual environment

A virtual environment is a private sandbox for this project's packages, so they don't clash with anything else on your computer.

**Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

When it's on, you'll see `(.venv)` at the start of your terminal line.

## 6. Install the packages

```bash
pip install -r requirements.txt
```

This reads the project's shopping list (`requirements.txt`) and installs everything on it. It can take a minute.

## 7. Run it

```bash
python forecast.py
```

Each folder's README names its script. Compare what prints with the **What you should see** section of that README. If they match, it worked! 🎉

## 8. When you're done

```bash
deactivate
```

Next time, you only need to `cd` into the folder and run the `activate` line from step 5. No need to reinstall.

## Common problems and fixes

- **`python3: command not found` (Mac)** or **`python is not recognized` (Windows):** Python isn't installed, or Windows can't find it. Reinstall it and tick "Add python.exe to PATH". On Windows, `py` often works in place of `python`.
- **`ModuleNotFoundError: No module named ...`:** your virtual environment isn't on. Run the `activate` line from step 5, then step 6 again.
- **`pip: command not found`:** use `python3 -m pip install -r requirements.txt` instead (Windows: `python -m pip ...`).
- **Windows says running scripts is disabled:** run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once in PowerShell, answer **Y**, then try `activate` again.
- **`No such file or directory: requirements.txt`:** you're in the wrong folder. Run `ls` (Windows: `dir`) and check you can see `requirements.txt` in the list.
- **XGBoost project on a Mac fails with `libomp`:** install it with `brew install libomp`, then run the script again.

Still stuck? [Open an issue](https://github.com/RichelCode/tech-made-easy-code/issues) and paste the error. I'm happy to help.

⬅️ [Back to all projects](README.md)
