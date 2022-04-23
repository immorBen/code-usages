https://docs.github.com/en/get-started/getting-started-with-git/why-is-git-always-asking-for-my-password

> If Git prompts you for a username and password every time you try to interact with GitHub, you're probably using the HTTPS clone URL for your repository.

> When Git prompts you for your password, enter your personal access token (PAT) instead. Password-based authentication for Git has been removed, and using a PAT is more secure. For more information, see "Creating a personal access token."

> You can avoid being prompted for your password by configuring Git to cache your credentials for you. Once you've configured credential caching, Git automatically uses your cached personal access token when you pull or push a repository using HTTPS.

steps:
1. check which way you are using for managing repositories, if it is HTTPS clone URL (*if you are going to use SSH, it may costs you some time to set up, see [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)*),
2. generate a token first (https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token), and then cache the token (https://docs.github.com/en/github/getting-started-with-github/caching-your-github-credentials-in-git)
3. cache the token:
   - install `gh` by *Chocolatey*: choco install gh (open power shell with administrator right) see [here](https://github.com/cli/cli#installation)

```bash
PS C:\Users\zoubentao> gh auth login
? What account do you want to log into? GitHub.com
? What is your preferred protocol for Git operations? HTTPS
? Authenticate Git with your GitHub credentials? Yes
? How would you like to authenticate GitHub CLI? Paste an authentication token
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens
The minimum required scopes are 'repo', 'read:org', 'workflow'.
? Paste your authentication token: ****************************************
- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as immorBen
PS C:\Users\zoubentao>
```
From [GitHub doc](https://docs.github.com/en/get-started/getting-started-with-git/configuring-git-to-handle-line-endings), because you are working on different operation systems, you may face with the problem of line endings.

For basic git commands, see https://docs.github.com/en/get-started/using-git/about-git
