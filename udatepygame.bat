@echo off
echo === Adding changes...
git add .

echo === Committing changes...
git commit -m "Auto update from script"

echo === Pushing to GitHub...
git push

echo === Done! 🚀
pause
