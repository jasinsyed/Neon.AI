import importlib.metadata

required_packages = [
    "python-dotenv",
    "groq",
    "AppOpener",
    "pywhatkit",
    "bs4",
    "Pillow",
    "rich",
    "requests",
    "keyboard",
    "cohere",
    "googlesearch-python",
    "selenium",
    "mtranslate",
    "pygame",
    "edge-tts",
    "PyQt5",
    "webdriver-manager"
]

installed_packages = {pkg.metadata["Name"].lower() for pkg in importlib.metadata.distributions()}
missing_packages = [pkg for pkg in required_packages if pkg.lower() not in installed_packages]

if missing_packages:
    print("Missing packages:", missing_packages)
else:
    print("All packages are installed.")

   