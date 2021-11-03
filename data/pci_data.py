# Array of Device IDs for different devices
class nvidia_ids:
    # Courteous of envytools as well as Macrumors:
    # https://envytools.readthedocs.io/en/latest/hw/pciid.html
    # https://forums.macrumors.com/threads/2011-imac-graphics-card-upgrade.1596614/
    curie_ids = [
        0x0040,
        0x00f0,
        0x0220,
        0x0140,
        0x0160,
        0x0090,
        0x01d0,
        0x0390,
        0x0290,
    ]

    tesla_ids = [
        # G80
        0x0190,  # G80 [GeForce 8800 GTS / 8800 GTX]
        0x0191,  # G80 [GeForce 8800 GTX]
        0x0193,  # G80 [GeForce 8800 GTS]
        0x0194,  # G80 [GeForce 8800 Ultra]
        0x019E,  # G80GL [Quadro FX 4600]
        0x019D,  # G80GL [Quadro FX 5600]
        # G84
        0x0400,  # G84 [8600 GTS]
        0x0401,  # G84 [8600 GT]
        0x0402,  # G84 [8600 GT]
        0x0403,  # G84 [8600 GS]
        0x0404,  # G84 [8400 GS]
        0x0405,  # G84 [9500M GS]
        0x0406,  # G84 [8300 GS]
        0x0407,  # G84 [8600M GT]
        0x0408,  # G84 [9650M GS]
        0x0409,  # G84 [8700M GT]
        0x040A,  # G84 [FX 370]
        0x040B,  # G84 [NVS 320M]
        0x040C,  # G84 [FX 570M]
        0x040D,  # G84 [FX 1600M]
        0x040E,  # G84 [FX 570]
        0x040F,  # G84 [FX 1700]
        # G86
        0x0420,  # G86 [8400 SE]
        0x0421,  # G86 [8500 GT]
        0x0422,  # G86 [8400 GS]
        0x0423,  # G86 [8300 GS]
        0x0424,  # G86 [8400 GS]
        0x0425,  # G86 [8600M GS]
        0x0426,  # G86 [8400M GT]
        0x0427,  # G86 [8400M GS]
        0x0428,  # G86 [8400M G]
        0x0429,  # G86 [NVS 140M]
        0x042A,  # G86 [NVS 130M]
        0x042B,  # G86 [NVS 135M]
        0x042C,  # G86 [9400 GT]
        0x042D,  # G86 [FX 360M]
        0x042E,  # G86 [9300M G]
        0x042F,  # G86 [NVS 290]
        # G92
        0x0410,  # G92 [GT 330]
        0x0600,  # G92 [8800 GTS 512]
        0x0601,  # G92 [9800 GT]
        0x0602,  # G92 [8800 GT]
        0x0603,  # G92 [GT 230]
        0x0604,  # G92 [9800 GX2]
        0x0605,  # G92 [9800 GT]
        0x0606,  # G92 [8800 GS]
        0x0607,  # G92 [GTS 240]
        0x0608,  # G92 [9800M GTX]
        0x0609,  # G92 [8800M GTS]
        0x060A,  # G92 [GTX 280M]
        0x060B,  # G92 [9800M GT]
        0x060C,  # G92 [8800M GTX]
        0x060F,  # G92 [GTX 285M]
        0x0610,  # G92 [9600 GSO]
        0x0611,  # G92 [8800 GT]
        0x0612,  # G92 [9800 GTX/9800 GTX+]
        0x0613,  # G92 [9800 GTX+]
        0x0614,  # G92 [9800 GT]
        0x0615,  # G92 [GTS 250]
        0x0617,  # G92 [9800M GTX]
        0x0618,  # G92 [GTX 260M]
        0x0619,  # G92 [FX 4700 X2]
        0x061A,  # G92 [FX 3700]
        0x061B,  # G92 [VX 200]
        0x061C,  # G92 [FX 3600M]
        0x061D,  # G92 [FX 2800M]
        0x061E,  # G92 [FX 3700M]
        0x061F,  # G92 [FX 3800M]
        # G94
        0x0621,  # G94 [GT 230]
        0x0622,  # G94 [9600 GT]
        0x0623,  # G94 [9600 GS]
        0x0624,  # G94 [9600 GT Green Edition]
        0x0625,  # G94 [9600 GSO 512]
        0x0626,  # G94 [GT 130]
        0x0627,  # G94 [GT 140]
        0x0628,  # G94 [9800M GTS]
        0x062A,  # G94 [9700M GTS]
        0x062B,  # G94 [9800M GS]
        0x062C,  # G94 [9800M GTS ]
        0x062D,  # G94 [9600 GT]
        0x062E,  # G94 [9600 GT]
        0x062F,  # G94 [9800 S]
        0x0631,  # G94 [GTS 160M]
        0x0635,  # G94 [9600 GSO]
        0x0637,  # G94 [9600 GT]
        0x0638,  # G94 [FX 1800]
        0x063A,  # G94 [FX 2700M]
        # G96
        0x0640,  # G96 [9500 GT]
        0x0641,  # G96 [9400 GT]
        0x0643,  # G96 [9500 GT]
        0x0644,  # G96 [9500 GS]
        0x0645,  # G96 [9500 GS]
        0x0646,  # G96 [GT 120]
        0x0647,  # G96 [9600M GT]
        0x0648,  # G96 [9600M GS]
        0x0649,  # G96 [9600M GT]
        0x064A,  # G96 [9700M GT]
        0x064B,  # G96 [9500M G]
        0x064C,  # G96 [9650M GT]
        0x0651,  # G96 [G 110M]
        0x0652,  # G96 [GT 130M]
        0x0653,  # G96 [GT 120M]
        0x0654,  # G96 [GT 220M]
        0x0655,  # G96 [GT 120]
        0x0656,  # G96 [GT 120 ]
        0x0658,  # G96 [FX 380]
        0x0659,  # G96 [FX 580]
        0x065A,  # G96 [FX 1700M]
        0x065B,  # G96 [9400 GT]
        0x065C,  # G96 [FX 770M]
        0x065F,  # G96 [G210]
        # G98
        0x06E0,  # G98 [9300 GE]
        0x06E1,  # G98 [9300 GS]
        0x06E2,  # G98 [8400]
        0x06E3,  # G98 [8400 SE]
        0x06E4,  # G98 [8400 GS]
        0x06E5,  # G98M [9300M GS]
        0x06E6,  # G98 [G100]
        0x06E7,  # G98 [9300 SE]
        0x06E8,  # G98 [9200M GS]
        0x06E9,  # G98 [9300M GS]
        0x06EA,  # G98 [NVS 150M]
        0x06EB,  # G98 [NVS 160M]
        0x06EC,  # G98 [G 105M]
        0x06ED,  # G98 [9600 GT / 9800 GT]
        0x06EF,  # G98 [G 103M]
        0x06F1,  # G98 [G105M]
        0x06F8,  # G98 [NVS 420]
        0x06F9,  # G98 [FX 370 LP]
        0x06FA,  # G98 [NVS 450]
        0x06FB,  # G98 [FX 370M]
        0x06FD,  # G98 [NVS 295]
        0x06FF,  # G98 [HICx16]
        # GT200
        0x05E0,  # GT200 [GTX 295]
        0x05E1,  # GT200 [GTX 280]
        0x05E2,  # GT200 [GTX 260]
        0x05E3,  # GT200 [GTX 285]
        0x05E6,  # GT200 [GTX 275]
        0x05E7,  # GT200 [C1060]
        0x05E9,  # GT200 [CX]
        0x05EA,  # GT200 [GTX 260]
        0x05EB,  # GT200 [GTX 295]
        0x05ED,  # GT200 [FX 5800]
        0x05EE,  # GT200 [FX 4800]
        0x05EF,  # GT200 [FX 3800]
        0x05FD,  # GT200GL [Quadro FX 5800]
        0x05FE,  # GT200GL [Quadro FX 4800]
        0x05FF,  # GT200GL [Quadro FX 3800]
        # MCP77 GPU
        0x0840,  # MCP77 GPU [8200M]
        0x0844,  # MCP77 GPU [9100M G]
        0x0845,  # MCP77 GPU [8200M G]
        0x0846,  # MCP77 GPU [9200]
        0x0847,  # MCP77 GPU [9100]
        0x0848,  # MCP77 GPU [8300]
        0x0849,  # MCP77 GPU [8200]
        0x084A,  # MCP77 GPU [730A]
        0x084B,  # MCP77 GPU [9200]
        0x084C,  # MCP77 GPU [980A/780A SLI]
        0x084D,  # MCP77 GPU [750A SLI]
        0x084F,  # MCP77 GPU [8100 / 720A]
        # MCP79 GPU
        0x0860,  # MCP79 GPU [9400]
        0x0861,  # MCP79 GPU [9400]
        0x0862,  # MCP79 GPU [9400M G]
        0x0863,  # MCP79 GPU [9400M]
        0x0864,  # MCP79 GPU [9300]
        0x0865,  # MCP79 GPU [ION]
        0x0866,  # MCP79 GPU [9400M G]
        0x0867,  # MCP79 GPU [9400]
        0x0868,  # MCP79 GPU [760i SLI]
        0x0869,  # MCP79 GPU [9400]
        0x086A,  # MCP79 GPU [9400]
        0x086C,  # MCP79 GPU [9300 / 730i]
        0x086D,  # MCP79 GPU [9200]
        0x086E,  # MCP79 GPU [9100M G]
        0x086F,  # MCP79 GPU [8200M G]
        0x0870,  # MCP79 GPU [9400M]
        0x0871,  # MCP79 GPU [9200]
        0x0872,  # MCP79 GPU [G102M]
        0x0873,  # MCP79 GPU [G102M]
        0x0874,  # MCP79 GPU [ION]
        0x0876,  # MCP79 GPU [ION]
        0x087A,  # MCP79 GPU [9400]
        0x087D,  # MCP79 GPU [ION]
        0x087E,  # MCP79 GPU [ION LE]
        0x087F,  # MCP79 GPU [ION LE]
        # GT215
        0x0CA0,  # GT215 [GT 330]
        0x0CA2,  # GT215 [GT 320]
        0x0CA3,  # GT215 [GT 240]
        0x0CA4,  # GT215 [GT 340]
        0x0CA5,  # GT215 [GT 220]
        0x0CA7,  # GT215 [GT 330]
        0x0CA9,  # GT215 [GTS 250M]
        0x0CAC,  # GT215 [GT 220]
        0x0CAF,  # GT215 [GT 335M]
        0x0CB0,  # GT215 [GTS 350M]
        0x0CB1,  # GT215 [GTS 360M]
        0x0CBC,  # GT215 [FX 1800M]
        # GT216
        0x0A20,  # GT216 [GT 220]
        0x0A22,  # GT216 [315]
        0x0A23,  # GT216 [210]
        0x0A26,  # GT216 [405]
        0x0A27,  # GT216 [405]
        0x0A28,  # GT216 [GT 230M]
        0x0A29,  # GT216 [GT 330M]
        0x0A2A,  # GT216 [GT 230M]
        0x0A2B,  # GT216 [GT 330M]
        0x0A2C,  # GT216 [NVS 5100M]
        0x0A2D,  # GT216 [GT 320M]
        0x0A32,  # GT216 [GT 415]
        0x0A34,  # GT216 [GT 240M]
        0x0A35,  # GT216 [GT 325M]
        0x0A38,  # GT216 [400]
        0x0A3C,  # GT216 [FX 880M]
        # GT218
        0x0A60,  # GT218 [G210]
        0x0A62,  # GT218 [205]
        0x0A63,  # GT218 [310]
        0x0A64,  # GT218 [ION]
        0x0A65,  # GT218 [210]
        0x0A66,  # GT218 [310]
        0x0A67,  # GT218 [315]
        0x0A68,  # GT218 [G105M]
        0x0A69,  # GT218 [G105M]
        0x0A6A,  # GT218 [NVS 2100M]
        0x0A6C,  # GT218 [NVS 3100M]
        0x0A6E,  # GT218 [305M]
        0x0A6F,  # GT218 [ION]
        0x0A70,  # GT218 [310M]
        0x0A71,  # GT218 [305M]
        0x0A72,  # GT218 [310M]
        0x0A73,  # GT218 [305M]
        0x0A74,  # GT218 [G210M]
        0x0A75,  # GT218 [310M]
        0x0A76,  # GT218 [ION]
        0x0A78,  # GT218 [FX 380 LP]
        0x0A7A,  # GT218 [315M]
        0x0A7C,  # GT218 [FX 380M]
        0x10C0,  # GT218 [9300 GS]
        0x10C3,  # GT218 [8400GS]
        0x10C5,  # GT218 [405]
        0x10D8,  # GT218 [NVS 300]
        # MCP89 GPU
        0x08A0,  # MCP89 GPU [320M]
        0x08A2,  # MCP89 GPU [320M]
        0x08A3,  # MCP89 GPU [320M]
        0x08A4,  # MCP89 GPU [320M]
    ]

    fermi_ids = [
        # GF100
        0x06C0,  # GF100 [GTX 480]
        0x06C4,  # GF100 [GTX 465]
        0x06CA,  # GF100 [GTX 480M]
        0x06CB,  # GF100 [GTX 480]
        0x06CD,  # GF100 [GTX 470]
        0x06D1,  # GF100 [C2050 / C2070]
        0x06D2,  # GF100 [M2070]
        0x06D8,  # GF100 [6000]
        0x06D9,  # GF100 [5000]
        0x06DA,  # GF100 [5000M]
        0x06DC,  # GF100 [6000]
        0x06DD,  # GF100 [4000]
        0x06DE,  # GF100 [T20]
        0x06DF,  # GF100 [M2070-Q]
        # GF104
        0x0E22,  # GF104 [GTX 460]
        0x0E23,  # GF104 [GTX 460 SE]
        0x0E24,  # GF104 [GTX 460 OEM]
        0x0E30,  # GF104 [GTX 470M]
        0x0E31,  # GF104 [GTX 485M]
        0x0E3A,  # GF104 [3000M]
        0x0E3B,  # GF104 [4000M]
        # GF114
        0x1200,  # GF114 [GTX 560 Ti]
        0x1201,  # GF114 [GTX 560]
        0x1202,  # GF114 [GTX 560 Ti OEM]
        0x1203,  # GF114 [GTX 460 SE v2]
        0x1205,  # GF114 [GTX 460 v2]
        0x1206,  # GF114 [GTX 555]
        0x1207,  # GF114 [GT 645 OEM]
        0x1208,  # GF114 [GTX 560 SE]
        0x1210,  # GF114 [GTX 570M]
        0x1211,  # GF114 [GTX 580M]
        0x1212,  # GF114 [GTX 675M]
        0x1213,  # GF114 [GTX 670M]
        # GF106
        0x0DC0,  # GF106 [GT 440]
        0x0DC4,  # GF106 [GTS 450]
        0x0DC5,  # GF106 [GTS 450]
        0x0DC6,  # GF106 [GTS 450]
        0x0DCD,  # GF106 [GT 555M]
        0x0DCE,  # GF106 [GT 555M]
        0x0DD1,  # GF106 [GTX 460M]
        0x0DD2,  # GF106 [GT 445M]
        0x0DD3,  # GF106 [GT 435M]
        0x0DD6,  # GF106 [GT 550M]
        0x0DD8,  # GF106 [2000]
        0x0DDA,  # GF106 [2000M]
        # GF116
        0x1241,  # GF116 [GT 545 OEM]
        0x1243,  # GF116 [GT 545]
        0x1244,  # GF116 [GTX 550 Ti]
        0x1245,  # GF116 [GTS 450 Rev. 2]
        0x1246,  # GF116 [GT 550M]
        0x1247,  # GF116 [GT 635M]
        0x1248,  # GF116 [GT 555M]
        0x1249,  # GF116 [GTS 450 Rev. 3]
        0x124B,  # GF116 [GT 640 OEM]
        0x124D,  # GF116 [GT 555M]
        0x1251,  # GF116 [GTX 560M]
        # GF108
        0x0DE0,  # GF108 [GT 440]
        0x0DE1,  # GF108 [GT 430]
        0x0DE2,  # GF108 [GT 420]
        0x0DE3,  # GF108 [GT 635M]
        0x0DE4,  # GF108 [GT 520]
        0x0DE5,  # GF108 [GT 530]
        0x0DE8,  # GF108 [GT 620M]
        0x0DE9,  # GF108 [GT 630M]
        0x0DEA,  # GF108 [610M]
        0x0DEB,  # GF108 [GT 555M]
        0x0DEC,  # GF108 [GT 525M]
        0x0DED,  # GF108 [GT 520M]
        0x0DEE,  # GF108 [GT 415M]
        0x0DEF,  # GF108 [NVS 5400M]
        0x0DF0,  # GF108 [GT 425M]
        0x0DF1,  # GF108 [GT 420M]
        0x0DF2,  # GF108 [GT 435M]
        0x0DF3,  # GF108 [GT 420M]
        0x0DF4,  # GF108 [GT 540M]
        0x0DF5,  # GF108 [GT 525M]
        0x0DF6,  # GF108 [GT 550M]
        0x0DF7,  # GF108 [GT 520M]
        0x0DF8,  # GF108 [600]
        0x0DF9,  # GF108 [500M]
        0x0DFA,  # GF108 [1000M]
        0x0DFC,  # GF108 [NVS 5200M]
        0x0F00,  # GF108 [GT 630]
        0x0F01,  # GF108 [GT 620]
        0x0F02,  # GF108 [GT 730]
        # GF110
        0x1080,  # GF110 [GTX 580]
        0x1081,  # GF110 [GTX 570]
        0x1082,  # GF110 [GTX 560 Ti]
        0x1084,  # GF110 [GTX 560]
        0x1086,  # GF110 [GTX 570]
        0x1087,  # GF110 [GTX 560 Ti]
        0x1088,  # GF110 [GTX 590]
        0x1089,  # GF110 [GTX 580]
        0x108B,  # GF110 [GTX 580]
        0x1091,  # GF110 [M2090]
        0x1096,  # GF110GL [Tesla C2050 / C2075]
        0x109A,  # GF110 [5010M]
        0x109B,  # GF110 [7000]
        # GF119
        0x1040,  # GF119 [GT 520]
        0x1042,  # GF119 [510]
        0x1048,  # GF119 [605]
        0x1049,  # GF119 [GT 620]
        0x104A,  # GF119 [GT 610]
        0x104B,  # GF119 [GT 625 OEM]
        0x104C,  # GF119 [GT 705]
        0x1050,  # GF119 [GT 520M]
        0x1051,  # GF119 [GT 520MX]
        0x1052,  # GF119 [GT 520M]
        0x1054,  # GF119 [410M]
        0x1055,  # GF119 [410M]
        0x1056,  # GF119 [NVS 4200M]
        0x1057,  # GF119 [NVS 4200M]
        0x1058,  # GF119 [610M]
        0x1059,  # GF119 [610M]
        0x105A,  # GF119 [610M]
        0x105B,  # GF119M [705M]
        0x107C,  # GF119 [NVS 315]
        0x107D,  # GF119 [NVS 310]
        # GF117
        0x1140,  # GF117 [GT 620M]
    ]

    kepler_ids = [
        # GK104
        0x1180,  # GK104 [GTX 680]
        0x1183,  # GK104 [GTX 660 Ti]
        0x1184,  # GK104 [GTX 770]
        0x1185,  # GK104 [GTX 660]
        0x1186,  # GK104 [GTX 660 Ti]
        0x1187,  # GK104 [GTX 760]
        0x1188,  # GK104 [GTX 690]
        0x1189,  # GK104 [GTX 670]
        0x118E,  # GK104 [GTX 760 OEM]
        0x118F,  # GK104GL [Tesla K10]
        0x1198,  # GTX 880M
        0x1199,  # GK104 [GTX 870M]
        0x119A,  # GTX 860M
        0x119D,  # GK104M [GTX 775M Mac Edition]
        0x119E,  # GTX 780M
        0x119F,  # GK104 [GTX 780M]
        0x11A0,  # GK104 [GTX 680M]
        0x11A1,  # GK104 [GTX 670MX]
        0x11A2,  # GK104 [GTX 675MX]
        0x11A3,  # GK104 [GTX 680MX]
        0x11A7,  # GK104 [GTX 675MX]
        0x11A9,  # GTX 870M
        0x11B4,  # GK104GL [Quadro K4200]
        0x11B6,  # Quadro K3100M
        0x11B7,  # Quadro K4100M
        0x11B8,  # Quadro K5100M
        0x11BA,  # GK104 [K5000]
        0x11BC,  # GK104 [K5000M]
        0x11BD,  # GK104 [K4000M]
        0x11BE,  # GK104 [K3000M]
        0x11BF,  # GK104 [GRID K2]
        # GK106
        0x11C0,  # GK106 [GTX 660]
        0x11C2,  # GK106 [GTX 650 Ti BOOST]
        0x11C6,  # GK106 [GTX 650 Ti]
        0x11E0,  # GK106 [GTX 770M]
        0x11E1,  # GTX 765M
        0x11E2,  # GTX 765M
        0x11FA,  # GK106 [K4000]
        0x11FC,  # Quadro K2100M
        # GK107
        0x0FC0,  # GK107 [GT 640]
        0x0FC1,  # GK107 [GT 640]
        0x0FC2,  # GK107 [GT 630]
        0x0FC6,  # GK107 [GTX 650]
        0x0FC8,  # GK107 [GT 740]
        0x0FCD,  # GK107M [GT 755M]
        0x0FD1,  # GK107 [GT 650M]
        0x0FD2,  # GK107 [GT 640M]
        0x0FD3,  # GK107 [GT 640M LE]
        0x0FD4,  # GK107 [GTX 660M]
        0x0FD5,  # GK107 [GT 650M]
        0x0FD8,  # GK107 [GT 640M]
        0x0FD9,  # GK107 [GT 645M]
        0x0FDF,  # GK107M [ GT 740M]
        0x0FE0,  # GK107 [GTX 660M]
        0x0FE1,  # GK107M [GT 730M]
        0x0FE3,  # GK107M [GT 745M]
        0x0FE4,  # GK107M [GT 750M]
        0x0FE9,  # GK107 [GT 750M Mac Edition]
        0x0FEA,  # GK107M [GT 755M Mac Edition]
        0x0FEE,  # GK107M [810M]
        0x0FF2,  # GK107GL [GRID K1]
        0x0FF3,  # GK107GL [Quadro K420]
        0x0FF6,  # Quadro K1100M
        0x0FF9,  # GK107 [K2000D]
        0x0FFA,  # GK107 [K600]
        0x0FFB,  # GK107 [K2000M]
        0x0FFC,  # GK107 [K1000M]
        0x0FFD,  # GK107 [NVS 510]
        0x0FFE,  # GK107 [K2000]
        0x0FFF,  # GK107 [410]
        # GK110
        0x1001,  # GK110B [GTX TITAN Z]
        0x1003,  # GK110 [GTX Titan LE]
        0x1004,  # GK110 [GTX 780]
        0x1005,  # GK110 [GTX Titan]
        0x1007,  # GK110 [GTX 780 Rev. 2]
        0x100A,  # GK110B [GTX 780 Ti]
        0x100C,  # GK110B [GTX TITAN Black]
        0x101F,  # GK110 [TEslA K20]
        0x1020,  # GK110 [TEslA K2]
        0x1021,  # GK110 [TEslA K2m]
        0x1022,  # GK110 [TEslA K20C]
        0x1023,  # GK110BGL [Tesla K40m]
        0x1024,  # GK180GL [Tesla K40c]
        0x1026,  # GK110 [TEslA K20s]
        0x1028,  # GK110 [TEslA K20m]
        0x102D,  # GK210GL [Tesla K80]
        0x103C,  # GK110GL [Quadro K5200]
        # GK208
        0x1280,  # GK208 [GT 635]
        0x1281,  # GK208 [GT 710]
        0x1282,  # GK208 [GT 640 REv. 2]
        0x1284,  # GK208 [GT 630 REv. 2]
        0x1286,  # GK208 [GT 720]
        0x1287,  # GK208B [GT 730]
        0x1288,  # GK208B [GT 720]
        0x1289,  # GK208 [GT 710]
        0x128B,  # GK208B [GT 710]
        0x1290,  # GK208 [GT 730M]
        0x1291,  # GK208 [GT 735M]
        0x1292,  # GK208 [GT 740M]
        0x1293,  # GK208 [GT 730M]
        0x1294,  # GK208 [GT 740M]
        0x1295,  # GK208 [710M]
        0x1296,  # GK208M [825M]
        0x1298,  # GK208M [GT 720M]
        0x1299,  # GK208BM [920M]
        0x129A,  # GK208BM [910M]
        0x12B9,  # GK208 [K610M]
        0x12BA,  # GK208 [K510M]
    ]


