<!-- Password Strength Checker Component -->
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
