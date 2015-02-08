#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
from PySide import QtUiTools
from idaapi import PluginForm
import urllib
import json
import idc
import bisect
import pickle
import os
import collections

import chardet

import json

import string
import csv

"""
The user interface of the Translation Plugin. Mostly auto-generated from Qt
Designer, with some custom tweaks.
"""
class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(487, 732)
		self.verticalLayout_4 = QtGui.QVBoxLayout(Dialog)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.groupBox = QtGui.QGroupBox(Dialog)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(2)
		sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
		self.groupBox.setSizePolicy(sizePolicy)
		self.groupBox.setObjectName("groupBox")
		self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label = QtGui.QLabel(self.groupBox)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
		self.label.setSizePolicy(sizePolicy)
		self.label.setObjectName("label")
		self.horizontalLayout.addWidget(self.label)
		self.encodingComboBox = QtGui.QComboBox(self.groupBox)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.encodingComboBox.sizePolicy().hasHeightForWidth())
		self.encodingComboBox.setSizePolicy(sizePolicy)
		self.encodingComboBox.setObjectName("encodingComboBox")
		self.horizontalLayout.addWidget(self.encodingComboBox)
		self.verticalLayout.addLayout(self.horizontalLayout)
		self.originalTextBox = QtGui.QPlainTextEdit(self.groupBox)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(2)
		sizePolicy.setHeightForWidth(self.originalTextBox.sizePolicy().hasHeightForWidth())
		self.originalTextBox.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(14)
		self.originalTextBox.setFont(font)
		self.originalTextBox.setObjectName("originalTextBox")
		self.verticalLayout.addWidget(self.originalTextBox)
		self.horizontalLayout_2 = QtGui.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")

###
# TODO: add custom font support
#		self.label_2 = QtGui.QLabel(self.groupBox)
#		self.label_2.setObjectName("label_2")
#		self.horizontalLayout_2.addWidget(self.label_2)
#		self.fontComboBox = QtGui.QFontComboBox(self.groupBox)
#		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
#		sizePolicy.setHorizontalStretch(0)
#		sizePolicy.setVerticalStretch(0)
#		sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
#		self.fontComboBox.setSizePolicy(sizePolicy)
#		self.fontComboBox.setObjectName("fontComboBox")
#		self.horizontalLayout_2.addWidget(self.fontComboBox)
#		self.fontSizeSpinBox = QtGui.QSpinBox(self.groupBox)
#		self.fontSizeSpinBox.setObjectName("fontSizeSpinBox")
#		self.horizontalLayout_2.addWidget(self.fontSizeSpinBox)
###

		self.verticalLayout.addLayout(self.horizontalLayout_2)
		self.verticalLayout_4.addWidget(self.groupBox)
		self.translateButton = QtGui.QPushButton(Dialog)
		self.translateButton.setObjectName("translateButton")
		self.verticalLayout_4.addWidget(self.translateButton)
		self.translatedTextBox = QtGui.QPlainTextEdit(Dialog)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.translatedTextBox.sizePolicy().hasHeightForWidth())
		self.translatedTextBox.setSizePolicy(sizePolicy)
		font = QtGui.QFont()
		font.setFamily("MS Shell Dlg 2")
		font.setPointSize(8)
		self.translatedTextBox.setFont(font)
		self.translatedTextBox.setObjectName("translatedTextBox")
		self.verticalLayout_4.addWidget(self.translatedTextBox)
		self.horizontalLayout_3 = QtGui.QHBoxLayout()
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.verticalLayout_2 = QtGui.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.commentCheckBox = QtGui.QCheckBox(Dialog)
		self.commentCheckBox.setObjectName("commentCheckBox")
		self.verticalLayout_2.addWidget(self.commentCheckBox)
		self.nameXrefCheckBox = QtGui.QCheckBox(Dialog)
		self.nameXrefCheckBox.setObjectName("nameXrefCheckBox")
		self.verticalLayout_2.addWidget(self.nameXrefCheckBox)
		self.horizontalLayout_3.addLayout(self.verticalLayout_2)
		spacerItem = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
		self.horizontalLayout_3.addItem(spacerItem)
		self.verticalLayout_3 = QtGui.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.buttonBox = QtGui.QDialogButtonBox(Dialog)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.verticalLayout_3.addWidget(self.buttonBox)
		self.horizontalLayout_3.addLayout(self.verticalLayout_3)
		self.verticalLayout_4.addLayout(self.horizontalLayout_3)

		self.retranslateUi(Dialog)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Translate Text", None, QtGui.QApplication.UnicodeUTF8))
		self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Original Text", None, QtGui.QApplication.UnicodeUTF8))
		self.label.setText(QtGui.QApplication.translate("Dialog", "Encoding:", None, QtGui.QApplication.UnicodeUTF8))
