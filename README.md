# No-IP Renew Docker Runner on GitHub
This project is a Docker-based solution that automates the renewal of No-IP dynamic DNS accounts, based on [simao-silva/noip-renewer](https://github.com/simao-silva/noip-renewer) on GitHub.

## Getting Started
### 1. Fork the Repository
Start by forking this repository to your GitHub account.

### 2. Set Up Secrets
Navigate to Settings → Secrets and variables → Actions in your forked repository, and add your No-IP account credentials as secrets. Each account requires three secrets:

* `NO_IP_USERNAME_1`, `NO_IP_PASSWORD_1`, `NO_IP_TOTP_KEY_1`
* `NO_IP_USERNAME_2`, `NO_IP_PASSWORD_2`, `NO_IP_TOTP_KEY_2`
* ...
Continue adding secrets for as many accounts as you need, incrementing the number for each additional set.

### 3. Enable Actions
Once your secrets are set up, go to Settings → Actions and click on New repository secret Actions. Then, select I understand my workflows, go ahead and enable them to enable GitHub Actions for your repository.

