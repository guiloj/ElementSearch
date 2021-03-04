import math


#c = int(input("by Name(1):\nby Symbol(2):\nby Melting point(3):\nby Boiling point(4):\nby Weight(5):\nby Atomic number(6):\n"))


#names = ['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'sodium', 'magnesium', 'aluminium', 'silicon', 'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc', 'gallium', 'germanium', 'arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 'xenon', 'caesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'darmstadtium', 'roentgenium', 'copernicium', 'nihonium', 'flerovium', 'moscovium', 'livermorium', 'tennessine', 'oganesson']
#symbols = ['h', 'he', 'li', 'be', 'b', 'c', 'n', 'o', 'f', 'ne', 'na', 'mg', 'al', 'si', 'p', 's', 'cl', 'ar', 'k', 'ca', 'sc', 'ti', 'v', 'cr', 'mn', 'fe', 'co', 'ni', 'cu', 'zn', 'ga', 'ge', 'as', 'se', 'br', 'kr', 'rb', 'sr', 'y', 'zr', 'nb', 'mo', 'tc', 'ru', 'rh', 'pd', 'ag', 'cd', 'in', 'sn', 'sb', 'te', 'i', 'xe', 'cs', 'ba', 'la', 'ce', 'pr', 'nd', 'pm', 'sm', 'eu', 'gd', 'tb', 'dy', 'ho', 'er', 'tm', 'yb', 'lu', 'hf', 'ta', 'w', 're', 'os', 'ir', 'pt', 'au', 'hg', 'tl', 'pb', 'bi', 'po', 'at', 'rn', 'fr', 'ra', 'ac', 'th', 'pa', 'u', 'np', 'pu', 'am', 'cm', 'bk', 'cf', 'es', 'fm', 'md', 'no', 'lr', 'rf', 'db', 'sg', 'bh', 'hs', 'mt', 'ds', 'rg', 'cn', 'nh', 'fl', 'mc', 'lv', 'ts', 'og']
#numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118']

#elements = list(zip(names, symbols, numbers))