#		self.label_2.setText(QtGui.QApplication.translate("Dialog", "Font", None, QtGui.QApplication.UnicodeUTF8))
		self.translateButton.setText(QtGui.QApplication.translate("Dialog", "Google Translate", None, QtGui.QApplication.UnicodeUTF8))
		self.commentCheckBox.setText(QtGui.QApplication.translate("Dialog", "Add comment", None, QtGui.QApplication.UnicodeUTF8))
		self.nameXrefCheckBox.setText(QtGui.QApplication.translate("Dialog", "Add public name xref", None, QtGui.QApplication.UnicodeUTF8))


"""
Translation icon
"""
XLATE_ICON = (
	"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x14\x00\x00\x00\x14\x08\x06\x00\x00\x00\x8d\x89\x1d\r\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x00!tEXtSoftware\x00GraphicConverter (Intel)w\x87\xfa\x19\x00\x00\x02.IDATx\x9c\xcc\x94MHTq\x14\xc5\xdf\xaeM\x0b7-\xda\xb4h\xd3\xa2Mp\xdd(\r\xc5\x04\x15\x15T\x88P\x11B\x08)\xa2\x96FI_\x06R\x16T\xf4I\x84\x8b\xa4\x82h\x11\xd5&\xa2E\x11m**\xf3c\x9845m\x1a3-?\x98\x1c'?\xe2t\x8e(<\x9d\xbfo\\\xb8\xe8\xc2ax\xf0\xde\x8f{\xef9w\xbcH\xe3\x1bo1\xb5\xa8\xb0Y\xc0\xd0\xdb\t\xd8\xcb1\xd8\xd3\x11\xd8\xc3a\xd8\xbd_\xb0\xfa\x1f\xb0\x9b=\xb0\xab1\xd8\x85.\xd8\xd9\x0eX\xcdgXu+\xecX\x14\xa1\x13\x11\xcc\x0b\x14\xac09\x89\x82\xde\x14v\xb7%\x90\xffn\x10;\x9e\xf7a\xeb\xa386\xdd\xeeF\xf8Z;Bg\xa2\xc8\xa9jFv\xf1\x07X\xde{\xd8\xa1\x96\x00 ;\x13\xcc.\x8f\xc2j\xd9]u\x1cV\xd5\t\xab\xf8\x04+k\x81\x954\xc2\x8a\x1b`E\x84\xed'l-U\xd1\x14\x00\xe4\x98M\x00&\xa8?\xd4\xc0\xd8$\xcao5`\xdf\xf5\xd7\xd8{\xe9\x15v\x9d\x7f\x81\xbc\xdag\xd8^\xf3\x04[N>\xc6\xc6\xa3\x0f\x10>|\x1f\xa1\x83w\x11\xae\xbc\x83t w\xd6<\rKR\xfd\x04\n\x96\xa9R\xec \xbb\xa8\xce\x01\xa4\x01\x91i\xd8oj\x98Rgs\xcb\xf3\xbcY\xcf\xc9q`M\xe1\r\x07\x90nF}\xb0AJc\xce\x07\x9c\xf9Mp\xa4\xd5\x05W\x1c@F\xa3\xd5\x07\xfbIig3\x1f\xbb\xa4\x1aJ\x01\xab\xf6\\t\x00\x99\xb36\x1f\xac\x8f\x92\x01\x99j`\x14X\x99\x7f\xce\x01dh\xdb}\xb0\xef\x94\xdc\xf4\x8f:\xb7;U\xff\x08\xb0b\xe7i\x07\x90\x17\xd0\xe9\x83\xc5)E#S\xf5r\xe9\xcb\xb7\x9dr\x00yN_|\xb0\xaf\x94r6\xfe7x\x87\xf1\x04\xb0l\xf3q\x07\x90\xb7\xd9\xcd\x17b\xd47\xaa\x87Rh\x95\xb3\xa0\x8a\xd1\xc5\xac\rG\xd2\x81:t\xdd\xa6\xce\xc9\xcayf\xa5\x1f\x91SZ?\x95\xb3\xa0\xea\x1a\x02\x96\xae\xabL\x07\xba\xa4\x0bP\xce\x14\r\xb9)\x03\xb43\x8d\xa9\xce\x04\xeb`,\x96\xe4\x96-\x0c\x98[R7\x15Z\xe5L\xd1\x90\x9b2@;\xd3\x98\xeaL\xb0\xac\xf5\x07\x16\x06\xfc/\xfe\xb1\xff\x01\x00\x00\xff\xff\x03\x00\x831gE\x18\x18k\x00\x00\x00\x00\x00IEND\xaeB`\x82")

