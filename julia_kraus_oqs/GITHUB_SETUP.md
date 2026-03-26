# GitHub Setup

## Local repo

From this folder:

```powershell
git init -b main
git add .
git commit -m "Initial commit: Julia Kraus simulation project"
```

## Create the GitHub repo

Recommended repository name:

`open-quantum-kraus-simulation`

If you use the GitHub CLI and are already logged in:

```powershell
gh repo create open-quantum-kraus-simulation --public --source=. --remote=origin --push
```

## Manual remote setup

If you create the empty repo on GitHub in the browser first, then run:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/open-quantum-kraus-simulation.git
git push -u origin main
```

## Final GitHub link

Replace `YOUR_USERNAME` with your actual GitHub username:

`https://github.com/YOUR_USERNAME/open-quantum-kraus-simulation`
