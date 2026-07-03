# Capability Injection

Supported host capabilities are `browser_current_page`, `browser_fetch_url`, `browser_extract_selection`, `screenshot_capture`, `screenshot_ocr`, `authenticated_session_fetch`, `local_file_picker`, `clipboard_read`, and `user_confirmation`.

Each response records capability identity, retrieval method and time, URL or artifact reference when present, raw-content hash, payload, confidence, and limitations. Capital Decision Lab never stores service credentials. A missing capability returns an actionable blocked state.
