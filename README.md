# Ben10dle
for %f in (*.ui) do python -m PyQt5.uic.pyuic -x "%f" -o "%~nf.py"