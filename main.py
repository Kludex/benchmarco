import os

from github import Github

GITHUB_REF = os.getenv("GITHUB_REF")
PR_NUMBER = int(GITHUB_REF.split("/")[2])

gh = Github(os.getenv("GITHUB_TOKEN"))
repo = gh.get_repo("Kludex/benchmarco")
pr = repo.get_pull(PR_NUMBER)
pr.create_issue_comment("This comment was created by a bot.")
