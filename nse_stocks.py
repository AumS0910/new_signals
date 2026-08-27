"""
NSE/BSE Stock Master List for Fuzzy Matching
Contains popular Indian stocks with their NSE symbols, full names, and common spoken aliases
(Hindi and English) used on Zee Business / financial TV channels.
"""

# Format: (NSE_SYMBOL, FULL_NAME, [ALIASES])
# Aliases include Hindi transliterations, common abbreviations, and spoken names

STOCK_MASTER_LIST = [
    # === NIFTY 50 ===
    ("RELIANCE", "Reliance Industries", ["रिलायंस", "Reliance", "RIL", "रिलायंस इंडस्ट्रीज"]),
    ("TCS", "Tata Consultancy Services", ["TCS", "टीसीएस", "टाटा कंसल्टेंसी", "Tata Consultancy"]),
    ("HDFCBANK", "HDFC Bank", ["HDFC Bank", "एचडीएफसी बैंक", "HDFC", "एचडीएफसी"]),
    ("INFY", "Infosys", ["Infosys", "इंफोसिस", "Infy", "इन्फी"]),
    ("ICICIBANK", "ICICI Bank", ["ICICI Bank", "आईसीआईसीआई बैंक", "ICICI", "आईसीआईसीआई"]),
    ("HINDUNILVR", "Hindustan Unilever", ["HUL", "Hindustan Unilever", "हिंदुस्तान यूनिलीवर", "एचयूएल"]),
    ("ITC", "ITC Limited", ["ITC", "आईटीसी"]),
    ("SBIN", "State Bank of India", ["SBI", "State Bank", "एसबीआई", "स्टेट बैंक"]),
    ("BHARTIARTL", "Bharti Airtel", ["Airtel", "Bharti Airtel", "एयरटेल", "भारती एयरटेल"]),
    ("KOTAKBANK", "Kotak Mahindra Bank", ["Kotak Bank", "Kotak", "कोटक बैंक", "कोटक महिंद्रा"]),
    ("LT", "Larsen & Toubro", ["L&T", "Larsen", "एलएंडटी", "लार्सन"]),
    ("AXISBANK", "Axis Bank", ["Axis Bank", "Axis", "एक्सिस बैंक"]),
    ("ASIANPAINT", "Asian Paints", ["Asian Paints", "एशियन पेंट्स", "Asian Paint"]),
    ("MARUTI", "Maruti Suzuki", ["Maruti", "Maruti Suzuki", "मारुति", "मारुति सुजुकी"]),
    ("HCLTECH", "HCL Technologies", ["HCL Tech", "HCL", "एचसीएल", "एचसीएल टेक"]),
    ("SUNPHARMA", "Sun Pharma", ["Sun Pharma", "Sun Pharmaceutical", "सन फार्मा"]),
    ("TITAN", "Titan Company", ["Titan", "टाइटन", "Titan Company"]),
    ("BAJFINANCE", "Bajaj Finance", ["Bajaj Finance", "बजाज फाइनेंस", "Bajaj Fin"]),
    ("WIPRO", "Wipro", ["Wipro", "विप्रो"]),
    ("ULTRACEMCO", "UltraTech Cement", ["UltraTech", "UltraTech Cement", "अल्ट्राटेक", "अल्ट्राटेक सीमेंट"]),
    ("NESTLEIND", "Nestle India", ["Nestle", "Nestle India", "नेस्ले", "नेस्ले इंडिया"]),
    ("TATAMOTORS", "Tata Motors", ["Tata Motors", "टाटा मोटर्स", "Tata Motor"]),
    ("TATASTEEL", "Tata Steel", ["Tata Steel", "टाटा स्टील"]),
    ("POWERGRID", "Power Grid Corporation", ["Power Grid", "पावर ग्रिड", "PGCIL"]),
    ("NTPC", "NTPC Limited", ["NTPC", "एनटीपीसी"]),
    ("M&M", "Mahindra & Mahindra", ["M&M", "Mahindra", "महिंद्रा", "महिंद्रा एंड महिंद्रा"]),
    ("ONGC", "Oil & Natural Gas Corporation", ["ONGC", "ओएनजीसी"]),
    ("JSWSTEEL", "JSW Steel", ["JSW Steel", "JSW", "जेएसडब्ल्यू स्टील", "जेएसडब्ल्यू"]),
    ("ADANIENT", "Adani Enterprises", ["Adani Enterprises", "Adani", "अडानी एंटरप्राइजेज", "अडानी"]),
    ("ADANIPORTS", "Adani Ports", ["Adani Ports", "अडानी पोर्ट्स", "APSEZ"]),
    ("BAJAJFINSV", "Bajaj Finserv", ["Bajaj Finserv", "बजाज फिनसर्व"]),
    ("COALINDIA", "Coal India", ["Coal India", "कोल इंडिया", "CIL"]),
    ("DRREDDY", "Dr. Reddy's Laboratories", ["Dr Reddy", "Dr. Reddy's", "डॉ रेड्डीज", "डॉक्टर रेड्डी"]),
    ("EICHERMOT", "Eicher Motors", ["Eicher Motors", "Eicher", "आइकर मोटर्स", "Royal Enfield", "रॉयल एनफील्ड"]),
    ("GRASIM", "Grasim Industries", ["Grasim", "ग्रासिम"]),
    ("HDFCLIFE", "HDFC Life Insurance", ["HDFC Life", "एचडीएफसी लाइफ"]),
    ("HEROMOTOCO", "Hero MotoCorp", ["Hero MotoCorp", "Hero", "हीरो मोटोकॉर्प", "हीरो"]),
    ("HINDALCO", "Hindalco Industries", ["Hindalco", "हिंडाल्को"]),
    ("INDUSINDBK", "IndusInd Bank", ["IndusInd Bank", "IndusInd", "इंडसइंड बैंक"]),
    ("CIPLA", "Cipla", ["Cipla", "सिप्ला"]),
    ("DIVISLAB", "Divi's Laboratories", ["Divi's Lab", "Divis", "डिविज लैब", "डिविज"]),
    ("SBILIFE", "SBI Life Insurance", ["SBI Life", "एसबीआई लाइफ"]),
    ("TECHM", "Tech Mahindra", ["Tech Mahindra", "Tech M", "टेक महिंद्रा"]),
    ("APOLLOHOSP", "Apollo Hospitals", ["Apollo Hospitals", "Apollo", "अपोलो हॉस्पिटल", "अपोलो"]),
    ("BPCL", "Bharat Petroleum", ["BPCL", "Bharat Petroleum", "बीपीसीएल", "भारत पेट्रोलियम"]),
    ("BRITANNIA", "Britannia Industries", ["Britannia", "ब्रिटानिया"]),
    ("TATACONSUM", "Tata Consumer Products", ["Tata Consumer", "टाटा कंज्यूमर", "Tata Consumer Products"]),
    ("LTIM", "LTIMindtree", ["LTIMindtree", "LTI Mindtree", "एलटीआई माइंडट्री"]),
    ("BAJAJ-AUTO", "Bajaj Auto", ["Bajaj Auto", "बजाज ऑटो"]),

    # === NIFTY NEXT 50 / POPULAR MID-CAPS ===
    ("VEDL", "Vedanta", ["Vedanta", "वेदांता", "Vedanta Ltd"]),
    ("SAIL", "Steel Authority of India", ["SAIL", "सेल", "Steel Authority"]),
    ("PNB", "Punjab National Bank", ["PNB", "पीएनबी", "Punjab National Bank"]),
    ("BANKBARODA", "Bank of Baroda", ["Bank of Baroda", "BOB", "बैंक ऑफ बड़ौदा", "बीओबी"]),
    ("CANBK", "Canara Bank", ["Canara Bank", "केनरा बैंक"]),
    ("IOC", "Indian Oil Corporation", ["IOC", "Indian Oil", "आईओसी", "इंडियन ऑयल"]),
    ("HPCL", "Hindustan Petroleum", ["HPCL", "Hindustan Petroleum", "एचपीसीएल"]),
    ("GAIL", "GAIL India", ["GAIL", "गेल"]),
    ("BEL", "Bharat Electronics", ["BEL", "Bharat Electronics", "बीईएल", "भारत इलेक्ट्रॉनिक्स"]),
    ("HAL", "Hindustan Aeronautics", ["HAL", "Hindustan Aeronautics", "एचएएल", "हिंदुस्तान एयरोनॉटिक्स"]),
    ("BHEL", "Bharat Heavy Electricals", ["BHEL", "भेल", "Bharat Heavy"]),
    ("RECLTD", "REC Limited", ["REC", "आरईसी"]),
    ("PFC", "Power Finance Corporation", ["PFC", "पीएफसी", "Power Finance"]),
    ("IRFC", "Indian Railway Finance", ["IRFC", "आईआरएफसी", "Railway Finance"]),
    ("IRCTC", "IRCTC", ["IRCTC", "आईआरसीटीसी"]),
    ("ZOMATO", "Zomato", ["Zomato", "ज़ोमैटो"]),
    ("PAYTM", "One97 Communications", ["Paytm", "पेटीएम", "One97"]),
    ("NYKAA", "FSN E-Commerce (Nykaa)", ["Nykaa", "नायका", "FSN"]),
    ("DELHIVERY", "Delhivery", ["Delhivery", "डेलिवेरी"]),
    ("POLICYBZR", "PB Fintech (PolicyBazaar)", ["PolicyBazaar", "पॉलिसीबाज़ार", "PB Fintech"]),
    ("TRENT", "Trent Limited", ["Trent", "ट्रेंट", "Westside"]),
    ("ZYDUSLIFE", "Zydus Lifesciences", ["Zydus", "ज़ायडस", "Zydus Life"]),
    ("PIDILITIND", "Pidilite Industries", ["Pidilite", "पिडिलाइट", "Fevicol"]),
    ("SIEMENS", "Siemens", ["Siemens", "सीमेंस"]),
    ("ABB", "ABB India", ["ABB", "एबीबी"]),
    ("HAVELLS", "Havells India", ["Havells", "हैवेल्स"]),
    ("VOLTAS", "Voltas", ["Voltas", "वोल्टास"]),
    ("DIXON", "Dixon Technologies", ["Dixon", "डिक्सन"]),
    ("TATAELXSI", "Tata Elxsi", ["Tata Elxsi", "टाटा एल्क्सी"]),
    ("PERSISTENT", "Persistent Systems", ["Persistent", "पर्सिस्टेंट"]),
    ("COFORGE", "Coforge", ["Coforge", "कोफोर्ज"]),
    ("MPHASIS", "MphasiS", ["Mphasis", "एमफेसिस"]),
    ("FEDERALBNK", "Federal Bank", ["Federal Bank", "फेडरल बैंक"]),
    ("IDFCFIRSTB", "IDFC First Bank", ["IDFC First", "IDFC First Bank", "आईडीएफसी फर्स्ट बैंक"]),
    ("BANDHANBNK", "Bandhan Bank", ["Bandhan Bank", "बंधन बैंक"]),
    ("AUBANK", "AU Small Finance Bank", ["AU Bank", "AU Small Finance", "एयू बैंक"]),
    ("CHOLAFIN", "Cholamandalam Finance", ["Chola Finance", "Cholamandalam", "चोलामंडलम"]),
    ("MUTHOOTFIN", "Muthoot Finance", ["Muthoot Finance", "Muthoot", "मुथूट फाइनेंस"]),
    ("MANAPPURAM", "Manappuram Finance", ["Manappuram", "मणप्पुरम"]),
    ("SHRIRAMFIN", "Shriram Finance", ["Shriram Finance", "Shriram", "श्रीराम फाइनेंस"]),

    # === POPULAR STOCKS ON ZEE BUSINESS ===
    ("TATACHEM", "Tata Chemicals", ["Tata Chemicals", "टाटा केमिकल्स"]),
    ("TATAPOWER", "Tata Power", ["Tata Power", "टाटा पावर"]),
    ("TATACOMM", "Tata Communications", ["Tata Communications", "Tata Comm", "टाटा कम्युनिकेशंस"]),
    ("SUZLON", "Suzlon Energy", ["Suzlon", "सुजलॉन"]),
    ("NHPC", "NHPC Limited", ["NHPC", "एनएचपीसी"]),
    ("SJVN", "SJVN Limited", ["SJVN", "एसजेवीएन"]),
    ("ADANIGREEN", "Adani Green Energy", ["Adani Green", "अडानी ग्रीन"]),
    ("ADANIPOWER", "Adani Power", ["Adani Power", "अडानी पावर"]),
    ("AMBUJACEM", "Ambuja Cements", ["Ambuja Cements", "Ambuja", "अंबुजा सीमेंट"]),
    ("ACC", "ACC Limited", ["ACC", "एसीसी"]),
    ("SHREECEM", "Shree Cement", ["Shree Cement", "श्री सीमेंट"]),
    ("DALBHARAT", "Dalmia Bharat", ["Dalmia Bharat", "Dalmia", "डालमिया भारत"]),
    ("RAMCOCEM", "Ramco Cements", ["Ramco Cements", "Ramco", "रामको सीमेंट"]),
    ("DLF", "DLF Limited", ["DLF", "डीएलएफ"]),
    ("GODREJPROP", "Godrej Properties", ["Godrej Properties", "Godrej Prop", "गोदरेज प्रॉपर्टीज"]),
    ("OBEROIRLTY", "Oberoi Realty", ["Oberoi Realty", "Oberoi", "ओबेरॉय रियल्टी"]),
    ("PRESTIGE", "Prestige Estates", ["Prestige", "प्रेस्टीज"]),
    ("LODHA", "Macrotech Developers (Lodha)", ["Lodha", "लोधा", "Macrotech"]),
    ("PHOENIXLTD", "Phoenix Mills", ["Phoenix Mills", "Phoenix", "फीनिक्स मिल्स"]),
    ("BHARATFORG", "Bharat Forge", ["Bharat Forge", "भारत फोर्ज"]),
    ("BOSCHLTD", "Bosch", ["Bosch", "बॉश"]),
    ("MRF", "MRF Limited", ["MRF", "एमआरएफ"]),
    ("APOLLOTYRE", "Apollo Tyres", ["Apollo Tyres", "अपोलो टायर्स"]),
    ("BALKRISIND", "Balkrishna Industries", ["BKT", "Balkrishna", "बालकृष्ण"]),
    ("MOTHERSON", "Samvardhana Motherson", ["Motherson", "Motherson Sumi", "मदरसन"]),
    ("ASHOKLEY", "Ashok Leyland", ["Ashok Leyland", "अशोक लेलैंड"]),
    ("ESCORTS", "Escorts Kubota", ["Escorts", "एस्कॉर्ट्स"]),
    ("SOLARINDS", "Solar Industries", ["Solar Industries", "सोलर इंडस्ट्रीज"]),
    ("DEEPAKNTR", "Deepak Nitrite", ["Deepak Nitrite", "दीपक नाइट्राइट"]),
    ("ATUL", "Atul Limited", ["Atul", "अतुल"]),
    ("PIIND", "PI Industries", ["PI Industries", "पीआई इंडस्ट्रीज"]),
    ("UPL", "UPL Limited", ["UPL", "यूपीएल"]),
    ("BIOCON", "Biocon", ["Biocon", "बायोकॉन"]),
    ("LAURUSLABS", "Laurus Labs", ["Laurus Labs", "Laurus", "लॉरस लैब्स"]),
    ("AUROPHARMA", "Aurobindo Pharma", ["Aurobindo", "Aurobindo Pharma", "ऑरोबिंदो फार्मा"]),
    ("LUPIN", "Lupin", ["Lupin", "ल्यूपिन"]),
    ("TORNTPHARM", "Torrent Pharma", ["Torrent Pharma", "Torrent", "टोरेंट फार्मा"]),
    ("ALKEM", "Alkem Laboratories", ["Alkem", "अल्केम"]),
    ("NATCOPHAR", "Natco Pharma", ["Natco Pharma", "Natco", "नैटको फार्मा"]),
    ("GRANULES", "Granules India", ["Granules", "ग्रैन्यूल्स"]),
    ("JKCEMENT", "JK Cement", ["JK Cement", "जेके सीमेंट"]),
    ("JUBLFOOD", "Jubilant FoodWorks", ["Jubilant Food", "Jubilant", "जुबिलेंट फूड"]),
    ("DEVYANI", "Devyani International", ["Devyani", "देवयानी"]),
    ("DMART", "Avenue Supermarts (DMart)", ["DMart", "D-Mart", "डीमार्ट", "Avenue Supermarts"]),
    ("PAGEIND", "Page Industries", ["Page Industries", "Page", "पेज इंडस्ट्रीज"]),
    ("TVSMOTOR", "TVS Motor", ["TVS Motor", "TVS", "टीवीएस मोटर"]),
    ("MARICO", "Marico", ["Marico", "मैरिको"]),
    ("DABUR", "Dabur India", ["Dabur", "डाबर"]),
    ("COLPAL", "Colgate Palmolive", ["Colgate", "Colgate Palmolive", "कोलगेट"]),
    ("GODREJCP", "Godrej Consumer Products", ["Godrej Consumer", "GCPL", "गोदरेज कंज्यूमर"]),
    ("BERGEPAINT", "Berger Paints", ["Berger Paints", "Berger", "बर्जर पेंट्स"]),
    ("KANSAINER", "Kansai Nerolac", ["Kansai Nerolac", "Nerolac", "कंसाई नेरोलैक", "नेरोलैक"]),
    ("INDIGO", "InterGlobe Aviation (IndiGo)", ["IndiGo", "इंडिगो", "InterGlobe"]),
    ("SPICEJET", "SpiceJet", ["SpiceJet", "स्पाइसजेट"]),
    ("IDEA", "Vodafone Idea", ["Vodafone Idea", "Vi", "वोडाफोन आइडिया", "वीआई"]),
    ("MTNL", "MTNL", ["MTNL", "एमटीएनएल"]),
    ("RBLBANK", "RBL Bank", ["RBL Bank", "आरबीएल बैंक"]),
    ("YESBANK", "Yes Bank", ["Yes Bank", "यस बैंक"]),
    ("STAR", "Star Health Insurance", ["Star Health", "स्टार हेल्थ"]),
    ("LICI", "Life Insurance Corporation", ["LIC", "एलआईसी", "Life Insurance"]),
    ("GICRE", "GIC Re", ["GIC Re", "जीआईसी"]),
    ("SBICARD", "SBI Cards", ["SBI Card", "SBI Cards", "एसबीआई कार्ड"]),
    ("MAXHEALTH", "Max Healthcare", ["Max Healthcare", "Max Health", "मैक्स हेल्थकेयर"]),
    ("FORTIS", "Fortis Healthcare", ["Fortis", "Fortis Healthcare", "फोर्टिस"]),
    ("METROPOLIS", "Metropolis Healthcare", ["Metropolis", "मेट्रोपोलिस"]),
    ("LALPATHLAB", "Dr. Lal PathLabs", ["Lal PathLab", "Dr Lal", "लाल पैथलैब"]),
    ("HINDPETRO", "Hindustan Petroleum", ["HPCL", "Hindustan Petroleum", "एचपीसीएल"]),
    ("PETRONET", "Petronet LNG", ["Petronet", "पेट्रोनेट"]),
    ("MGL", "Mahanagar Gas", ["Mahanagar Gas", "MGL", "महानगर गैस"]),
    ("IGL", "Indraprastha Gas", ["IGL", "Indraprastha Gas", "आईजीएल"]),
    ("ATGL", "Adani Total Gas", ["Adani Total Gas", "Adani Gas", "अडानी टोटल गैस"]),
    ("JSWENERGY", "JSW Energy", ["JSW Energy", "जेएसडब्ल्यू एनर्जी"]),
    ("TORNTPOWER", "Torrent Power", ["Torrent Power", "टोरेंट पावर"]),
    ("CESC", "CESC Limited", ["CESC", "सीईएससी"]),
    ("NALCO", "National Aluminium", ["NALCO", "नाल्को", "National Aluminium"]),
    ("HINDZINC", "Hindustan Zinc", ["Hindustan Zinc", "Zinc", "हिंदुस्तान जिंक"]),
    ("NMDC", "NMDC", ["NMDC", "एनएमडीसी"]),
    ("MOIL", "MOIL Limited", ["MOIL", "मॉइल"]),
    ("WELCORP", "Welspun Corp", ["Welspun", "वेल्सपन"]),
    ("JINDALSTEEL", "Jindal Steel & Power", ["JSPL", "Jindal Steel", "जिंदल स्टील"]),
    ("APLAPOLLO", "APL Apollo Tubes", ["APL Apollo", "एपीएल अपोलो"]),
    ("RATNAMANI", "Ratnamani Metals", ["Ratnamani", "रत्नमणी"]),
    ("CROMPTON", "Crompton Greaves", ["Crompton", "क्रॉम्प्टन"]),
    ("POLYCAB", "Polycab India", ["Polycab", "पॉलीकैब"]),
    ("KEI", "KEI Industries", ["KEI", "केईआई"]),
    ("KAYNES", "Kaynes Technology", ["Kaynes", "कायन्स"]),
    ("COCHINSHIP", "Cochin Shipyard", ["Cochin Shipyard", "कोचीन शिपयार्ड"]),
    ("GRSE", "Garden Reach Shipbuilders", ["GRSE", "Garden Reach", "गार्डन रीच"]),
    ("MAZAGON", "Mazagon Dock", ["Mazagon Dock", "मझगांव डॉक"]),
    ("BDL", "Bharat Dynamics", ["BDL", "Bharat Dynamics", "भारत डायनामिक्स"]),
    ("PARAS", "Paras Defence", ["Paras Defence", "पारस डिफेंस"]),
    ("CENTRALBK", "Central Bank of India", ["Central Bank", "सेंट्रल बैंक"]),
    ("INDIANB", "Indian Bank", ["Indian Bank", "इंडियन बैंक"]),
    ("UNIONBANK", "Union Bank of India", ["Union Bank", "यूनियन बैंक"]),
    ("MAHABANK", "Bank of Maharashtra", ["Bank of Maharashtra", "बैंक ऑफ महाराष्ट्र"]),
    ("UCOBANK", "UCO Bank", ["UCO Bank", "यूको बैंक"]),
    ("SYNGENE", "Syngene International", ["Syngene", "सिनजीन"]),
    ("IIFL", "IIFL Finance", ["IIFL", "आईआईएफएल"]),
    ("ANGELONE", "Angel One", ["Angel One", "Angel Broking", "एंजल वन"]),
    ("CDSL", "CDSL", ["CDSL", "सीडीएसएल"]),
    ("BSE", "BSE Limited", ["BSE", "बीएसई"]),
    ("MCX", "Multi Commodity Exchange", ["MCX", "एमसीएक्स"]),
    ("CAMS", "CAMS", ["CAMS", "कैम्स"]),
    ("KPITTECH", "KPIT Technologies", ["KPIT", "KPIT Tech", "केपीआईटी"]),
    ("LTTS", "L&T Technology Services", ["LTTS", "L&T Tech", "एलटीटीएस"]),
    ("CYIENT", "Cyient", ["Cyient", "साइएंट"]),
    ("SONACOMS", "Sona BLW Precision", ["Sona Comstar", "Sona BLW", "सोना कॉमस्टार"]),
    ("HAPPSTMNDS", "Happiest Minds", ["Happiest Minds", "हैप्पिएस्ट माइंड्स"]),
    ("ZEEL", "Zee Entertainment", ["Zee Entertainment", "ZEEL", "जी एंटरटेनमेंट"]),
    ("PVR", "PVR INOX", ["PVR INOX", "PVR", "पीवीआर"]),
    ("RAJESHEXPO", "Rajesh Exports", ["Rajesh Exports", "राजेश एक्सपोर्ट्स"]),
    ("KALYANFBK", "Kalyan Jewellers", ["Kalyan Jewellers", "कल्याण ज्वेलर्स"]),
    ("SENCO", "Senco Gold", ["Senco Gold", "Senco", "सेनको गोल्ड"]),
    ("RVNL", "Rail Vikas Nigam", ["RVNL", "आरवीएनएल", "Rail Vikas"]),
    ("RAILTEL", "RailTel Corporation", ["RailTel", "रेलटेल"]),
    ("TIINDIA", "Tube Investments", ["Tube Investments", "TI India", "ट्यूब इन्वेस्टमेंट्स"]),
    ("CUMMINSIND", "Cummins India", ["Cummins", "कमिंस"]),
    ("THERMAX", "Thermax", ["Thermax", "थर्मैक्स"]),
    ("EXIDEIND", "Exide Industries", ["Exide", "एक्साइड"]),
    ("AMARAJABAT", "Amara Raja Energy", ["Amara Raja", "अमरा राजा"]),

    # === STOCKS SEEN IN ZEE BUSINESS RECOMMENDATION SEGMENTS ===
    ("IDEA", "Vodafone Idea", ["Idea", "Vodafone Idea"]),
    ("JUNIPERGREEN", "Juniper Green Energy", ["Juniper Green", "Juniper Green Energy"]),
    ("NETWEB", "Netweb Technologies", ["Netweb", "Netweb Tech", "Netweb Technologies"]),
    ("ASHOKLEY", "Ashok Leyland", ["Ashok Leyland", "Ashok Ley"]),
    ("MOSCHIP", "MosChip Technologies", ["MosChip", "Moschip"]),
    ("WPIL", "WPIL Limited", ["WPIL", "WPIL Ltd"]),
    ("AMBER", "Amber Enterprises", ["Amber", "Amber Enterprises", "Amber Ent"]),
    ("VOLTAS", "Voltas", ["Voltas"]),
    ("NCC", "NCC Limited", ["NCC", "NCC Ltd"]),
    ("TATVACHINTAN", "Tatva Chintan Pharma Chem", ["Tatva Chintan", "Tatva Chintan Pharma"]),
    ("HONASA", "Honasa Consumer", ["Honasa", "Honasa Consumer"]),
    ("CUB", "City Union Bank", ["CUB", "City Union Bank"]),

    # === INDICES (commonly mentioned) ===
    ("NIFTY", "Nifty 50", ["Nifty", "Nifty 50", "निफ्टी", "Nifty50"]),
    ("BANKNIFTY", "Nifty Bank", ["Bank Nifty", "Nifty Bank", "बैंक निफ्टी"]),
    ("FINNIFTY", "Nifty Financial Services", ["Fin Nifty", "Finnifty", "फिन निफ्टी"]),
    ("SENSEX", "BSE Sensex", ["Sensex", "सेंसेक्स", "BSE Sensex"]),
    ("MIDCPNIFTY", "Nifty Midcap", ["Midcap Nifty", "Nifty Midcap", "मिडकैप निफ्टी"]),

    # === COMMODITIES (frequently discussed) ===
    ("GOLD", "Gold", ["Gold", "सोना", "गोल्ड"]),
    ("SILVER", "Silver", ["Silver", "चांदी", "सिल्वर"]),
    ("CRUDEOIL", "Crude Oil", ["Crude Oil", "Crude", "क्रूड ऑयल", "क्रूड"]),
    ("NATURALGAS", "Natural Gas", ["Natural Gas", "नैचुरल गैस"]),
    ("COPPER", "Copper", ["Copper", "कॉपर", "तांबा"]),
]

