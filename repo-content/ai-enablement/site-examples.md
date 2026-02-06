# AI Enablement Examples
## (https://digital-corps-pdx.github.io/AI-enablement/examples.html)

---

Templates for disclosing AI authority across public services. Click to expand full statements.

**Jump to:** [Benefits](#benefits) | [Public Safety](#safety) | [Licensing & Permits](#licensing) | [Education](#education) | [Housing & Inspection](#housing)

---

## Public Benefits

### Assistive | Medicaid Recertification

**System:** "Auto-renews coverage when no changes detected. Flags complex cases for worker review."

**Key disclosure:** "60% auto-renewed. 40% need human review. Coverage continues during review."

**View Full Statement**

**Service:** Medicaid Expansion Eligibility Recertification
**Agency:** [State] Medicaid Program

**What This System Does:** Automated recertification every 6 months (federal requirement).

**AI's Role:**
- Checks databases for income, employment, address changes
- Auto-renews if no changes and still eligible
- Flags data mismatches for worker review

**Human Authority:**
- Workers review all flagged cases
- Workers determine what additional info is needed
- Workers make final determination

**For Members:**
If auto-renewed: confirmation notice, no action needed
If flagged: letter explaining what we need, 30 days to respond

**How to Challenge:**
- Call worker: [phone]
- Submit reconsideration if terminated
- 90-day appeal window

**Oversight:**
- Monthly monitoring of auto-renewal and termination rates
- Quarterly review for unnecessary documentation requests
- Bias testing for disproportionate flagging

---

### Advisory | Unemployment Fraud Detection

**System:** "Generates risk scores (0-100). Investigator must find independent evidence before any action."

**Key disclosure:** "Score cannot deny benefits. Human investigation required. Claimant notified before review begins."

**View Full Statement**

**Service:** Unemployment Insurance Fraud Detection
**Agency:** [State] Employment Security Department

**What This System Does:** Flags claims for potential fraud investigation.

**AI's Role (Advisory Only):**
- Generates risk score based on application patterns, data inconsistencies
- Score alone CANNOT deny benefits or trigger penalties

**Human Authority:**
- All high-risk scores reviewed by fraud investigator
- Investigator must document independent evidence
- No action based on score alone

**If Flagged:**
- Written notice within 3 business days
- Right to provide documentation before determination
- Determination must cite investigator findings, not just score

**Oversight:**
- Independent audit every 6 months
- False positive rate published quarterly (target <5%)
- System disabled if false positive >10%

**Safeguards Learned from Michigan MiDAS Failure (93% false positive rate):**
- No automated denials
- Mandatory human review
- Claimant notification before investigation

---

### Advisory | SNAP Documentation Check

**System:** "Scans case files for missing docs. Worker decides if additional info needed."

**Key disclosure:** "System does NOT determine eligibility, calculate benefits, or auto-deny applications."

**View Full Statement**

**Service:** SNAP Error Rate Reduction
**Agency:** [State] Department of Human Services

**What This System Does:** Helps workers identify missing documentation before federal audits.

**AI's Role:**
- Scans for missing income verification, address docs, signatures
- Generates checklist for worker review

**Human Authority:**
- Worker reviews alerts and decides if additional docs needed
- Worker can mark alerts "not applicable"
- Worker makes final eligibility determination

**For Applicants:**
What changes: May get requests for additional documentation
What doesn't: Eligibility criteria, benefit amounts, timelines

**Why This Exists:** Federal law (HR1) penalizes states for insufficient documentation. This helps workers complete case files to protect state SNAP funding.

**What We DON'T Do:**
- Calculate benefit amounts
- Determine eligibility
- Auto-deny applications
- Share data with immigration enforcement

---

## Public Safety

### Advisory + Limited Determinative | Child Welfare Hotline

**System:** "Generates risk scores (0-20). Scores above 18 trigger mandatory investigation. Below 18, screener decides."

**Key disclosure:** "The information summarized by the score does not replace clinical judgment" for 95% of calls.

**View Full Statement**

**Service:** Child Welfare Hotline Screening
**Agency:** [County] Department of Human Services

**What This System Does:** Generates risk assessment scores for incoming hotline calls.

**AI's Role:**
- Scores 0-20 based on CPS history, child age, allegation type, environmental factors
- Scores 18-20: automatic face-to-face investigation within 24 hours (state law)
- Scores below 18: score is ONE input, screener decides

**Human Authority:**
- Screeners review ALL calls
- Can upgrade response regardless of score
- Supervisory review required to screen out calls scored above 15

**Contestability:**
- Request supervisor review during call
- Administrative review within 5 business days
- Score and notes available through records request

**Oversight:**
- Weekly screener calibration sessions
- Quarterly bias audit (race, zip code, reporter type)
- Annual recalibration
- Community advisory board reviews aggregate data

---

### Advisory | 911 Call Prioritization

**System:** "Suggests priority level based on call keywords and location. Dispatcher makes final determination."

**Key disclosure:** "Dispatcher can override any suggestion. All life-threatening calls get immediate response regardless of system suggestion."

**View Full Statement**

**Service:** Emergency Call Dispatch
**Agency:** [City] 911 Communications

**What This System Does:** Assists dispatchers in prioritizing emergency response.

**AI's Role:**
- Analyzes call keywords, location, historical patterns
- Suggests priority level (1-5, 1 being highest)
- Flags potential life-threatening situations

**Human Authority:**
- Dispatcher makes all final determinations
- Can override any suggestion without documentation requirement
- Life-threatening calls get immediate response regardless of system input

**For Callers:** System helps speed up response, but trained dispatcher always makes the call about what resources to send.

**Oversight:**
- Weekly review of override rates
- Monthly audit of response times by priority level
- Quarterly review of calls where system suggestion differed significantly from dispatcher decision

**System Limitations:**
- Cannot assess caller tone or urgency beyond keywords
- May not recognize regional dialects or uncommon emergency descriptions
- Dispatcher training emphasizes trusting professional judgment over system

---

## Licensing & Permits

### Assistive | Business License Application

**System:** "Auto-approves when all requirements verified. Flags incomplete or complex applications for reviewer."

**Key disclosure:** "Automatic approval only when requirements clearly met. All edge cases get human review."

**View Full Statement**

**Service:** Business License Application Processing
**Agency:** [City] Business Licensing Department

**What This System Does:** Processes routine business license applications.

**AI's Role:**
- Verifies business address, zoning compliance, fee payment
- Auto-approves when ALL requirements met and no complications
- Flags for review: zoning questions, special permits needed, incomplete info

**Human Authority:**
- Licensing specialist reviews all flagged applications
- Specialist determines what additional documentation needed
- Specialist makes final determination on complex cases

**For Applicants:**
Auto-approved: License issued within 24 hours
Flagged: Email within 2 business days explaining next steps

**How to Challenge:**
- Request manual review: [email/phone]
- Appeal denial: [process link]
- All denials include specific reasons and required corrections

**Oversight:**
- Sample 5% of auto-approvals monthly for accuracy
- Track approval/denial rates by business type and neighborhood
- Quarterly bias review

---

## Education

### Advisory | Special Education Screening

**System:** "Flags students who may need evaluation. School team makes all decisions about assessment and services."

**Key disclosure:** "System identifies patterns, does not diagnose or determine eligibility."

**View Full Statement**

**Service:** Special Education Needs Identification
**Agency:** [District] Special Education Services

**What This System Does:** Helps identify students who may benefit from special education evaluation.

**AI's Role:**
- Analyzes attendance patterns, grades, behavioral referrals
- Flags students showing patterns associated with learning challenges
- Does NOT diagnose conditions or determine eligibility

**Human Authority:**
- Teacher or parent can request evaluation regardless of system flag
- School team (teachers, specialists, parents) review all flagged cases
- Licensed professionals conduct assessments and determine eligibility

**For Families:** System helps ensure no student is overlooked, but evaluation decisions involve you and school team, not the algorithm.

**Oversight:**
- Monthly review of flagged students by special education coordinator
- Annual bias audit by demographic group
- Parent feedback collected on referral process

**What This Is NOT:**
- Not a diagnosis tool
- Not an eligibility determination
- Cannot be used to deny parent-requested evaluations

---

## Housing & Inspection

### Advisory | Building Inspection Prioritization

**System:** "Ranks properties for inspection based on risk factors. Inspector decides final inspection schedule and findings."

**Key disclosure:** "System helps prioritize limited inspection resources. Does not determine pass/fail or penalties."

**View Full Statement**

**Service:** Building Safety Inspection Scheduling
**Agency:** [City] Building & Safety Department

**What This System Does:** Helps prioritize which properties get inspected when.

**AI's Role:**
- Ranks properties based on: building age, prior violations, complaint history, neighborhood risk factors
- Suggests inspection priority order
- Does NOT determine if property passes/fails or what penalties apply

**Human Authority:**
- Inspector can move urgent cases up in queue
- Inspector conducts all inspections and makes findings
- Inspector determines violations and required corrections

**For Property Owners:**
- You can request inspection regardless of system priority
- System ranking does not affect inspection standards or outcomes
- All violations and penalties determined by licensed inspector

**Oversight:**
- Monthly review: are high-priority properties actually higher risk?
- Quarterly demographic analysis to prevent biased targeting
- Annual review of inspection outcomes vs. system predictions

**Transparency:**
- Ranking factors publicly documented
- Property owners can request their property's risk score
- System logic published at [URL]

---

### Assistive | Housing Assistance Eligibility

**System:** "Verifies income and household size. Auto-approves clear cases. Housing specialist reviews complex situations."

**Key disclosure:** "Automatic approval only when income verified and household composition clear. All edge cases get human review."

**View Full Statement**

**Service:** Section 8 Housing Choice Voucher Eligibility
**Agency:** [City] Housing Authority

**What This System Does:** Determines initial eligibility for housing assistance.

**AI's Role:**
- Verifies income through database checks (employment, tax records)
- Confirms household size and composition
- Auto-approves when: income clearly below threshold, household verified, no complications
- Flags: income near threshold, household composition questions, special circumstances

**Human Authority:**
- Housing specialist reviews all flagged applications
- Specialist assesses special circumstances (medical expenses, childcare costs)
- Specialist makes final determination on complex cases

**For Applicants:**
If auto-approved: Notification within 5 days, move to waitlist
If flagged: Specialist contacts you within 10 days for additional info

**How to Challenge:**
- Request manual review: [phone/email]
- Provide additional documentation at any time
- Appeal denial through [process]
- Free legal assistance available at [organization]

**Oversight:**
- Sample auto-approvals for accuracy
- Monitor denial rates by demographic group
- Track how often manual review overturns auto-decision

**System Limitations:**
- Cannot verify unreported income
- Cannot assess special hardship circumstances
- May miss household composition changes
- These require specialist review

---

## More Examples Coming Soon

We're adding templates for:

* **Healthcare:** Prior authorization, hospital bed allocation, Medicaid service approvals
* **Immigration:** Visa screening, case prioritization
* **Employment:** Civil service hiring, promotion eligibility
* **Emergency Services:** Ambulance routing, disaster relief allocation

Have an example to contribute? [Share it here](/AI-enablement/contribute.html)

---

## Using These Templates

1. **Choose the example closest to your use case**
2. **Adapt the structure** - keep sections, change content to match your system
3. **Be specific** - real numbers, real contact info, real processes
4. **Be honest** - if accuracy is unknown, say so. If humans rubber-stamp, don't claim review
5. **Publish it** - put it where people use your service (/ai or /transparency)
6. **Share back** - submit your real implementation so others can learn

---

[View Full Frameworks](/AI-enablement/frameworks.html) [Contribute Your Example](/AI-enablement/contribute.html)

Public domain. CC0. State Capacity AI.
