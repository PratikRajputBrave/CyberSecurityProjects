# 🔍 Password strength Checker
<section class="password-checker" aria-labelledby="pw-checker-title">
  <h2 id="pw-checker-title">Password Strength Checker</h2>

  <label for="pw-input">Enter Password</label>
  <input
    type="password"
    id="pw-input"
    name="password"
    placeholder="Type your password"
    aria-describedby="pw-strength-msg"
    autocomplete="new-password"
    required
  />

  <div
    id="pw-strength-msg"
    role="status"
    aria-live="polite"
    class="strength-message"
  >
    <!-- Dynamic strength feedback appears here -->
  </div>

  <ul class="pw-rules" aria-label="Password requirements">
    <li id="rule-length" class="invalid">Minimum 8 characters</li>
    <li id="rule-uppercase" class="invalid">At least 1 uppercase letter</li>
    <li id="rule-lowercase" class="invalid">At least 1 lowercase letter</li>
    <li id="rule-number" class="invalid">At least 1 number</li>
    <li id="rule-special" class="invalid">At least 1 special character (!@#$%^&*)</li>
  </ul>
</section>

----------------------------------------------------------------------------------------------

# 🔍 Web Vulnerability Scanner (Basic)

A beginner-friendly Python tool to scan websites for common security issues:

- ✅ Open Ports (80, 443, 8080)
- 🛡️ Missing HTTP Security Headers
- 💉 Basic XSS Injection Testing (Reflected)

> ⚠️ For **educational purposes only**. Do not scan sites you don’t own or have permission to test.

---

## 📦 Features

- Written in pure Python
- CLI-based, interactive target entry
- Clear output of scan results
- Modular code for future expansion

---

## 🛠 Requirements

- Python 3.x
- Libraries:
  - `requests`
  


