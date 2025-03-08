import os
import subprocess

# Define the repository directory
repo_dir = r'd:\python\Cosmos\cosmosclassroom.github.io'

# Change to the repository directory
os.chdir(repo_dir)

# Convert markdown to HTML using Pandoc
subprocess.run(['pandoc', '--standalone', "Markdown.md", '-c', 'style.css', '-o', "index.html"])

# Run Git commands
subprocess.run(['git', 'status'])
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', 'Updated website with new content'])
subprocess.run(['git', 'pull', 'origin', 'main'])
subprocess.run(['git', 'push', 'origin', 'main'])