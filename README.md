# About the IDA Pro Translator plugin

The IDA Pro translator is a plugin for IDA Pro that assists in decoding arbitrary character sets in an IDA Pro database into Unicode, then automatically invoking a web-based translation service (currently Google Translate) to translate that foreign text into English. While newer versions of IDA Pro include support for Unicode, this support is limited to text encoded in UTF-8 and UTF-16, and the font support for display is limited.

## Installation

### Prerequisites

1. IDA (of course), version 6.3 or above
2. Python 2.7 or above, as bundled with IDA)
3. IDAPython (1.5.3 or later, as bundled with IDA Pro)
4. [PySide Python-Qt bindings](https://www.hex-rays.com/products/ida/support/download.shtml).
5. [The Python chardet module](http://pypi.python.org/pypi/chardet).
6. Appropriate fonts for the scripts you will encounter in your IDA databases. For example, to ensure you have the fonts required to display Chinese text in Windows XP, install the East Asian font pack. If you don't have a font to display the text, you will just see the Unicode fallback character (a rectangle on Windows).
7. (optional) [A Google Translate API key](https://code.google.com/apis/console/b/0/) if you want to use the automatic translation feature.

Once the prerequisites are installed, drop the translator.py file into your IDA 6.x plugins directory. Launch IDA and you will now have a new entry in Edit->Plugins named "Translations". Select the menu item or hit the hot key `Ctrl-Alt-R`. The first time the plugin is launched, it will ask for your Google Translate API key. Get one from [Google's API page](https://code.google.com/apis/console/b/0/) and enter it into this dialog box.

Now the Translate plugin is initialized. Upon launch it will create a new dockable top-level window named "Translations". Every time the plugin's hotkey (`Ctrl-R`) is invoked and a new translation is created, it will be added to this window. Translations are stored in the IDB database and so are persistent across restarts of IDA, even across machines.

The translation dialog is invoked by using the `Ctrl-R` keyboard shortcut. By default, the plugin will start scanning for a string beginning at the first byte under the cursor until the next NULL byte. Note that, in many cases, IDA tries really hard to make "strings" out of byte sequences in the data section. The default algorithm in the plugin is to stop the string once a new "defined" item (ie. a named entity) is encountered. Therefore, be sure to undefine any errant strings before hitting the hotkey, or highlight the extent of the string manually before hitting `Ctrl-R`. If, for some reason, the default algorithm fails to detect the string length properly, you can also highlight the full string in IDA and then hit `Ctrl-R` and the Translator will use the highlighted range instead.

The translation dialog will display the character set that was automatically detected, and the string is displayed in the top text box. If the character set was incorrectly detected, you can pull down the drop down and try a different character set. The text box will update automatically. Once the text encoding has been correctly determined, you can click the "Google Translate" button to translate the text into English. The translation is shown in the bottom text box.

Both the original text box and the translated text box are editable, so if a manual translation is available, or if the translation is incomprehensible, then you can manually edit the translation. Now that the translation is available, you can click the OK button to add a comment to the IDB file and create a named cross-reference. An entry will be added to the Translations window as well.

In the Translations window, you can copy individual translations to the clipboard buffer by using `Ctrl-C` or right-clicking and selecting `Copy`. You can also export the entire list of translations to a CSV file with the `Shift-Ins` shortcut key.

## Technical details

The translations are stored in an IDA "array", which is actually just an abstraction over the IDA "netnode" structure. The netnodes are stored in the IDB file, so they are persistent across invocations.

In Windows, your Google Translate API key is stored in your user's AppData folder under Hex-Rays\IDA Pro.
