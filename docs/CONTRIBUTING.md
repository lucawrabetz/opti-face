# Contributing to opti-face
We want to make contributing to this project as inclusive as possible, so we accept all of the following contributions from anyone interested in the project:
- reporting a bug or submitting a fix;
- contributing code, designs, or documentation;
- providing opinionated and / or critical user feedback, and potentially proposing and discussing new features or roadmap directions.

If you think you can help in any of these ways - open an issue or pull request! If you are looking to get involved as soon as possible, look for an interesting issue in the [issues](https://github.com/lucawrabetz/opti-face/issues) tab.

The development process assumes that you have a basic familiarity with contributing to open-source projects using the *forking workflow*. If you are new to contributing to open-source, or need a refresher on the workflow, here are some good places to start:
- **GitHub's Guide to Contributing**: [Understanding the GitHub flow](https://guides.github.com/introduction/flow/)
- **Forking Workflow Tutorial**: [Forking Projects](https://guides.github.com/activities/forking/)
- **Video Tutorial on GitHub Forking**: [GitHub for Beginners: Don't Get Scared, Get Started](https://www.youtube.com/watch?v=0fKg7e37bQE)

## Development process
1. If you are a first-time contributor, set up your local development environment before proceeding to step (2):
- Fork the repository, and clone it to your local machine:
    ```bash
    git clone git@github.com:your-username/opti-face.git
    ```
- Navigate to the project directory and add the upstream repository:
    ```bash
    git remote add upstream git@github.com:lucawrabetz/opti-face.git
    ```
- Now, you have remote repositories named:
    - `upstream`, which refers to the `opti-face` repository
    - `origin`, which refers to your personal fork

- Add the development requirements to your local environment (this step assumes you have completed the local environment set up in the [installation guide](../README.md). The next step will add the development packages to your *opti-face* environment, whether you used `conda` or `pip`):
    ```bash
    pip install -r requirements/requirements-dev.txt
    ```

- Install the pre-commit hooks (optional but highly recommended):
    ```bash
    pre-commit install
    ```

2. If you are a returning contributor, or you have completed step (1), you can develop your contribution:
- Pull the latest changes from upstream:
    ```bash
    git checkout main
    git pull upstream main
    ```

- Create a branch for your contribution. Since the branch name will appear in the merge message, use a sensible name such as 'bugfix-for-issue-1234':
    ```bash
    git checkout -b bugfix-for-issue-1234 main
    ```

- Commit locally as you progress using `git add` and `git commit` (TODO: [address style issue wrt commit messages](https://github.com/lucawrabetz/opti-face/issues/4)).

3. Test your contribution locally:
- TODO: [add testing instructions](https://github.com/lucawrabetz/opti-face/issues/5)

4. Ensure proper formatting!
- If you installed the pre-commit hooks, you already have formatting checks and fixes at every commit. If the hooks catch any formatting errors, the appropriate fixes will be applied automatically - just remember `git add` and `git commit` again.
- If you chose not to install the pre-commit hooks, or if the above doesn't work for some reason, just run the following command before committing, remembering to re-stage any ensuing changes:

    ```bash
    pre-commit run --all-files
    ```

## Documentation and other discussions
We currently use GitHub to host all documentation, designs and other project-related files (see /docs). Any other project-related files or discussions that are hosted elsewhere will be linked to from here when they are created.

## Any contributions you make will be under the MIT Software License
In short, when you submit code changes, your submissions are understood to be under the same [MIT License](../LICENSE) that covers the project. By contributing, you agree that your contributions will be licensed under its MIT License. Feel free to contact the maintainers if that's a concern.

## Report bugs using Github's [issues](https://github.com/lucawrabetz/opti-face/issues)

**Great Bug Reports** tend to have:
- A concise summary and/or background
- Steps to reproduce
  - Be specific (OS or hosting version details, environment details, etc.)!
  - Give sample code, or screenshots, if you can.
- What you expected would happen
- What actually happens
- Notes (possibly including why you think this might be happening, or stuff you tried that didn't work, or any other relevant information)
