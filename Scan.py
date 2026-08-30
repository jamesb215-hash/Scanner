import os
import re

print("==============================")
print("   SIMPLE LINK SAFETY SCANNER")
print("==============================\n")

# Safe domains
safe_domains = [
    "google.com",
    "classroom.google.com",
    "youtube.com",
    "github.com",
    "microsoft.com"
]

# Dangerous signs in links
dangerous_signs = [
    ".exe", ".scr", ".bat", ".zip", ".ru", 
    "@", "bit.ly", "tinyurl"
]

def scan_link(link):
    link = link.lower()
    print(f"Scanning: {link}\n")

    # Check if safe domain
    for safe in safe_domains:
        if safe in link:
            print(f"✓ Contains trusted domain: {safe}")
            print("Result: SAFE - Official link")
            return

    # Check for dangerous signs
    for sign in dangerous_signs:
        if sign in link:
            print(f"! Found suspicious pattern: {sign}")
            print("Result: DANGEROUS - Blocked!")
            return
    
    # Check for https
    if not link.startswith("https://"):
        print("! Not using https://")
        print("Result: WARNING - Not secure")
    else:
        print("Result: UNKNOWN - Use caution, not in trusted list")

# --- TEST YOUR LINK HERE ---
scan_link("")
