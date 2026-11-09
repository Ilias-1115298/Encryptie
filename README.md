# Encryptie applicatie

### Inleiding
Voor het vak Security & Cyberwarfare heb ik een programma gemaakt waarmee je tekst kun versleutelen en weer kunt ontsleutelen. Met deze heb ik geleerd hoe symmetrische encryptie werkt en hoe je gegevens kunt beveiligen door gebruik te maken van een geheime sleutel. 

Voor het maken van deze applicatie heb ik Python gebruikt. Daarnaast heb ik voor de gebruikersinterface gebruik gemaakt van Tkinter. Ik heb daarnaast ook gebruik gemaakt van de cryptography library voor het versleutelen en ontsleutelen van de tekst. 


### Hoe werkt de applicatie?
De gebruiker heeft een eenvoudige gebruikersinterface die ik heb gemaakt met Tkinter. De gebruiker kan een bericht invoeren en vervolgens kiezen om het bericht te versleutelen of weer te ontsleutelen.

Als de gebruiker op de knop 'Versleutelen' klikt, wordt de tekst omgezet naar een onleesbare bericht. En wanneer de gebruiker op 'Ontsleutelen' klikt, dan wordt de tekst weer omgezet naar de originele tekst.

Ik heb getest of een versleuteld bericht nog steeds kon worden ontsleuteld nadat de applicatie was afgesloten en opnieuw was gestart. Dit werkte goed, omdat dezelfde geheime sleutel opnieuw wordt gebruikt. 


### Encryptiemethode 
De applicatie maakt gebruik van symmetrische encryptie. Dit betekent dat dezelfde geheime sleutel wordt gebruikt om tekts te versleutelen en te ontsleutelen.

Voor de encryptie is de Python-library cryptography gebruikt met de methode Fernet. Fernet gebruikt AES-128 in CBC-modus om gegevens te versleutelen. Ik heb voor Fernet gekozen omdat het een bestaande en goed geteste oplossing is. Fernet gebruikt HMAC-SHA256 om te controleren of de versleutelde gegevens niet zijn aangepast.


### Sleutelbeheer
Voor het sleutelbeheer heb ik sleutelbeheer.py gemaakt. De applicatie controleert of secret.key al bestaat. Als dit niet zo is, wordt er een nieuwe sleutel aangemaakt en opgeslagen. Anders wordt de bestaande sleutel gebruikt.

De sleutel wordt alleen lokaal opgeslagen en niet met andere gebruikers gedeeld. Hierdoor is de applicatie vooral bedoeld om op dezelfde computer teksten te verstleutelen en te ontsleutelen

Ik heb secret.key toegevoegd aan .gitignore, zodat deze niet op GitHub komt.

Een nadeel is dat de sleutel geen extra beveiliging heeft. Als iemand toegang krijgt tot het bestand, kan diegene ook de berichten ontsleutelen. Bij een grotere applicatie met meerdere gebruikers zou het sleutelbeheer wel beter beveiligd moeten worden

### Kerckhoff's Principe
Kerckhoff's Principe houdt in dat een encryptiesysteem veilig moet blijven, zelfs als anderen weten hoe het systeem werkt. Alleen de geheime sleutel moet geheim blijven. 

De applicatie sluit hierbij aan, omdat ik Fernet gebruik. Fernet is openbaar, maar zonder de juiste sleutel kunnen de versleutelde berichten niet worden ontsleuteld.


### Installatie en gebruik
Om de applicatie te gebruiken moet Python geïnstalleerd zijn.
- Installeer de cryptography library:
  - pip install cryptography
- Start de applicatie:
  - run het bestand interface.py

De applicatie is opgestart. 
1. Voer een tekst in die je wilt versleutelen
2. Klik op 'Versleutelen' om de tekst te versleutelen
3. Kopieer de versleutelde tekst naar het invoerveld
4. Klik op 'Ontsleutelen' om de oorspronkelijke tekst terug te krijgen


### Bronnen
- DJ Oamen. (2023, August 17). How to Create Encryption and Decryption App  with Tkinter in Python [Video]. YouTube. https://www.youtube.com/watch?v=9To1hvQh9ME
- Team, E. (2026, July 16). Wat is symmetrische encryptie? | Encryptie Consulting. Encryption Consulting LLC. https://www.encryptionconsulting.com/nl/education-center/what-is-symmetric-encryption/
- Noah Does Coding. (2025, June 9). Fernet in Python: Encrypt & Decrypt Files (Beginner Tutorial) [Video]. YouTube. https://www.youtube.com/watch?v=6iwb8ynRM-A
- Team, E. (2026b, July 22). Symmetrische en asymmetrische encryptie | Welke is beter? Encryption Consulting LLC. https://www.encryptionconsulting.com/nl/education-center/symmetric-vs-asymmetric-encryption/
- AxCrypt. (n.d.). Symmetrische versus Asymmetrische Versleuteling: Belangrijkste Verschillen Uitgelegd. https://axcrypt.net/nl/blog/symmetric-vs-asymmetric-encryption/
- Turtle Code. (2025, November 13). Python Encryption Tutorial: How to Encrypt & Decrypt Data with cryptography Fernet [Video]. YouTube. https://www.youtube.com/watch?v=es_5TMQc-Bk
- CDVI Benelux. (2026b, March 4). Wat is AES-encryptie en hoe werkt het? | CDVI Benelux. https://www.cdvibenelux.com/nl/wat-is-aes-encryptie-en-hoe-werkt-het/
- Pereira, S., & Pereira, S. (2023b, September 14). Wat houdt het principe van Kerckhoff in? EITCA Academy. https://nl.eitca.org/internetveiligheid/eitc-is-ccf-klassieke-cryptografie-fundamentals/geschiedenis-van-cryptografie/modulaire-rekenkundige-en-historische-cijfers/Het-kerckhoffss-principe-stelt-dat-cryptosystemen-veilig-moeten-zijn%2C-zelfs-als-alleen-de-decoderingssleutel-geheim-wordt-gehouden/
