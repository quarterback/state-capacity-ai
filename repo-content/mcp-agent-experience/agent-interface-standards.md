# Agent Interface Standards for Public Service Systems

**Version 1.0 Draft**

## Purpose of the Standard

Public service systems now receive requests from human users and from autonomous agents that act on behalf of those users. This standard establishes clear rules for agent interaction with public systems. It supports reliability, clarity, fairness, and traceability across all service types, including benefits programs, licensing systems, adjudication systems, and resource allocation tools.

The standard creates a unified approach for policy expression, action surfaces, handoff rules, audit trails, and context delivery. Agencies adopt this framework to ensure dependable behavior from agents and consistent accountability within government services.

## Part One: Policy Logic as Versioned Interfaces

Agents operate through logic that must remain stable and readable across time. Policy logic therefore requires a versioned and structured interface with the following properties:

### 1. Canonical Representation of Policy

The agency publishes a single authoritative expression of policy rules. This representation is machine-readable, human-readable, and consistent across programs. It includes eligibility rules, procedural steps, and outcomes that depend on user-supplied facts.

### 2. Version Control Requirements

Every update to policy logic receives a unique version identifier. Agents carry this identifier within all determinations. Appeals, reviews, or audits refer directly to the version in force at the time of the determination.

### 3. Reasoning Attachments

Agents attach a reasoning file to each action. The file includes inputs, policy version applied, rule path selected, and intermediate steps used to reach the outcome. This attachment supports fairness, transparency, and future oversight.

## Part Two: Action Surfaces for Agent Interaction

Agents require clear surfaces for action. Action surfaces describe what an agent may do within the system and the context required for the action.

### 1. Definition of Action Types

The agency publishes all allowed action types, such as data retrieval, submission of forms, updates to case records, scheduling of appointments, and execution of procedural steps. Each action has a complete schema for inputs and outputs.

### 2. Context Requirements

Each action describes mandatory context that an agent supplies with the request. Examples include identity attributes, case identifiers, data provenance, and user consent documentation.

### 3. Outcome Rules

The agency defines the full range of outcomes for each action. These outcomes include successful completion, incomplete information, policy restriction, human review requirement, and procedural hold states.

### 4. Escalation Conditions

The system identifies conditions that require escalation to a human caseworker. These conditions include ambiguous information, user distress, rights-related determinations, or signals of hardship. Escalation creates a handoff object that contains all relevant agent reasoning.

## Part Three: Handoff Protocols Between Agents and Caseworkers

Agents support human workers through structured transition moments.

### 1. Triggers for Handoff

The agency specifies clear triggers, such as uncertainty thresholds, procedural transitions, legal significance of the action, or user request for human assistance.

### 2. Handoff Package Structure

The handoff object contains four required elements:
- the agent reasoning file
- the data inputs
- the policy version
- the full action history with timestamps

### 3. Caseworker Response Path

Upon handoff, a caseworker receives a queue entry with a complete overview of the agent activity. The caseworker may proceed with a determination, request further data, or return instructions to the agent.

### 4. Restoration of Context for Users

The system restores human-readable context at the moment of handoff. This includes summary information free from jargon, clear next steps, and record of actions already completed.

## Part Four: Audit Trails for Public Accountability

Public trust depends on full traceability. The agent interface standard requires durable audit trails that record every step.

### 1. Complete Reasoning History

Every agent action creates an entry with reasoning, version identifiers, all values supplied by the user, and all intermediate decisions. These entries join into a chain of reasoning for the entire case.

### 2. Policy Version Anchoring

Each determination references the specific policy version in force. Appeals cannot proceed without this anchor.

### 3. Temporal Record

Every action has a timestamp. Every update has a timestamp. The system stores these records permanently under the archival schedule for the program.

### 4. Rights Review Path

Any person may request an explanation of an outcome. The system can reconstruct the full reasoning path, including policy version and case facts.

## Part Five: Context Delivery Requirements for Agents

Agents operate best when they receive structured context that aligns with system rules.

### 1. Structured Data Access

Agents receive access to data through clearly defined schemas. These schemas support precise interpretation and reduce ambiguity. Each schema describes ownership, sensitivity level, and required consent.

### 2. Machine-Oriented Documentation

The system includes documentation that supports agent comprehension. This includes step sequences, common cases, examples, and error guidance in plain structured text.

### 3. Stable Interaction Patterns

The agency maintains predictable patterns for system interaction. Stable patterns allow strong performance from agents and reduce friction across services.

### 4. Consent and Authorization Flow

Every agent action includes explicit user consent. The system confirms identity, makes a complete record of the consent event, and attaches this record to all relevant reasoning files.

## Part Six: Public Value Principles for Agent-Mediated Systems

This standard grounds agent use in civic purpose.

### 1. Equity of Access

Agents may support users across many abilities, languages, or literacy levels. The system ensures that agent-mediated paths offer the same rights and due process as human-mediated paths.

### 2. Clarity for the Public

Every agent-mediated service includes a clear public explanation of what the agent can do and what remains the responsibility of human workers.

### 3. Protection of Human Judgment

Agents assist with precision, scale, and speed. Human workers retain judgment for areas that involve interpretation, empathy, or rights-related outcomes.

### 4. Continuous Review

The agency reviews agent interaction logs for drift, unfair patterns, and systemic distortion. This review produces periodic public findings.
