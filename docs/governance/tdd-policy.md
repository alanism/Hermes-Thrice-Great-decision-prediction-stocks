# Red/green policy

Each behavior begins with a focused failing test. The failure is captured before implementation. The smallest in-scope behavior is then added, the focused suite is rerun, and relevant mutation probes must detect their injected faults before the next slice begins.

Harness rules are not weakened to make implementation pass.