campos = ['Atomic number','Symbol','Name', 'Group', 'Period', 'Melting point', 'Boiling point', 'Atomic weight',]
print('Element Search: version 1.0, Python 3.9.2, 04/03/2021, languages, English')
print('Credits on GitHub: @guiloj, @luccasaz, @Taskmaster3000')
print('This git is protected under the GNU General Public License v3.0')
print('In this program it is possible to search for elements in the periodic table by using', len(campos),'different search terms including:')
print(campos)
print('for', campos[5],',', campos[6],'and', campos[7], 'use degree Celsius and u (unified atomic mass unit) accordingly to make your search')
print("Search:\n")
elements = [['1', 'h', 'hydrogen', '1', '1', '287.16', '293.43', '1'],
            ['2', 'he', 'helium', '18', '1', 'null', '277.37', '4.002602'],
            ['3', 'li', 'lithium', '1', '2', '726.84', '1833.15', '6.94'],
            ['4', 'be', 'beryllium', '2', '2', '1833.15', '3015.15', '9.0121831'],
            ['5', 'b', 'boron', '13', '2', '2622.15', '4473.15', '10.81'],
            ['6', 'c', 'carbon', '14', '2', '4273.15', '4573.15', '12.011'],
            ['7', 'n', 'nitrogen', '15', '2', '336.3', '350.51', '14.007'],
            ['8', 'o', 'oxygen', '16', '2', '327.51', '363.35', '15.999'],
            ['9', 'f', 'fluorine', '17', '2', '326.68', '358.18', '18.998403163'],
            ['10', 'ne', 'neon', '18', '2', '297.71', '300.22', '20.1797'],
            ['11', 'na', 'sodium', '1', '3', '644.02', '1429.15', '22.98976928'],
            ['12', 'mg', 'magnesium', '2', '3', '1196.15', '1636.15', '24.305'],
            ['13', 'al', 'aluminium', '13', '3', '1206.62', '3065.15', '26.9815384'],
            ['14', 'si', 'silicon', '14', '3', '1960.15', '3811.15', '28.085'],
            ['15', 'p', 'phosphorus', '15', '3', '590.45', '823.15', '30.973761998'],
            ['16', 's', 'sulfur', '16', '3', '661.51', '991.02', '32.06'],
            ['17', 'cl', 'chlorine', '17', '3', '444.75', '512.26', '35.45'],
            ['18', 'ar', 'argon', '18', '3', '356.95', '360.45', '39.95'],
            ['19', 'k', 'potassium', '1', '4', '609.68', '1305.15', '39.0983'],
            ['20', 'ca', 'calcium', '2', '4', '1388.15', '2030.15', '40.078'],
            ['21', 'sc', 'scandium', '3', '4', '2087.15', '3382.15', '44.955908'],
            ['22', 'ti', 'titanium', '4', '4', '2214.15', '3833.15', '47.867'],
            ['23', 'v', 'vanadium', '5', '4', '2456.15', '3953.15', '50.9415'],
            ['24', 'cr', 'chromium', '6', '4', '2453.15', '3217.15', '51.9961'],
            ['25', 'mn', 'manganese', '7', '4', '1792.15', '2607.15', '54.938043'],
            ['26', 'fe', 'iron', '8', '4', '2084.15', '3407.15', '55.845'],
            ['27', 'co', 'cobalt', '9', '4', '2041.15', '3473.15', '58.933194'],
            ['28', 'ni', 'nickel', '10', '4', '2001.15', '3459.15', '58.6934'],
            ['29', 'cu', 'copper', '11', '4', '1630.92', '3108.15', '63.546'],
            ['30', 'zn', 'zinc', '12', '4', '966.03', '1453.15', '65.38'],
            ['31', 'ga', 'gallium', '13', '4', '576.0646', '2946.15', '69.723'],
            ['32', 'ge', 'germanium', '14', '4', '1484.55', '3379.15', '72.63'],
            ['33', 'as', 'arsenic', '15', '4', '1363.15', '1160.15', '74.921595'],
            ['34', 'se', 'selenium', '16', '4', '726.15', '1231.15', '78.971'],
            ['35', 'br', 'bromine', '17', '4', '538.95', '605.15', '79.904'],
            ['36', 'kr', 'krypton', '18', '4', '388.94', '393.08', '83.798'],
            ['37', 'rb', 'rubidium', '1', '5', '585.61', '1234.15', '85.4678'],
            ['38', 'sr', 'strontium', '2', '5', '1323.15', '1928.15', '87.62'],
            ['39', 'y', 'yttrium', '3', '5', '2072.15', '3882.15', '88.90584'],
            ['40', 'zr', 'zirconium', '4', '5', '2401.15', '4955.15', '91.224'],
            ['41', 'nb', 'niobium', '5', '5', '3023.15', '5290.15', '92.90637'],
            ['42', 'mo', 'molybdenum', '6', '5', '3169.15', '5185.15', '95.95'],
            ['43', 'tc', 'technetium', '7', '5', '2703.15', '4811.15', '98'],
            ['44', 'ru', 'ruthenium', '8', '5', '2880.15', '4696.15', '101.07'],
            ['45', 'rh', 'rhodium', '9', '5', '2510.15', '4241.15', '102.90549'],
            ['46', 'pd', 'palladium', '10', '5', '2101.2', '3509.15', '106.42'],
            ['47', 'ag', 'silver', '11', '5', '1508.08', '2708.15', '107.8682'],
            ['48', 'cd', 'cadmium', '12', '5', '867.37', '1313.15', '112.414'],
            ['49', 'in', 'indium', '13', '5', '702.9', '2618.15', '114.818'],
            ['50', 'sn', 'tin', '14', '5', '778.23', '3148.15', '118.71'],
            ['51', 'sb', 'antimony', '15', '5', '1176.93', '2133.15', '121.76'],
            ['52', 'te', 'tellurium', '16', '5', '995.81', '1534.15', '127.6'],
            ['53', 'i', 'iodine', '17', '5', '660', '730.55', '126.90447'],
            ['54', 'xe', 'xenon', '18', '5', '434.55', '438.18', '131.293'],
            ['55', 'cs', 'caesium', '1', '6', '574.74', '1217.15', '132.90545196'],
            ['56', 'ba', 'barium', '2', '6', '1273.15', '2443.15', '137.327'],
            ['57', 'la', 'lanthanum', 'null', '6', '1466.15', '4010.15', '138.90547'],
            ['58', 'ce', 'cerium', 'null', '6', '1341.15', '3989.15', '140.116'],
            ['59', 'pr', 'praseodymium', 'null', '6', '1481.15', '4066.15', '140.90766'],
            ['60', 'nd', 'neodymium', 'null', '6', '1570.15', '3620.15', '144.242'],
            ['61', 'pm', 'promethium', 'null', '6', '1588.15', '3546.15', '145'],
            ['62', 'sm', 'samarium', 'null', '6', '1618.15', '2340.15', '150.36'],
            ['63', 'eu', 'europium', 'null', '6', '1372.15', '2075.15', '151.964'],
            ['64', 'gd', 'gadolinium', 'null', '6', '1858.15', '3819.15', '157.25'],
            ['65', 'tb', 'terbium', 'null', '6', '1902.15', '3776.15', '158.925354'],
            ['66', 'dy', 'dysprosium', 'null', '6', '1953.15', '3113.15', '162.5'],
            ['67', 'ho', 'holmium', 'null', '6', '2007.15', '3266.15', '164.930328'],
            ['68', 'er', 'erbium', 'null', '6', '2075.15', '3414.15', '167.259'],
            ['69', 'tm', 'thulium', 'null', '6', '2091.15', '2496.15', '168.934218'],
            ['70', 'yb', 'ytterbium', 'null', '6', '1370.15', '1742.15', '173.045'],
            ['71', 'lu', 'lutetium', '3', '6', '2198.15', '3948.15', '174.9668'],
            ['72', 'hf', 'hafnium', '4', '6', '2779.15', '5149.15', '178.49'],
            ['73', 'ta', 'tantalum', '5', '6', '3563.15', '6004.15', '180.94788'],
            ['74', 'w', 'tungsten', '6', '6', '3968.15', '6101.15', '183.84'],
            ['75', 're', 'rhenium', '7', '6', '3732.15', '6142.15', '186.207'],
            ['76', 'os', 'osmium', '8', '6', '3579.15', '5558.15', '190.23'],
            ['77', 'ir', 'iridium', '9', '6', '2992.15', '4974.15', '192.217'],
            ['78', 'pt', 'platinum', '10', '6', '2314.55', '4371.15', '195.084'],
            ['79', 'au', 'gold', '11', '6', '1610.48', '3402.15', '196.96657'],
            ['80', 'hg', 'mercury', '12', '6', '507.58', '903.03', '200.592'],
            ['81', 'tl', 'thallium', '13', '6', '850.15', '2019.15', '204.38'],
            ['82', 'pb', 'lead', '14', '6', '873.76', '2295.15', '207.2'],
            ['83', 'bi', 'bismuth', '15', '6', '817.85', '2110.15', '208.9804'],
            ['84', 'po', 'polonium', '16', '6', '800.15', '1508.15', '209'],
            ['85', 'at', 'astatine', '17', '6', '848.15', '883.15', '210'],
            ['86', 'rn', 'radon', '18', '6', '475.15', '484.45', '222'],
            ['87', 'fr', 'francium', '1', '7', '554.15', '1163.15', '223'],
            ['88', 'ra', 'radium', '2', '7', '1246.15', '2283.15', '226'],
            ['89', 'ac', 'actinium', 'null', '7', '1596.15', '3744.15', '227'],
            ['90', 'th', 'thorium', 'null', '7', '2388.15', '5334.15', '232.0377'],
            ['91', 'pa', 'protactinium', 'null', '7', '2114.15', '4573.15', '231.03588'],
            ['92', 'u', 'uranium', 'null', '7', '1678.45', '4677.15', '238.02891'],
            ['93', 'np', 'neptunium', 'null', '7', '1190.15', '4546.15', '237'],
            ['94', 'pu', 'plutonium', 'null', '7', '1185.65', '3774.15', '244'],
            ['95', 'am', 'americium', 'null', '7', '1722.15', '3153.15', '243'],
            ['96', 'cm', 'curium', 'null', '7', '1886.15', '3656.15', '247'],
            ['97', 'bk', 'berkelium', 'null', '7', '1532.15', '3173.15', '247'],
            ['98', 'cf', 'californium', 'null', '7', '1446.15', '2016.15', '251'],
            ['99', 'es', 'einsteinium', 'null', '7', '1406.15', '1542.15', '252'],
            ['100', 'fm', 'fermium', 'null', '7', '1398.15', 'null', '257'],
            ['101', 'md', 'mendelevium', 'null', '7', '1373.15', 'null', '258'],
            ['102', 'no', 'nobelium', 'null', '7', '1373.15', 'null', '259'],
            ['103', 'lr', 'lawrencium', '3', '7', '2173.15', 'null', '266'],
            ['104', 'rf', 'rutherfordium', '4', '7', '2673.15', '6073.15', '267'],
            ['105', 'db', 'dubnium', '5', '7', 'null', 'null', '268'],
            ['106', 'sg', 'seaborgium', '6', '7', 'null', 'null', '269'],
            ['107', 'bh', 'bohrium', '7', '7', 'null', 'null', '270'],
            ['108', 'hs', 'hassium', '8', '7', 'null', 'null', '270'],
            ['109', 'mt', 'meitnerium', '9', '7', 'null', 'null', '278'],
            ['110', 'ds', 'darmstadtium', '10', '7', 'null', 'null', '281'],
            ['111', 'rg', 'roentgenium', '11', '7', 'null', 'null', '282'],
            ['112', 'cn', 'copernicium', '12', '7', '556.15', '613.15', '285'],
            ['113', 'nh', 'nihonium', '13', '7', '973.15', '1673.15', '286'],
            ['114', 'fl', 'flerovium', '14', '7', '73.15', '-106.85', '289'],
            ['115', 'mc', 'moscovium', '15', '7', '973.15', '1673.15', '290'],
            ['116', 'lv', 'livermorium', '16', '7', '973.15', '1373.15', '293'],
            ['117', 'ts', 'tennessine', '17', '7', '973.15', '1156.15', '294'],
            ['118', 'og', 'oganesson', '18', '7', '598.15', '723.15', '294']]
c = 0

while c <= 8:
    for i in range(8):
        print('by '+ campos[i], '(' ,i+1,  ')')
    c = int(input("Stop ( 0 )\n"))
    if c > 8:
        print('This number: ', c, ', is not any of the above, TRY AGAIN')
    elif c == 0:
        break
    else:
        print('You are searching for: ', campos[c-1])
        search = input(campos[c-1] + ': ').lower()
        def elementFilter(elemento):
            if c in [6, 7, 8]:
                if search == 'null':
                    return elemento[c-1] == search
                elif elemento[c-1] == 'null':
                    return 0
                return round(float(search))==round(float(elemento[c-1]))
            else:
                return search == elemento[c-1]
        results = list(filter(elementFilter, elements))
        print(campos)
        for result in results:
            print(result)