class amd_ids:

    gcn_7000_ids = [
        # GCN v1
        # AMDPitcairnGraphicsAccelerator - AMD7000Controller
        0x6800,  # HD 7970M
        0x6801,  # HD 8970M
        0x6806,  # Unknown
        0x6808,  # W7000
        0x6810,  # R7 370 / R9 270X/370X
        0x6818,  # HD 7870
        0x6819,  # HD 7850 / R7 265 / R9 270 1024SP
        # AMDTahitiGraphicsAccelerator - AMD7000Controller
        0x6790,  # Unknown
        0x6798,  # HD 7970/8970 OEM / R9 280X / D700
        0x679A,  # HD 7950/8950 OEM / R9 280
        0x679E,  # HD 7870 XT
        0x6780,  # W9000
        # AMDVerdeGraphicsAccelerator - AMD7000Controller
        0x6820,  # HD 8890M / R9 M275X/M375X / M5100
        0x6821,  # HD 8870M / R9 M270X/M370X
        0x6823,  # HD 8850M / R9 M265X
        0x6825,  # HD 7870M
        0x6827,  # HD 7850M/8850M
        0x682B,  # HD 8830M / R7 250 / R7 M465X
        0x682D,  # M4000
        0x682F,  # HD 7730M
        0x6835,  # R9 255
        0x6839,  # Unknown
        0x683B,  # Unknown
        0x683D,  # HD 7770/8760 / R7 250X
        0x683F,  # HD 7750/8740 / R7 250E
    ]

    gcn_8000_ids = [
        # GCN v2
        # AMDBonaireGraphicsAccelerator - AMD8000Controller
        0x6640,  # M6100
        0x6641,  # HD 8930M
        0x6646,  # R9 M280X / W6170M
        0x6647,  # R9 M270X/M280X
        0x6650,  # Unknown
        0x6651,  # Unknown
        0x665C,  # HD 7790/8770 / R7 360 / R9 260/360
        0x665D,  # R7 200
        # AMDHawaiiGraphicsAccelerator - AMD8000Controller
        0x67B0,  # R9 290X/390X
    ]

    gcn_9000_ids = [
        # GCN v3
        # AMDFijiGraphicsAccelerator - AMD9000Controller
        0x7300,  # R9 FURY / NANO
        0x730F,  # Unknown
        # AMDTongaGraphicsAccelerator - AMD9000Controller
        0x6920,  # R9 M395/ M395X
        0x6921,  # R9 M295X / M390X
        0x6930,  # Unknown
        0x6938,  # R9 380X / R9 M295X
        0x6939,  # R9 285/380
    ]

    polaris_ids = [
        # GCN v4
        # AMDRadeonX4000
        # AMDBaffinGraphicsAccelerator - AMD9500Controller
        0x67E0,
        0x67E3,
        0x67E8,
        0x67EB,
        0x67EF,
        0x67FF,
        0x67E1,
        0x67E7,
        0x67E9,
        # AMDEllesmereGraphicsAccelerator - AMD9500Controller
        0x67C0,
        0x67C1,
        0x67C2,
        0x67C4,
        0x67C7,
        0x67DF,
        0x67D0,
        0x67C8,
        0x67C9,
        0x67CA,
        0x67CC,
        0x67CF,
    ]

    vega_ids = [
        # GCN v5
        # AMDRadeonX5000
        # AMDVega10GraphicsAccelerator - AMD10000Controller
        0x6860,
        0x6861,
        0x6862,
        0x6863,
        0x6864,
        0x6867,
        0x6868,
        0x6869,
        0x686A,
        0x686B,
        0x686C,
        0x686D,
        0x686E,
        0x686F,
        0x687F,
        # AMDVega12GraphicsAccelerator - AMD10000Controller
        0x69A0,
        0x69A1,
        0x69A2,
        0x69A3,
        0x69AF,
        # AMDVega20GraphicsAccelerator - AMD10000Controller
        0x66A0,
        0x66A1,
        0x66A2,
        0x66A3,
        0x66A7,
        0x66AF,
    ]

    navi_ids = [
        # AMDRadeonX6000
        # AMDNavi10GraphicsAccelerator
        0x7310,
        0x7312,
        0x7318,
        0x7319,
        0x731A,
        0x731B,
        0x731F,
        # AMDNavi12GraphicsAccelerator
        0x7360,  # 5600M
        # AMDNavi14GraphicsAccelerator
        0x7340,  # 5500/5500M / Pro 5500M
        0x7341,  # Pro W5500
        0x7343,  # Unknown
        0x7347,  # Pro W5500M
        0x734F,  # Pro W5300M
        # AMDNavi21GraphicsAccelerator
        0x73A2,  # Pro W6900X
        0x73AB,  # Pro W6800X/Pro W6800X Duo
        0x73BF,  # 6800/6800 XT / 6900 XT
        # AMDNavi23GraphicsAccelerator
        0x73E3,  # Pro W6600
        0x73FF,  # 6600/6600 XT/6600M
    ]

    r500_ids = [
        0x7187,  # X1300/X1550
        0x7146,  # X1300/X1550
        0x71c5,  # Mobile X1600
        0x7249,  # X1900 XT
    ]

    terascale_1_ids = [
        0x9400,
        0x9401,
        0x9402,
        0x9403,
        0x9581,
        0x9583,
        0x9588,
        0x94C8,
        0x94C9,
        0x9500,
        0x9501,
        0x9505,
        0x9507,
        0x9504,
        0x9506,
        0x9598,
        0x9488,
        0x9599,
        0x9591,
        0x9593,
        0x9440,
        0x9442,
        0x944A,
        0x945A,
        0x9490,
        0x949E,
        0x9480,
        0x9540,
        0x9541,
        0x954E,
        0x954F,
        0x9552,
        0x9553,
        0x94A0,
    ]

    terascale_2_ids = [
        0x6738,  # HD 6870
        0x6739,  # HD 6850
        0x6720,  # HD 6970M/6990M
        0x6722,  # Unknown
        0x6768,  # Unknown
        0x6770,  # HD 6450A/7450A
        0x6779,  # HD 6450/7450/8450 / R5 230 OEM
        0x6760,  # HD 6400M/7400M
        0x6761,  # HD 6430M
        0x68E0,  # HD 5430/5450/547
        0x6898,  # HD 5870
        0x6899,  # HD 5850
        0x68B8,  # HD 5770
        0x68B0,  # Unknown
        0x68B1,  # Unknown
        0x68A0,  # HD 5870 (mobile)
        0x68A1,  # HD 5850 (mobile)
        0x6840,  # HD 7500M/7600M
        0x6841,  # HD 7550M/7570M/7650M
        0x68D8,  # HD 5670/5690/5730
        0x68C0,  # HD 5730 / 6570M
        0x68C1,  # HD 5650/5750 / 6530M/6550M
        0x68D9,  # HD 5550/5570/5630/6510/6610/7570
        0x6750,  # HD 6650A/7650A
        0x6758,  # HD 6670/7670
        0x6759,  # HD 6570/7570/8550
        0x6740,  # HD 6730M/6770M/7690M XT
        0x6741,  # HD 6630M/6650M/6750M/7670M/7690M
        0x6745,  # Unknown
    ]


