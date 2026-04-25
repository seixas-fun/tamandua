# flags_data.py

import unicodedata

from babel import Locale

FLAG_SETS = {
    "national": {
        "folder": "national_flags",
        "data": [
            {"id": 1, "name": "Afghanistan", "synonyms": ["afghanistan"], "image": "afghanistan.png"},
            {"id": 2, "name": "Albania", "synonyms": ["albania"], "image": "albania.png"},
            {"id": 3, "name": "Algeria", "synonyms": ["algeria"], "image": "algeria.png"},
            {"id": 4, "name": "Andorra", "synonyms": ["andorra"], "image": "andorra.png"},
            {"id": 5, "name": "Angola", "synonyms": ["angola"], "image": "angola.png"},
            {"id": 6, "name": "Antigua and Barbuda", "synonyms": ["antigua and barbuda"], "image": "antigua_and_barbuda.png"},
            {"id": 7, "name": "Argentina", "synonyms": ["argentina"], "image": "argentina.png"},
            {"id": 8, "name": "Armenia", "synonyms": ["armenia"], "image": "armenia.png"},
            {"id": 9, "name": "Australia", "synonyms": ["australia"], "image": "australia.png"},
            {"id": 10, "name": "Austria", "synonyms": ["austria"], "image": "austria.png"},
            {"id": 11, "name": "Azerbaijan", "synonyms": ["azerbaijan"], "image": "azerbaijan.png"},
            {"id": 12, "name": "The Bahamas", "synonyms": ["bahamas", "the bahamas"], "image": "bahamas.png"},
            {"id": 13, "name": "Bahrain", "synonyms": ["bahrain"], "image": "bahrain.png"},
            {"id": 14, "name": "Bangladesh", "synonyms": ["bangladesh"], "image": "bangladesh.png"},
            {"id": 15, "name": "Barbados", "synonyms": ["barbados"], "image": "barbados.png"},
            {"id": 16, "name": "Belarus", "synonyms": ["belarus"], "image": "belarus.png"},
            {"id": 17, "name": "Belgium", "synonyms": ["belgium"], "image": "belgium.png"},
            {"id": 18, "name": "Belize", "synonyms": ["belize"], "image": "belize.png"},
            {"id": 19, "name": "Benin", "synonyms": ["benin"], "image": "benin.png"},
            {"id": 20, "name": "Bhutan", "synonyms": ["bhutan"], "image": "bhutan.png"},
            {"id": 21, "name": "Bolivia", "synonyms": ["bolivia"], "image": "bolivia.png"},
            {"id": 22, "name": "Bosnia and Herzegovina", "synonyms": ["bosnia and herzegovina"], "image": "bosnia_and_herzegovina.png"},
            {"id": 23, "name": "Botswana", "synonyms": ["botswana"], "image": "botswana.png"},
            {"id": 24, "name": "Brazil", "synonyms": ["brazil"], "image": "brazil.png"},
            {"id": 25, "name": "Brunei", "synonyms": ["brunei"], "image": "brunei.png"},
            {"id": 26, "name": "Bulgaria", "synonyms": ["bulgaria"], "image": "bulgaria.png"},
            {"id": 27, "name": "Burkina Faso", "synonyms": ["burkina faso"], "image": "burkina_faso.png"},
            {"id": 28, "name": "Burundi", "synonyms": ["burundi"], "image": "burundi.png"},
            {"id": 29, "name": "Cambodia", "synonyms": ["cambodia"], "image": "cambodia.png"},
            {"id": 30, "name": "Cameroon", "synonyms": ["cameroon"], "image": "cameroon.png"},
            {"id": 31, "name": "Canada", "synonyms": ["canada"], "image": "canada.png"},
            {"id": 32, "name": "Cape Verde", "synonyms": ["cape verde"], "image": "cape_verde.png"},
            {"id": 33, "name": "Central African Republic", "synonyms": ["central african republic", "car"], "image": "central_african_republic.png"},
            {"id": 34, "name": "Chad", "synonyms": ["chad"], "image": "chad.png"},
            {"id": 35, "name": "Chile", "synonyms": ["chile"], "image": "chile.png"},
            {"id": 36, "name": "China", "synonyms": ["china"], "image": "china.png"},
            {"id": 37, "name": "Colombia", "synonyms": ["colombia"], "image": "colombia.png"},
            {"id": 38, "name": "Comoros", "synonyms": ["comoros"], "image": "comoros.png"},
            {"id": 39, "name": "Costa Rica", "synonyms": ["costa rica"], "image": "costa_rica.png"},
            {"id": 40, "name": "Cote d'Ivoire", "synonyms": ["cote divoire", "cote d'ivoire", "ivory coast"], "image": "cote_divoire.png"},
            {"id": 41, "name": "Croatia", "synonyms": ["croatia"], "image": "croatia.png"},
            {"id": 42, "name": "Cuba", "synonyms": ["cuba"], "image": "cuba.png"},
            {"id": 43, "name": "Cyprus", "synonyms": ["cyprus"], "image": "cyprus.png"},
            {"id": 44, "name": "Czechia", "synonyms": ["czech republic", "czechia"], "image": "czechia.png"},
            {"id": 45, "name": "Denmark", "synonyms": [ "denmark"], "image": "denmark.png"},
            {"id": 46, "name": "Djibouti", "synonyms": ["djibouti"], "image": "djibouti.png"},
            {"id": 47, "name": "Dominica", "synonyms": ["dominica"], "image": "dominica.png"},
            {"id": 48, "name": "Dominican Republic", "synonyms": ["dominican republic"], "image": "dominican_republic.png"},
            {"id": 49, "name": "Democratic Republic of the Congo", "synonyms": ["democratic republic of the congo", "drc"], "image": "democratic_republic_of_the_congo.png"},
            {"id": 50, "name": "Ecuador", "synonyms": ["ecuador"], "image": "ecuador.png"},
            {"id": 51, "name": "Egypt", "synonyms": ["egypt"], "image": "egypt.png"},
            {"id": 52, "name": "El Salvador", "synonyms": ["el salvador"], "image": "el_salvador.png"},
            {"id": 53, "name": "Equatorial Guinea", "synonyms": ["equatorial guinea"], "image": "equatorial_guinea.png"},
            {"id": 54, "name": "Eritrea", "synonyms": ["eritrea"], "image": "eritrea.png"},
            {"id": 55, "name": "Estonia", "synonyms": ["estonia"], "image": "estonia.png"},
            {"id": 56, "name": "Eswatini", "synonyms": ["eswatini"], "image": "eswatini.png"},
            {"id": 57, "name": "Ethiopia", "synonyms": ["ethiopia"], "image": "ethiopia.png"},
            {"id": 58, "name": "Fiji", "synonyms": ["fiji"], "image": "fiji.png"},
            {"id": 59, "name": "Finland", "synonyms": ["finland"], "image": "finland.png"},
            {"id": 60, "name": "France", "synonyms": ["france"], "image": "france.png"},
            {"id": 61, "name": "Gabon", "synonyms": ["gabon"], "image": "gabon.png"},
            {"id": 62, "name": "The Gambia", "synonyms": ["gambia", "the gambia"], "image": "gambia.png"},
            {"id": 63, "name": "Georgia", "synonyms": ["georgia"], "image": "georgia.png"},
            {"id": 64, "name": "Germany", "synonyms": ["germany"], "image": "germany.png"},
            {"id": 65, "name": "Ghana", "synonyms": ["ghana"], "image": "ghana.png"},
            {"id": 66, "name": "Greece", "synonyms": ["greece"], "image": "greece.png"},
            {"id": 67, "name": "Grenada", "synonyms": ["grenada"], "image": "grenada.png"},
            {"id": 68, "name": "Guatemala", "synonyms": ["guatemala"], "image": "guatemala.png"},
            {"id": 69, "name": "Guinea-Bissau", "synonyms": ["guinea-bissau"], "image": "guinea-bissau.png"},
            {"id": 70, "name": "Guinea", "synonyms": ["guinea"], "image": "guinea.png"},
            {"id": 71, "name": "Guyana", "synonyms": ["guyana"], "image": "guyana.png"},
            {"id": 72, "name": "Haiti", "synonyms": ["haiti"], "image": "haiti.png"},
            {"id": 73, "name": "Honduras", "synonyms": ["honduras"], "image": "honduras.png"},
            {"id": 74, "name": "Hungary", "synonyms": ["hungary"], "image": "hungary.png"},
            {"id": 75, "name": "Iceland", "synonyms": ["iceland"], "image": "iceland.png"},
            {"id": 76, "name": "India", "synonyms": ["india"], "image": "india.png"},
            {"id": 77, "name": "Indonesia", "synonyms": ["indonesia"], "image": "indonesia.png"},
            {"id": 78, "name": "Iran", "synonyms": ["iran"], "image": "iran.png"},
            {"id": 79, "name": "Iraq", "synonyms": ["iraq"], "image": "iraq.png"},
            {"id": 80, "name": "Ireland", "synonyms": ["ireland"], "image": "ireland.png"},
            {"id": 81, "name": "Israel", "synonyms": ["israel"], "image": "israel.png"},
            {"id": 82, "name": "Italy", "synonyms": ["italy"], "image": "italy.png"},
            {"id": 83, "name": "Jamaica", "synonyms": ["jamaica"], "image": "jamaica.png"},
            {"id": 84, "name": "Japan", "synonyms": ["japan"], "image": "japan.png"},
            {"id": 85, "name": "Jordan", "synonyms": ["jordan"], "image": "jordan.png"},
            {"id": 86, "name": "Kazakhstan", "synonyms": ["kazakhstan"], "image": "kazakhstan.png"},
            {"id": 87, "name": "Kenya", "synonyms": ["kenya"], "image": "kenya.png"},
            {"id": 88, "name": "Kiribati", "synonyms": ["kiribati"], "image": "kiribati.png"},
            {"id": 89, "name": "Kuwait", "synonyms": ["kuwait"], "image": "kuwait.png"},
            {"id": 90, "name": "Kyrgyzstan", "synonyms": ["kyrgyzstan"], "image": "kyrgyzstan.png"},
            {"id": 91, "name": "Laos", "synonyms": ["laos"], "image": "laos.png"},
            {"id": 92, "name": "Latvia", "synonyms": ["latvia"], "image": "latvia.png"},
            {"id": 93, "name": "Lebanon", "synonyms": ["lebanon"], "image": "lebanon.png"},
            {"id": 94, "name": "Lesotho", "synonyms": ["lesotho"], "image": "lesotho.png"},
            {"id": 95, "name": "Liberia", "synonyms": ["liberia"], "image": "liberia.png"},
            {"id": 96, "name": "Libya", "synonyms": ["libya"], "image": "libya.png"},
            {"id": 97, "name": "Liechtenstein", "synonyms": ["liechtenstein"], "image": "liechtenstein.png"},
            {"id": 98, "name": "Lithuania", "synonyms": ["lithuania"], "image": "lithuania.png"},
            {"id": 99, "name": "Luxembourg", "synonyms": ["luxembourg"], "image": "luxembourg.png"},
            {"id": 100, "name": "Madagascar", "synonyms": ["madagascar"], "image": "madagascar.png"},
            {"id": 101, "name": "Malawi", "synonyms": ["malawi"], "image": "malawi.png"},
            {"id": 102, "name": "Malaysia", "synonyms": ["malaysia"], "image": "malaysia.png"},
            {"id": 103, "name": "Maldives", "synonyms": ["maldives"], "image": "maldives.png"},
            {"id": 104, "name": "Mali", "synonyms": ["mali"], "image": "mali.png"},
            {"id": 105, "name": "Malta", "synonyms": ["malta"], "image": "malta.png"},
            {"id": 106, "name": "Marshall Islands", "synonyms": ["marshall islands"], "image": "marshall_islands.png"},
            {"id": 107, "name": "Mauritania", "synonyms": ["mauritania"], "image": "mauritania.png"},
            {"id": 108, "name": "Mauritius", "synonyms": ["mauritius"], "image": "mauritius.png"},
            {"id": 109, "name": "Mexico", "synonyms": ["mexico"], "image": "mexico.png"},
            {"id": 110, "name": "Micronesia", "synonyms": ["micronesia"], "image": "micronesia.png"},
            {"id": 111, "name": "Moldova", "synonyms": ["moldova"], "image": "moldova.png"},
            {"id": 112, "name": "Monaco", "synonyms": ["monaco"], "image": "monaco.png"},
            {"id": 113, "name": "Mongolia", "synonyms": ["mongolia"], "image": "mongolia.png"},
            {"id": 114, "name": "Montenegro", "synonyms": ["montenegro"], "image": "montenegro.png"},
            {"id": 115, "name": "Morocco", "synonyms": ["morocco"], "image": "morocco.png"},
            {"id": 116, "name": "Mozambique", "synonyms": ["mozambique"], "image": "mozambique.png"},
            {"id": 117, "name": "Myanmar", "synonyms": ["myanmar"], "image": "myanmar.png"},
            {"id": 118, "name": "Namibia", "synonyms": ["namibia"], "image": "namibia.png"},
            {"id": 119, "name": "Nauru", "synonyms": ["nauru"], "image": "nauru.png"},
            {"id": 120, "name": "Nepal", "synonyms": ["nepal"], "image": "nepal.png"},
            {"id": 121, "name": "Netherlands", "synonyms": ["netherlands"], "image": "netherlands.png"},
            {"id": 122, "name": "New Zealand", "synonyms": ["new zealand"], "image": "new_zealand.png"},
            {"id": 123, "name": "Nicaragua", "synonyms": ["nicaragua"], "image": "nicaragua.png"},
            {"id": 124, "name": "Niger", "synonyms": ["niger"], "image": "niger.png"},
            {"id": 125, "name": "Nigeria", "synonyms": ["nigeria"], "image": "nigeria.png"},
            {"id": 126, "name": "North Korea", "synonyms": ["north korea"], "image": "north_korea.png"},
            {"id": 127, "name": "North Macedonia", "synonyms": ["north macedonia"], "image": "north_macedonia.png"},
            {"id": 128, "name": "Norway", "synonyms": ["norway"], "image": "norway.png"},
            {"id": 129, "name": "Oman", "synonyms": ["oman"], "image": "oman.png"},
            {"id": 130, "name": "Pakistan", "synonyms": ["pakistan"], "image": "pakistan.png"},
            {"id": 131, "name": "Palau", "synonyms": ["palau"], "image": "palau.png"},
            {"id": 132, "name": "Palestine", "synonyms": ["palestine"], "image": "palestine.png"},
            {"id": 133, "name": "Panama", "synonyms": ["panama"], "image": "panama.png"},
            {"id": 134, "name": "Papua New Guinea", "synonyms": ["papua new guinea"], "image": "papua_new_guinea.png"},
            {"id": 135, "name": "Paraguay", "synonyms": ["paraguay"], "image": "paraguay.png"},
            {"id": 136, "name": "Peru", "synonyms": ["peru"], "image": "peru.png"},
            {"id": 137, "name": "Philippines", "synonyms": ["philippines"], "image": "philippines.png"},
            {"id": 138, "name": "Poland", "synonyms": ["poland"], "image": "poland.png"},
            {"id": 139, "name": "Portugal", "synonyms": ["portugal"], "image": "portugal.png"},
            {"id": 140, "name": "Qatar", "synonyms": ["qatar"], "image": "qatar.png"},
            {"id": 141, "name": "Republic of the Congo", "synonyms": ["republic of the congo", "congo"], "image": "republic_of_the_congo.png"},
            {"id": 142, "name": "Romania", "synonyms": ["romania"], "image": "romania.png"},
            {"id": 143, "name": "Russia", "synonyms": ["russia"], "image": "russia.png"},
            {"id": 144, "name": "Rwanda", "synonyms": ["rwanda"], "image": "rwanda.png"},
            {"id": 145, "name": "Saint Kitts and Nevis", "synonyms": ["saint kitts and nevis"], "image": "saint_kitts_and_nevis.png"},
            {"id": 146, "name": "Saint Lucia", "synonyms": ["saint lucia"], "image": "saint_lucia.png"},
            {"id": 147, "name": "Saint Vincent and the Grenadines", "synonyms": ["saint vincent and the grenadines"], "image": "saint_vincent_and_the_grenadines.png"},
            {"id": 148, "name": "Samoa", "synonyms": ["samoa"], "image": "samoa.png"},
            {"id": 149, "name": "San Marino", "synonyms": ["san marino"], "image": "san_marino.png"},
            {"id": 150, "name": "São Tomé and Príncipe", "synonyms": ["sao tome and principe"], "image": "sao_tome_and_principe.png"},
            {"id": 151, "name": "Saudi Arabia", "synonyms": ["saudi arabia"], "image": "saudi_arabia.png"},
            {"id": 152, "name": "Senegal", "synonyms": ["senegal"], "image": "senegal.png"},
            {"id": 153, "name": "Serbia", "synonyms": ["serbia"], "image": "serbia.png"},
            {"id": 154, "name": "Seychelles", "synonyms": ["seychelles"], "image": "seychelles.png"},
            {"id": 155, "name": "Sierra Leone", "synonyms": ["sierra leone"], "image": "sierra_leone.png"},
            {"id": 156, "name": "Singapore", "synonyms": ["singapore"], "image": "singapore.png"},
            {"id": 157, "name": "Slovakia", "synonyms": ["slovakia"], "image": "slovakia.png"},
            {"id": 158, "name": "Slovenia", "synonyms": ["slovenia"], "image": "slovenia.png"},
            {"id": 159, "name": "Solomon Islands", "synonyms": ["solomon islands"], "image": "solomon_islands.png"},
            {"id": 160, "name": "Somalia", "synonyms": ["somalia"], "image": "somalia.png"},
            {"id": 161, "name": "South Africa", "synonyms": ["south africa"], "image": "south_africa.png"},
            {"id": 162, "name": "South Korea", "synonyms": ["south korea"], "image": "south_korea.png"},
            {"id": 163, "name": "South Sudan", "synonyms": ["south sudan"], "image": "south_sudan.png"},
            {"id": 164, "name": "Spain", "synonyms": ["spain"], "image": "spain.png"},
            {"id": 165, "name": "Sri Lanka", "synonyms": ["sri lanka"], "image": "sri_lanka.png"},
            {"id": 166, "name": "Sudan", "synonyms": ["sudan"], "image": "sudan.png"},
            {"id": 167, "name": "Suriname", "synonyms": ["suriname"], "image": "suriname.png"},
            {"id": 168, "name": "Sweden", "synonyms": ["sweden"], "image": "sweden.png"},
            {"id": 169, "name": "Switzerland", "synonyms": ["switzerland"], "image": "switzerland.png"},
            {"id": 170, "name": "Syria", "synonyms": ["syria"], "image": "syria.png"},
            {"id": 171, "name": "Tajikistan", "synonyms": ["tajikistan"], "image": "tajikistan.png"},
            {"id": 172, "name": "Tanzania", "synonyms": ["tanzania"], "image": "tanzania.png"},
            {"id": 173, "name": "Thailand", "synonyms": ["thailand"], "image": "thailand.png"},
            {"id": 174, "name": "Timor-Leste", "synonyms": ["timor-leste", "timor leste", "east timor"], "image": "timor-leste.png"},
            {"id": 175, "name": "Togo", "synonyms": ["togo"], "image": "togo.png"},
            {"id": 176, "name": "Tonga", "synonyms": ["tonga"], "image": "tonga.png"},
            {"id": 177, "name": "Trinidad and Tobago", "synonyms": ["trinidad and tobago"], "image": "trinidad_and_tobago.png"},
            {"id": 178, "name": "Tunisia", "synonyms": ["tunisia"], "image": "tunisia.png"},
            {"id": 179, "name": "Turkey", "synonyms": ["turkey", "turkiye"], "image": "turkey.png"},
            {"id": 180, "name": "Turkmenistan", "synonyms": ["turkmenistan"], "image": "turkmenistan.png"},
            {"id": 181, "name": "Tuvalu", "synonyms": ["tuvalu"], "image": "tuvalu.png"},
            {"id": 182, "name": "United Arab Emirates", "synonyms": ["united arab emirates", "uae"], "image": "united_arab_emirates.png"},
            {"id": 183, "name": "Uganda", "synonyms": ["uganda"], "image": "uganda.png"},
            {"id": 184, "name": "Ukraine", "synonyms": ["ukraine"], "image": "ukraine.png"},
            {"id": 185, "name": "United Kingdom", "synonyms": ["united kingdom", "uk"], "image": "united_kingdom.png"},
            {"id": 186, "name": "Uruguay", "synonyms": ["uruguay"], "image": "uruguay.png"},
            {"id": 187, "name": "United States of America", "synonyms": ["united states of america", "united states", "usa"], "image": "united_states_of_america.png"},
            {"id": 188, "name": "Uzbekistan", "synonyms": ["uzbekistan"], "image": "uzbekistan.png"},
            {"id": 189, "name": "Vanuatu", "synonyms": ["vanuatu"], "image": "vanuatu.png"},
            {"id": 190, "name": "Vatican City", "synonyms": ["vatican city", "vatican"], "image": "vatican_city.png"},
            {"id": 191, "name": "Venezuela", "synonyms": ["venezuela"], "image": "venezuela.png"},
            {"id": 192, "name": "Vietnam", "synonyms": ["vietnam"], "image": "vietnam.png"},
            {"id": 193, "name": "Yemen", "synonyms": ["yemen"], "image": "yemen.png"},
            {"id": 194, "name": "Zambia", "synonyms": ["zambia"], "image": "zambia.png"},
            {"id": 195, "name": "Zimbabwe", "synonyms": ["zimbabwe"], "image": "zimbabwe.png"}
        ]
    }, 

    "world_cup": {
        "folder": "world_cup_flags",
        "data": [
            {"id": 1, "name": "Mexico", "synonyms": ["mexico"], "image": "mexico.png"},
            {"id": 2, "name": "South Africa", "synonyms": ["africa do sul", "south africa"], "image": "south_africa.png"},
            {"id": 3, "name": "South Korea", "synonyms": ["coreia do sul", "south korea"], "image": "south_korea.png"},
            {"id": 4, "name": "Czechia", "synonyms": ["republica tcheca", "czech republic", "czechia"], "image": "czechia.png"},
            {"id": 5, "name": "Canada", "synonyms": ["canada"], "image": "canada.png"},
            {"id": 6, "name": "Bosnia and Herzegovina", "synonyms": ["bosnia and herzegovina", "bosnia", "herzegovina"], "image": "bosnia_and_herzegovina.png"},
            {"id": 7, "name": "Qatar", "synonyms": ["qatar", "catar"], "image": "qatar.png"},
            {"id": 8, "name": "Switzerland", "synonyms": ["suica", "switzerland"], "image": "switzerland.png"},
            {"id": 9, "name": "Brazil", "synonyms": ["brasil", "brazil"], "image": "brazil.png"},
            {"id": 10, "name": "Morocco", "synonyms": ["morocco"], "image": "morocco.png"},
            {"id": 11, "name": "Haiti", "synonyms": ["haiti"], "image": "haiti.png"},
            {"id": 12, "name": "Scotland", "synonyms": ["scotland"], "image": "scotland.png"},
            {"id": 13, "name": "United States of America", "synonyms": ["united states of america", "united states", "usa"], "image": "united_states_of_america.png"},
            {"id": 14, "name": "Paraguay", "synonyms": ["paraguay"], "image": "paraguay.png"},
            {"id": 15, "name": "Australia", "synonyms": ["australia"], "image": "australia.png"},
            {"id": 16, "name": "Turkey", "synonyms": ["turkey", "turkiye"], "image": "turkey.png"},
            {"id": 17, "name": "Germany", "synonyms": ["germany"], "image": "germany.png"},
            {"id": 18, "name": "Curaçao", "synonyms": ["curacao"], "image": "curacao.png"},
            {"id": 19, "name": "Cote d'Ivoire", "synonyms": ["cote divoire", "cote d'ivoire", "ivory coast"], "image": "cote_divoire.png"},
            {"id": 20, "name": "Ecuador", "synonyms": ["ecuador"], "image": "ecuador.png"},
            {"id": 21, "name": "Netherlands", "synonyms": ["netherlands"], "image": "netherlands.png"},
            {"id": 22, "name": "Japan", "synonyms": ["japan"], "image": "japan.png"},
            {"id": 23, "name": "Sweden", "synonyms": ["sweden"], "image": "sweden.png"},
            {"id": 24, "name": "Tunisia", "synonyms": ["tunisia"], "image": "tunisia.png"},
            {"id": 25, "name": "Belgium", "synonyms": ["belgium"], "image": "belgium.png"},
            {"id": 26, "name": "Egypt", "synonyms": ["egypt"], "image": "egypt.png"},
            {"id": 27, "name": "Iran", "synonyms": ["iran"], "image": "iran.png"},
            {"id": 28, "name": "New Zealand", "synonyms": ["new zealand"], "image": "new_zealand.png"},
            {"id": 29, "name": "Spain", "synonyms": ["spain"], "image": "spain.png"},
            {"id": 30, "name": "Cape Verde", "synonyms": ["cape verde"], "image": "cape_verde.png"},
            {"id": 31, "name": "Saudi Arabia", "synonyms": ["saudi arabia"], "image": "saudi_arabia.png"},
            {"id": 32, "name": "Uruguay", "synonyms": ["uruguay"], "image": "uruguay.png"},
            {"id": 33, "name": "France", "synonyms": ["france"], "image": "france.png"},
            {"id": 34, "name": "Senegal", "synonyms": ["senegal"], "image": "senegal.png"},
            {"id": 35, "name": "Iraq", "synonyms": ["iraq"], "image": "iraq.png"},
            {"id": 36, "name": "Norway", "synonyms": ["norway"], "image": "norway.png"},
            {"id": 37, "name": "Argentina", "synonyms": ["argentina"], "image": "argentina.png"},
            {"id": 38, "name": "Algeria", "synonyms": ["algeria"], "image": "algeria.png"},
            {"id": 39, "name": "Austria", "synonyms": ["austria"], "image": "austria.png"},
            {"id": 40, "name": "Jordan", "synonyms": ["jordan"], "image": "jordan.png"},
            {"id": 41, "name": "Portugal", "synonyms": ["portugal"], "image": "portugal.png"},
            {"id": 42, "name": "Democratic Republic of the Congo", "synonyms": ["democratic republic of the congo", "drc"], "image": "democratic_republic_of_the_congo.png"},
            {"id": 43, "name": "Uzbekistan", "synonyms": ["uzbekistan"], "image": "uzbekistan.png"},
            {"id": 44, "name": "Colombia", "synonyms": ["colombia"], "image": "colombia.png"},
            {"id": 45, "name": "England", "synonyms": ["england"], "image": "england.png"},
            {"id": 46, "name": "Croatia", "synonyms": ["croatia"], "image": "croatia.png"},
            {"id": 47, "name": "Ghana", "synonyms": ["ghana"], "image": "ghana.png"},
            {"id": 48, "name": "Panama", "synonyms": ["panama"], "image": "panama.png"}
        ]
    },

    "brazil_states": {
        "folder": "brazilian_states_flags",
        "data": [
            {"id": 1, "name": "Acre", "synonyms": ["acre"], "image": "acre.png"},
            {"id": 2, "name": "Alagoas", "synonyms": ["alagoas"], "image": "alagoas.png"},
            {"id": 3, "name": "Amapá", "synonyms": ["amapa"], "image": "amapa.png"},
            {"id": 4, "name": "Amazonas", "synonyms": ["amazonas"], "image": "amazonas.png"},
            {"id": 5, "name": "Bahia", "synonyms": ["bahia"], "image": "bahia.png"},
            {"id": 6, "name": "Ceará", "synonyms": ["ceara"], "image": "ceara.png"},
            {"id": 7, "name": "Distrito Federal", "synonyms": ["distrito federal"], "image": "distrito_federal.png"},
            {"id": 8, "name": "Espírito Santo", "synonyms": ["espirito santo"], "image": "espirito_santo.png"},
            {"id": 9, "name": "Goiás", "synonyms": ["goias"], "image": "goias.png"},
            {"id": 10, "name": "Maranhão", "synonyms": ["maranhao"], "image": "maranhao.png"},
            {"id": 11, "name": "Mato Grosso", "synonyms": ["mato grosso"], "image": "mato_grosso.png"},
            {"id": 12, "name": "Mato Grosso do Sul", "synonyms": ["mato grosso do sul"], "image": "mato_grosso_do_sul.png"},
            {"id": 13, "name": "Minas Gerais", "synonyms": ["minas gerais"], "image": "minas_gerais.png"},
            {"id": 14, "name": "Pará", "synonyms": ["para"], "image": "para.png"},
            {"id": 15, "name": "Paraíba", "synonyms": ["paraiba"], "image": "paraiba.png"},
            {"id": 16, "name": "Paraná", "synonyms": ["parana"], "image": "parana.png"},
            {"id": 17, "name": "Pernambuco", "synonyms": ["pernambuco"], "image": "pernambuco.png"},
            {"id": 18, "name": "Piauí", "synonyms": ["piaui"], "image": "piaui.png"},
            {"id": 19, "name": "Rio de Janeiro", "synonyms": ["rio de janeiro"], "image": "rio_de_janeiro.png"},
            {"id": 20, "name": "Rio Grande do Norte", "synonyms": ["rio grande do norte"], "image": "rio_grande_do_norte.png"},
            {"id": 21, "name": "Rio Grande do Sul", "synonyms": ["rio grande do sul"], "image": "rio_grande_do_sul.png"},
            {"id": 22, "name": "Rondônia", "synonyms": ["rondonia"], "image": "rondonia.png"},
            {"id": 23, "name": "Roraima", "synonyms": ["roraima"], "image": "roraima.png"},
            {"id": 24, "name": "Santa Catarina", "synonyms": ["santa catarina"], "image": "santa_catarina.png"},
            {"id": 25, "name": "São Paulo", "synonyms": ["sao paulo"], "image": "sao_paulo.png"},
            {"id": 26, "name": "Sergipe", "synonyms": ["sergipe"], "image": "sergipe.png"},
            {"id": 27, "name": "Tocantins", "synonyms": ["tocantins"], "image": "tocantins.png"}
        ]
    },
}


