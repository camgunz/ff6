DTE = [''] * 256
DTE_BATTLE = [''] * 256

DTE[0x00] = '/'
DTE[0x01] = '*'
DTE[0x02] = 'TERRA'
DTE[0x03] = 'LOCKE'
DTE[0x04] = 'CYAN'
DTE[0x05] = 'SHADOW'
DTE[0x06] = 'EDGAR'
DTE[0x07] = 'SABIN'
DTE[0x08] = 'CELES'
DTE[0x09] = 'STRAGO'
DTE[0x0A] = 'RELM'
DTE[0x0B] = 'SETZER'
DTE[0x0C] = 'MOG'
DTE[0x0D] = 'GAU'
DTE[0x0E] = 'GOGO'
DTE[0x0F] = 'UMARO'
DTE[0x13] = '*'
DTE[0x20] = 'A'
DTE[0x21] = 'B'
DTE[0x22] = 'C'
DTE[0x23] = 'D'
DTE[0x24] = 'E'
DTE[0x25] = 'F'
DTE[0x26] = 'G'
DTE[0x27] = 'H'
DTE[0x28] = 'I'
DTE[0x29] = 'J'
DTE[0x2A] = 'K'
DTE[0x2B] = 'L'
DTE[0x2C] = 'M'
DTE[0x2D] = 'N'
DTE[0x2E] = 'O'
DTE[0x2F] = 'P'
DTE[0x30] = 'Q'
DTE[0x31] = 'R'
DTE[0x32] = 'S'
DTE[0x33] = 'T'
DTE[0x34] = 'U'
DTE[0x35] = 'V'
DTE[0x36] = 'W'
DTE[0x37] = 'X'
DTE[0x38] = 'Y'
DTE[0x39] = 'Z'
DTE[0x3A] = 'a'
DTE[0x3B] = 'b'
DTE[0x3C] = 'c'
DTE[0x3D] = 'd'
DTE[0x3E] = 'e'
DTE[0x3F] = 'f'
DTE[0x40] = 'g'
DTE[0x41] = 'h'
DTE[0x42] = 'i'
DTE[0x43] = 'j'
DTE[0x44] = 'k'
DTE[0x45] = 'l'
DTE[0x46] = 'm'
DTE[0x47] = 'n'
DTE[0x48] = 'o'
DTE[0x49] = 'p'
DTE[0x4A] = 'q'
DTE[0x4B] = 'r'
DTE[0x4C] = 's'
DTE[0x4D] = 't'
DTE[0x4E] = 'u'
DTE[0x4F] = 'v'
DTE[0x50] = 'w'
DTE[0x51] = 'x'
DTE[0x52] = 'y'
DTE[0x53] = 'z'
DTE[0x54] = '0'
DTE[0x55] = '1'
DTE[0x56] = '2'
DTE[0x57] = '3'
DTE[0x58] = '4'
DTE[0x59] = '5'
DTE[0x5A] = '6'
DTE[0x5B] = '7'
DTE[0x5C] = '8'
DTE[0x5D] = '9'
DTE[0x5E] = '!'
DTE[0x5F] = '?'
DTE[0x61] = ':'
DTE[0x62] = '"'
DTE[0x63] = "'"
DTE[0x64] = '-'
DTE[0x65] = '.'
DTE[0x66] = ','
DTE[0x67] = '...'
DTE[0x68] = ';'
DTE[0x69] = '#'
DTE[0x6A] = '+'
DTE[0x6B] = '('
DTE[0x6C] = ')'
DTE[0x6D] = '%'
DTE[0x6E] = '~'
DTE[0x70] = '@'
DTE[0x71] = '<note>'
DTE[0x72] = '='
DTE[0x73] = '"'
DTE[0x76] = '<pearl>'
DTE[0x77] = '<death>'
DTE[0x78] = '<lit>'
DTE[0x79] = '<wind>'
DTE[0x7A] = '<earth>'
DTE[0x7B] = '<ice>'
DTE[0x7C] = '<fire>'
DTE[0x7D] = '<water>'
DTE[0x7E] = '<poison>'
DTE[0x7F] = ' '
DTE[0x80] = 'e '
DTE[0x81] = ' t'
DTE[0x82] = ': '
DTE[0x83] = 'th'
DTE[0x84] = 't '
DTE[0x85] = 'he'
DTE[0x86] = 's '
DTE[0x87] = 'er'
DTE[0x88] = ' a'
DTE[0x89] = 're'
DTE[0x8A] = 'in'
DTE[0x8B] = 'ou'
DTE[0x8C] = 'd '
DTE[0x8D] = ' w'
DTE[0x8E] = ' s'
DTE[0x8F] = 'an'
DTE[0x90] = 'o '
DTE[0x91] = ' h'
DTE[0x92] = ' o'
DTE[0x93] = 'r '
DTE[0x94] = 'n '
DTE[0x95] = 'at'
DTE[0x96] = 'to'
DTE[0x97] = ' i'
DTE[0x98] = ', '
DTE[0x99] = 've'
DTE[0x9A] = 'ng'
DTE[0x9B] = 'ha'
DTE[0x9C] = ' m'
DTE[0x9D] = 'Th'
DTE[0x9E] = 'st'
DTE[0x9F] = 'on'
DTE[0xA0] = 'yo'
DTE[0xA1] = ' b'
DTE[0xA2] = 'me'
DTE[0xA3] = 'y '
DTE[0xA4] = 'en'
DTE[0xA5] = 'it'
DTE[0xA6] = 'ar'
DTE[0xA7] = 'll'
DTE[0xA8] = 'ea'
DTE[0xA9] = 'I '
DTE[0xAA] = 'ed'
DTE[0xAB] = ' f'
DTE[0xAC] = ' y'
DTE[0xAD] = 'hi'
DTE[0xAE] = 'is'
DTE[0xAF] = 'es'
DTE[0xB0] = 'or'
DTE[0xB1] = 'l '
DTE[0xB2] = ' c'
DTE[0xB3] = 'ne'
DTE[0xB4] = "'s"
DTE[0xB5] = 'nd'
DTE[0xB6] = 'le'
DTE[0xB7] = 'se'
DTE[0xB8] = ' I'
DTE[0xB9] = 'a '
DTE[0xBA] = 'te'
DTE[0xBB] = ' l'
DTE[0xBC] = 'pe'
DTE[0xBD] = 'as'
DTE[0xBE] = 'ur'
DTE[0xBF] = 'u '
DTE[0xC0] = 'al'
DTE[0xC1] = ' p'
DTE[0xC2] = 'g '
DTE[0xC3] = 'om'
DTE[0xC4] = ' d'
DTE[0xC5] = 'f '
DTE[0xC6] = ' g'
DTE[0xC7] = 'ow'
DTE[0xC8] = 'rs'
DTE[0xC9] = 'be'
DTE[0xCA] = 'ro'
DTE[0xCB] = 'us'
DTE[0xCC] = 'ri'
DTE[0xCD] = 'wa'
DTE[0xCE] = 'we'
DTE[0xCF] = 'Wh'
DTE[0xD0] = 'et'
DTE[0xD1] = ' r'
DTE[0xD2] = 'nt'
DTE[0xD3] = 'm '
DTE[0xD4] = 'ma'
DTE[0xD5] = "I'"
DTE[0xD6] = 'li'
DTE[0xD7] = 'ho'
DTE[0xD8] = 'of'
DTE[0xD9] = 'Yo'
DTE[0xDA] = 'h '
DTE[0xDB] = ' n'
DTE[0xDC] = 'ee'
DTE[0xDD] = 'de'
DTE[0xDE] = 'so'
DTE[0xDF] = 'gh'
DTE[0xE0] = 'ca'
DTE[0xE1] = 'ra'
DTE[0xE2] = "n'"
DTE[0xE3] = 'ta'
DTE[0xE4] = 'ut'
DTE[0xE5] = 'el'
DTE[0xE6] = '! '
DTE[0xE7] = 'fo'
DTE[0xE8] = 'ti'
DTE[0xE9] = 'We'
DTE[0xEA] = 'lo'
DTE[0xEB] = 'e!'
DTE[0xEC] = 'ld'
DTE[0xED] = 'no'
DTE[0xEE] = 'ac'
DTE[0xEF] = 'ce'
DTE[0xF0] = 'k '
DTE[0xF1] = ' u'
DTE[0xF2] = 'oo'
DTE[0xF3] = 'ke'
DTE[0xF4] = 'ay'
DTE[0xF5] = 'w '
DTE[0xF6] = '!!'
DTE[0xF7] = 'ag'
DTE[0xF8] = 'il'
DTE[0xF9] = 'ly'
DTE[0xFA] = 'co'
DTE[0xFB] = '. '
DTE[0xFC] = 'ch'
DTE[0xFD] = 'go'
DTE[0xFE] = 'ge'
DTE[0xFF] = 'e...'