# Build lookup dictionaries for fast matching
def build_lookup():
    """Build lookup dictionaries from master list"""
    symbol_lookup = {}  # alias -> (symbol, full_name)
    all_aliases = []    # flat list of all aliases for fuzzy matching

    for symbol, full_name, aliases in STOCK_MASTER_LIST:
        # Add symbol itself
        symbol_lookup[symbol.upper()] = (symbol, full_name)
        all_aliases.append(symbol.upper())

        # Add full name
        symbol_lookup[full_name.upper()] = (symbol, full_name)
        all_aliases.append(full_name.upper())

        # Add all aliases
        for alias in aliases:
            symbol_lookup[alias.upper()] = (symbol, full_name)
            all_aliases.append(alias.upper())

    return symbol_lookup, all_aliases


# Action keywords in Hindi and English
ACTION_KEYWORDS = {
    "BUY": ["buy", "खरीदें", "खरीदो", "खरीदना", "खरीद", "लॉन्ग", "long", "bullish", "बुलिश",
            "accumulate", "अक्यूमुलेट", "add", "एड"],
    "SELL": ["sell", "बेचें", "बेचो", "बेचना", "बेच", "शॉर्ट", "short", "bearish", "बेयरिश",
             "book profit", "प्रॉफिट बुक", "profit booking"],
    "HOLD": ["hold", "होल्ड", "रखें", "maintain", "मेंटेन"],
    "TARGET": ["target", "टारगेट", "लक्ष्य"],
    "STOP LOSS": ["stop loss", "स्टॉप लॉस", "SL", "एसएल", "stoploss"],
}

# Price pattern keywords
PRICE_KEYWORDS = [
    "रुपये", "रुपए", "Rs", "₹", "रूपये", "rupees", "rupee",
    "price", "प्राइस", "कीमत", "level", "लेवल",
]


if __name__ == "__main__":
    symbol_lookup, all_aliases = build_lookup()
    print(f"Loaded {len(STOCK_MASTER_LIST)} stocks/indices/commodities")
    print(f"Total aliases: {len(all_aliases)}")
    print(f"Unique aliases: {len(symbol_lookup)}")