SUPPORTED_LANGS = ("en", "pt", "es")

_TERRITORIES = {lang: Locale.parse(lang).territories for lang in SUPPORTED_LANGS}

_NAME_CODE_ALIASES = {
    "the bahamas": "BS",
    "democratic republic of the congo": "CD",
    "the gambia": "GM",
    "myanmar": "MM",
    "palestine": "PS",
    "republic of the congo": "CG",
    "saint kitts and nevis": "KN",
    "saint lucia": "LC",
    "saint vincent and the grenadines": "VC",
    "turkey": "TR",
    "united states of america": "US",
}

_CUSTOM_LOCALIZED_NAMES = {
    "Bahrain": {
        "pt": ["Bahrein"],
        "es": ["Baréin"],
    },
    "Belarus": {
        "pt": ["Belarus"],
        "es": ["Belarús"],
    },
    "Democratic Republic of the Congo": {
        "pt": ["República Democrática do Congo", "Congo-Kinshasa"],
        "es": ["República Democrática del Congo", "Congo-Kinsasa"],
    },
    "England": {
        "pt": ["Inglaterra"],
        "es": ["Inglaterra"],
    },
    "Myanmar": {
        "pt": ["Myanmar", "Birmânia"],
        "es": ["Myanmar", "Birmania"],
    },
    "Palestine": {
        "pt": ["Palestina"],
        "es": ["Palestina"],
    },
    "Republic of the Congo": {
        "pt": ["República do Congo", "Congo-Brazzaville"],
        "es": ["República del Congo", "Congo-Brazzaville"],
    },
    "Saint Kitts and Nevis": {
        "pt": ["São Cristóvão e Nevis"],
        "es": ["San Cristóbal y Nieves"],
    },
    "Saint Lucia": {
        "pt": ["Santa Lúcia"],
        "es": ["Santa Lucía"],
    },
    "Saint Vincent and the Grenadines": {
        "pt": ["São Vicente e Granadinas"],
        "es": ["San Vicente y las Granadinas"],
    },
    "Scotland": {
        "pt": ["Escócia"],
        "es": ["Escocia"],
    },
    "Tajikistan": {
        "pt": ["Tajiquistão"],
        "es": ["Tayikistán"],
    },
    "The Bahamas": {
        "pt": ["Bahamas"],
        "es": ["Bahamas"],
    },
    "The Gambia": {
        "pt": ["Gâmbia"],
        "es": ["Gambia"],
    },
    "Turkey": {
        "pt": ["Turquia"],
        "es": ["Turquía"],
    },
    "United States of America": {
        "pt": ["Estados Unidos", "Estados Unidos da América"],
        "es": ["Estados Unidos", "Estados Unidos de América"],
    },
}


