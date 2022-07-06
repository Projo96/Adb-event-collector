'''
Modified version of the code written by Diego Torres Milano
original repository https://github.com/dtmilano/AndroidViewClient
'''

KEY_MAP = dict()
KEY_MAP["ESCAPE"] = 1
KEY_MAP["1"] = 2
KEY_MAP["2"] = 3
KEY_MAP["3"] = 4
KEY_MAP["4"] = 5
KEY_MAP["5"] = 6
KEY_MAP["6"] = 7
KEY_MAP["7"] = 8
KEY_MAP["8"] = 9
KEY_MAP["9"] = 10
KEY_MAP["0"] = 11
KEY_MAP["MINUS"] = 12
KEY_MAP["EQUALS"] = 13
KEY_MAP["DEL"] = 14
KEY_MAP["TAB"] = 15
KEY_MAP["Q"] = 16
KEY_MAP["W"] = 17
KEY_MAP["E"] = 18
KEY_MAP["R"] = 19
KEY_MAP["T"] = 20
KEY_MAP["Y"] = 21
KEY_MAP["U"] = 22
KEY_MAP["I"] = 23
KEY_MAP["O"] = 24
KEY_MAP["P"] = 25
KEY_MAP["LEFT_BRACKET"] = 26
KEY_MAP["RIGHT_BRACKET"] = 27
KEY_MAP["ENTER"] = 28
KEY_MAP["CTRL_LEFT"] = 29
KEY_MAP["A"] = 30
KEY_MAP["S"] = 31
KEY_MAP["D"] = 32
KEY_MAP["F"] = 33
KEY_MAP["G"] = 34
KEY_MAP["H"] = 35
KEY_MAP["J"] = 36
KEY_MAP["K"] = 37
KEY_MAP["L"] = 38
KEY_MAP["SEMICOLON"] = 39
KEY_MAP["APOSTROPHE"] = 40
KEY_MAP["GRAVE"] = 41
KEY_MAP["SHIFT_LEFT"] = 42
KEY_MAP["BACKSLASH"] = 43
KEY_MAP["Z"] = 44
KEY_MAP["X"] = 45
KEY_MAP["C"] = 46
KEY_MAP["V"] = 47
KEY_MAP["B"] = 48
KEY_MAP["N"] = 49
KEY_MAP["M"] = 50
KEY_MAP["COMMA"] = 51
KEY_MAP["PERIOD"] = 52
KEY_MAP["SLASH"] = 53
KEY_MAP["SHIFT_RIGHT"] = 54
KEY_MAP["NUMPAD_MULTIPLY"] = 55
KEY_MAP["ALT_LEFT"] = 56
KEY_MAP["SPACE"] = 57
KEY_MAP["CAPS_LOCK"] = 58
KEY_MAP["F1"] = 59
KEY_MAP["F2"] = 60
KEY_MAP["F3"] = 61
KEY_MAP["F4"] = 62
KEY_MAP["F5"] = 63
KEY_MAP["F6"] = 64
KEY_MAP["F7"] = 65
KEY_MAP["F8"] = 66
KEY_MAP["F9"] = 67
KEY_MAP["F10"] = 68
KEY_MAP["NUM_LOCK"] = 69
KEY_MAP["SCROLL_LOCK"] = 70
KEY_MAP["NUMPAD_7"] = 71
KEY_MAP["NUMPAD_8"] = 72
KEY_MAP["NUMPAD_9"] = 73
KEY_MAP["NUMPAD_SUBTRACT"] = 74
KEY_MAP["NUMPAD_4"] = 75
KEY_MAP["NUMPAD_5"] = 76
KEY_MAP["NUMPAD_6"] = 77
KEY_MAP["NUMPAD_ADD"] = 78
KEY_MAP["NUMPAD_1"] = 79
KEY_MAP["NUMPAD_2"] = 80
KEY_MAP["NUMPAD_3"] = 81
KEY_MAP["NUMPAD_0"] = 82
KEY_MAP["NUMPAD_DOT"] = 83
KEY_MAP["ZENKAKU_HANKAKU"] = 85
KEY_MAP["BACKSLASH"] = 86
KEY_MAP["F11"] = 87
KEY_MAP["F12"] = 88
KEY_MAP["RO"] = 89
KEY_MAP["HENKAN"] = 92
KEY_MAP["KATAKANA_HIRAGANA"] = 93
KEY_MAP["MUHENKAN"] = 94
KEY_MAP["NUMPAD_COMMA"] = 95
KEY_MAP["NUMPAD_ENTER"] = 96
KEY_MAP["CTRL_RIGHT"] = 97
KEY_MAP["NUMPAD_DIVIDE"] = 98
KEY_MAP["SYSRQ"] = 99
KEY_MAP["ALT_RIGHT"] = 100
KEY_MAP["MOVE_HOME"] = 102
KEY_MAP["DPAD_UP"] = 103
KEY_MAP["PAGE_UP"] = 104
KEY_MAP["DPAD_LEFT"] = 105
KEY_MAP["DPAD_RIGHT"] = 106
KEY_MAP["MOVE_END"] = 107
KEY_MAP["DPAD_DOWN"] = 108
KEY_MAP["PAGE_DOWN"] = 109
KEY_MAP["INSERT"] = 110
KEY_MAP["FORWARD_DEL"] = 111
KEY_MAP["VOLUME_MUTE"] = 113
KEY_MAP["VOLUME_DOWN"] = 114
KEY_MAP["VOLUME_UP"] = 115
KEY_MAP["POWER"] = 116
KEY_MAP["NUMPAD_EQUALS"] = 117
KEY_MAP["BREAK"] = 119
KEY_MAP["NUMPAD_COMMA"] = 121
KEY_MAP["KANA"] = 122
KEY_MAP["EISU"] = 123
KEY_MAP["YEN"] = 124
KEY_MAP["META_LEFT"] = 125
KEY_MAP["META_RIGHT"] = 126
KEY_MAP["MENU"] = 127
KEY_MAP["MEDIA_STOP"] = 128
KEY_MAP["MENU"] = 139
KEY_MAP["CALCULATOR"] = 140
# KEY_MAP["POWER"]=142
# KEY_MAP["POWER"]=143
KEY_MAP["EXPLORER"] = 150
# KEY_MAP["POWER"]=152
KEY_MAP["ENVELOPE"] = 155
KEY_MAP["BOOKMARK"] = 156
KEY_MAP["BACK"] = 158
KEY_MAP["FORWARD"] = 159
KEY_MAP["MEDIA_CLOSE"] = 160
KEY_MAP["MEDIA_EJECT"] = 161
KEY_MAP["MEDIA_EJECT"] = 162
KEY_MAP["MEDIA_NEXT"] = 163
KEY_MAP["MEDIA_PLAY_PAUSE"] = 164
KEY_MAP["MEDIA_PREVIOUS"] = 165
KEY_MAP["MEDIA_STOP"] = 166
KEY_MAP["MEDIA_RECORD"] = 167
KEY_MAP["MEDIA_REWIND"] = 168
KEY_MAP["CALL"] = 169
KEY_MAP["MUSIC"] = 171
KEY_MAP["HOME"] = 172
KEY_MAP["PAGE_UP"] = 177
KEY_MAP["PAGE_DOWN"] = 178
KEY_MAP["NUMPAD_LEFT_PAREN"] = 179
KEY_MAP["NUMPAD_RIGHT_PAREN"] = 180
KEY_MAP["MEDIA_PLAY"] = 200
KEY_MAP["MEDIA_PAUSE"] = 201
KEY_MAP["MEDIA_PLAY"] = 207
KEY_MAP["MEDIA_FAST_FORWARD"] = 208
KEY_MAP["CAMERA"] = 212
KEY_MAP["MUSIC"] = 213
KEY_MAP["ENVELOPE"] = 215
KEY_MAP["SEARCH"] = 217
KEY_MAP["BRIGHTNESS_DOWN"] = 224
KEY_MAP["BRIGHTNESS_UP"] = 225
KEY_MAP["HEADSETHOOK"] = 226
KEY_MAP["BUTTON_1"] = 256
KEY_MAP["BUTTON_2"] = 257
KEY_MAP["BUTTON_3"] = 258
KEY_MAP["BUTTON_4"] = 259
KEY_MAP["BUTTON_5"] = 260
KEY_MAP["BUTTON_6"] = 261
KEY_MAP["BUTTON_7"] = 262
KEY_MAP["BUTTON_8"] = 263
KEY_MAP["BUTTON_9"] = 264
KEY_MAP["BUTTON_10"] = 265
KEY_MAP["BUTTON_11"] = 266
KEY_MAP["BUTTON_12"] = 267
KEY_MAP["BUTTON_13"] = 268
KEY_MAP["BUTTON_14"] = 269
KEY_MAP["BUTTON_15"] = 270
KEY_MAP["BUTTON_16"] = 271
KEY_MAP["BUTTON_1"] = 288
KEY_MAP["BUTTON_2"] = 289
KEY_MAP["BUTTON_3"] = 290
KEY_MAP["BUTTON_4"] = 291
KEY_MAP["BUTTON_5"] = 292
KEY_MAP["BUTTON_6"] = 293
KEY_MAP["BUTTON_7"] = 294
KEY_MAP["BUTTON_8"] = 295
KEY_MAP["BUTTON_9"] = 296
KEY_MAP["BUTTON_10"] = 297
KEY_MAP["BUTTON_11"] = 298
KEY_MAP["BUTTON_12"] = 299
KEY_MAP["BUTTON_13"] = 300
KEY_MAP["BUTTON_14"] = 301
KEY_MAP["BUTTON_15"] = 302
KEY_MAP["BUTTON_16"] = 303
KEY_MAP["BUTTON_A"] = 304
KEY_MAP["BUTTON_B"] = 305
KEY_MAP["BUTTON_C"] = 306
KEY_MAP["BUTTON_X"] = 307
KEY_MAP["BUTTON_Y"] = 308
KEY_MAP["BUTTON_Z"] = 309
KEY_MAP["BUTTON_L1"] = 310
KEY_MAP["BUTTON_R1"] = 311
KEY_MAP["BUTTON_L2"] = 312
KEY_MAP["BUTTON_R2"] = 313
KEY_MAP["BUTTON_SELECT"] = 314
KEY_MAP["BUTTON_START"] = 315
KEY_MAP["BUTTON_MODE"] = 316
KEY_MAP["BUTTON_THUMBL"] = 317
KEY_MAP["BUTTON_THUMBR"] = 318
KEY_MAP["DPAD_CENTER"] = 353
KEY_MAP["GUIDE"] = 362
KEY_MAP["DVR"] = 366
KEY_MAP["TV"] = 377
KEY_MAP["CALENDAR"] = 397
KEY_MAP["CHANNEL_UP"] = 402
KEY_MAP["CHANNEL_DOWN"] = 403
KEY_MAP["CONTACTS"] = 429
KEY_MAP["FUNCTION"] = 464
KEY_MAP["ESCAPE"] = 465
KEY_MAP["F1"] = 466
KEY_MAP["F2"] = 467
KEY_MAP["F3"] = 468
KEY_MAP["F4"] = 469
KEY_MAP["F5"] = 470
KEY_MAP["F6"] = 471
KEY_MAP["F7"] = 472
KEY_MAP["F8"] = 473
KEY_MAP["F9"] = 474
KEY_MAP["F10"] = 475
KEY_MAP["F11"] = 476
KEY_MAP["F12"] = 477
KEY_MAP["1"] = 478
KEY_MAP["2"] = 479
KEY_MAP["D"] = 480
KEY_MAP["E"] = 481
KEY_MAP["F"] = 482
KEY_MAP["S"] = 483
KEY_MAP["B"] = 484
KEY_MAP["TV_HOME"] = 668