"""
The list of encodings that we recognize.
"""
default_encodings = [
 'ascii',
 'big5',
 'big5hkscs',
 'cp037',
 'cp424',
 'cp437',
 'cp500',
 'cp720',
 'cp737',
 'cp775',
 'cp850',
 'cp852',
 'cp855',
 'cp856',
 'cp857',
 'cp858',
 'cp860',
 'cp861',
 'cp862',
 'cp863',
 'cp864',
 'cp865',
 'cp866',
 'cp869',
 'cp874',
 'cp875',
 'cp932',
 'cp949',
 'cp950',
 'cp1006',
 'cp1026',
 'cp1140',
 'cp1250',
 'cp1251',
 'cp1252',
 'cp1253',
 'cp1254',
 'cp1255',
 'cp1256',
 'cp1257',
 'cp1258',
 'euc_jp',
 'euc_jis_2004',
 'euc_jisx0213',
 'euc_kr',
 'gb2312',
 'gbk',
 'gb18030',
 'hz',
 'iso2022_jp',
 'iso2022_jp_1',
 'iso2022_jp_2',
 'iso2022_jp_2004',
 'iso2022_jp_3',
 'iso2022_jp_ext',
 'iso2022_kr',
 'latin_1',
 'iso8859_2',
 'iso8859_3',
 'iso8859_4',
 'iso8859_5',
 'iso8859_6',
 'iso8859_7',
 'iso8859_8',
 'iso8859_9',
 'iso8859_10',
 'iso8859_13',
 'iso8859_14',
 'iso8859_15',
 'iso8859_16',
 'johab',
 'koi8_r',
 'koi8_u',
 'mac_cyrillic',
 'mac_greek',
 'mac_iceland',
 'mac_latin2',
 'mac_roman',
 'mac_turkish',
 'ptcp154',
 'shift_jis',
 'shift_jis_2004',
 'shift_jisx0213',
 'utf_32',
 'utf_32_be',
 'utf_32_le',
 'utf_16',
 'utf_16_be',
 'utf_16_le',
 'utf_7',
 'utf_8',
 'utf_8_sig',
 'mbcs',
 'palmos']


def getString(startea, endea):
	outstr = []
	for i in range(startea, endea):
		outstr.append(chr(Byte(i)))
	return ''.join(outstr)

def getUnicodeTranslatedString(startea, endea):
	thestr = getString(startea, endea)
	the_charset = chardet.detect(thestr)
	encoding = the_charset['encoding']

	return (encoding, thestr.decode(encoding))

