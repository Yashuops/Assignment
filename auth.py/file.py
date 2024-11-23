from github import Github

# Replace with your personal access token from GitHub
GITHUB_ACCESS_TOKEN = "your_personal_access_token"

# Authenticate to GitHub
g = Github(GITHUB_ACCESS_TOKEN)

# Get the authenticated user
user = g.get_user()

# Print the user's login
print(f"Authenticated as: {user.login}")

# List all repositories for the user
print("Repositories:")
for repo in user.get_repos():
    print(f"- {repo.name}")

# Create a new repository
repo_name = "sample-repo"
description = "This is a sample repository created using PyGithub"
private = False  # Set to True to create a private repository

new_repo = user.create_repo(
    name=repo_name,
    description=description,
    private=private,
)

print(f"New repository created: {new_repo.name}")