def _normalize_lookup(text):
    if not text:
        return ""
    normalized = "".join(
        char for char in unicodedata.normalize("NFD", text)
        if unicodedata.category(char) != "Mn"
    )
    return (
        normalized.lower()
        .replace("&", "and")
        .replace("’", "")
        .replace("'", "")
        .replace("-", " ")
        .replace(",", " ")
        .strip()
    )


_ENGLISH_TERRITORY_CODES = {
    _normalize_lookup(name): code
    for code, name in _TERRITORIES["en"].items()
}


def _dedupe(items):
    seen = set()
    result = []
    for item in items:
        value = item.strip()
        if not value:
            continue
        key = _normalize_lookup(value)
        if key in seen:
            continue
        seen.add(key)
        result.append(value)
    return result


def _localized_candidates(flag_name, lang):
    if lang == "en":
        return [flag_name]

    custom = _CUSTOM_LOCALIZED_NAMES.get(flag_name, {}).get(lang)
    if custom:
        return custom

    territory_code = _ENGLISH_TERRITORY_CODES.get(_normalize_lookup(flag_name))
    if territory_code is None:
        territory_code = _NAME_CODE_ALIASES.get(_normalize_lookup(flag_name))

    if territory_code is None:
        return [flag_name]

    translated = _TERRITORIES[lang].get(territory_code)
    return [translated] if translated else [flag_name]


def get_display_name(flag, lang):
    localized = flag.get(f"synonyms_{lang}", [])
    if localized:
        return localized[0]
    return flag["name"]


def get_synonyms_for_language(flag, lang):
    language = lang if lang in SUPPORTED_LANGS else "en"
    return flag.get(f"synonyms_{language}", [flag["name"]])


def _localize_flag_sets():
    for set_data in FLAG_SETS.values():
        for flag in set_data["data"]:
            base_synonyms = flag.pop("synonyms", [])

            for lang in SUPPORTED_LANGS:
                localized_names = _localized_candidates(flag["name"], lang)
                flag[f"synonyms_{lang}"] = _dedupe(
                    [*localized_names, *base_synonyms, flag["name"]]
                )


_localize_flag_sets()
