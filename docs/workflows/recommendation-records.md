# Recommendation Records

A recommendation contains the hashes of the portfolio, belief state, evidence synthesis, Kelly analysis, convexity analysis, margin analysis, and model-health result. It also records current exposure, target exposure, delta, reason codes, confidence, and limitations.

Recording requires a separate human-confirmed authorization bound to the recommendation hash. The local append is atomic and identical replay is idempotent. No recommendation executes an order.
