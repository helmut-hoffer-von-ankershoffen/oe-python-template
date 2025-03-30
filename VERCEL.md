# Vercel

You can host the API as a serverless function on Vercel

## Register at Vercel

[Sign-Up](https://vercel.com/signup) and create a "Hobby" account - it's free.

## Install Vercel CLI

```shell
pnpm i -g vercel
```

## Generate, link and deploy Vercel Distribution

```shell
make dist_vercel
vercel login
vercel link --cwd dist_vercel --project oe-python-template --yes
vercel deploy --cwd dist_vercel
```

Visit the [production deployment](https://oe-python-template.vercel.app/)

## Wire the CI/CD

1. Show organisation and project id by executing `cat dist_vercel/.vercel/project.json`
2. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/settings/secrets/actions/new) called `VERCEL_PROJECT_ID` with the value of `projectId` from step 1
3. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/settings/secrets/actions/new) called `VERCEL_ORG_ID` with the value of `orgId` from step 1
4. Goto [Vercel Account Settings](https://vercel.com/account/settings/tokens) and create a new token with project scope, copy the token to clipboard.
5. [Create secret](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template/settings/secrets/actions/new) called `VERCEL_TOKEN` with the value of `projectId` from the previous command

That's it. The rest is automatic, deploy happening on build of main.