def doTranslate(original_string, api_key):
		query_param = urllib.urlencode({'q': original_string.encode('utf8'), 'target': 'en', 'key': api_key})
		url = 'https://www.googleapis.com/language/translate/v2?' + query_param
		u = urllib.urlopen(url)
		d = u.read()
		u.close()

		json_decoder = json.JSONDecoder(encoding='utf-8')
		translation = json_decoder.decode(d)
		# take the first translation
		translated_string = translation['data']['translations'][0]['translatedText']
		return translated_string

"""
Model class that contains all of the translations performed in this IDB file.
The model is initialized when the plugin is initialized from an IDC array 
stored inside of the IDB file, so translations are persistent across IDA
invocations.
"""
class TranslateModel(QtCore.QAbstractTableModel):
	def __init__(self, parent = None):
		super(TranslateModel, self).__init__(parent)

		self.icon = QtGui.QPixmap()
		self.icon.loadFromData(XLATE_ICON, "PNG")

		# initialize from netnodes in the current idb file
		self.xlate_array = GetArrayId('translations')
		if self.xlate_array == -1:
			self.xlate_array = CreateArray('translations')

		self.translations = collections.OrderedDict()

		cur_ea = GetFirstIndex(AR_STR, self.xlate_array)
		while cur_ea != -1:
			entry = pickle.loads(GetArrayElement(AR_STR, self.xlate_array, cur_ea))
			self.translations[entry[0]] = entry
			cur_ea = GetNextIndex(AR_STR, self.xlate_array, cur_ea)

		print '[TranslatePlugin] Loaded %d translations' % len(self.translations)

	def rowCount(self, index=QtCore.QModelIndex()):
		return len(self.translations)

	def columnCount(self, index=QtCore.QModelIndex()):
		return 3

	def data(self, index, role=QtCore.Qt.DisplayRole):
		if not index.isValid():
			return None

		if not 0 <= index.row() < len(self.translations):
			return None

		if role == QtCore.Qt.DisplayRole:
			i = index.row()
			(address, original_string, translation) = self.translations.values()[i]

			if index.column() == 0:
				return '%08x' % address
			elif index.column() == 1:
				return original_string
			elif index.column() == 2:
				return translation
			else:
				return None

		if role == QtCore.Qt.FontRole:
			return QtGui.QFont().setPointSize(30)

		if role == QtCore.Qt.DecorationRole and index.column() == 0:
			return self.icon

	def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
		if role != QtCore.Qt.DisplayRole:
			return None

		if orientation == QtCore.Qt.Horizontal:
			if section == 0:
				return "Address"
			elif section == 1:
				return "Original String"
			elif section == 2:
				return "Translation"
			else:
				return None

	def addTranslation(self, ea, original_text, translated_text):
		element = (ea, original_text, translated_text)
		pos = bisect.bisect(self.translations.keys(), ea)
		if ea not in self.translations:
			# we're adding a new element
			self.beginInsertRows(QtCore.QModelIndex(), pos, pos)
			self.translations[ea] = element
			# Note: OrderedDict is not SortedDict
			self.translations = collections.OrderedDict(sorted(self.translations.iteritems(), key=lambda x: x[0]))
			self.endInsertRows()
		else:
			# modify existing element
			self.translations[ea] = element

		# add to idb
		SetArrayString(self.xlate_array, ea, pickle.dumps(element))


