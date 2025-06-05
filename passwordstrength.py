import re

# Simple common password list (for demo)
common_passwords = ['password', '123456', '123456789', 'qwerty', 'abc123', 'letmein']

def check_password_strength(password):
    score = 0
    issues = []

    if len(password) >= 12:
        score += 1
    else:
        issues.append("Password should be at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        issues.append("Add at least one special character (!@#$ etc).")

    if password.lower() not in common_passwords:
        score += 1
    else:
        issues.append("Password is too common. Try something unique.")

    return score, issues

# Main loop
while True:
    user_password = input("🔐 Enter your password: ")
    score, issues = check_password_strength(user_password)

    if score == 6:
        print("\n✅ Great! This looks like a strong password.")
        print("🎉 Nice work choosing a secure one!\n")
        choice = input("🔁 Do you want to test another password? (yes/no): ").strip().lower()
        if choice != "yes":
            print("👋 Stay safe! Goodbye.")
            break
    else:
        print("\n❌ Password is not strong enough. Here's what to fix:")
        for issue in issues:
            print(f" - {issue}")
        print("🔁 Try again.\n")
