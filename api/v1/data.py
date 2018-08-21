from api.v1.model import Questions

questions = [Questions (1, "What is GitHub?", "GitHub is a Git repository hosting service, but it adds many of its own features. While Git is a command line tool, GitHub provides a Web-based graphical interface. It also provides access control and several collaboration features, such as a wikis and basic task management tools for every project." ),
            Questions (2, "How do I share my github repository?", "Navigate to the repository on Github you wish to share with your collaborator.Click on the Settings tab on the right side of the menu at the top of the screen.On the new page, click the Collaborators menu item on the left side of the page.Start typing the new collaborator's GitHub username into the text box.Select the GitHub user from the list that appears below the text box.Click the Add button.The added user should now be able to push to your repository on GitHub."),
            Questions (3, "What is a repo?", "a repository, or “repo” for short, a digital directory or storage space where you can access your project, its files, and all the versions of its files that Git saves.")
        ]

def get_single_question(qnId):

    for question in questions:
        if question.qnId == qnId:
            return question 