"""
Dialog box that is invoked when the hotkey is pressed. This dialog should have
no direct interactions with IDA, allowing it to be pulled out to other
applications. All interactions with IDA are handled by the Translator class
below.
"""
class TranslatorDialog(QtGui.QDialog):
	def __init__(self, parent, cfg):
		super(TranslatorDialog, self).__init__(parent)

		self.config = cfg
		self.callback_fn = None

		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.ui.commentCheckBox.setChecked(True)
		self.ui.nameXrefCheckBox.setChecked(True)

		self.ui.translateButton.clicked.connect(self.translateButtonPressed)
		self.accepted.connect(self.successCallback)
		self.ui.translatedTextBox.textChanged.connect(self.translatedTextChanged)

		self.detected_encoding = None
		self.previous_encoding = None

		self.isValidEncoding = False

	def translatedTextChanged(self):
		doc = self.ui.translatedTextBox.document()
		self.translated_text = doc.toPlainText()
		charCount = len(self.translated_text)
		if charCount == 0:
			self.enableTranslationCheckboxes(False)
		else:
			self.enableTranslationCheckboxes(True)

		self.translated_text = doc.toPlainText()

	def setEncoding(self, encoding):
		self.encoding = encoding
		new_text = ''
		try:
			new_text = self.original_text.decode(encoding)
			self.isValidEncoding = True
			self.ui.translateButton.setEnabled(True)
		except UnicodeDecodeError as e:
			new_text = "(Error: %s)" % (e,)
			self.ui.translateButton.setEnabled(False)
			self.isValidEncoding = False

		self.ui.originalTextBox.setPlainText(new_text)
		self.clearTranslatedText()

	def encodingChanged(self, new_encoding_idx):
		self.setEncoding(self.ui.encodingComboBox.itemData(new_encoding_idx))

	def translateButtonPressed(self):
		# call translate upon button press
		if self.isValidEncoding:
			translated_string = doTranslate(self.ui.originalTextBox.toPlainText(), self.config.getApiKey())
			self.setTranslatedText(translated_string)

	def setOriginalText(self, original_text, detected_encoding):
		self.original_text = original_text
		self.setEncoding(detected_encoding)

		self.initializeEncodingList(detected_encoding)

	def enableTranslationCheckboxes(self, flag):
		self.ui.commentCheckBox.setEnabled(flag)
		self.ui.nameXrefCheckBox.setEnabled(flag)

	def clearTranslatedText(self):
		self.setTranslatedText('')

	def setTranslatedText(self, translated_text):
		self.ui.translatedTextBox.setPlainText(translated_text)

	def registerSuccessCallback(self, fn):
		self.callback_fn = fn

	def successCallback(self):
		if self.callback_fn != None and self.isValidEncoding:
			self.callback_fn(self.translated_text, self.original_text.decode(self.encoding),
				self.ui.commentCheckBox.isChecked(), self.ui.nameXrefCheckBox.isChecked())

	def initializeEncodingList(self, detected_encoding):
		for s in default_encodings:
			self.ui.encodingComboBox.addItem(s, s)
		self.detected_encoding = detected_encoding
		self.ui.encodingComboBox.insertSeparator(0)
		self.ui.encodingComboBox.insertItem(0, "%s (auto-detected)" % detected_encoding, detected_encoding)
		self.ui.encodingComboBox.setCurrentIndex(0)
		self.isValidEncoding = True

		self.ui.encodingComboBox.currentIndexChanged.connect(self.encodingChanged)

"""
The controller class that mediates between the TranslateModel,
TranslatorDialog, and the translation functions (doTranslate, etc) that
perform the actual translation.
"""
class Translator(object):
	def __init__(self, parent, model, cfg):
		self.parent = parent
		self.model = model
		self.config = cfg

		self.deletechars=''.join([chr(x) for x in range(0,0x20) + range(0x21, 0x30) + range(0x3a, 0x41) \
			+ range(0x5b, 0x61) + range(0x7b, 0xff)])
		self.transtable = ''.join([chr(x) for x in range(0,256)])

		# read in configuration (api key)
		pass

	def hotkeyPressed(self):
		# XXX: the following line is used to work around an error importing chardet when this
		# function is invoked as a hotkey from IDA. WTF?
		chardet = __import__('chardet', globals(), locals(), [], -1)

		# get the parameters (address, length) from IDA
		ea = SelStart()
		end_ea = SelEnd()
		if ea == BADADDR:
			ea = ScreenEA()
			if ItemSize(ea) > 1:
				end_ea = ea + ItemSize(ea)
			else:
				# find next named byte
				end_ea = NextHead(ScreenEA())
				for i in range(ea+1, end_ea):
					name = GetTrueNameEx(BADADDR, i)
					b = Byte(i)
					if name != '':
						end_ea = i
						break
					elif b == 0:
						end_ea = i
						break

		length = end_ea - ea

		print '[TranslatePlugin] Found string at [%08x:%08x] len %08x' % (ea, end_ea, length)

		self.ea = ea

		try:
			(encoding,original_string) = getUnicodeTranslatedString(ea,end_ea)
		except:
			encoding = "ascii"

		# display the dialog box
		self.displayDialogBox(ea, length, getString(ea,end_ea), encoding)

	def displayDialogBox(self, ea, length, original_string, encoding):
		# build and display dialog box
		dialog = TranslatorDialog(self.parent, self.config)
		dialog.setOriginalText(original_string, encoding)
		dialog.registerSuccessCallback(self.gotTranslatedData)
		dialog.setModal(True)
		dialog.show() # can't do exec() since ida will show its "running python script" window

	def gotTranslatedData(self, translation, original, do_comment, do_xref):
		self.model.addTranslation(self.ea, original, translation)

		if len(translation) > 0:
			if do_comment:
				MakeRptCmt(self.ea, translation.encode('ascii'))
			if do_xref:
				xref_name = string.translate(translation.encode('ascii'), self.transtable, self.deletechars)
				MakeName(self.ea, 'a'+''.join([a.title() for a in xref_name.split(' ')]))
		idaapi.refresh_idaview_anyway()

