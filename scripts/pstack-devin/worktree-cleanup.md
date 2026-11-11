### Worktree and simulator cleanup

1. List worktrees with git worktree list --porcelain. For each candidate, check its exact branch, untracked and modified files, merge state relative to the intended base, and open PRs. Report space estimates.
2. Cross-check use against the user's active sessions or an explicitly supplied export. Record unknown activity as unknown. Retain the main worktree, active worktrees, and any tree with uncertain ownership.
3. Show the exact proposed removals and wait for approval covering those paths. Use git worktree remove for each approved clean worktree. If it refuses, report why and retain it.
4. Inventory simulator or cache storage separately when requested. Verify the exact targets and their ownership before proposing removal. Report actual reclaimed space and retained targets.