class intel_ids:
    gma_950_ids = [
        0x2582,
        0x2592,
        0x2772,
        0x27A2,
    ]

    gma_x3100_ids = [
        0x2a02,
    ]

    iron_ids = [
        # AppleIntelHDGraphics IDs
        0x0044,
        0x0046,
    ]

    sandy_ids = [
        # AppleIntelHD3000Graphics IDs
        # AppleIntelSNBGraphicsFB IDs
        0x0106,
        0x0601,
        0x0116,
        0x0102,
        0x0126,
    ]

    ivy_ids = [
        # AppleIntelHD4000Graphics IDs
        # AppleIntelFramebufferCapri IDs
        0x0152,
        0x0156,
        0x0162,
        0x0166,
    ]

    haswell_ids = [
        # AppleIntelHD5000Graphics IDs
        # AppleIntelFramebufferAzul IDs
        0x0D26,
        0x0A26,
        0x0A2E,
        0x0D22,
        0x0412,
    ]

    broadwell_ids = [
        # AppleIntelBDWGraphicsFramebuffer IDs
        0x0BD1,
        0x0BD2,
        0x0BD3,
        0x1606,
        0x160E,
        0x1616,
        0x161E,
        0x1626,
        0x1622,
        0x1612,
        0x162B,
    ]

    skylake_ids = [
        # AppleIntelSKLGraphicsFramebuffer IDs
        0x1916,
        0x191E,
        0x1926,
        0x1927,
        0x1912,
        0x1932,
        0x1902,
        0x1917,
        0x193B,
        0x191B,
    ]

    kaby_lake_ids = [
        # AppleIntelKBLGraphicsFramebuffer IDs
        0x5912,
        0x5916,
        0x591B,
        0x591C,
        0x591E,
        0x5926,
        0x5927,
        0x5923,
    ]

    coffee_lake_ids = [
        # AppleIntelCFLGraphicsFramebuffer IDs
        0x3E9B,
        0x3EA5,
        0x3EA6,
        0x3E92,
        0x3E91,
        0x3E98,
    ]

    comet_lake_ids = [
        0x9BC8,
        0x9BC5,
        0x9BC4,
    ]

    ice_lake_ids = [
        # AppleIntelICLLPGraphicsFramebuffer IDs
        0xFF05,
        0x8A70,
        0x8A71,
        0x8A51,
        0x8A5C,
        0x8A5D,
        0x8A52,
        0x8A53,
        0x8A5A,
        0x8A5B,
    ]

    AppleIntel8254XEthernet = [
        # AppleIntel8254XEthernet IDs
        0x1096,
        0x100F,
        0x105E,
    ]

    AppleIntelI210Ethernet = [
        # AppleIntelI210Ethernet IDs
        0x1533,  # I210
        0x15F2,  # I225
        0x15F3,  # I225
        0x3100,  # I225
        0x3101,  # I225
        0x5502,  # I225
        0x0D9F,  # I225
        0x15F8,  # I225
        0x15F7,  # I225
        0x15FD,  # I225
    ]

    Intel82574L = [
        # Intel82574L IDs
        0x104B,
        0x10F6,
    ]


