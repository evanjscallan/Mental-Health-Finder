import pandas as pd

newvar = ([
  [
    [
      "Resolution Ranch Academy"
    ],
    [
      "2274 County Road 203 Loop",
      "Cameron, Texas 76520"
    ],
    [
      "Phone: (254) 697-2422"
    ],
    [
      "Intake: (254) 718-3364"
    ],
    [
      "1 MH 2 RES TELE 3 RTCC 4 AT BMT CBT CFT DBT GT IPT PTM",
      "6 PVTP 8 OSF SF 10 CO 11 CM DEC ES FPSY HS PRS 13 SMPD 14",
      "CHLD"
    ]
  ],
  [
    [
      "Andrews Center Behavioral Healthcare"
    ],
    [
      "575 West Highway 243",
      "Canton, Texas 75103"
    ],
    [
      "Phone: (903) 567-4197"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 BMT CBT IDD IPT PTM TT 5 CIT",
      "WI 6 PVTN 7 STMH 8 CLF CMHG MC MD MI PI SCJJ SF SI SMHA",
      "VAF 9 PA SS 10 CJ CO 11 ACT CDM CM COOT ICM IMR IPC PEER",
      "PRS SEMP SH SPS 12 STU 13 SMON 14 ADLT CHLD SNR YAD 17 SP"
    ]
  ],
  [
    [
      "Upb New Life Childrens Treatment Ctr"
    ],
    [
      "650 Scarbourough",
      "Canyon Lake, Texas 78133"
    ],
    [
      "Phone: (830) 964-4390"
    ],
    [
      "Intake: (830) 924-4390 (830) 624-4667"
    ],
    [
      "1 MH 2 RES TELE 3 RTCC 4 AT CBT CFT DBT GT IPT PTM TT",
      "6 PVTN 8 ITU MD SCJJ SEF SF SWFS 10 PTSD SED 11 CM ES FPSY",
      "ICM SPS 13 SMON 14 CHLD 17 SP"
    ]
  ],
  [
    [
      "Springstone Inc"
    ],
    [
      "Carrollton Springs",
      "2225 Parker Road",
      "Carrollton, Texas 75010"
    ],
    [
      "Phone: (972) 242-4114"
    ],
    [
      "1 MH 2 HI PHDT TELE 3 PSY 4 AT BMT CBT CFT GT IDD IPT",
      "PTM TT 5 CIT WI 6 PVTP 7 STMH 8 MC MI PI SF 10 SE CO",
      "TRMA PTSD SMI 11 DEC ES FPSY PRS SPS 12 NRT NSC STU TCC 13",
      "SMPD 14 ADLT SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Community Healthcore - Panola County"
    ],
    [
      "1701 South Adams Street",
      "Suite A",
      "Carthage, Texas 75633"
    ],
    [
      "Phone: (903) 693-7811"
    ],
    [
      "Intake: (800) 446-8253 (800) 4IN-TAKE"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT CFT GT IPT PTM TT 5 CIT",
      "PVTN 7 STMH 8 CLF CMHG CSBG MC MD PI SF SI SMHA 10 VET",
      "CO SED SMI 11 CM DEC HS IMR PRS SEMP SH SPS VRS 12 STU 13",
      "SMON 14 ADLT CHLD SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Hunt Regional Outpatient Behav Health"
    ],
    [
      "2904 Sterling Hart Drive",
      "Commerce, Texas 75428"
    ],
    [
      "Phone: (903) 886-2238"
    ],
    [
      "1 MH 2 OP 3 OMH 4 BMT CBT CFT DBT GT IPT PTM 6 PVTP",
      "7 STMH 8 MC MD MI PI SF 10 SE CO 11 CM ICM SPS 12 NSC TCC",
      "13 SMON 14 ADLT SNR 16 AH"
    ]
  ],
  [
    [
      "Aspire Hospital LLC"
    ],
    [
      "2006 South Loop 336 West",
      "Suite 500",
      "Conroe, Texas 77304"
    ],
    [
      "Phone: (936) 647-3500"
    ],
    [
      "Intake: (936) 200-6201"
    ],
    [
      "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT BMT CBT CFT DBT GT",
      "IDD IPT PTM TT 5 WI 6 PVTP 8 CLF MC MD MI PI SF SI SMHA",
      "VAF 10 SE VET CO HV TRMA ALZ PED PTSD SMI 11 CDM COOT",
      "DEC ES FPSY HS IMR IPC PRS SPS 12 NRT NSC STU 13 SMON 14",
      "ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Tri County Behavioral Healthcare"
    ],
    [
      "706 Old Montgomery Road",
      "Conroe, Texas 77304"
    ],
    [
      "Phone: (936) 521-6100"
    ],
    [
      "Intake: (800) 550-8408"
    ],
    [
      "1 MH 2 HI TELE 4 IDD PTM 5 CIT WI 6 LMG 7 STMH 8 CLF",
      "CMHG MC MD OSF PI SF SI SMHA 9 SS 10 CO 11 DEC ES IMR SPS 12",
      "NRT NSC STU 13 SMPD 14 ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Behavioral Health Ctr of Nueces County - Mental Health Services"
    ],
    [
      "1546 South Brownlee Boulevard",
      "Corpus Christi, Texas 78404"
    ],
    [
      "Phone: (361) 886-6900"
    ],
    [
      "Intake: (361) 886-6970"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT GT IPT PTM 5 CIT 6 SMA 7",
      "STMH 8 CLF CMHG CSBG MC MD MI OSF PI SF SI SMHA 10 VET CJ",
      "SMI 11 ACT CM COOT ES FPSY HS ICM IMR IPC PEER PRS SEMP SH",
      "SPS VRS 12 NRT NSC STU TCC 13 SMON 14 ADLT SNR YAD 16 AH",
      "17 SP"
    ]
  ],
  [
    [
      "Christus Spohn Memorial Hospital - Care Integrated Behavioral Health"
    ],
    [
      "2606 Hospital Boulevard",
      "Corpus Christi, Texas 78405"
    ],
    [
      "Phone: (361) 902-4006"
    ],
    [
      "1 MH 2 HI 3 PSY 4 AT BMT CBT CFT GT IDD IPT PTM TT 5 WI",
      "6 PVTN 8 CLF MC MD MI PI SCJJ SF SI SMHA 10 SE CO ALZ SMI 11",
      "FPSY SPS 12 NSC STU TCC 13 SMON 14 ADLT SNR YAD 17 SP"
    ]
  ],
  [
    [
      "Corpus Christi Medical Center Northwest"
    ],
    [
      "13725 NW Boulevard",
      "Corpus Christi, Texas 78410"
    ],
    [
      "Phone: (361) 986-8200"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 AT GT IDD IPT PTM TT 6 PVTP",
      "7 STMH 8 CLF MC MD MI PI SF SI SMHA SWFS VAF 10 TAY SE CO",
      "SED SMI 11 SPS 12 STU 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17",
      "SP"
    ]
  ],
  [
    [
      "Childrens Health System of Texas - Childrens Medical Center Dallas"
    ],
    [
      "1935 Medical District Drive",
      "Dallas, Texas 75235"
    ],
    [
      "Phone: (214) 456-5900"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 AT BMT CBT CFT GT IDD IPT",
      "PTM 5 WI 6 PVTN 7 STMH 8 MC MD MI PI SF SMHA SWFS 10",
      "GL CO SED 11 ES FPSY SPS 12 NRT STU TCC 13 SMON 14 CHLD 16",
      "AH 17 SP"
    ]
  ],
  [
    [
      "Medical City Green Oaks Hospital"
    ],
    [
      "7808 Clodus Fields Drive",
      "Dallas, Texas 75251"
    ],
    [
      "Phone: (972) 991-9504"
    ],
    [
      "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT ECT GT IDD IPT PTM 5",
      "CIT WI 6 PVTP 8 MC MD MI PI SF 10 CO 11 CM DEC FPSY IPC",
      "PEER PRS SPS 12 NRT NSC STU TCC 13 SMON 14 ADLT CHLD SNR",
      "YAD 16 AH"
    ]
  ],
  [
    [
      "Metrocare Services - Lancaster/Kiest OP Clinic"
    ],
    [
      "3330 South Lancaster Road",
      "Dallas, Texas 75216"
    ],
    [
      "Phone: (214) 371-6639"
    ],
    [
      "1 MH 2 OP 3 CMHC 4 CBT CFT IDD IPT PTM 5 WI 6 LMG 8",
      "CLF CMHG CSBG MC MD OSF PI SF SI SMHA SWFS 11 CM IMR IPC",
      "PRS SH 12 STU 13 SMON 14 ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Texas Health Behavioral Health Dallas"
    ],
    [
      "8200 Walnut Hill Lane",
      "Dallas, Texas 75231"
    ],
    [
      "Phone: (214) 345-7355"
    ],
    [
      "Intake: (682) 236-6023"
    ],
    [
      "1 MH 2 HI 3 PSY 4 AT CBT GT IPT PTM 5 CIT WI 6 PVTN 7",
      "STMH 8 MC MD MI PI SF 11 CM DEC FPSY PEER SPS 12 NRT NSC",
      "STU TCC 13 SMON 14 ADLT SNR YAD"
    ]
  ],
  [
    [
      "Texas Health Behavioral Health Dallas"
    ],
    [
      "8140 Walnut Hill Lane",
      "Suite 204",
      "Dallas, Texas 75231"
    ],
    [
      "Phone: (214) 345-7355"
    ],
    [
      "Intake: (682) 236-6023"
    ],
    [
      "1 MH 2 OP PHDT 3 PH 4 CBT CFT DBT GT IPT PTM 5 CIT WI",
      "6 PVTN 8 MC MD PI SF 11 CM DEC FPSY SPS 12 STU TCC 13",
      "SMPD 14 ADLT SNR YAD"
    ]
  ],
  [
    [
      "UT Southwestern University Hospital - Zale Lipshy"
    ],
    [
      "5151 Harry Hines Boulevard",
      "4th Floor",
      "Dallas, Texas 75390"
    ],
    [
      "Phone: (214) 645-4490"
    ],
    [
      "Intake: (214) 630-7285"
    ],
    [
      "1 MH 2 HI 3 PSY 4 AT BMT CBT CFT ECT GT IPT PTM TT 6",
      "PVTN 8 MC MI PI SF 10 SE CO TRMA TBI PTSD SMI 11 DEC ES FPSY",
      "IMR SPS 12 NRT NSC STU TCC 13 SMON 14 ADLT SNR YAD 16 AH",
      "17 SP F28 F30 F42 F43 F47 F67 F70 F92"
    ]
  ],
  [
    [
      "VA North Texas HCS/Dallas VAMC"
    ],
    [
      "4500 South Lancaster Road",
      "Dallas, Texas 75216"
    ],
    [
      "Phone: (800) 849-3597"
    ],
    [
      "Intake: (214) 857-0853"
    ],
    [
      "1 MH 2 HI OP PHDT RES TELE 4 AT BMT CBT CFT DBT ECT GT",
      "IDD IPT PTM TT 5 CIT WI 6 VAMC 7 STMH 8 MI PI SF VAF 10",
      "SE GL VET ADM MF CJ CO TRMA TBI ALZ PTSD SMI 11 ACT CDM",
      "CM DEC ES FPSY HS ICM IMR IPC LAD PEER PRS SEMP SH SPS VRS 12",
      "NRT NSC STU TCC 13 SMPD 14 ADLT SNR YAD 15 VO 17 SP"
    ]
  ],
  [
    [
      "West Texas Centers - Yoakum County"
    ],
    [
      "104 West 2nd Street",
      "Denver City, Texas 79323"
    ],
    [
      "Phone: (806) 592-8226"
    ],
    [
      "Intake: (800) 375-4357"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 BMT CBT GT IDD IPT PTM 5 CIT",
      "WI 6 PVTN 7 STMH 8 CLF MC MD MI PI SCJJ SF SI SMHA SWFS",
      "9 SS 10 TAY SE VET CO TRMA SMI 11 ACT CM COOT ES FPSY HS",
      "ICM IMR PEER PRS SEMP SH SPS VRS 12 NSC STU TCC 13 SMON 14",
      "ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Dallas Behavioral Healthcare Hospital"
    ],
    [
      "800 Kirnwood Drive",
      "Desoto, Texas 75115"
    ],
    [
      "Phone: (972) 982-0897"
    ],
    [
      "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT CBT CFT GT IDD IPT",
      "PTM 5 CIT WI 6 PVTP 8 MC MD MI OSF PI SF SI SMHA VAF 10 SE",
      "VET CO SMI 11 CM DEC ES FPSY IMR IPC LAD SPS 12 NRT NSC STU",
      "TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Hickory Trail Hospital"
    ],
    [
      "2000 Old Hickory Trail",
      "Desoto, Texas 75115"
    ],
    [
      "Phone: (972) 298-7323"
    ],
    [
      "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT CBT CFT DBT GT IDD",
      "IPT PTM TT 5 CIT WI 6 PVTP 8 MC MD MI PI SF VAF 10 SE CO",
      "SED SMI 11 CM ES FPSY SPS 12 STU 13 SMPD 14 ADLT CHLD SNR",
      "YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Texas Panhandle Centers"
    ],
    [
      "500 East 1st Street",
      "Suite 203",
      "Dumas, Texas 79029"
    ],
    [
      "Phone: (806) 935-5691"
    ],
    [
      "Intake: (806) 337-1000"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 CBT PTM 5 CIT 6 SMA 7 STMH",
      "8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SI SMHA SWFS VAF",
      "9 PA SS 10 VET MF SED SMI 11 CM COOT ICM IMR IPC PRS SEMP",
      "SH SPS 12 NRT STU TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Behavioral Hospital at Renaisance"
    ],
    [
      "5510 Raphael Drive",
      "Edinburg, Texas 78539"
    ],
    [
      "Phone: (956) 362-4357"
    ],
    [
      "Intake: (956) 362-2725"
    ],
    [
      "1 MH 2 HI OP 3 PSY 4 AT BMT CBT CFT DBT GT IDD IPT PTM",
      "TT 5 CIT WI 6 PVTP 7 STMH 8 CLF CMHG CSBG ITU MC MD",
      "MI OSF PI SCJJ SEF SF SI SMHA SWFS VAF 10 TAY SE GL VET ADM M",
      "CJ CO HV TRMA TBI ALZ PED PTSD SMI 11 CDM CM DEC ES FPSY",
      "ICM IMR IPC SPS 12 STU TCC 13 SMPD 14 ADLT CHLD SNR YAD",
      "AH 17 SP"
    ]
  ],
  [
    [
      "Emergence Health Network - Central Outpatient Services"
    ],
    [
      "1551 Montana Avenue",
      "El Paso, Texas 79902"
    ],
    [
      "Phone: (915) 747-3510"
    ],
    [
      "Intake: (915) 887-3410 (915) 779-1800"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT CFT GT IDD IPT PTM TT 5",
      "WI 6 PVTN 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SF",
      "SMHA 10 CO TRMA PED PTSD 11 CM COOT ICM IMR PEER PRS",
      "SEMP SH SPS VRS 12 NRT NSC STU TCC 13 SMPD 14 ADLT SNR YAD",
      "16 AH 17 SP"
    ]
  ],
  [
    [
      "Emergence Health Network - ChAMhPs"
    ],
    [
      "8500 Boeing Drive",
      "El Paso, Texas 79925"
    ],
    [
      "Phone: (915) 599-6600"
    ],
    [
      "Intake: (915) 887-3410"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 CBT CFT GT IPT PTM TT 5 CIT WI",
      "6 SMA 7 STMH FQHC 8 MD MI PI SF SI SWFS 10 SED 11 CM",
      "COOT FPSY ICM PRS SPS 13 SMON 14 CHLD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Emergence Health Network - East Valley Outpatient Services"
    ],
    [
      "2400 Trawood Drive",
      "Suite 301",
      "El Paso, Texas 79936"
    ],
    [
      "Phone: (915) 599-6735"
    ],
    [
      "Intake: (915) 599-6735x2 (915) 779-1800"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 CBT GT IDD IPT PTM TT 6 LMG 7",
      "STMH 8 CLF ITU MC MD MI OSF PI SCJJ SF SI SMHA SWFS 10 SMI",
      "11 CM COOT DEC FPSY IMR PEER PRS SEMP SH SPS 12 NRT STU",
      "TCC 13 SMON 14 ADLT SNR YAD 17 SP"
    ]
  ],
  [
    [
      "JPS Behavioral Center/Northeast"
    ],
    [
      "3200 West Euless Boulevard",
      "Euless, Texas 76040"
    ],
    [
      "Phone: (817) 702-3100"
    ],
    [
      "1 MH 2 OP PHDT 3 PH 4 AT BMT CFT GT IPT TT 5 CIT 6",
      "PVTN 7 STMH FQHC 8 MC MD PI SCJJ SF SI SWFS 9 PA 10 SE",
      "TRMA PTSD SMI 11 FPSY PRS 13 SMON 14 ADLT SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Heart of Texas Region MHMR Center"
    ],
    [
      "Freestone County Office",
      "622 West Main Street",
      "Fairfield, Texas 75840"
    ],
    [
      "Phone: (866) 752-3451"
    ],
    [
      "Intake: (254) 752-3451"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 PTM 5 CIT 6 LMG 7 STMH 8",
      "CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SMHA VAF 9 PA SS 11",
      "CM DEC IMR IPC PRS SEMP SH SPS 12 STU 13 SMON 14 ADLT CHLD",
      "SNR YAD 17 SP"
    ]
  ],
  [
    [
      "Whispering Hills Achievement Center"
    ],
    [
      "4110 FM 609",
      "Flatonia, Texas 78941"
    ],
    [
      "Phone: (361) 865-3083"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 BMT CBT CFT GT IPT PTM TT 5 CIT 6",
      "PVTP 8 MD SI SWFS 10 TRMA PTSD SED 11 CM ES SPS 13 SMON 14",
      "CHLD"
    ]
  ],
  [
    [
      "MH/MR/TC Circle Drive Clinic"
    ],
    [
      "1200 Circle Drive",
      "Suite 401",
      "Fort Worth, Texas 76119"
    ],
    [
      "Phone: (817) 569-4750-4756"
    ],
    [
      "Intake: (817) 335-3022"
    ],
    [
      "1 MH 2 OP 3 OMH 4 AT BMT CBT GT IDD PTM 6 LMG 7",
      "STMH FQHC 8 MC MD PI SF SMHA 9 PA 10 CO SMI 11 CDM CM",
      "DEC ES FPSY HS ICM IMR IPC PEER PRS SEMP SH SPS VRS 12 NRT",
      "NSC STU TCC 13 SMPD 14 ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "MH/MR/TC Fair West Clinic - Mental Health Services"
    ],
    [
      "1527 Hemphill Street",
      "Fort Worth, Texas 76104"
    ],
    [
      "Phone: (817) 569-5900"
    ],
    [
      "Intake: (817) 335-3022 (800) 866-2465"
    ],
    [
      "1 MH 2 OP 3 CMHC 4 BMT CBT CFT GT IDD IPT PTM TT 5",
      "CIT WI 6 PVTP 7 STMH FQHC 8 MC MD PI SCJJ SF SI SMHA 10",
      "TAY CJ CO PTSD SED 11 CDM CM COOT FPSY HS ICM IMR LAD",
      "PEER PRS SEMP SH SPS TPC VRS 12 NRT STU TCC 13 SMON 14",
      "CHLD YAD 16 AH 17 SP F25 F30 F92 F10 F88"
    ]
  ],
  [
    [
      "MH/MR/TC Homeless Services Clinic - CJ Impact"
    ],
    [
      "1350 East Lancaster",
      "Fort Worth, Texas 76102"
    ],
    [
      "Phone: (817) 569-5400"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT IDD IPT TT 5 WI 6 LMG 7",
      "STMH FQHC 8 MC MD 10 CO SMI 11 CM HS ICM IMR IPC PEER",
      "PRS SEMP SH SPS VRS 12 NRT STU TCC 13 SMPD 14 ADLT SNR YAD",
      "16 AH"
    ]
  ],
  [
    [
      "Texas Health Behavioral Health Southwest"
    ],
    [
      "7213 Red Hawk Court",
      "Fort Worth, Texas 76132"
    ],
    [
      "Phone: (682) 236-3662"
    ],
    [
      "Intake: (682) 236-6023"
    ],
    [
      "1 MH 2 OP PHDT TELE 3 PH 4 CBT DBT GT PTM TT 6 PVTN",
      "8 PI SF 10 SMI 11 CM SPS 12 STU 13 SMON 14 ADLT SNR YAD 16",
      "AH"
    ]
  ],
  [
    [
      "Texas Health Huguley Behavioral Health"
    ],
    [
      "11801 South Freeway",
      "Fort Worth, Texas 76115"
    ],
    [
      "Phone: (817) 568-5950"
    ],
    [
      "Intake: (682) 236-6023"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 BMT CBT GT IPT PTM 5 CIT WI",
      "6 PVTN 8 MC MD PI SF SI 11 CM DEC ES FPSY 12 NRT NSC STU",
      "TCC 13 SMON 14 ADLT SNR YAD 17 SP"
    ]
  ],
  [
    [
      "VA North Texas Healthcare System"
    ],
    [
      "Dallas VAMC/Fort Worth OP Clinic",
      "2201 SE Loop 820",
      "Fort Worth, Texas 76119"
    ],
    [
      "Phone: (817) 730-0000-23115]",
      [
        "Intake: (817) 730-0000 (817) 730-0102"
      ],
      [
        "1 MH 2 OP TELE 3 OMH 4 AT CBT CFT DBT GT IDD IPT PTM",
        "TT 5 WI 6 VAMC 8 MC MD MI PI SF VAF 10 VET TRMA PTSD 11",
        "CM ES FPSY IPC SPS 12 NRT NSC STU TCC 13 SMPD 14 ADLT SNR",
        "YAD 15 VO"
      ]
    ],
    [
      [
        "UTMB Outpatient Clinic"
      ],
      [
        "400 Harborside Drive",
        "Galveston, Texas 77555"
      ],
      [
        "Phone: (409) 772-0770"
      ],
      [
        "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT DBT IDD IPT PTM 6",
        "PVTN 8 MC MD PI SF SI 10 TAY 11 FPSY IPC SPS 13 SMON 14 ADLT",
        "CHLD SNR YAD 16 AH"
      ]
    ],
    [
      [
        "Georgetown Behavioral Health Institute"
      ],
      [
        "101 South Austin Avenue",
        "Georgetown, Texas 78626"
      ],
      [
        "phone: (512) 819-1100"
      ],
      [
        "intake: (512) 819-1154"
      ],
      [
        "1 MH 2 HI PHDT 3 PSY 4 AT CBT CFT DBT GT IPT PTM 5 WI",
        "PVTP 8 MC MD MI PI SCJJ SF SI SMHA SWFS VAF 10 SE VET CO",
        "ED 11 CM IMR SPS 12 NRT NSC STU TCC 13 SMPD 14 ADLT CHLD",
        "NR YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "*Rock Springs*"
      ],
      [
        "00 SE Inner Loop",
        "Georgetown, Texas 78626"
      ],
      [
        "phone: (512) 819-9400"
      ],
      [
        "1 MH 2 HI OP PHDT 3 PSY 4 AT CBT CFT GT IPT PTM TT 5",
        "I 6 PVTP 8 CLF ITU MC MD MI PI SF SI SMHA VAF 10 ADM CO",
        "RMA PTSD SMI 11 CM FPSY SPS 12 NRT STU TCC 13 SMPD 14",
        "DLT SNR YAD 16 AH"
      ]
    ],
    [
      [
        "New Horizons Ranch and Center - The Ranch"
      ],
      [
        "850 FM 574 West",
        "Goldthwaite, Texas 76844"
      ],
      [
        "Phone: (325) 938-5518"
      ],
      [
        "1 MH 2 RES TELE 3 RTCC 4 AT CBT CFT GT IPT PTM TT 6",
        "PVTN 8 CLF MD OSF PI SCJJ SEF SF SI SMHA SWFS 10 TRMA PTSD",
        "SED 11 CM ES FPSY 13 SMON 14 CHLD"
      ]
    ],
    [
      [
        "Glen Oaks Hospital"
      ],
      [
        "301 Division Street",
        "Greenville, Texas 75401"
      ],
      [
        "Phone: (903) 454-6000"
      ],
      [
        "Intake: (800) 443-1109"
      ],
      [
        "1 MH 2 HI PHDT 3 PSY 4 AT GT IDD IPT PTM 5 WI 6 PVTP",
        "7 STMH 8 CMHG MC MD MI PI SF SI SMHA 10 CO 11 SPS 12 NRT",
        "NSC STU TCC 13 SMPD 14 ADLT SNR YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Lakes Regional MH/MR Center"
      ],
      [
        "4200 Stuart Street",
        "Greenville, Texas 75401"
      ],
      [
        "Phone: (903) 455-3987"
      ],
      [
        "Intake: (888) 800-6799"
      ],
      [
        "1 MH 2 OP 3 OMH 4 CBT DBT IDD IPT PTM 6 OSG 8 CLF",
        "CMHG CSBG MC MD MI OSF PI SCJJ SF SI SMHA SWFS VAF 9 PA 10",
        "SED SMI 11 ACT CDM CM COOT DEC FPSY HS ICM IMR IPC PEER",
        "PRS SEMP SH SPS VRS 12 STU TCC 13 SMPD 14 ADLT CHLD SNR",
        "YAD 17 SP"
      ]
    ],
    [
      [
        "Texas Panhandle Centers"
      ],
      [
        "426 Main Street",
        "Suite D",
        "Hereford, Texas 79045"
      ],
      [
        "Phone: (806) 364-6111"
      ],
      [
        "Intake: (806) 337-1000"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 CBT DBT PTM 5 CIT 6 PVTN 7",
        "STMH 8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SI SMHA SWFS",
        "VAF 9 SS 10 TAY VET SED SMI 11 CM COOT DEC HS ICM IMR IPC",
        "PRS SEMP SH SPS VRS 12 NRT STU TCC 13 SMON 14 ADLT CHLD",
        "SNR YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Heart of Texas Region MHMR Center - Hill County Office"
      ],
      [
        "130 North Covington Street",
        "Hillsboro, Texas 76645"
      ],
      [
        "Phone: (254) 752-3451"
      ],
      [
        "Intake: (866) 752-3451"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 CBT DBT GT IDD PTM TT 5 CIT",
        "6 LMG 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF",
        "SMHA VAF 9 PA SS 11 CM DEC IMR PRS SEMP SH SPS 12 STU 13",
        "SMON 14 ADLT CHLD SNR YAD 17 SP"
      ]
    ],
    [
      [
        "Behavioral Hospital of Bellaire"
      ],
      [
        "5314 Dashwood Drive",
        "Suite 300",
        "Houston, Texas 77081"
      ],
      [
        "Phone: (713) 600-9500"
      ],
      [
        "1 MH 2 HI PHDT TELE 3 PSY 4 AT BMT CBT CFT DBT GT IDD",
        "IPT PTM TT 5 CIT WI 6 PVTP 7 STMH 8 CLF MC MD MI OSF PI",
        "SCJJ SEF SF SI SMHA SWFS VAF 10 SE CO SMI 11 COOT SPS 12 NRT",
        "NSC STU TCC 13 SMPD 14 ADLT CHLD SNR YAD 16 AH 17 F92"
      ]
    ],
    [
      [
        "Ben Taub Hospital Behavioral Health"
      ],
      [
        "1502 Taub Loop",
        "NPC Building, Room 2 125",
        "Houston, Texas 77030"
      ],
      [
        "Phone: (713) 873-5130"
      ],
      [
        "1 MH 2 HI OP TELE 3 PSY 4 AT BMT CBT CFT DBT ECT GT IDD",
        "IPT PTM TT 5 WI 6 LMG 7 STMH 8 CLF MC MD PI SF SI SMHA",
        "SWFS 9 SS 10 TAY SE GL CO HV TRMA ALZ PTSD SED SMI 11 CDM",
        "CM DEC ES FPSY IMR IPC 12 NRT NSC STU TCC 13 SMON 14 ADLT",
        "CHLD SNR YAD 17 SP F4 F17 F36 F47 F92 F91"
      ]
    ],
    [
      [
        "Center for Success and Independence"
      ],
      [
        "3722 Pinemont Drive",
        "Houston, Texas 77018"
      ],
      [
        "Phone: (713) 426-4545"
      ],
      [
        "Intake: (713) 426-4545-105"
      ],
      [
        "1 MH 2 OP RES 3 RTCC 4 BMT CBT CFT DBT GT IDD IPT PTM",
        "TT 6 PVTN 8 MD PI SCJJ SF SI SMHA 10 GL CO TRMA PTSD SED",
        "11 ES FPSY SPS 13 SMON 14 CHLD 17 SP"
      ]
    ],
    [
      [
        "Cypress Creek Hospital"
      ],
      [
        "17750 Cali Drive",
        "Houston, Texas 77090"
      ],
      [
        "Phone: (281) 586-7600"
      ],
      [
        "Intake: (281) 586-5953"
      ],
      [
        "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT CBT CFT DBT ECT GT",
        "IDD IPT PTM TT 5 CIT WI 6 PVTP 8 MC MD MI PI SF SI SMHA 10",
        "CO TRMA PTSD SMI 11 DEC FPSY IPC SPS 12 NRT NSC STU TCC 13",
        "SMPD 14 ADLT CHLD SNR YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Innerwisdom Inc"
      ],
      [
        "10777 Stella Link Road",
        "Houston, Texas 77025"
      ],
      [
        "Phone: (713) 592-9292"
      ],
      [
        "Intake: (713) 592-9292x133 (713) 592-9292x131"
      ],
      [
        "1 MH 2 OP PHDT 3 CMHC 4 BMT CBT CFT DBT GT IDD IPT",
        "PTM TT 6 PVTP 8 MC MD PI SF 9 SS 10 SE CO SMI 11 COOT ES",
        "FPSY 13 SMPD 14 ADLT CHLD SNR YAD"
      ]
    ],
    [
      [
        "Intracare North Hospital"
      ],
      [
        "1120 Cypress Station Drive",
        "Houston, Texas 77090"
      ],
      [
        "Phone: (281) 893-7200"
      ],
      [
        "1 MH 2 HI PHDT 3 PSY 4 AT CBT CFT GT IDD IPT PTM 5 WI",
        "6 PVTN 8 MC MD MI PI SF SWFS 10 CO SED SMI 11 CM SPS 12",
        "NRT 13 SMPD 14 ADLT CHLD SNR YAD 17 SP"
      ]
    ],
    [
      [
        "Jewish Family Service"
      ],
      [
        "4131 South Braeswood Boulevard",
        "Houston, Texas 77025"
      ],
      [
        "Phone: (713) 667-9336"
      ],
      [
        "1 MH 2 OP 3 OMH 4 BMT CBT CFT DBT GT IPT PTM TT 6",
        "PVTN 8 CLF MC MI PI SF 9 SS 10 TAY SE TRMA SED SMI 11 CM",
        "FPSY SEMP VRS 13 SMPD 14 ADLT CHLD SNR YAD 17 F17 F35 F70"
      ]
    ],
    [
      [
        "MH/MR Authority of Harris County - Northwest Clinic"
      ],
      [
        "3737 Dacoma Street",
        "Houston, Texas 77092"
      ],
      [
        "Phone: (713) 970-8400"
      ],
      [
        "Intake: (713) 970-7000"
      ],
      [
        "1 MH 2 OP 3 CMHC 4 CBT GT IPT PTM 5 CIT 6 LMG 7",
        "STMH 8 CLF CMHG MC MD OSF SCJJ SF SI SMHA SWFS 10 SMI 11",
        "ACT CM ICM IMR PRS SEMP SH 13 SMON 14 ADLT SNR YAD 16 AH",
        "17 SP"
      ]
    ],
    [
      [
        "Michael E DeBakey VAMC - Mental Healthcare Line (116A)"
      ],
      [
        "2002 Holcombe Boulevard",
        "Houston, Texas 77030"
      ],
      [
        "Phone: (713) 791-1414-28907]",
        [
          "Intake: (713) 791-1414x27561 (800) 639-5137x27561"
        ],
        [
          "1 MH 2 HI OP PHDT TELE 4 AT BMT CBT CFT DBT ECT GT ID",
          "IPT PTM TT 5 CIT WI 6 VAMC 8 MI PI SF VAF 10 SE GL VET CJ",
          "CO HV TRMA TBI ALZ PED PTSD SMI 11 ACT CDM CM COOT DEC",
          "ES FPSY HS ICM IMR IPC LAD PEER PRS SEMP SH SPS VRS 12 NRT",
          "NSC STU TCC 13 SMPD 14 ADLT SNR YAD 15 VO 16 AH 17 SP F4",
          "F17 F28 F36 F47 F70 F81 F92 F62 F69"
        ]
      ],
      [
        [
          "New Dimensions Day Treatment Centers"
        ],
        [
          "1345 Space Park Drive",
          "Suite C",
          "Houston, Texas 77058"
        ],
        [
          "Phone: (281) 333-2284"
        ],
        [
          "Intake: (800) 685-9796"
        ],
        [
          "1 MH 2 OP PHDT TELE 3 PH 4 BMT CBT CFT DBT GT IDD IPT",
          "PTM TT 6 PVTP 8 PI SF 10 CO TRMA PTSD 11 CM FPSY SPS 13",
          "SMPD 14 ADLT CHLD SNR YAD"
        ]
      ],
      [
        [
          "Post Oak Care Center"
        ],
        [
          "1147 Brittmoore Road",
          "Suite 4",
          "Houston, Texas 77043"
        ],
        [
          "Phone: (713) 960-0344"
        ],
        [
          "1 MH 2 OP PHDT 3 OMH 4 CFT GT IPT PTM 6 PVTP 7 STMH",
          "8 MC MD MI PI SF SI SMHA VAF 10 SE CO SMI 11 ES 13 SMPD 14",
          "ADLT CHLD SNR YAD 17 F36 F170 F82"
        ]
      ],
      "ACCESS",
      [
        [
          "Jacksonville"
        ],
        [
          "1011 College Avenue",
          "Jacksonville, Texas 75766"
        ],
        [
          "Phone: (903) 586-5507"
        ],
        [
          "Intake: (903) 589-9000"
        ],
        [
          "1 MH 2 OP TELE 3 CMHC 4 CBT GT IDD IPT PTM 5 CIT 6",
          "PVTN 7 STMH 8 CLF MC MD OSF PI SCJJ SF SI SMHA SWFS 9 PA",
          "SS 10 SED SMI 11 ACT CM COOT ICM IPC SEMP SH 13 SMPD 14",
          "ADLT CHLD SNR YAD 16 AH 17 SP"
        ]
      ],
      [
        [
          "Excel Center"
        ],
        [
          "2900 Commercial Center Boulevard",
          "Suite 102",
          "Katy, Texas 77494"
        ],
        [
          "Phone: (281) 647-0020"
        ],
        [
          "Intake: (281) 647-0020-0"
        ],
        [
          "1 MH 2 OP PHDT TELE 3 OMH 4 BMT CBT DBT GT IDD PTM",
          "6 PVTP 7 STMH 8 CLF MC MD PI SCJJ SF SI 10 SE CO TRMA SED",
          "SMI 11 CM FPSY IMR SPS 13 SMPD 14 ADLT CHLD SNR YAD"
        ]
      ],
      [
        [
          "Lutheran Soc Servs of the South Inc - Krause Childrens Center"
        ],
        [
          "25752 Kingsland Boulevard",
          "Katy, Texas 77494"
        ],
        [
          "Phone: (281) 392-7505"
        ],
        [
          "1 MH 2 RES 3 RTCC 4 AT CBT CFT DBT GT IPT PTM TT 6",
          "PVTN 8 MD SF 10 SED 11 CM DEC ES FPSY 13 SMON 14 CHLD"
        ]
      ],
      [
        [
          "New Dimensions Day Treatment Centers Katy"
        ],
        [
          "607 Park Grove Drive",
          "Suite A",
          "Katy, Texas 77450"
        ],
        [
          "Phone: (800) 685-9796"
        ],
        [
          "1 MH 2 OP PHDT 3 PH 4 CBT CFT DBT GT IDD IPT PTM TT",
          "PVTP 8 PI SF 10 CO 11 COOT FPSY 13 SMPD 14 ADLT CHLD SNR",
          "YAD"
        ]
      ],
      [
        [
          "West Texas Centers Winkler County"
        ],
        [
          "203 East Halley Street",
          "Kermit, Texas 79745"
        ],
        [
          "Phone: (432) 586-2016"
        ],
        [
          "Intake: (800) 375-4357"
        ],
        [
          "1 MH 2 OP TELE 3 CMHC 4 BMT CBT GT IDD IPT PTM 5 CIT",
          "WI 6 PVTN 7 STMH 8 CLF MC MD MI PI SCJJ SF SI SMHA SWFS",
          "9 SS 10 TAY SE VET CO TRMA SMI 11 ACT CM COOT ES FPSY HS",
          "ICM IMR PEER PRS SEMP SH SPS VRS 12 NSC STU TCC 13 SMON 14",
          "ADLT CHLD SNR YAD 16 AH 17 SP"
        ]
      ],
      [
        [
          "Cedar Crest Clinic"
        ],
        [
          "2206 East Central Texas Expressway",
          "Killeen, Texas 76542"
        ],
        [
          "Phone: (254) 519-4162"
        ],
        [
          "1 MH 2 OP 3 OMH 4 AT BMT CBT CFT DBT GT IDD IPT PTM",
          "TT 5 CIT 6 PVTP 8 MC MI PI SF VAF 9 PA 10 TAY SE GL VET",
          "ADM MF CJ CO HV TRMA TBI ALZ PED PTSD SED SMI 11 COOT",
          "DEC FPSY LAD PRS SPS 12 TCC 13 SMPD 14 ADLT CHLD SNR YAD",
          "16 AH"
        ]
      ],
      [
        [
          "Denton County MH/MR Center - Lewisville Outpatient Clinic"
        ],
        [
          "101 East Corporate Drive",
          "Suite 150",
          "Lewisville, Texas 75067"
        ],
        [
          "Phone: (940) 381-5000"
        ],
        [
          "Intake: (800) 762-0157"
        ],
        [
          "1 MH 2 OP 3 CMHC 4 CBT GT IPT PTM TT 5 CIT WI 6 PVTN",
          "7 STMH 8 CLF CMHG CSBG MC MD OSF PI SCJJ SF SMHA 9 PA SS",
          "10 TAY CO SED SMI 11 ACT CDM CM COOT HS ICM IMR PEER PRS",
          "SEMP SH SPS 12 TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17",
          "SP F25 F30"
        ]
      ],
      [
        [
          "Millwood Hospital - Excel Center of Lewisville"
        ],
        [
          "190 Civic Circle",
          "Suite 170",
          "Lewisville, Texas 75067"
        ],
        [
          "Phone: (972) 906-5522"
        ],
        [
          "1 MH 2 PHDT 3 PH 4 CBT DBT GT PTM 6 PVTP 8 MD MI PI",
          "SF 10 GL TRMA PTSD SED 11 CM FPSY 13 SMON 14 CHLD 17 SP"
        ]
      ],
      [
        [
          "Tri County Behavioral Healthcare"
        ],
        [
          "2000 Panther Lane",
          "Liberty, Texas 77575"
        ],
        [
          "Phone: (936) 334-3299"
        ],
        [
          "Intake: (800) 550-8408"
        ],
        [
          "1 MH 2 OP TELE 3 CMHC 4 CBT IPT PTM TT 5 CIT WI 6",
          "LMG 7 STMH 8 CLF CMHG CSBG MC MD MI PI SF SI SMHA 9 PA",
          "SS 10 TAY SE VET CJ TRMA SED SMI 11 ACT CDM CM COOT FPSY",
          "ICM IMR IPC PRS SEMP SH SPS VRS 12 STU 13 SMON 14 ADLT",
          "CHLD SNR YAD 16 AH 17 SP"
        ]
      ],
      [
        [
          "Burke Center - Polk County Family Csl Association"
        ],
        [
          "1100 Ogletree Drive",
          "Livingston, Texas 77351"
        ],
        [
          "Phone: (936) 327-3786"
        ],
        [
          "Intake: (936) 634-5010 (866) 242-4556"
        ],
        [
          "1 MH 2 OP TELE 3 CMHC 4 BMT CBT CFT DBT GT IDD IPT",
          "PTM TT 5 CIT WI 6 PVTN 7 STMH 8 CLF CMHG CSBG MC MD",
          "MI OSF PI SCJJ SF SI SMHA SWFS 9 PA SS 10 GL CO SED 11 ACT",
          "CDM CM COOT DEC FPSY HS ICM IMR PEER PRS SEMP SH SPS VRS",
          "12 NSC STU TCC 13 SMPD 14 CHLD 16 AH 17 SP"
        ]
      ],
      [
        [
          "Pegasus Schools Inc"
        ],
        [
          "896 Robin Ranch Road",
          "Lockhart, Texas 78644"
        ],
        [
          "Phone: (512) 376-2101"
        ],
        [
          "1 MH 2 RES 3 RTCC 4 AT BMT CBT GT IDD IPT PTM TT 5 CIT",
          "6 PVTN 8 CLF MD OSF SCJJ SI SMHA SWFS 10 CO TRMA PTSD 11",
          "CM ES FPSY 12 TCC 13 SMPD 14 CHLD 17 SP"
        ]
      ],
      [
        [
          "Sunrise Canyon Outpatient Services"
        ],
        [
          "1950 Aspen Avenue",
          "Lubbock, Texas 79403"
        ],
        [
          "Phone: (806) 766-0233"
        ],
        [
          "Intake: (806) 740-1421 (806) 766-0310"
        ],
        [
          "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT BMT CBT GT IDD IPT",
          "PTM TT 5 CIT WI 6 SMA 7 STMH 8 CLF CMHG CSBG MC MD",
          "MI OSF PI SCJJ SEF SF SI SMHA SWFS 9 PA SS 10 TAY SE VET CJ CO",
          "HV TRMA PTSD SMI 11 ACT CDM CM COOT DEC ES FPSY ICM IMR",
          "IPC PEER PRS SPS 12 NRT NSC STU 13 SMON 14 ADLT CHLD SNR",
          "YAD 16 AH 17 SP"
        ]
      ],
      [
        [
          "Seton Edgar B Davis Hospital - SEBD Heritage Program"
        ],
        [
          "130 Hays Street",
          "Luling, Texas 78648"
        ],
        [
          "Phone: (830) 875-7000"
        ],
        [
          "1 MH 2 OP 3 OMH 4 CBT DBT GT IPT PTM TT 6 PVTN 8 MC",
          "MD MI PI 10 SE 11 CM 13 SMPD 14 SNR 16 AH 17 SP"
        ]
      ],
      [
        [
          "Shiloh Treatment Center"
        ],
        [
          "3926 Bahler Road",
          "Manvel, Texas 77578"
        ],
        [
          "Phone: (281) 489-1290"
        ],
        [
          "1 MH 2 PHDT RES 3 RTCC 4 BMT CBT CFT GT IPT PTM 6",
          "PVTP 8 MD PI SEF SF 10 TRMA TBI PTSD SED 11 CM ES FPSY HS PRS",
          "13 SMON 14 CHLD 17 SP"
        ]
      ],
      [
        "Heart of Texas Region MHMR Center - Falls County Office"
      ],
      [
        "365 Coleman Street",
        "Marlin, Texas 76661"
      ],
      [
        "Phone: (866) 752-3451"
      ],
      [
        "Intake: (254) 752-3451"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 IPT PTM 5 CIT 6 LMG 7 STMH",
        "8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SMHA VAF 9 PA SS",
        "11 CM DEC IMR IPC PRS SEMP SH SPS 12 STU 13 SMON 14 ADLT",
        "CHLD SNR YAD 17 SP"
      ]
    ],
    [
      [
        "Community Healthcore"
      ],
      [
        "401 North Grove Street",
        "Suite A",
        "Marshall, Texas 75670"
      ],
      [
        "Phone: (903) 938-7721"
      ],
      [
        "Intake: (800) 446-8253"
      ],
      [
        "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT GT IPT PTM TT 5",
        "CIT 6 PVTN 8 MD PI SF SI 10 TRMA PTSD SED 11 CM SPS 13",
        "SMON 14 CHLD 17 SP"
      ]
    ],
    [
      [
        "Valley Coastal Bend Healthcare System - McAllen Outpatient Clinic"
      ],
      [
        "901 East Hackberry Avenue"
      ],
      "McAllen, Texas 78503"
    ],
    [
      "Phone: (956) 618-7100"
    ],
    [
      "1 MH 2 OP TELE 4 BMT CBT CFT DBT GT IDD IPT PTM TT 5",
      "CIT WI 6 VAMC 8 VAF 10 VET PTSD SMI 11 CDM CM DEC HS",
      "ICM IPC SEMP SH SPS VRS 12 NRT NSC STU TCC 13 SMPD 14 ADLT",
      "SNR YAD 15 VO 16 AH 17 SP"
    ]
  ],
  [
    [
      "Parkview Regional Hospital"
    ],
    [
      "600 South Bonham Street",
      "Mexia, Texas 76667"
    ],
    [
      "Phone: (254) 562-5332-2021",
      [
        "Intake: (254) 562-0408-1989"
      ],
      [
        "1 MH 2 HI 3 PSY 4 AT BMT CBT CFT GT IPT PTM 6 PVTP 7",
        "STMH 8 MC MI PI SF 10 SE ALZ 11 CM DEC FPSY HS PRS 12 NRT",
        "NSC STU TCC 13 SMON 14 SNR 16 AH 17 SP"
      ]
    ],
    [
      [
        "Permian Basin Community Ctrs for MH/MR"
      ],
      [
        "401 East Illinois Avenue",
        "Midland, Texas 79701"
      ],
      [
        "Phone: (432) 570-3300"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 BMT CBT GT IDD IPT PTM 5 CIT",
        "6 PVTN 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SF SI",
        "SMHA 9 PA SS 10 TAY SE VET CO SED SMI 11 ACT CM HS ICM IMR",
        "IPC PRS SEMP SH SPS VRS 12 STU 13 SMON 14 ADLT CHLD SNR",
        "YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Permian Basin Community Ctrs for MH/MR"
      ],
      [
        "700 West Broadway",
        "Midland, Texas 79701"
      ],
      [
        "Phone: (432) 283-2732"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 BMT CBT IDD PTM 5 CIT 6",
        "PVTN 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SF SI SMHA",
        "9 PA 10 TAY SE VET CO SED SMI 11 ACT CM COOT ICM IMR PRS",
        "SEMP SH SPS 12 STU TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH",
        "17 SP"
      ]
    ],
    [
      [
        "Permian Basin Community Ctrs for MH/MR"
      ],
      [
        "600 North Grant Avenue",
        "Midland, Texas 79701"
      ],
      [
        "Phone: (432) 333-3265"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 BMT CBT IDD IPT PTM 5 CIT WI",
        "6 PVTN 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SI",
        "SMHA 9 PA 10 TAY SE VET CO SED SMI 11 ACT CM HS ICM IMR",
        "IPC PRS SEMP SH SPS VRS 12 STU 13 SMON 14 ADLT CHLD SNR",
        "YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Andrews Center Behavioral Healthcare"
      ],
      [
        "703 West Patten Street",
        "Mineola, Texas 75773"
      ],
      [
        "Phone: (903) 569-5409"
      ],
      [
        "1 MH 2 OP TELE 3 OMH 4 CBT CFT IPT PTM TT 5 CIT WI 6",
        "SMA 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SF SI SMHA 9",
        "SS 10 CJ CO SED SMI 11 ACT CM ES FPSY ICM IMR PEER PRS SEMP",
        "SH SPS 12 STU 13 SMON 14 ADLT CHLD SNR YAD 16 AH"
      ]
    ],
    [
      [
        "Pecan Valley Centers for Behav and Developmental Healthcare"
      ],
      [
        "214 SW 26th Avenue",
        "Suite A",
        "Mineral Wells, Texas 76067"
      ],
      [
        "Phone: (940) 325-9541"
      ],
      [
        "Intake: (800) 772-5987"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 CBT GT IPT PTM TT 5 CIT WI 6",
        "LMG 7 STMH 8 CLF MC MD MI OSF PI SCJJ SF SMHA VAF 9 PA SS",
        "10 TAY VET CJ CO TRMA SED SMI 11 ACT CM COOT ICM IMR IPC",
        "PRS SEMP SH SPS 12 NRT STU TCC 13 SMON 14 ADLT CHLD SNR",
        "YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Spindletop Center - Orange"
      ],
      [
        "4305 Tejas Parkway",
        "Orange, Texas 77632"
      ],
      [
        "Phone: (409) 883-7074"
      ],
      [
        "Intake: (409) 839-1063 (800) 317-5809"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 CBT IDD IPT PTM TT 5 CIT WI 6",
        "OSG 7 STMH 8 CLF CMHG MC MD MI PI SF SI SMHA 9 PA SS 10",
        "SE CO PTSD SMI 11 ACT CM ES FPSY HS IMR IPC SEMP SH SPS 12",
        "NRT STU TCC 13 SMON 14 ADLT SNR YAD 16 AH"
      ]
    ],
    [
      [
        "ACCESS - Palestine"
      ],
      [
        "2320 South Loop 256",
        "Palestine, Texas 75801"
      ],
      [
        "Phone: (903) 723-6136"
      ],
      [
        "1 MH 2 OP TELE 3 CMHC 4 CBT CFT GT IDD IPT PTM 5 CIT",
        "WI 6 PVTN 7 STMH 8 CLF MC MD MI OSF PI SCJJ SF SI SMHA",
        "SWFS VAF 9 PA SS 10 CJ SED SMI 11 ACT CM COOT ICM IPC SEMP",
        "SH 13 SMPD 14 ADLT CHLD SNR YAD 16 AH 17 SP"
      ]
    ],
    [
      [
        "Texas VA Healthcare System - Palestine CBOC"
      ],
      [
        "2000 South Loop 256",
        "Suite 124",
        "Palestine, Texas 75801"
      ],
      [
        "Phone: (903) 723-9006"
      ],
      [
        "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT GT IPT PTM TT 5",
        "CIT WI 6 VAMC 8 ITU MC MD MI PI SF SI VAF 10 VET TRMA",
        "PTSD 11 CDM CM COOT FPSY IPC SPS 12 NRT NSC STU TCC 13",
        "SMPD 14 ADLT SNR YAD 15 VO"
      ],
      [
        "Behavioral Health Unit - Pampa Regional Medical Center"
      ],
      "1 Medical Plaza",
      "Pampa, Texas 79065"
    ],
    [
      "Phone: (806) 663-5570"
    ],
    [
      "1 MH 2 HI OP TELE 3 PSY 4 AT BMT CBT DBT GT IDD IPT PT",
      "TT 6 PVTN 7 STMH 8 MC MD MI PI SF SI VAF 9 SS 10 SE CJ",
      "TRMA 11 CDM CM ES FPSY IPC PRS SPS 12 NRT NSC STU TCC 13",
      "SMON 14 SNR 17 SP"
    ]
  ],
  [
    [
      "Texas Panhandle Centers - Pampa Clinic"
    ],
    [
      "615 West Buckler Avenue",
      "Pampa, Texas 79065"
    ],
    [
      "Phone: (806) 669-3371"
    ],
    [
      "Intake: (806) 935-5691"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT DBT IPT PTM 5 CIT 6 PVTN",
      "7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SI SMHA",
      "SWFS VAF 9 PA SS 10 TAY VET SED SMI 11 CM ICM IMR IPC PRS",
      "SEMP SH SPS VRS 12 NRT STU TCC 13 SMON 14 ADLT CHLD SNR",
      "YAD 16 AH"
    ]
  ],
  [
    [
      "Child and Family Guidance Center - Collin County/Plano"
    ],
    [
      "4031 West Plano Parkway",
      "Suite 211",
      "Plano, Texas 75093"
    ],
    [
      "Phone: (214) 351-3490"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT DBT GT IPT PTM TT",
      "6 PVTN 8 CLF MC MD MI OSF PI SCJJ SF SI SMHA SWFS 9 SS 10",
      "SED SMI 11 ACT CM COOT FPSY HS ICM PEER PRS SEMP SPS 13",
      "SMPD 14 ADLT CHLD SNR YAD 17 SP"
    ]
  ],
  [
    [
      "LifePath Systems"
    ],
    [
      "7308 Alma Drive",
      "Plano, Texas 75025"
    ],
    [
      "Phone: (972) 422-5939"
    ],
    [
      "Intake: (844) 544-5939"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT GT IDD IPT PTM TT 5 CIT",
      "WI 6 LMG 7 STMH 8 CLF CMHG CSBG MC MD MI PI SCJJ SF SI",
      "SMHA SWFS 9 PA SS 10 TAY CJ CO SED SMI 11 ACT CM COOT",
      "FPSY HS ICM IMR IPC PEER PRS SEMP SH SPS VRS 12 NRT NSC STU",
      "TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17 SP F4 F25 F36"
    ]
  ],
  [
    [
      "Medical City Green Oaks Hospital - Plano Outpatient Services"
    ],
    [
      "4001 West 15th Street",
      "Suite 465",
      "Plano, Texas 75093"
    ],
    [
      "Phone: (972) 985-1599"
    ],
    [
      "1 MH 2 OP 3 OMH 4 BMT CBT CFT GT IPT TT 5 CIT 6 PVTP",
      "8 PI SF 11 CM ES FPSY 12 STU 13 SMON 14 ADLT CHLD SNR YAD"
    ]
  ],
  [
    [
      "Presbyterian Hospital of Plano - Seay Behavioral Health Center"
    ],
    [
      "6110 West Parker Road",
      "Plano, Texas 75093"
    ],
    [
      "Phone: (972) 981-8301"
    ],
    [
      "Intake: (972) 981-8305"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 AT CBT CFT DBT GT IPT PTM TT",
      "5 CIT WI 6 PVTN 7 STMH 8 MC MD PI SF SI 10 TAY CO TRMA",
      "SED SMI 11 SPS 12 STU 13 SMON 14 ADLT CHLD SNR YAD 16 AH"
    ]
  ],
  [
    [
      "VA North Texas Healthcare System - Dallas VAMC Plano CBOC"
    ],
    [
      "3804 West 15th Street",
      "Plano, Texas 75075"
    ],
    [
      "Phone: (972) 801-4200"
    ],
    [
      "1 MH 2 OP 4 BMT CBT CFT DBT GT IDD IPT PTM TT 5 CIT WI",
      "6 VAMC 10 SE GL VET MF CO TRMA ALZ PED PTSD SMI 11 FPSY",
      "SPS 12 NSC STU TCC 13 SMPD 14 ADLT SNR YAD 15 VO"
    ]
  ],
  [
    [
      "WellBridge Healthcare of Greater Dallas"
    ],
    [
      "4301 Mapleshade Lane",
      "Plano, Texas 75093"
    ],
    [
      "Phone: (972) 596-5445"
    ],
    [
      "1 MH 2 HI TELE 3 PSY 4 AT CBT DBT GT IDD IPT PTM 5 WI",
      "6 PVTP 8 MC PI SF 10 SE 11 CM ES 12 STU 13 SMPD 14 SNR 16 AH"
    ]
  ],
  [
    [
      "Medical Center of Southeast Texas"
    ],
    [
      "2555 Jimmy Johnson Boulevard",
      "Port Arthur, Texas 77640"
    ],
    [
      "Phone: (409) 853-5729"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 AT CBT CFT GT IPT PTM 5 WI 6",
      "PVTP 8 MC MD MI PI SF SMHA 10 SE 11 CM FPSY SPS 12 NRT STU",
      "TCC 13 SMON 14 ADLT SNR YAD 16 AH"
    ]
  ],
  [
    [
      "DePelchin Childrens Center - Richmond Campus"
    ],
    [
      "710 South 7th Street",
      "Richmond, Texas 77469"
    ],
    [
      "Phone: (281) 342-4906"
    ],
    [
      "Intake: (713) 558-6375 (713) 558-3980"
    ],
    [
      "1 MH 2 RES TELE 3 RTCC 4 AT BMT CBT CFT GT IPT PTM TT",
      "5 CIT 6 PVTN 8 CSBG MD SWFS 10 TRMA SED 11 CM ES FPSY 13",
      "SMPD 14 CHLD"
    ]
  ],
  [
    [
      "Westpark Springs Hospital"
    ],
    [
      "6902 South Peek Road",
      "Richmond, Texas 77407"
    ],
    [
      "Phone: (832) 535-2770"
    ],
    [
      "1 MH 2 HI PHDT 3 PSY 4 BMT CBT DBT GT IDD PTM 5 CIT",
      "WI 6 PVTP 7 STMH 8 MC MD MI PI SF SI 10 CO 11 CM COOT",
      "FPSY SPS 13 SMPD 14 ADLT CHLD SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Nueces Center for Mental Health - Robstown Outpatient Clinic"
    ],
    [
      "1038 Texas Yes Boulevard",
      "Robstown, Texas 78380"
    ],
    [
      "Phone: (361) 886-1445"
    ],
    [
      "1 MH 2 OP 3 CMHC 4 CBT PTM 5 CIT 6 PVTN 7 STMH 8",
      "MD SF 9 PA 11 CM FPSY ICM IMR PRS SEMP SH SPS 12 NRT STU",
      "TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Bluebonnet Trails Community Services - Adult Clinic"
    ],
    [
      "1009 North Georgetown Street",
      "Round Rock, Texas 78664"
    ],
    [
      "Phone: (512) 244-8480"
    ],
    [
      "Intake: (844) 309-6385"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT CFT DBT GT IDD IPT PTM 5",
      "CIT WI 6 PVTN 7 STMH FQHC 8 MC MD MI PI SF SI 9 PA SS 10",
      "TAY SE VET CJ CO PTSD SED SMI 11 ACT CM COOT FPSY HS ICM",
      "IMR IPC PRS SEMP SH VRS 13 SMON 14 ADLT CHLD SNR YAD 16",
      "AH 17 SP F4 F17 F28 F30 F31 F35 F36 F37 F42 F43 F47 F66 F67 F70 F81",
      "F92"
    ]
  ],
  [
    [
      "Rusk State Hospital"
    ],
    [
      "805 North Dickinson Drive",
      "Rusk, Texas 75785"
    ],
    [
      "Phone: (903) 683-3421"
    ],
    [
      "Intake: (903) 683-7400"
    ],
    [
      "1 MH 2 HI RES 3 PSY 4 AT GT IDD PTM TT 5 CIT WI 6 OSG",
      "7 STMH 8 MC MD MI OSF PI SF SI SMHA 10 SE CJ SMI 11 CDM",
      "DEC IMR IPC PEER PRS SPS 12 NRT NSC STU 13 SMON 14 ADLT SNR",
      "YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Center for Healthcare Services - Crisis/Jail Diversion Program"
    ],
    [
      "601 North Frio Street",
      "San Antonio, Texas 78207"
    ],
    [
      "Phone: (210) 261-3032"
    ],
    [
      "Intake: (210) 261-1250"
    ],
    [
      "1 MH 2 HI OP RES TELE 3 CMHC 4 CBT GT IDD PTM TT 5",
      "CIT WI 6 LMG 7 STMH 8 CLF CMHG CSBG MC MD OSF PI SF SI",
      "SMHA 9 PA SS 10 SE CJ CO HV TRMA PTSD SMI 11 CM COOT ICM",
      "IMR IPC PEER PRS SPS 12 NRT STU TCC 13 SMPD 14 ADLT SNR YAD",
      "16 AH 17 SP F28"
    ]
  ],
  [
    [
      "Center for Healthcare Services - Justice Programs"
    ],
    [
      "2711 Palo Alto Road",
      "San Antonio, Texas 78211"
    ],
    [
      "Phone: (210) 261-3200"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 GT IPT PTM 6 PVTP 7 STMH 8",
      "CLF CMHG CSBG MC MD MI OSF PI SEF SF SI SMHA VAF 10 CJ SMI",
      "11 COOT ICM IMR LAD PRS SEMP SH 13 SMPD 14 ADLT SNR YAD",
      "16 AH 17 SP"
    ]
  ],
  [
    [
      "Center for Healthcare Services - Northwest Clinic"
    ],
    [
      "5372 Fredericksburg Road",
      "Building F",
      "San Antonio, Texas 78229"
    ],
    [
      "Phone: (210) 261-1600"
    ],
    [
      "Intake: (210) 261-1250"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 CBT CFT GT IDD IPT PTM TT 5 WI",
      "6 LMG 7 STMH 8 CLF CMHG CSBG MC MD MI OSF PI SCJJ SF SI",
      "SMHA SWFS 9 PA SS 10 SE GL CJ CO HV TRMA PTSD SMI 11 ACT",
      "CM COOT FPSY ICM IMR IPC PRS SPS 12 NRT NSC STU TCC 13",
      "SMPD 14 ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Clarity Child Guidance Center"
    ],
    [
      "8535 Tom Slick Drive",
      "San Antonio, Texas 78229"
    ],
    [
      "Phone: (210) 616-0300"
    ],
    [
      "1 MH 2 HI OP PHDT 3 PSY 4 AT CBT CFT DBT GT IPT PTM TT",
      "5 CIT WI 6 PVTN 8 CLF ITU MD MI OSF PI SCJJ SEF SF SI SMHA",
      "SWFS VAF 9 PA SS 10 SED 11 CM FPSY SPS 13 SMON 14 CHLD 16",
      "AH 17 SP"
    ]
  ],
  [
    [
      "Family Service Association of San Antonio Inc"
    ],
    [
      "702 San Pedro Avenue",
      "San Antonio, Texas 78212"
    ],
    [
      "Phone: (210) 299-2400"
    ],
    [
      "1 MH 2 OP 3 OMH 4 BMT CBT CFT DBT GT IPT TT 6 PVTN 8",
      "CLF MC MD MI OSF PI SCJJ SF SI SWFS 9 PA SS 10 VET ADM MF CO",
      "TRMA SED 11 ACT CM COOT ES FPSY ICM SPS 12 STU TCC 13",
      "SMON 14 ADLT CHLD SNR YAD 16 AH 17 SP F4"
    ]
  ],
  [
    [
      "Hector Garza Center"
    ],
    [
      "620 East Afton Oaks Boulevard",
      "San Antonio, Texas 78232"
    ],
    [
      "Phone: (210) 568-8600"
    ],
    [
      "Intake: (210) 517-4079"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT BMT CBT CFT GT IPT PTM TT 5 CIT",
      "6 PVTP 8 MD SCJJ SI SWFS 10 CJ TRMA PTSD SED 11 CM ES FPSY",
      "HS PRS SPS TPC 12 STU 13 SMON 14 CHLD 17 SP"
    ]
  ],
  [
    [
      "Southwest General Hospital Behavioral Health"
    ],
    [
      "7400 Barlite Boulevard",
      "San Antonio, Texas 78224"
    ],
    [
      "Phone: (210) 921-2000"
    ],
    [
      "Intake: (210) 332-1341"
    ],
    [
      "1 MH 2 HI 3 PSY 4 AT CBT GT IDD IPT PTM 5 CIT WI 6 PVTP",
      "8 MC MD MI PI SF VAF 11 CM SPS 12 NRT STU 13 SMON 14 ADLT",
      "SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "San Marcos Treatment Center"
    ],
    [
      "120 Bert Brown Street",
      "San Marcos, Texas 78666"
    ],
    [
      "Phone: (512) 396-8500-3245"
    ],
    [
      "Intake: (512) 396-8500-3202 (800) 848-9090"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT BMT CBT CFT DBT GT IDD IPT PTM",
      "TT 6 PVTP 8 CLF MD MI OSF PI SCJJ SF SI SMHA SWFS 10 MF CO",
      "TRMA PTSD SED 11 CM DEC ES FPSY IPC PRS 13 SMON 14 CHLD 17 SP"
    ]
  ],
  [
    [
      "WellBridge Healthcare San Marcos"
    ],
    [
      "1106 North IH 35",
      "San Marcos, Texas 78666"
    ],
    [
      "Phone: (512) 353-0194"
    ],
    [
      "Intake: (512) 353-0194-611"
    ],
    [
      "1 MH 2 HI OP TELE 3 PSY 4 AT BMT CBT GT IPT PTM 6 PVTP",
      "7 STMH 8 CLF MC MD MI OSF PI SF 10 SE CO TRMA ALZ PTSD",
      "SMI 11 CDM CM DEC ES FPSY IPC SPS 12 STU 13 SMON 14 ADLT",
      "SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Bluebonnet Trails Community Services - Guadalupe County"
    ],
    [
      "1104 Jefferson Avenue",
      "Seguin, Texas 78155"
    ],
    [
      "Phone: (830) 386-2700"
    ],
    [
      "Intake: (844) 309-6385"
    ],
    [
      "1 MH 2 OP PHDT TELE 3 OMH 4 BMT CBT CFT DBT GT IDD",
      "IPT PTM TT 5 CIT WI 6 SMA 9 SS 10 GL VET MF CJ CO TRMA",
      "PTSD SED SMI 11 ACT CM COOT ES FPSY ICM IPC LAD PEER PRS",
      "SPS 12 NRT NSC STU TCC 13 SMON 14 ADLT CHLD SNR YAD 16",
      "AH 17 SP"
    ]
  ],
  [
    [
      "Guadalupe Regional Medical Center"
    ],
    [
      "1215 East Court Street",
      "Seguin, Texas 78155"
    ],
    [
      "Phone: (830) 401-1367"
    ],
    [
      "1 MH 2 OP 3 OMH 4 CBT CFT GT IDD IPT TT 5 CIT WI 6",
      "LMG 8 MC MD MI OSF PI SCJJ SF SI SMHA SWFS 9 SS 10 SE GL VE",
      "MF CJ CO HV TRMA PED PTSD SMI 11 COOT SPS 12 STU TCC 13",
      "SMPD 14 ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "West Texas Centers - Gaines County"
    ],
    [
      "702 Hobbs Highway",
      "Seminole, Texas 79360"
    ],
    [
      "Phone: (432) 758-4028"
    ],
    [
      "Intake: (800) 375-4357"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 BMT CBT GT IDD IPT PTM 5 CIT",
      "WI 6 PVTN 7 STMH 8 CLF MC MD MI PI SCJJ SF SI SMHA SWFS",
      "9 SS 10 TAY SE VET CO TRMA SMI 11 ACT CM COOT ES FPSY HS",
      "ICM IMR PEER PRS SEMP SH SPS VRS 12 NSC STU TCC 13 SMON 14",
      "ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Houston Wee Care Shelter Inc"
    ],
    [
      "28915 South Plum Creek Drive",
      "Spring, Texas 77386"
    ],
    [
      "Phone: (281) 363-4020"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT CBT CFT GT PTM TT 6 PVTN 8",
      "CLF OSF SCJJ SWFS 10 TRMA PTSD SED 11 CM COOT DEC PRS VRS",
      "13 SMON 14 CHLD 17 SP"
    ]
  ],
  [
    [
      "New Dimensions Day Treatment Centers"
    ],
    [
      "25511 Budde Road",
      "Suite 2401",
      "Spring, Texas 77380"
    ],
    [
      "Phone: (800) 685-9796-1309"
    ],
    [
      "Intake: (800) 685-9796"
    ],
    [
      "1 MH 2 OP PHDT TELE 3 PH 4 BMT CBT CFT DBT GT IDD IPT",
      "PTM TT 6 PVTP 8 PI SF 10 CO 11 FPSY SPS 13 SMPD 14 ADLT",
      "CHLD SNR YAD"
    ]
  ],
  [
    [
      "Sheltering Harbour"
    ],
    [
      "17803 West Strack Drive",
      "Spring, Texas 77379"
    ],
    [
      "Phone: (281) 379-4578"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT BMT CBT CFT GT IDD IPT PTM 6",
      "PVTN 8 CLF CMHG OSF PI SCJJ SEF SI SMHA SWFS 10 SED 13",
      "SMON 14 CHLD"
    ]
  ],
  [
    [
      "Woodlands District Office"
    ],
    [
      "1600 Lake Front Circle",
      "Suite 200",
      "Spring, Texas 77380"
    ],
    [
      "Phone: (713) 861-4849"
    ],
    [
      "1 MH 2 OP 3 OMH 4 BMT CBT CFT GT IPT TT 6 PVTN 7",
      "STMH 8 CLF CMHG CSBG MC MD MI PI SCJJ SF SI SMHA SWFS VAF",
      "9 SS 10 TAY VET TRMA PTSD 11 CM COOT FPSY 13 SMPD 14",
      "ADLT CHLD SNR YAD 17 SP"
    ]
  ],
  [
    [
      "Fort Bend District Office"
    ],
    [
      "12300 Parc Crest Drive",
      "Stafford, Texas 77477"
    ],
    [
      "Phone: (713) 861-4849"
    ],
    [
      "1 MH 2 OP 3 OMH 4 AT BMT CBT CFT DBT GT IDD IPT TT 6",
      "PVTN 8 MC MD MI PI SF SI VAF 9 SS 10 TAY SE VET MF CO TRMA",
      "PTSD SMI 11 CM COOT ES FPSY IMR 13 SMPD 14 ADLT CHLD SNR",
      "YAD 17 F9"
    ]
  ],
  [
    [
      "Sweeny Community Hospital - Senior Horizons/Counseling Associates"
    ],
    [
      "305 North McKinney Street",
      "Sweeny, Texas 77480"
    ],
    [
      "Phone: (979) 548-1500-1550"
    ],
    [
      "Intake: (979) 548-1550 (979) 548-1553"
    ],
    [
      "1 MH 2 OP PHDT 3 MSNH 4 CBT CFT GT IPT PTM 6 LMG 8",
      "MC MD PI SF SI 10 SE CO 11 CM FPSY SPS 13 SMPD 14 ADLT CHLD",
      "SNR YAD"
    ]
  ],
  [
    [
      "Gulf Coast Center Mainland Community Service Center"
    ],
    [
      "7510 FM 1765",
      "Texas City, Texas 77591"
    ],
    [
      "Phone: (409) 935-6083"
    ],
    [
      "Intake: (800) 643-0967"
    ],
    [
      "1 MH 2 OP 3 CMHC 4 CBT GT IDD IPT PTM 5 CIT WI 6 OSG",
      "7 STMH 8 CLF CMHG CSBG MC MD OSF PI SF SI SMHA 9 PA SS",
      "10 CJ CO SMI 11 ACT CM COOT HS ICM IMR PEER PRS SEMP SH SPS",
      "12 STU 13 SMPD 14 ADLT SNR YAD 16 AH"
    ]
  ],
  [
    [
      "Tomball Regional Medical Center - Senior Care Behavioral Health"
    ],
    [
      "605 Holderrieth Boulevard",
      "Tomball, Texas 77375"
    ],
    [
      "Phone: (281) 401-7264"
    ],
    [
      "1 MH 2 HI 3 PSY 4 AT BMT CBT CFT GT IPT PTM 5 CIT WI 6",
      "PVTP 7 STMH 8 MC MI PI SF VAF 10 SE 11 CDM CM DEC ES FPSY",
      "IMR IPC SPS 12 NRT NSC STU TCC 13 SMON 14 SNR"
    ]
  ],
  [
    [
      "Andrews Center Behavioral Healthcare"
    ],
    [
      "2323 West Front Street",
      "Tyler, Texas 75702"
    ],
    [
      "Phone: (903) 597-1351-7314"
    ],
    [
      "Intake: (903) 597-1351 (800) 374-6058"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 BMT CBT CFT DBT IDD IPT PTM",
      "TT 5 CIT WI 6 PVTN 7 STMH 8 CLF CMHG MC MD PI SCJJ SF SI",
      "SMHA SWFS 9 PA SS 10 TAY SE VET ADM MF CJ CO TRMA PTSD",
      "SED SMI 11 ACT CM COOT FPSY ICM IMR IPC PRS SH SPS 12 NRT",
      "STU TCC 13 SMPD 14 ADLT CHLD SNR YAD 17 SP"
    ]
  ],
  [
    [
      "University of Texas Health Northeast"
    ],
    [
      "11937 Highway 271",
      "Tyler, Texas 75708"
    ],
    [
      "Phone: (903) 877-7777-5210"
    ],
    [
      "Intake: (903) 877-7777 (903) 877-8520"
    ],
    [
      "1 MH 2 HI OP PHDT TELE 3 PSY 4 AT BMT CBT CFT GT IPT",
      "PTM TT 6 OSG 7 STMH 8 CLF MC MD MI OSF PI SEF SF SI SMHA",
      "10 SE SMI 11 CM IPC 13 SMON 14 ADLT SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "VA North Texas HCS/Dallas VAMC  - Tyler VA Clinic"
    ],
    [
      "7916 South Broadway",
      "Tyler, Texas 75701"
    ],
    [
      "Phone: (903) 266-5900"
    ],
    [
      "Intake: (855) 375-6930"
    ],
    [
      "1 MH 2 OP TELE 4 BMT CBT CFT GT IDD IPT PTM TT 5 CIT WI",
      "6 VAMC 7 STMH 8 VAF 10 VET CO TRMA PTSD 11 CDM CM",
      "DEC ES FPSY HS IMR IPC PRS SH SPS VRS 12 NRT NSC STU TCC 13",
      "SMPD 14 ADLT SNR YAD 15 VO"
    ]
  ],
  [
    [
      "Crossroads Behavioral Health Services - Uvalde County Hospital Authority"
    ],
    [
      "100 Royal Lane",
      "Uvalde, Texas 78801"
    ],
    [
      "Phone: (830) 278-8144"
    ],
    [
      "Intake: (830) 278-6251-1420"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT GT IPT PTM TT 6",
      "PVTN 8 MC MD PI 10 SE ALZ 11 CM DEC FPSY IPC 13 SMON 14",
      "SNR 17 SP"
    ]
  ],
  [
    [
      "Heart of Texas Region MHMR Center - Klaras Center for Families"
    ],
    [
      "1105 Jefferson Avenue",
      "Waco, Texas 76701"
    ],
    [
      "Phone: (254) 752-3451"
    ],
    [
      "Intake: (866) 752-3451"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 AT BMT CBT CFT GT IDD IPT PTM",
      "TT 5 CIT WI 6 LMG 7 STMH 8 CLF CMHG CSBG MC MD MI",
      "OSF PI SCJJ SF SMHA VAF 9 PA SS 10 MF CJ CO TRMA PTSD SED 11",
      "CM COOT ES FPSY ICM PEER SEMP SPS 12 STU 13 SMON 14 CHLD",
      "17 SP"
    ]
  ],
  [
    [
      "Waco Center for Youth"
    ],
    [
      "3501 North 19th Street",
      "Waco, Texas 76708"
    ],
    [
      "Phone: (254) 756-2171"
    ],
    [
      "Intake: (254) 745-5302 (254) 745-5175"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT BMT CBT CFT DBT GT IPT PTM TT",
      "6 OSG 8 OSF PI SF SMHA SWFS 9 PA SS 10 SED 11 DEC ES FPSY 12",
      "STU TCC 13 SMON 14 CHLD 16 AH"
    ]
  ],
  [
    [
      "Pecan Valley Centers for Behav and Developmental Healthcare"
    ],
    [
      "1715 Santa Fe Drive",
      "Weatherford, Texas 76086"
    ],
    [
      "Phone: (817) 599-7634"
    ],
    [
      "Intake: (800) 772-5987"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT CFT GT IPT PTM TT 5 CIT",
      "WI 6 LMG 7 STMH 8 CLF MC MD MI OSF PI SCJJ SF SMHA VAF 9",
      "PA SS 10 TAY VET CJ CO TRMA SED SMI 11 ACT CM COOT ICM",
      "IMR IPC PEER PRS SEMP SH SPS 12 NRT STU TCC 13 SMON 14 ADLT",
      "CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "Pecan Valley Centers for Behav and Developmental Healthcare"
    ],
    [
      "1429 Clear Lake Road",
      "Weatherford, Texas 76086"
    ],
    [
      "Phone: (817) 579-4400"
    ],
    [
      "Intake: (800) 772-5987"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 5 CIT WI 6 LMG 7 STMH 8 CLF",
      "MC MD MI OSF PI SCJJ SF VAF 9 PA SS 10 TAY VET ADM CJ PTSD",
      "SED SMI 11 ACT CM FPSY ICM IMR IPC PEER PRS SEMP SH SPS 12",
      "NRT STU TCC 13 SMON 14 ADLT CHLD SNR YAD 16 AH 17 SP"
    ]
  ],
  [
    [
      "UTMB Psychiatry Webster Clinic"
    ],
    [
      "400 Texas Avenue",
      "Webster, Texas 77598"
    ],
    [
      "Phone: (281) 338-2798"
    ],
    [
      "Intake: (409) 772-0220"
    ],
    [
      "1 MH 2 OP TELE 3 OMH 4 BMT CBT CFT DBT IDD IPT PTM TT",
      "6 PVTN 8 MC MD PI SF SI SMHA SWFS 10 TAY 11 FPSY IPC 13",
      "SMON 14 ADLT CHLD SNR YAD 16 AH"
    ]
  ],
  [
    [
      "North Fork Educational Center"
    ],
    [
      "3001 Elm Grove Road",
      "Wylie, Texas 75098"
    ],
    [
      "Phone: (972) 412-2444"
    ],
    [
      "1 MH 2 RES 3 RTCC 4 AT BMT CBT CFT DBT GT IPT PTM TT",
      "6 PVTP 8 CLF OSF SCJJ SEF SF SWFS 10 CO TRMA PTSD SED 11",
      "ACT CM ES FPSY ICM IPC TPC VRS 13 SMON 14 CHLD 16 AH"
    ]
  ],
  [
    [
      "Border Region BHC Zapata"
    ],
    [
      "Zapata, Texas 78076"
    ],
    [
      "Phone: (956) 765-9664"
    ],
    [
      "Intake: (956) 765-9667"
    ],
    [
      "1 MH 2 OP TELE 3 CMHC 4 CBT GT PTM 5 CIT WI 6 OSG 7",
      "STMH 8 CMHG CSBG MC MD PI SF 9 PA SS 11 CM IMR IPC PRS",
      "SEMP SH SPS 12 NRT NSC TCC 13 SMON 14 ADLT CHLD SNR YAD",
      "16 AH 17 SP"
    ]
  ]
]
)
