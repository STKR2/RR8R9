from pyrogram import Client, filters
import requests
from AarohiX import app

def chunk_string(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

@app.on_message(filters.command("allrepo"))
async def all_repo_command(client, message):
    try:
        if len(message.command) > 1:
            github_username = message.command[1]
            repo_info = get_all_repository_info(github_username)
            chunked_repo_info = chunk_string(repo_info, 4000)
            for chunk in chunked_repo_info:
                await message.reply_text(chunk)
        else:
            await message.reply_text("Please enter a GitHub username after the /allrepo command.")
    except Exception as e:
        await message.reply_text(f"An error occurred: {str(e)}")

def get_all_repository_info(github_username):
    github_api_url = f"https://api.github.com/users/{github_username}/repos"
    response = requests.get(github_api_url)
    data = response.json()
    repo_info = "\n\n".join([
        f"Repository: {repo['full_name']}\n"
        f"Description: {repo['description']}\n"
        f"Stars: {repo['stargazers_count']}\n"
        f"Forks: {repo['forks_count']}\n"
        f"URL: {repo['html_url']}"
        for repo in data
    ])
    return repo_info
