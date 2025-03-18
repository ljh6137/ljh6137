import requests

# Fetch GitHub language stats
def fetch_language_stats(username):
    url = f"https://api.github.com/users/ljh6137/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
        languages = {}
        for repo in repos:
            lang_response = requests.get(repo["languages_url"])
            if lang_response.status_code == 200:
                repo_langs = lang_response.json()
                for lang, bytes in repo_langs.items():
                    languages[lang] = languages.get(lang, 0) + bytes
        return languages
    return {}

# Generate language stats markdown
def generate_language_stats(languages):
    total_bytes = sum(languages.values())
    stats = []
    for lang, bytes in languages.items():
        percentage = (bytes / total_bytes) * 100
        stats.append(f"- ​**{lang}**: {percentage:.2f}%")
    return "\n".join(stats)

# Update README.md
def update_readme():
    username = "yourusername"  # Replace with your GitHub username
    languages = fetch_language_stats(username)
    language_stats = generate_language_stats(languages)

    with open("README.md", "r") as file:
        readme = file.read()

    # Replace placeholders in README.md with dynamic content
    updated_readme = readme.replace("<!-- LANGUAGE_STATS -->", language_stats)

    with open("README.md", "w") as file:
        file.write(updated_readme)

if __name__ == "__main__":
    update_readme()