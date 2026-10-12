Continue the existing Assignment 3 project. Apply this updated product
direction to the current implementation, then continue the remaining
autonomous project work.

Project root:
"/Users/jakebutler/Documents/ChatGPT/Mental Health"

The confirmed application name is now GUAC.

My existing authorization for implementation, necessary dependencies,
testing, commits, merges, public GitHub repository creation, and pushes
remains active. Do not ask again for these approvals.

CHECK

Read the current README, AGENTS.md, design notes, and handoff. Inspect
the actual implementation and Git state before editing.

Identify the files responsible for:
- Application branding and design tokens.
- Chat input, model context, and response handling.
- Exercise recommendations and navigation.
- The breathing balloon.
- Saved conversations, sessions, and preferences.
- Evaluation and milestone documentation.

Preserve completed work and implement this revision in the existing
project. Keep the current project folder and working setup.

TAKE ACTION

1. RENAME THE APPLICATION GUAC

Use Guac throughout the visible interface, page title, application
metadata, current documentation, and provider application header.

Create a distinctive Guac wordmark and simple custom avocado mark.
Keep historical milestone evidence and source references accurate.

2. MAKE THE CONVERSATION RECOMMEND A RELEVANT EXERCISE

The conversation should interpret what the person says they are feeling,
consider the immediate context, briefly reflect it back, and recommend
either breathing or grounding with a short explanation.

Use these tentative product rules:
- Feeling wound up, tense, or keyed up may lead to breathing, with a
  steady rhythm as the reason.
- Feeling scattered or stuck in repetitive thoughts may lead to
  grounding, with noticing the present surroundings as the reason.
- An explicit preference overrides the inferred recommendation.
- “No breathing” must not produce a breathing recommendation.
- For vague or mixed input, ask at most one optional clarification.
  Keep both exercises directly available.
- Accept “neither,” corrections, and requests to stop without persuasion.

Use contextual interpretation, not a single-keyword lookup or the same
generic response every time. Avoid diagnoses, clinical scores, certainty
about hidden feelings, or promises that an exercise will fix the problem.

Return a short reflection, a structured recommended skill, and a concise
user-visible reason. Validate the response in application code. Keep the
model request small and normally return the reply and recommendation
together in one request.

Show a clear primary action for the recommendation and an easy alternative.
Starting an exercise always requires the person’s deliberate selection.
They can also begin either exercise without chatting.

A delayed model response must not interrupt an exercise already started.
On model failure, both exercise actions and support access remain usable.

3. APPLY THE AVOCADO VISUAL SYSTEM

Use these initial tokens:
- Peel: #243D25
- Leaf: #4D7137
- Flesh: #DCE8AD
- Lime: #B8D45B
- Cream: #FAF8EF
- Pit: #8B563B

Make Guac fun, joyful, exciting, professional, and bespoke through
original composition, warm typography, avocado-inspired shapes,
thoughtful writing, and polished interaction.

Use dark peel text on light surfaces and cream text on leaf-green buttons.
Verify actual rendered contrast and interaction states.

Make the conversation the main focus, with a contextual recommendation
panel when useful. Put essential interaction before decoration on mobile.

Use one clear primary action per state, consistent spacing, readable
labels, generous tap targets, visible keyboard focus, predictable
navigation, and immediate feedback.

Keep history and preferences available through progressive disclosure.
Avoid mandatory onboarding, mood questionnaires, or repeated questions.

Match the response tone to what the person shares. Keep active exercises
visually focused while retaining Guac’s welcoming identity.

4. UPDATE THE BALLOON

Use avocado green as the new default. Keep red available in the optional
color picker and preserve an explicitly saved color.

Retain the hyperrealistic latex material, convincing volume, highlights,
shading, knot, and smooth shape changes.

Preserve:
- Four-second inhale.
- Six-second exhale.
- Six cycles.
- Application-clock timing.
- Synchronized pause and resume.
- Immediate stopping.
- An equally timed reduced-motion alternative.

Keep color selection outside active breathing.

5. PRESERVE THE ASSIGNMENT REQUIREMENTS

Continue using Vue, FastAPI, SQLite, and the verified class model setup.

Preserve conversation/session history, user control, the exact grounding
sequence, exercise-duration requirements, independent support access,
fictional evaluation, evidence, milestone reports, and AI-use disclosure.

Save enough information to distinguish what Guac recommended from what
the person actually chose. Do not add inferred clinical profiles or
emotion scores to history.

VERIFY

Run the relevant existing checks and add meaningful coverage for:
- A contextual breathing recommendation.
- A contextual grounding recommendation.
- Negated preferences and corrected feelings.
- Vague input without mandatory questioning.
- Current choices overriding saved preferences.
- Accepting or choosing the alternative in one action.
- Unsupported model recommendations.
- Late responses and provider failure.
- Accurate persistence and unchanged exercise timing.

Inspect the real interface on desktop and narrow mobile layouts.
Check the software-keyboard layout, keyboard navigation, contrast,
touch controls, reduced motion, and balloon appearance.

Refine the visual result after inspection. Compilation alone does not
establish that the design is finished.

Update the design rationale, evaluation evidence, current documentation,
and handoff. Then continue the remaining authorized project phases
through the verified public GitHub push.