"""
The TranslateTableView class exists only so we can intercept keyPressEvent
in order to handle the case where the user hits Enter on a line in our
QTableView.
"""
class TranslateTableView(QtGui.QTableView):
	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Return:
			selectedRows = self.selectionModel().selectedRows()
			if selectedRows:
				selectedRow = selectedRows[0]
				self.doubleClicked.emit(selectedRow)
		else:
			QtGui.QTableView.keyPressEvent(self, event)

"""
TranslateFormClass is a view to the TranslateModel, displaying all
translations in a dockable IDA window. We don't use IDA's built-in choose2
class here since it doesn't support Unicode characters. Instead, we try to
emulate choose2's behavior as closely as possible.
"""
class TranslateFormClass(PluginForm):
	def __init__(self,cfg):
		super(TranslateFormClass, self).__init__()
		self.config = cfg

	def OnCreate(self,form):
		self.parent = self.FormToPySideWidget(form)
		self.PopulateModel()
		self.PopulateMainForm()
		self.CreateContextMenu()
		translator = Translator(self.parent, self.translationModel, self.config)

		# XXX: the following line is used to work around an error importing chardet when this
		# function is invoked as a hotkey from IDA. WTF?
		chardet = __import__('chardet', globals(), locals(), [], -1)

		chardet.detect('')

		# set hotkey
		try:
			hotkey_ctx
			if idaapi.del_hotkey(hotkey_ctx):
				del hotkey_ctx
		except:
			hotkey_ctx = idaapi.add_hotkey("Ctrl-R", translator.hotkeyPressed)
			if hotkey_ctx is None:
				del hotkey_ctx


	def CreateContextMenu(self):
		self.contextMenu = QtGui.QMenu(self.parent)
		copyAction = self.contextMenu.addAction("&Copy")
		exportAction = self.contextMenu.addAction("E&xport...")
		self.contextMenu.addSeparator()

		copyAction.triggered.connect(self.copyItem)
		exportAction.triggered.connect(self.exportAll)

	def getSelectedRow(self):
		selectedRows = self.tableview.selectionModel().selectedIndexes()
		if len(selectedRows) == 0:
			return None
		else:
			return [self.translationModel.data(item) for item in selectedRows]

	def copyItem(self):
		theItem = self.getSelectedRow()
		if theItem != None:
			toCopy = u' '.join([unicode(x) for x in theItem])
			QtGui.QApplication.clipboard().setText(toCopy)

	def exportAll(self):
		outputfilename = QtGui.QFileDialog.getSaveFileName(self.parent, 'Save CSV export to...')
		if outputfilename == None:
			return

		numcolumns = self.translationModel.columnCount()
		with open(outputfilename[0], 'wb') as outputfile:
			outputfile.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
			csvout = csv.writer(outputfile)
			# write the header
			csvout.writerow([self.translationModel.headerData(x, QtCore.Qt.Horizontal) for x in range(0,numcolumns)])
			for row in range(0,self.translationModel.rowCount()):
				csvout.writerow([self.translationModel.data(index).encode('utf8') \
					for index in \
					[self.translationModel.index(row, column) for column in range(0,numcolumns)]])
			print '[TranslatePlugin] Exported %d translations to %s' % (self.translationModel.rowCount(), str(outputfilename[0]))

	def showContextMenu(self):
		self.contextMenu.exec_(QtGui.QCursor.pos())

	def PopulateModel(self):
		self.translationModel = TranslateModel()

	def PopulateMainForm(self):
		layout = QtGui.QVBoxLayout()
		tableview = QtGui.QTableView()

		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)

		tableview = TranslateTableView()
		tableview.setModel(self.translationModel)
		tableview.setSortingEnabled(False)
		tableview.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		tableview.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
		tableview.setShowGrid(False)
		hdr = tableview.verticalHeader()
		hdr.setHighlightSections(False)
		hdr.setDefaultSectionSize(hdr.minimumSectionSize())
		hdr = tableview.horizontalHeader()
		hdr.setHighlightSections(False)
		hdr.setDefaultAlignment(QtCore.Qt.AlignLeft)

		tableview.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
		copyAction = QtGui.QAction("&Copy", self.parent)
		copyAction.setShortcut("Ctrl+C")
		exportAction = QtGui.QAction("E&xport all to CSV...", self.parent)
		exportAction.setShortcut("Shift+Ins")
		separator = QtGui.QAction(self.parent)
		separator.setSeparator(True)
		tableview.addAction(copyAction)
		tableview.addAction(exportAction)
		tableview.addAction(separator)

		copyAction.triggered.connect(self.copyItem)
		exportAction.triggered.connect(self.exportAll)

		layout.addWidget(tableview)
		self.parent.setLayout(layout)

		tableview.doubleClicked.connect(self.rowClicked)
		tableview.resizeColumnsToContents()

		self.tableview = tableview

	def rowClicked(self, index):
		ea = self.translationModel.translations.keys()[index.row()]
		print '[TranslatePlugin] Selected translation @ ea %08x' % ea
		Jump(ea)

	def OnClose(self,form):
		pass

