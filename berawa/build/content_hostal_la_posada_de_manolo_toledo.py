# Contenido de la demo La Posada de Manolo (Toledo) (es/en/fr/de). Hechos de laposadademanolo.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones; sin precios (su pagina de habitaciones tiene una cifra «desde» incoherente, no se usa ninguna).
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran la posada real.','en':' Images are illustrations and do not show the actual inn.','fr':' Les images sont des illustrations et ne montrent pas l’auberge réelle.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Gasthaus.'}
H={'es':['Doble Pequeña y Dobles Estándar','Doble Confort y Superior con Patio'],'en':['Small Double and Standard Doubles','Comfort Double and Superior with Patio'],'fr':['Petite Double et Doubles Standard','Double Confort et Supérieure avec Patio'],'de':['Kleines Doppelzimmer und Standard-Doppelzimmer','Komfort-Doppelzimmer und Superior mit Patio']}
RD={
'es':['Interiores y tranquilas, con luz del patio toledano, o exteriores con un pequeño balcón a la calle y decoración temática.','Las más amplias, con vigas de madera y balcón, y la Superior con Patio, con techo de artesonado, para uso doble o triple.'],
'en':['Quiet interior rooms lit from the Toledo-style patio, or exterior rooms with a small balcony onto the street and themed decor.','The most spacious rooms, with wooden beams and a balcony, and the Superior with Patio, with a coffered ceiling, for double or triple use.'],
'fr':['Intérieures et calmes, éclairées par le patio tolédan, ou extérieures avec un petit balcon sur rue et une décoration thématique.','Les plus spacieuses, avec poutres en bois et balcon, et la Supérieure avec Patio, au plafond à caissons, pour un usage double ou triple.'],
'de':['Ruhige Innenzimmer mit Licht vom toledanischen Patio oder Außenzimmer mit kleinem Balkon zur Straße und thematischer Einrichtung.','Die geräumigsten Zimmer mit Holzbalken und Balkon sowie das Superior mit Patio mit Kassettendecke, für zwei oder drei Personen.']}
ART={
'hero':('arches',9981,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'intro':('columns',9982,['#f2ece2','#faf6ee','#8a5a2e','#6e4622','#3a2410']),
'r1':('arches',9991,['#f0e9de','#c99350','#8a5a2e','#6e4622','#3a2410']),
'r2':('skyline',9992,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a']),
'g1':('skyline',9993,['#2b1d14','#d9a35a','#f1d29a','#8a5a2e','#6e4622','#3a2410']),
'g2':('arches',9994,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g3':('hills',9995,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c']),
'g4':('columns',9996,['#2b1d14','#e0aa64','#f4d7a6','#9a6a3e','#7a5230','#40281a'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='La Posada de Manolo · Posada familiar junto a la Catedral de Toledo',see_rooms='Ver las habitaciones',hero_k='Toledo · Calle Sixto Ramón Parro 8',hero_t='Como en casa, en el corazón de Toledo',hero_s='Una casa familiar del siglo XV al lado de la Catedral.',
 intro_t='Una historia de familia',intro_p1='En 1979 Manuel Sánchez Nieto compró esta casa con más de quinientos años de historia. En 2001 su familia cumplió su sueño y abrió La Posada de Manolo como homenaje a él.',
 intro_p2='Manolo y Almudena, pareja en el trabajo y en la vida, dejaron la veterinaria para recibir a sus huéspedes. Las habitaciones se reparten en tres plantas, Judía, Cristiana y Árabe, decoradas con los oficios de las tres culturas.',
 stats=['Casa del siglo XV','2 minutos de la Catedral','Desayuno buffet','Terraza con vistas'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Todas con calefacción, aire acondicionado en verano, TV, baño privado con ducha y wifi gratuito.',
 svcs=['Desayuno buffet','Terraza con vistas a la Catedral','Libros Viajeros','Guardaequipaje','Información turística','Garaje para moto y bicicleta'],
 around_s='A 2 minutos de la Catedral, 7 de Zocodover, 8 del Alcázar y 16 de San Juan de los Reyes, a pie.',
 loc_p='Calle Sixto Ramón Parro 8 · 45001 Toledo, al lado de la Catedral. Check-in de 14:00 a 17:00 h; check-out hasta las 11:00 h.',
 chips=['¿Qué habitaciones tenéis?','¿Hay desayuno?','¿Dónde aparco?','¿Cómo reservo?']),
'en':dict(title='La Posada de Manolo · Family inn next to Toledo Cathedral',see_rooms='See the rooms',hero_k='Toledo · Calle Sixto Ramón Parro 8',hero_t='At home in the heart of Toledo',hero_s='A 15th-century family house next to the Cathedral.',
 intro_t='A family story',intro_p1='In 1979 Manuel Sánchez Nieto bought this house with over five hundred years of history. In 2001 his family fulfilled his dream and opened La Posada de Manolo in his honour.',
 intro_p2='Manolo and Almudena, partners in work and life, left veterinary medicine to welcome guests. The rooms are spread over three floors, Jewish, Christian and Arab, decorated with the trades of the three cultures.',
 stats=['15th-century house','2 minutes from the Cathedral','Breakfast buffet','Terrace with views'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='All with heating, air conditioning in summer, TV, private bathroom with shower and free wifi.',
 svcs=['Breakfast buffet','Terrace with Cathedral views','Travelling books','Luggage storage','Tourist information','Motorbike and bicycle garage'],
 around_s='2 minutes from the Cathedral, 7 from Zocodover, 8 from the Alcázar and 16 from San Juan de los Reyes, on foot.',
 loc_p='Calle Sixto Ramón Parro 8 · 45001 Toledo, next to the Cathedral. Check-in 14:00 to 17:00; check-out until 11:00.',
 chips=['Which rooms do you have?','Is there breakfast?','Where can I park?','How do I book?']),
'fr':dict(title='La Posada de Manolo · Auberge familiale près de la cathédrale de Tolède',see_rooms='Voir les chambres',hero_k='Tolède · Calle Sixto Ramón Parro 8',hero_t='Comme à la maison, au cœur de Tolède',hero_s='Une maison familiale du XVe siècle à côté de la cathédrale.',
 intro_t='Une histoire de famille',intro_p1='En 1979, Manuel Sánchez Nieto a acheté cette maison riche de plus de cinq cents ans d’histoire. En 2001, sa famille a réalisé son rêve et ouvert La Posada de Manolo en son hommage.',
 intro_p2='Manolo et Almudena, couple au travail comme dans la vie, ont quitté la médecine vétérinaire pour accueillir leurs hôtes. Les chambres sont réparties sur trois étages, juif, chrétien et arabe, décorés avec les métiers des trois cultures.',
 stats=['Maison du XVe siècle','2 minutes de la cathédrale','Petit-déjeuner buffet','Terrasse avec vue'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Toutes avec chauffage, climatisation en été, TV, salle de bain privée avec douche et wifi gratuit.',
 svcs=['Petit-déjeuner buffet','Terrasse avec vue sur la cathédrale','Livres voyageurs','Bagagerie','Information touristique','Garage pour moto et vélo'],
 around_s='À 2 minutes de la cathédrale, 7 de Zocodover, 8 de l’Alcázar et 16 de San Juan de los Reyes, à pied.',
 loc_p='Calle Sixto Ramón Parro 8 · 45001 Tolède, à côté de la cathédrale. Arrivée de 14:00 à 17:00 ; départ jusqu’à 11:00.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un petit-déjeuner ?','Où me garer ?','Comment réserver ?']),
'de':dict(title='La Posada de Manolo · Familiengasthaus neben der Kathedrale von Toledo',see_rooms='Zimmer ansehen',hero_k='Toledo · Calle Sixto Ramón Parro 8',hero_t='Wie zu Hause, im Herzen von Toledo',hero_s='Ein Familienhaus aus dem 15. Jahrhundert neben der Kathedrale.',
 intro_t='Eine Familiengeschichte',intro_p1='1979 kaufte Manuel Sánchez Nieto dieses Haus mit über fünfhundert Jahren Geschichte. 2001 erfüllte seine Familie seinen Traum und eröffnete ihm zu Ehren La Posada de Manolo.',
 intro_p2='Manolo und Almudena, Paar im Beruf und im Leben, gaben die Tiermedizin auf, um Gäste zu empfangen. Die Zimmer verteilen sich auf drei Etagen, jüdisch, christlich und arabisch, geschmückt mit den Handwerken der drei Kulturen.',
 stats=['Haus aus dem 15. Jh.','2 Minuten zur Kathedrale','Frühstücksbuffet','Terrasse mit Aussicht'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Alle mit Heizung, Klimaanlage im Sommer, TV, eigenem Bad mit Dusche und kostenlosem WLAN.',
 svcs=['Frühstücksbuffet','Terrasse mit Blick auf die Kathedrale','Reisebücher','Gepäckaufbewahrung','Touristeninformation','Garage für Motorrad und Fahrrad'],
 around_s='2 Minuten zur Kathedrale, 7 zur Zocodover, 8 zum Alcázar und 16 nach San Juan de los Reyes, zu Fuß.',
 loc_p='Calle Sixto Ramón Parro 8 · 45001 Toledo, neben der Kathedrale. Check-in 14:00 bis 17:00 Uhr; Check-out bis 11:00 Uhr.',
 chips=['Welche Zimmer gibt es?','Gibt es Frühstück?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RE='https://www.laposadademanolo.com/bookingstep1/?idHotel=100121343';REN='https://www.laposadademanolo.com/en/bookingstep1/?idHotel=100121343';RFR='https://www.laposadademanolo.com/fr/bookingstep1/?idHotel=100121343'
BOOK=dict(mode='engine',url=dict(es=RE,en=REN,fr=RFR,de=REN))
D=dict(name='La Posada de Manolo',ac='#2b1d14',ac2='#8a5a2e',ac2_a11y='#6e4622',book=BOOK,around=['Catedral de Toledo','Plaza de Zocodover'],foot=FOOT,
 address='Calle Sixto Ramón Parro 8 · 45001 Toledo',phones=['+34 925 25 89 85'],emails=['toledo@laposadademanolo.com'],maps='La Posada de Manolo, Calle Sixto Ramón Parro 8, 45001 Toledo',t=T)
META=dict(repo='demo-hostal-la-posada-de-manolo-toledo',name='La Posada de Manolo',legal_name='Hostal La Posada de Manolo S.L. (aviso legal de su web)',registry_ids=['B45483922'],
 url='https://www.laposadademanolo.com/',domain='laposadademanolo.com',municipality='Toledo',province='Toledo',sector='posada familiar en una casa del siglo XV junto a la Catedral de Toledo',
 read_at='2026-10-30T11:14:00+01:00',created_at='2026-10-30T11:13:00+01:00',built_at='2026-10-30T11:30:00+01:00',audit_date='2026-10-30T11:06:44+01:00',
 rating=dict(value=4.7,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/La+Posada+de+Manolo+Toledo'),
 book=dict(mode='engine',url=RE,note='motor de reservas real de su web (Mirai, página bookingstep1 con idHotel 100121343; versiones /en/ y /fr/), HTTP 200 comprobado el 30/10/2026; su web no tiene alemán: de usa la versión inglesa.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay desayuno?','K02'),('¿Dónde aparco?','K03'),('¿A qué hora es el check-in?','K04'),('¿Admitís mascotas?','K05'),('¿Dónde está la posada?','K06'),('¿Qué hay cerca?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay terraza?','K09'),('¿Qué son los libros viajeros?','K10'),('¿Hay wifi?','K11'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there breakfast?','K02'),('Where can I park?','K03'),('What time is check-in?','K04'),('Do you accept pets?','K05'),('Where is the inn?','K06'),('What is nearby?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there a terrace?','K09'),('What are the travelling books?','K10'),('Is there wifi?','K11'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il un petit-déjeuner ?','K02'),('Où me garer ?','K03'),('À quelle heure est l’arrivée ?','K04'),('Acceptez-vous les animaux ?','K05'),('Où se trouve l’auberge ?','K06'),('Qu’y a-t-il à proximité ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il une terrasse ?','K09'),('Que sont les livres voyageurs ?','K10'),('Y a-t-il le wifi ?','K11'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es Frühstück?','K02'),('Wo kann ich parken?','K03'),('Wann ist der Check-in?','K04'),('Sind Haustiere erlaubt?','K05'),('Wo liegt das Gasthaus?','K06'),('Was gibt es in der Nähe?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es eine Terrasse?','K09'),('Was sind die Reisebücher?','K10'),('Gibt es WLAN?','K11'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
