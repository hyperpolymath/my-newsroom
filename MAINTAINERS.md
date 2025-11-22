# Maintainers

**Version:** 1.0.0
**Last Updated:** 2025-11-22
**Governance:** TPCF (Tri-Perimeter Contribution Framework)

---

## Current Maintainers

### Perimeter 1: Core Maintainers

**Full commit access, release authority, governance decisions**

| Name | Role | Focus Areas | GitLab | Contact |
|------|------|-------------|--------|---------|
| [Your Name] | Project Lead | Architecture, Research, Ensemble dialect | @hyperpolymath | [email] |

### Perimeter 2: Verified Contributors

**Review and merge authority for non-protected branches**

*None yet - accepting nominations! See [CONTRIBUTING.md](CONTRIBUTING.md)*

### Perimeter 3: Community Contributors

**All other contributors** - See [.well-known/humans.txt](.well-known/humans.txt) for full credits.

---

## Responsibilities by Perimeter

### Perimeter 1 Responsibilities

**Technical:**
- [ ] Approve architectural changes
- [ ] Review and merge high-risk PRs (>500 LOC, core changes)
- [ ] Create releases and tags
- [ ] Maintain CI/CD pipeline
- [ ] Manage secrets and credentials

**Governance:**
- [ ] Enforce Code of Conduct
- [ ] Invite new Perimeter 2 members
- [ ] Make final decisions on disputed issues
- [ ] Set project direction and roadmap

**Communication:**
- [ ] Respond to security reports (72-hour SLA)
- [ ] Update stakeholders (funders, partners, users)
- [ ] Represent project at conferences
- [ ] Coordinate with external collaborators

**Time Commitment:** ~10-20 hours/week

### Perimeter 2 Responsibilities

**Technical:**
- [ ] Review and merge routine PRs (<500 LOC)
- [ ] Triage and label issues
- [ ] Write documentation
- [ ] Maintain test coverage

**Community:**
- [ ] Welcome new contributors
- [ ] Answer questions in discussions
- [ ] Mentor junior contributors

**Time Commitment:** ~5-10 hours/week

### Perimeter 3 (All Contributors)

**Participation:**
- [ ] Submit merge requests
- [ ] Report bugs
- [ ] Suggest features
- [ ] Improve documentation

**Time Commitment:** As available (no minimum)

---

## Becoming a Maintainer

### Path to Perimeter 2 (Verified Contributor)

**Eligibility:**
1. ≥5 merged contributions (code, docs, or research)
2. ≥3 months active participation
3. Demonstrated understanding of project values
4. No Code of Conduct violations

**Process:**
1. Self-nominate or be nominated by existing maintainer
2. Submit application to maintainers@[project-domain] with:
   - Summary of contributions (link to merged MRs)
   - Areas of expertise
   - Why you want to be a maintainer
   - Time availability
3. Perimeter 1 maintainers vote (simple majority)
4. If accepted, added to team with 30-day probation

**Probation:**
- First 30 days: can review PRs, but merges require Perimeter 1 approval
- After 30 days: full Perimeter 2 privileges

### Path to Perimeter 1 (Core Maintainer)

**Eligibility:**
1. ≥20 merged contributions
2. ≥6 months active participation as Perimeter 2
3. Deep expertise in ≥1 dialect or subsystem
4. Trusted by existing Perimeter 1 members

**Process:**
1. Invitation-only by unanimous Perimeter 1 vote
2. Candidate accepts or declines
3. If accepted, 60-day probation with mentorship

---

## Inactive Maintainers

**Definition:** No activity (commits, reviews, or communication) for ≥90 days

**Process:**
1. Send check-in email after 60 days of inactivity
2. If no response after 30 days → move to "Emeritus" status
3. Emeritus maintainers lose technical access but keep advisory role

**Reactivation:**
- Emeritus maintainers can request reinstatement anytime
- Must commit to ≥5 hours/week for next 3 months
- Restored to previous perimeter level

---

## Stepping Down

**Voluntary:**
1. Email maintainers@[project-domain] with ≥14 days notice
2. Transfer active PRs/issues to other maintainers
3. Document any in-progress work
4. Revoke technical access (GPG keys, credentials)
5. Move to Emeritus status (optional)

