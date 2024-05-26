import nltk
import subprocess

# Install necessary packages
subprocess.check_call(['pip', 'install', '-r', 'requirements.txt'])

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
