from deep_translator import GoogleTranslator
import polib

# Load the .po file
po_file = 'translations/fr/LC_MESSAGES/messages.po'
po = polib.pofile(po_file)

# Specify target language (e.g., French)
target_language = 'fr'

# Translate each entry
translator = GoogleTranslator(source='en', target=target_language)

for entry in po:
    if not entry.msgstr:  # Only translate if msgstr is empty
        entry.msgstr = translator.translate(entry.msgid)
        print(f"Translated: {entry.msgid} -> {entry.msgstr}")

# Save the updated .po file
po.save(po_file)
print(f"Translation completed and saved to {po_file}")
