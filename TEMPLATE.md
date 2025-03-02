# Readme of the template

## Wiring external Services

### Reporting code coverage via CodeCov

1. Sign-Up at https://app.codecov.io/
2. Configure via https://app.codecov.io/gh/{{ github_repository_owner }}
3. Copy value of `CODECOV_TOKEN` into your clipboard
4. Goto {{ github_repository_url_https }}/settings/secrets/actions/new and create a new repository secret called `CODECOV_TOKEN`, pasting the token from your clipboard as value
5. Re-run the `CI / test` GitHub job in case you tried before and it failed as Codecov was not yet wired up

### Analyzing code quality and security analysis via SonarQube cloud

1. Sign-Up at https://sonarcloud.io
2. Grant access to your new repo via https://github.com/settings/installations -> Configure
3. Goto https://sonarcloud.io/projects/create and select the repo
4. Select Previous Code when prompted
5. Configure by going to https://sonarcloud.io/project/configuration?id={{ sonarqube_key }} and clicking on "With GitHub Actions". Copy the value of `SONAR_TOKEN` into your clipboard.
6. Goto {{ github_repository_url_https }}/settings/secrets/actions/new and create a new repository secret called `SONAR_TOKEN`, pasting the token from your clipboard as value
6. Goto https://sonarcloud.io/project/settings?id={{ sonarqube_key }} and select "Quality Gate" in the left menu. Select "Sonar way" as default quality gate.
7. Re-run the `CI / test` GitHub job in case you tried before and it failed as SonarQube was not yet wired up

### Publishing package to Python Package Index (PyPI)

1. Sign-Up at https://pypi.org/
2. Goto https://pypi.org/manage/account/ and create an API token for your new repository, calling it {{ github_repository_name }}
