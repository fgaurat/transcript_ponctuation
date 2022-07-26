mkdir youtube_transcript
cd youtube_transcript
venv
touch main.py
chmod +x main.py
code .
pip install deepmultilingualpunctuation
brew install cmake <- pour le build de la lib, ça n'était pas installé sur ma machine
pip install sentencepiece
pip install protobuf==3.20 < La dernière version ne fonctionnait pas chez moi du coup isntallation d'une version plus anciennes

./main.py