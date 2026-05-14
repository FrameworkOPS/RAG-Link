# Framework OPS Knowledge Base

Obsidian vault for Framework OPS LLC — fractional COO playbooks, client briefs, and engagement materials.

## Structure

| Folder | Contents |
|---|---|
| `_templates/` | Obsidian note templates — SOP, client brief, meeting notes |
| `playbooks/` | Generic operator knowledge — KPIs, benchmarks, cash flow, SOP/automation/tech-stack frameworks |
| `business/` | Framework OPS internal — service tiers, engagement process, ICP, proposal/onboarding/diagnostic templates, positioning |
| `clients/` | Per-client project briefs |
| `meetings/` | Meeting notes, organized by client |

## Workflow

1. New writeup needed → describe it to Claude in chat.
2. Claude writes the markdown and pushes it to this repo.
3. Run `git pull` (or let the Obsidian Git plugin auto-pull) → the note appears in your vault.

Point Obsidian at the `knowledge-base/` folder as the vault root so the code in the rest of the repo stays hidden.
