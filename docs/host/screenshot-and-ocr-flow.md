# Screenshot and OCR Flow

Screenshot and OCR results always begin as `unverified_extraction`. Low-confidence fields also require confirmation even when the overall response confidence is high.

The user may confirm, correct, or reject the extraction. Confirmation is hash-bound to the extraction result. Confirmed data becomes `user_verified`; corrected data becomes `user_corrected`; rejected data becomes `failed`. Only usable statuses can influence recommendations.
