# Pre-Deploy

## Potential Impact

- [ ] 1 - Major
- [ ] 2 - Medium
- [ ] 3 - Minor (_Template is Optional For These_)

### _Description_

> A description of the background, problem, and/or suggested solution.

### _Test Instructions_

> How do you test this?

### _Dependencies_

> Any other PRs we should know about?

### _What could go wrong?_

> Use this to raise any concerns that may not be apparent to all.

## Checklist

- [ ] Manual testing completed.
- [ ] Change can be monitored (Datadog, Kibana, Cloudwatch, etc.).
- [ ] Has automated test coverage. (Any of the following - Unit, Postman, Selenium, Load, Cypress).
- [ ] QA targets (data-qa) added to properly select elements for test automation.
- [ ] Communication to necessary parties. (Pendo, Slack, Ops, etc.).
- [ ] Branch name follows SDLC guidelines (Linked below).

### _Special Snowflake Deployment_

- [ ] After Hours / Weekend Deploy
- [ ] Deploy in isolation

# Post-Deploy

Someone on the team will be available for the following:

- [ ] Test deployed changes in prod.
- [ ] Monitor for any anomalies.
- [ ] Support in case of incident.

## Rollback Plan

> Any special considerations for rollback?

#### _SDLC Documentation_

https://docs.google.com/document/d/1fKQnoXO2dM54qJ6XVKApt_QWJ30GcRGp46JTfIanE2I/edit

## Merge Instructions

- Use a `squash and merge` or `rebase and merge` when merging a feature branch into `risk`
- Use a `merge commit` when merging `risk` into `main`
- See [documentation](https://orthofi.atlassian.net/wiki/spaces/DEV/pages/2509078549/Software+Development+Lifecycle) for more details
