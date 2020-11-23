from github import Github

def getUserInfo(user):
    return user.login, user.id, user.name, user.location, user.bio, user.public_repos, user.followers, user.following


def getRepoInfo(repo):
    return repo.name, repo.id, repo.description



def getUserFollowers(user):
    return user.get_followers()


def getUserFollowing(user):
    return user.get_following()


def printUserInfo(user, inline):
    p_end = ' ' if inline else '\n'
    temp = list(getUserInfo(user))
    index = ['Login','ID','Name','Location', 'Bio', 'Public Repos', 'Followers', 'Following']

    for i in range(0, len(index)):
        print(str(index[i])+": "+str(temp[i]), end=p_end)

    print("")


def printRepoInfo(repo, inline):
    p_end = ' ' if inline else '\n'
    temp = list(getRepoInfo(repo))
    index = ['Name','ID','Description']

    for i in range(0, len(index)):
        print(str(index[i])+": "+str(temp[i]), end=p_end)

    print("")


def printCommitInfo(repo):
    pass



def main():
    # Take input from the user
    personal_token = input("Enter Username or Token for GitHub account: ")

    try:
        g = Github(login_or_token=personal_token)
        user = g.get_user()
        login = user.login
        print(user)
        print("--------- User Information ---------")
        printUserInfo(user, False)

        print("------------ Followers -------------")

        # Print all the followers
        for pers in user.get_followers():
            printUserInfo(pers, True)


        print("\n----------- Following -------------")
        # Print all they are following
        for pers in user.get_following():
            printUserInfo(pers, True)


        print("\n----------- Repositories -------------")
        for repo in user.get_repos():
            count = 0
            printRepoInfo(repo, False)

            # Find the language used in each repository
            print(repo.languages_url)
            # for lang,x in repo.get_languages():
            #     print(lang,x)

            # Find the number of commits made by this user in each repo
            for commit in repo.get_commits():
                # print(commit.author.login)    # conorlolynch
                if commit.author.login == user.login:
                    count += 1
                    # print(commit.sha)

            print("Number of commits: "+str(count))

            print("\n")


        print("------------- Languages ---------------")


    except Exception as e:
        print(e)


main()
