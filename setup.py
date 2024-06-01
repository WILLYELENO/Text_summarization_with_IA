import nltk
import subprocess

# Install necessary packages
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])


# Descargar recursos de NLTK si es necesario

nltk.download('punkt')
nltk.download('stopwords')
