import streamlit as st
import math
import string


st.set_page_config(
    page_title="Password Security Analyzer",
    page_icon="🔐"
)


def calculate_entropy(password):
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.1f} seconds"

    minutes = seconds / 60

    if minutes < 60:
        return f"{minutes:.1f} minutes"

    hours = minutes / 60

    if hours < 24:
        return f"{hours:.1f} hours"

    days = hours / 24

    if days < 365:
        return f"{days:.1f} days"

    years = days / 365

    if years < 1000:
        return f"{years:.1f} years"

    if years < 1_000_000:
        return f"{years / 1000:.1f} thousand years"

    return f"{years:.1e} years"


def analyze_password(password):
    entropy = calculate_entropy(password)

    # Illustrative high-speed offline guessing assumption.
    guesses_per_second = 1_000_000_000

    possible_combinations = 2 ** entropy

    average_guesses = possible_combinations / 2

    seconds = average_guesses / guesses_per_second

    if entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return entropy, seconds, strength


# -------------------------
# Streamlit UI
# -------------------------

st.title("🔐 Password Security Analyzer")

st.write(
    "Analyze the strength of a password and estimate "
    "how long a hypothetical high-speed offline guessing "
    "attack could take."
)

password = st.text_input(
    "Enter your password",
    type="password"
)

show_password = st.checkbox("Show password")

if show_password:
    st.info("Password visibility is controlled by the input field above.")

if password:

    entropy, seconds, strength = analyze_password(password)

    st.subheader("Security Analysis")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Length", len(password))

    with col2:
        st.metric("Entropy", f"{entropy:.1f} bits")

    with col3:
        st.metric("Strength", strength)

    st.divider()

    st.subheader("⏱️ Estimated Guessing Time")

    st.success(format_time(seconds))

    st.caption(
        "This is an illustrative estimate based on an assumed "
        "offline guessing rate. Real-world attack times vary "
        "greatly depending on the password, hashing method, "
        "hardware, and attack strategy."
    )

    st.subheader("Password Characteristics")

    checks = {
        "Lowercase letters": any(c.islower() for c in password),
        "Uppercase letters": any(c.isupper() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Special characters": any(
            c in string.punctuation for c in password
        ),
        "At least 12 characters": len(password) >= 12
    }

    for name, passed in checks.items():
        if passed:
            st.write("✅", name)
        else:
            st.write("❌", name)

    st.subheader("💡 Suggestions")

    if len(password) < 12:
        st.warning("Use a longer password or passphrase.")

    if not any(c.isupper() for c in password):
        st.write("• Add uppercase letters.")

    if not any(c.islower() for c in password):
        st.write("• Add lowercase letters.")

    if not any(c.isdigit() for c in password):
        st.write("• Add numbers.")

    if not any(c in string.punctuation for c in password):
        st.write("• Add special characters.")

    if entropy >= 60:
        st.success("Your password has relatively high estimated entropy.")
