import requests
from matplotlib import pyplot as plt

# Fetch GitHub language stats
def fetch_language_stats(username):
    url = f"https://api.github.com/users/{username}/repos"
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

# Generate a pie chart
def generate_pie_chart(languages):
    labels = list(languages.keys())
    sizes = list(languages.values())
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("language_stats.png")

# Update README.md
def update_readme():
    username = "yourusername"  # Replace with your GitHub username
    languages = fetch_language_stats(username)
    generate_pie_chart(languages)

    with open("README.md", "r") as file:
        readme = file.read()

    # Replace placeholders in README.md with dynamic content
    updated_readme = readme.replace("<!-- LANGUAGE_STATS -->", "![Language Stats](language_stats.png)")

    with open("README.md", "w") as file:
        file.write(updated_readme)

if __name__ == "__main__":
    update_readme()