"""
Configuration object. Right now we only store the API key for Google 
Translate.
"""
class TranslatorConfig(object):
	def __init__(self):
		self.doDefaults()
		self.Read()

	def doDefaults(self):
		self.config = {}
		self.config_file_name = idaapi.get_user_idadir() + os.sep + 'translateplugin.conf'

	def Read(self):
		try:
			with open(self.config_file_name, 'rb') as infile:
				self.config = json.load(infile)
		except:
			pass

	def Write(self):
		try:
			with open(self.config_file_name, 'wb') as infile:
				json.dump(self.config, infile)
		except:
			pass

	def getApiKey(self):
		if self.config.has_key('api_key'):
			return self.config['api_key']
		else:
			return None

	def setApiKey(self,new_key):
		self.config['api_key'] = new_key


plg = None

"""
Main plugin class.
"""
class TranslatePlugin(idaapi.plugin_t):
	flags = 0
	comment = ""
	help = ""
	wanted_name = "Translations"
	wanted_hotkey = "Ctrl-Alt-R"

	def startPlugin(self):
		global plg

		# check to see if we've configured the translator yet.
		tc = TranslatorConfig()
		if tc.getApiKey() == None:
			# show dialog to get API key for Google Translate
			translate_key = AskStr('', 'Enter in an API key for Google Translate')
			if translate_key == 0 or translate_key == '':
				return
			else:
				tc.setApiKey(translate_key)
				tc.Write()

		if not plg:
			plg = TranslateFormClass(tc)

		plg.Show("Translations")

	def init(self):
		global plg
		plg = None

		return idaapi.PLUGIN_OK

	def run(self, arg=0):
		self.startPlugin()

	def term(self):
		pass

def PLUGIN_ENTRY():
	return TranslatePlugin()