**Involuntary (Code of Conduct Violation):**
- Temporary ban → Perimeter access suspended for duration
- Permanent ban → All access revoked, removed from credits

---

## Decision-Making Process

### Routine Decisions (Examples)

- Merging small PRs (<100 LOC)
- Triaging issues
- Minor documentation updates

**Process:** Single Perimeter 2+ maintainer approval

### Significant Decisions (Examples)

- New features (>500 LOC)
- Breaking API changes
- Adding dependencies
- Updating Code of Conduct

**Process:**
1. Open GitLab issue with `rfc` label (Request for Comments)
2. ≥7 days discussion period
3. Simple majority of Perimeter 1 maintainers

### Major Decisions (Examples)

- Changing license
- Archiving project
- Removing Perimeter 1 maintainer
- Trademark/branding changes

**Process:**
1. Open GitLab issue with `rfc-major` label
2. ≥14 days discussion period
3. Unanimous Perimeter 1 approval OR 2/3 supermajority if ≥4 maintainers

---

## Conflict Resolution

### Between Contributors

1. **Self-resolution:** Try to resolve privately first
2. **Mediation:** Ask Perimeter 1 maintainer to mediate
3. **Code of Conduct:** If behavior violates CoC, file report

### Between Maintainers

1. **Discussion:** Open private discussion among Perimeter 1
2. **Vote:** If no consensus after 7 days, simple majority vote
3. **External mediation:** If vote is tied, invite neutral third party (e.g., academic advisor, OSS governance expert)

---

## Maintainer Resources

### Tools & Access

**Required:**
- GitLab account with appropriate permissions
- GPG key for signing commits/tags
- Email alias (@[project-domain] if available)

**Optional:**
- PGP key for encrypted security reports
- SSH access to CI/CD infrastructure
- Access to analytics (download stats, etc.)

### Communication Channels

- **Private:** maintainers@[project-domain]
- **Public:** https://gitlab.com/Hyperpolymath/My-newsroom/-/discussions
- **Security:** security@[project-domain]
- **Code of Conduct:** conduct@[project-domain]

### Recurring Meetings

**Currently:** No regular meetings (async-first workflow)

**Future (if team grows):**
- Monthly sync (1 hour) - Project updates, roadmap alignment
- Quarterly planning (2 hours) - Review priorities, adjust roadmap

---

## Maintainer Expectations

### Code of Conduct

Maintainers are held to a **higher standard**:
- Lead by example (respectful communication, inclusive language)
- Respond to CoC violations within 72 hours
- Recuse from decisions where you have conflicts of interest
- Disclose affiliations that might bias decisions

### Responsiveness

**Expected response times:**
- Security issues: ≤72 hours (ideally ≤24 hours for critical)
- Code of Conduct reports: ≤72 hours
- Routine PRs: ≤7 days
- Questions in discussions: ≤3 days

**If you're away:**
- Set GitLab "busy" status
- Post in maintainers@ channel
- Delegate urgent items to other maintainers

### Transparency

**Public by default:**
- Technical decisions documented in issues/MRs
- Roadmap changes announced in CHANGELOG
- Governance discussions summarized publicly (unless confidential)

**Private when necessary:**
- Security vulnerabilities (until patched)
- Code of Conduct reports (to protect privacy)
- Personal information about contributors

---

## Recognition

**Ways we recognize maintainer contributions:**

- Listed in this file (MAINTAINERS.md)
- Credit in release notes
- Acknowledgments in academic papers
- Conference talk co-authorship (for research contributions)
- Reference letters (upon request)

---

## Acknowledgments

**Emeritus Maintainers:**

*None yet - awaiting first cohort!*

**Special Thanks:**

- Anthropic (Claude AI assistance in bootstrapping project)
- Rhodium Project (RSR framework inspiration)
- Contributor Covenant (Code of Conduct template)

---

## Changelog

### 2025-11-22 - Initial Version

- Established TPCF governance structure
- Defined responsibilities for each perimeter
- Created maintainer nomination process

---

## Contact

Questions about maintainership? Email maintainers@[project-domain] or open a GitLab discussion.

**We're actively seeking Perimeter 2 maintainers!** If you're passionate about epistemic programming, neurosymbolic AI, or journalism tech, we'd love to have you on the team. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get involved. 🚀
