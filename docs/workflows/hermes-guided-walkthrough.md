# Hermes Guided Walkthrough

Capital Decision Lab can walk a user from current portfolio through thesis, evidence gathering, Bayesian updates, Kelly sizing, convexity, margin safety, model health, a model-implied recommendation, and a user-authorized record.

The opening loop asks for a portfolio snapshot, thesis, and available evidence. It then resolves missing fields through explicit mini-loops. Retrieved values carry source URLs or artifact hashes, retrieval timestamps, methods, confidence, verification status, and limitations.

Recommendations remain separate from authorization. The system can investigate and recommend, but it cannot execute a trade.