class broadcom_ids:
    AppleBCMWLANBusInterfacePCIe = [
        0x43DC,  # BCM4355
        0x4464,  # BCM4364
        0x4488,  # BCM4377b
        0x4425,  # Unknown
    ]

    AirPortBrcmNIC = [
        # AirPortBrcmNIC IDs
        0x43BA,  # BCM43602
        0x43A3,  # BCM4350
        0x43A0,  # BCM4360
    ]

    AirPortBrcm4360 = [
        # AirPortBrcm4360 IDs (removed duplicates for 4360 class cards)
        0x4331,  # BCM94331
        0x4353,  # BCM943224
    ]

    AirPortBrcm4331 = [
        # AirPortBrcm4331 IDs (removed duplicates for 4331 class cards)
        0x432B,  # BCM94322
    ]

    AppleAirPortBrcm43224 = [
        # AppleAirPortBrcm43224 IDs
        0x4311,  # BCM4311 - never used by Apple
        0x4312,  # BCM4311 - never used by Apple
        0x4313,  # BCM4311 - never used by Apple
        0x4318,  # BCM4318 - never used by Apple
        0x4319,  # BCM4318 - never used by Apple
        0x431A,  # Unknown - never used by Apple
        0x4320,  # BCM4306 - never used by Apple
        0x4324,  # BCM4309 - never used by Apple
        0x4325,  # BCM4306 - never used by Apple
        0x4328,  # BCM4328
        0x432C,  # BCM4322 - never used by Apple
        0x432D,  # BCM4322 - never used by Apple
    ]

    AppleBCM5701Ethernet = [
        # AppleBCM5701Ethernet IDs
        0x1684,
        0x16B0,
        0x16B4,
        0x1682,
        0x1686,
    ]