DTE_BATTLE[0x00] = ''
DTE_BATTLE[0x80] = 'A'
DTE_BATTLE[0x81] = 'B'
DTE_BATTLE[0x82] = 'C'
DTE_BATTLE[0x83] = 'D'
DTE_BATTLE[0x84] = 'E'
DTE_BATTLE[0x85] = 'F'
DTE_BATTLE[0x86] = 'G'
DTE_BATTLE[0x87] = 'H'
DTE_BATTLE[0x88] = 'I'
DTE_BATTLE[0x89] = 'J'
DTE_BATTLE[0x8A] = 'K'
DTE_BATTLE[0x8B] = 'L'
DTE_BATTLE[0x8C] = 'M'
DTE_BATTLE[0x8D] = 'N'
DTE_BATTLE[0x8E] = 'O'
DTE_BATTLE[0x8F] = 'P'
DTE_BATTLE[0x90] = 'Q'
DTE_BATTLE[0x91] = 'R'
DTE_BATTLE[0x92] = 'S'
DTE_BATTLE[0x93] = 'T'
DTE_BATTLE[0x94] = 'U'
DTE_BATTLE[0x95] = 'V'
DTE_BATTLE[0x96] = 'W'
DTE_BATTLE[0x97] = 'X'
DTE_BATTLE[0x98] = 'Y'
DTE_BATTLE[0x99] = 'Z'
DTE_BATTLE[0x9A] = 'a'
DTE_BATTLE[0x9B] = 'b'
DTE_BATTLE[0x9C] = 'c'
DTE_BATTLE[0x9D] = 'd'
DTE_BATTLE[0x9E] = 'e'
DTE_BATTLE[0x9F] = 'f'
DTE_BATTLE[0xA0] = 'g'
DTE_BATTLE[0xA1] = 'h'
DTE_BATTLE[0xA2] = 'i'
DTE_BATTLE[0xA3] = 'j'
DTE_BATTLE[0xA4] = 'k'
DTE_BATTLE[0xA5] = 'l'
DTE_BATTLE[0xA6] = 'm'
DTE_BATTLE[0xA7] = 'n'
DTE_BATTLE[0xA8] = 'o'
DTE_BATTLE[0xA9] = 'p'
DTE_BATTLE[0xAA] = 'q'
DTE_BATTLE[0xAB] = 'r'
DTE_BATTLE[0xAC] = 's'
DTE_BATTLE[0xAD] = 't'
DTE_BATTLE[0xAE] = 'u'
DTE_BATTLE[0xAF] = 'v'
DTE_BATTLE[0xB0] = 'w'
DTE_BATTLE[0xB1] = 'x'
DTE_BATTLE[0xB2] = 'y'
DTE_BATTLE[0xB3] = 'z'
DTE_BATTLE[0xB4] = '0'
DTE_BATTLE[0xB5] = '1'
DTE_BATTLE[0xB6] = '2'
DTE_BATTLE[0xB7] = '3'
DTE_BATTLE[0xB8] = '4'
DTE_BATTLE[0xB9] = '5'
DTE_BATTLE[0xBA] = '6'
DTE_BATTLE[0xBB] = '7'
DTE_BATTLE[0xBC] = '8'
DTE_BATTLE[0xBD] = '9'
DTE_BATTLE[0xBE] = '!'
DTE_BATTLE[0xBF] = '?'
DTE_BATTLE[0xC0] = 'ú'
DTE_BATTLE[0xC1] = ':'
DTE_BATTLE[0xC2] = '"'
DTE_BATTLE[0xC3] = "'"
DTE_BATTLE[0xC4] = '-'
DTE_BATTLE[0xC5] = '.'
DTE_BATTLE[0xC6] = '.'
DTE_BATTLE[0xC7] = 'ú'
DTE_BATTLE[0xC8] = ';'
DTE_BATTLE[0xC9] = '#'
DTE_BATTLE[0xCA] = '+'
DTE_BATTLE[0xCB] = '('
DTE_BATTLE[0xCC] = ')'
DTE_BATTLE[0xCD] = '%'
DTE_BATTLE[0xCE] = '~'
DTE_BATTLE[0xCF] = 'ú'
DTE_BATTLE[0xD0] = 'ú'
DTE_BATTLE[0xD1] = 'ú'
DTE_BATTLE[0xD2] = '='
DTE_BATTLE[0xFE] = ' '
DTE_BATTLE[0xFF] = ''
