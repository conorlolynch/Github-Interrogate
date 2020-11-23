# Github-Interrogate
Interrogate the GitHub API to retrieve and display data regarding the logged in developer.

## Getting Started

To get started just run the collector.py file. Due to the new changes with the GitHub API V3 a personal token for the users account must be used to log in. Create a token for youre account following this guide: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token 

### Prerequisites

Following modules are required to run this program:

```
PyGithub==1.53
```


## Usage and Explanation

If a valid access token is provided by the user then the API can successfully connect to the users account and return information about their account such as user details and repository information.

### Demonstration

![alt text](images/usage-git-interrogate.png)

### Additional Information

- This project is a prerequisite of the final software engineering module project called: Github-Access
