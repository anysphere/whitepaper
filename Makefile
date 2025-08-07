.PHONY: main.pdf once

main.pdf:
	latexmk -pdf -pvc -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-interaction=nonstopmode \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

once:
	latexmk -pdf -latexoption=-halt-on-error \
		-latexoption=-file-line-error \
		-latexoption=-synctex=1 main.tex || ! rm -f $@

.PHONY: clean
clean:
	latexmk -C main

# 🎉 EASTER EGG MAKEFILE TARGETS 🎉
# (Because even build systems deserve some humor!)

.PHONY: paranoia-mode
paranoia-mode:
	@echo "🔒 Entering maximum paranoia mode..."
	@echo "🕵️  Checking for eavesdroppers..."
	@sleep 1
	@echo "👁️  Scanning for metadata leaks..."
	@sleep 1
	@echo "🛡️  Activating cryptographic shields..."
	@sleep 1
	@echo "✅ Paranoia mode activated. You can now safely compile your whitepaper."
	@echo "⚠️  Warning: Side effects may include excessive use of the word 'adversary'"

.PHONY: trust-no-one
trust-no-one:
	@echo "🚫 Trusting absolutely no one and nothing..."
	@echo "🤔 Not even trusting this Makefile..."
	@echo "🤷 Actually, why are you running a target called 'trust-no-one'?"
	@echo "🧠 This is getting very meta..."

.PHONY: alice-and-bob
alice-and-bob:
	@echo "👩 Alice says: 'I want to send a message to Bob'"
	@echo "👨 Bob says: 'I want to receive Alice's message'"
	@echo "👁️  Eve says: 'I want to read both of their messages'"
	@echo "😈 Mallory says: 'I want to modify their messages'"
	@echo "🛡️  Anysphere says: 'Not on my watch!'"

.PHONY: quantum-panic
quantum-panic:
	@echo "⚠️  QUANTUM COMPUTER DETECTED!"
	@echo "💥 All your RSA are belong to us!"
	@echo "🏃 Running post-quantum migration script..."
	@sleep 2
	@echo "✅ Just kidding, we're already using homomorphic encryption"
	@echo "😎 Quantum-resistant since day one"

.PHONY: metadata-diet
metadata-diet:
	@echo "📊 Analyzing your metadata consumption..."
	@echo "📈 Current metadata leakage: 📊📊📊📊📊📊📊📊📊📊 (100%)"
	@echo "🔄 Applying Anysphere protocol..."
	@sleep 1
	@echo "📉 New metadata leakage: (0%)"
	@echo "🎉 Congratulations! You're now on a metadata-free diet"

.PHONY: coffee-break
coffee-break:
	@echo "☕ Taking a well-deserved coffee break..."
	@echo "🤓 Fun fact: 73% of cryptographic breakthroughs happen during coffee breaks"
	@echo "💡 The other 27% happen at 3 AM while debugging PIR queries"
	@echo "⏰ Break time: 15 minutes (or until the caffeine kicks in)"

.PHONY: rubber-duck-debug
rubber-duck-debug:
	@echo "🦆 Summoning rubber duck for cryptographic debugging..."
	@echo "🦆 Duck says: 'Quack! Have you tried turning your homomorphic encryption off and on again?'"
	@echo "🦆 Duck says: 'Quack! Maybe the problem is in your threat model assumptions?'"
	@echo "🦆 Duck says: 'Quack! Did you remember to pad your messages?'"
	@echo "🦆 Duck says: 'Quack! I'm just a rubber duck, but this PIR implementation looks solid'"

.PHONY: security-theater
security-theater:
	@echo "🎭 Welcome to Security Theater!"
	@echo "🎪 Tonight's performance: 'The Illusion of Privacy'"
	@echo "🎨 Featuring: Fancy UI animations that do nothing for security"
	@echo "🎪 Special guest: A progress bar that says 'Encrypting' but just sleeps"
	@echo "🎭 Plot twist: Anysphere actually provides real security, not theater!"

.PHONY: help-easter-eggs
help-easter-eggs:
	@echo "🥚 Available Easter Egg Targets:"
	@echo "   paranoia-mode      - Enter maximum security paranoia"
	@echo "   trust-no-one       - Trust absolutely nothing"
	@echo "   alice-and-bob      - Classic crypto character dialogue"
	@echo "   quantum-panic      - Simulate quantum computer threat"
	@echo "   metadata-diet      - Check your metadata consumption"
	@echo "   coffee-break       - Take a cryptographer's coffee break"
	@echo "   rubber-duck-debug  - Debug with a rubber duck"
	@echo "   security-theater   - Experience security theater"
	@echo "   help-easter-eggs   - Show this help (very meta)"