class aquantia_ids:
    AppleEthernetAquantiaAqtion = [
        # AppleEthernetAquantiaAqtion IDs
        0x0001,  # AQC107
        0xD107,  # AQC107
        0x07B1,  # AQC107
        0x80B1,  # AQC107
        0x87B1,  # AQC107
        0x88B1,  # AQC107
        0x89B1,  # AQC107
        0x91B1,  # AQC107
        0x92B1,  # AQC107
        0x00C0,  # AQC113
        0x04C0,  # AQC113
    ]


class marvell_ids:
    MarvelYukonEthernet = [
        # AppleYukon2.kext IDs
        # AppleYukon2 supports 2 vendors (Marvell and SysKonnect)
        0x9E00,
        0x2100,
        0x9E00,
        0x2200,
        0x9E00,
        0x8100,
        0x9E00,
        0x8200,
        0x9E00,
        0x9100,
        0x9E00,
        0x9200,
        0x9000,
        0x2100,
        0x9000,
        0x2200,
        0x9000,
        0x8100,
        0x9000,
        0x8200,
        0x9000,
        0x9100,
        0x9000,
        0x9200,
        0x9E00,
        0x2200,
        0x9E00,
        0x2200,
    ]


class syskonnect_ids:
    MarvelYukonEthernet = [
        # AppleYukon2.kext IDs
        # AppleYukon2 supports 2 vendors (Marvell and SysKonnect)
        0x4365,
        0x4360,
        0x435A,
        0x4354,
        0x4362,
        0x4363,
        0x00BA,
        0x436A,
    ]


class atheros_ids:
    AtherosWifi = [
        # AirPortAtheros40 IDs
        0x0030,  # AR93xx
        0x002A,  # AR928X
        0x001C,  # AR242x / AR542x
        0x0023,  # AR5416 - never used by Apple
        0x0024,  # AR5418
    ]
