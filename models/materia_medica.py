from config.database import get_db_connection

class MateriamedDatabaseSetup:
    """Setup and manage Materia Medica database"""
    
    @staticmethod
    def init_materia_medica():
        """Initialize Materia Medica table with homeopathic medicines"""
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create Materia Medica table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS materia_medica (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                medicine_name TEXT NOT NULL UNIQUE,
                common_name TEXT,
                potencies TEXT,
                dosage_recommendation TEXT,
                indications TEXT,
                keynote_symptoms TEXT,
                mental_state TEXT,
                physical_symptoms TEXT,
                modalities TEXT,
                contraindications TEXT,
                interactions TEXT,
                side_effects TEXT,
                complementary_medicines TEXT,
                incompatible_medicines TEXT,
                constitutional_type TEXT,
                temperature_preference TEXT,
                relations TEXT,
                source TEXT,
                remarks TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        
        # Check if data already exists
        cursor.execute('SELECT COUNT(*) as count FROM materia_medica')
        result = cursor.fetchone()
        
        if result['count'] == 0:
            # Insert comprehensive Materia Medica data
            MateriamedDatabaseSetup.populate_materia_medica_data(cursor, conn)
        
        conn.close()
    
    @staticmethod
    def populate_materia_medica_data(cursor, conn):
        """Populate Materia Medica with homeopathic medicines data"""
        
        medicines_data = [
            # Arnica Montana
            (
                'Arnica Montana',
                'Leopard\'s Bane',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets thrice daily or as directed',
                'Trauma, bruises, soreness, shock, falls, injuries',
                'Shock from injuries | Black and blue spots | Soreness of body | Fear of being touched',
                'Anxiety about illness | Desire to be left alone | Irritability | Fear of death',
                'Sensation of soreness and bruising | Black and blue discoloration | Muscle aches | Pains from blows',
                'Better: Lying down | Worse: Touch, motion, pressure',
                'None known',
                'None known',
                'Rare: Skin irritation on external use',
                'Calendula, Hypericum',
                'None known',
                'Traumatic constitution',
                'Not specific',
                'Follows well after: Aconite | Followed well by: Calendula',
                'Mountain plant - Compositae family',
                'Most effective immediately after injury',
            ),
            # Belladonna
            (
                'Belladonna',
                'Deadly Nightshade',
                '6C, 12C, 30C, 200C, 1M, CM',
                '2-3 tablets every 2-3 hours in acute cases',
                'Fever, inflammation, acute conditions, throbbing pain, congestion',
                'Sudden onset | Violent symptoms | Dilated pupils | Flushed face | Throbbing pain',
                'Delirium | Restlessness | Fear | Violent behavior | Confusion',
                'Burning heat | Flushed face | Dilated pupils | Throbbing sensation | Red skin',
                'Better: Rest, dark room | Worse: Light, noise, touch, motion',
                'Use with caution in severe cases',
                'None known',
                'None known',
                'Aconite, Calcarea, Mercurius',
                'Alcohol based preparations',
                'Sanguine, plethoric',
                'Likes heat | Aversion to cold',
                'Antidotes: Camphor, Coffee | Followed by: Calcarea, Hepar',
                'Solanaceae family - Poisonous plant',
                'One of the most important acute remedy',
            ),
            # Bryonia Alba
            (
                'Bryonia Alba',
                'Wild Hops, White Bryony',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Headaches, cough, constipation, rheumatism, abdominal pain',
                'Stitching pain on motion | Dryness of mucous membranes | Irritability | Wants to be quiet',
                'Irritable, wants to be left alone | Fears poverty | Anxious about business',
                'Dry mucous membranes | Constipation | Stitching pains | Burning sensations',
                'Worse: Motion, warmth, pressure | Better: Rest, cold, lying on painful side',
                'Use cautiously in pregnancy',
                'None known',
                'Possible gastrointestinal irritation',
                'Aconite, Calcarea, Phosphorus',
                'Alcohol',
                'Bilious temperament',
                'Prefers cold | Thirsty',
                'Follows: Aconite, Belladonna | Followed by: Rhus tox',
                'Cucurbitaceae family',
                'Excellent for delayed recovery',
            ),
            # Calcarea Carbonica
            (
                'Calcarea Carbonica',
                'Calcium Carbonate',
                '6C, 12C, 30C, 200C, 1M, 10M',
                '2 tablets 2-3 times daily or higher potencies as single dose',
                'Weakness, delayed development, obesity, bone diseases, profuse sweating',
                'Chilliness | Profuse sweating | Sour odor | Slow metabolism | Pale, clammy skin',
                'Anxiety, especially about health | Fearful | Aversion to work | Dull, slow comprehension',
                'Slow digestion | Tendency to obesity | Enlarged abdomen | Cold extremities | Night sweats',
                'Better: Lying down | Worse: Damp, exertion, climbing, cold, pressure of clothes',
                'Not for acute conditions',
                'Avoid with Phosphorus',
                'Well-tolerated',
                'Followed by: Silica, Sulphur | Complementary: Lycopodium',
                'Lachesis, Mercury',
                'Lymphatic, scrofulous type',
                'Chilly person | Aversion to cold | Craves sweets and eggs',
                'Antidoted by: Nit-acid | Follows: Many remedies | Deep acting',
                'Mineral origin - Oyster shell',
                'Constitutional remedy - requires careful case management',
            ),
            # Lycopodium Clavatum
            (
                'Lycopodium Clavatum',
                'Club Moss, Stag\'s Horn Moss',
                '6C, 12C, 30C, 200C, 1M, 10M, CM',
                '2-3 tablets 2-3 times daily or as constitutional dose',
                'Digestive disorders, liver complaints, impotence, hair loss, respiratory issues',
                'Bloating and fullness after small meals | Flatulence | Right-sided symptoms | Weak at 4-8 PM',
                'Loss of confidence | Fear of failure | Desire to be admired | Melancholy | Inability to concentrate',
                'Bloated abdomen | Excessive gas | Constipation with hard stool | Liver problems | Baldness',
                'Better: Motion, heat, warm drinks | Worse: Pressure, 4-8 PM, cold, mental exertion',
                'Constitutional remedy - requires supervision',
                'Avoid strong coffee',
                'Generally well-tolerated',
                'Followed by: Sulphur, Calcarea',
                'Alcohol',
                'Thin, lean, dyspeptic',
                'Prefers heat | Dislikes cold | Craves sweets',
                'Deep-acting remedy | Follows well after: Pulsatilla',
                'Plant origin - Lycopodiaceae family',
                'Often called the remedy of worn-out mind and body',
            ),
            # Nux Vomica
            (
                'Nux Vomica',
                'Poison Nut',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Constipation, digestive disorders, insomnia, hangover, stress, back pain',
                'Constipation with urging but incomplete evacuation | Chilly | Irritable | Oversensitive',
                'Extremely irritable | Impatient | Hypersensitive to smells, sounds | Ambitious | Cannot tolerate failure',
                'Constipation | Indigestion | Retching | Backache | Insomnia (falls asleep late, wakes early)',
                'Better: After vomiting, rest, warm room | Worse: Cold, stress, spices, alcohol, early morning',
                'Not for prolonged use',
                'Avoid alcohol, coffee, spices',
                'Generally safe in recommended doses',
                'Followed by: Sulphur, Sepia, Thuja',
                'Alcohol, other strong substances',
                'Choleric, irritable temperament',
                'Dislikes cold | Chilly | Craves strong foods',
                'Antidoted by: Alcohol, Coffee | Antidote to: Many poisons',
                'Loganiaceae family - Poisonous seed',
                'Excellent for type A personalities and office workers',
            ),
            # Phosphorus
            (
                'Phosphorus',
                'Phosphorus',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Hemorrhage, respiratory issues, anxiety, sensory disturbances, tuberculosis',
                'Bleeding tendencies (nosebleed, hemoptysis) | Right-sided symptoms | Burning pain | Thirst for cold water',
                'Anxiety, sympathetic | Sensitive to impressions | Clairvoyance tendency | Fear of thunderstorms',
                'Burning sensations | Hoarseness | Hemorrhagic tendency | Trembling | Burning thirst for cold water',
                'Better: Cold food/drink, massage, company | Worse: Warmth, lie on left side, at twilight',
                'Constitutional remedy - careful prescribing needed',
                'Avoid Calcarea, Mercury',
                'Side effects possible with overuse',
                'Followed by: Sulphur, Sepia',
                'Alcohol',
                'Tall, thin, sensitive type',
                'Craves cold drinks and salt',
                'Deep-acting remedy | Follows many remedies',
                'Mineral substance - burn phosphorus',
                'Important remedy for hemorrhage and respiratory conditions',
            ),
            # Pulsatilla Nigricans
            (
                'Pulsatilla Nigricans',
                'Wind Flower, Pasque Flower',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Menstrual disorders, cough, indigestion, emotional sensitivity, rheumatism',
                'Changeable symptoms | Weeping mood | Mildness | Thirstlessness despite dryness | Absence of thirst',
                'Emotional, weeping, mild, timid | Craves sympathy | Aversion to heat | Sensitive to contradiction',
                'Variable symptoms | Dry mouth without thirst | Soft stools | Scanty menses | Flatulence',
                'Better: Open air, cold, gentle motion | Worse: Heat, stuffy rooms, rich food, evening',
                'Safe remedy for emotional and female conditions',
                'Avoid strong smells',
                'Generally well-tolerated',
                'Followed by: Sepia, Sulphur',
                'Coffee reduces potency',
                'Mild, timid, sensitive, emotional type - Female remedy',
                'Craves open air | Dislikes heat',
                'Antidoted by: Camphor, Coffee | Follows: Many remedies',
                'Plant origin - Ranunculaceae family',
                'Often called woman\'s remedy',
            ),
            # Sulphur
            (
                'Sulphur',
                'Sulphur',
                '6C, 12C, 30C, 200C, 1M, 10M, CM',
                '2-3 tablets 2-3 times daily or constitutional dose',
                'Skin diseases, respiratory issues, digestion, chronic illness, constitutional treatment',
                'Burning sensations | Offensive discharges | Lack of vital heat | Red orifices | Skin eruptions',
                'Indifferent | Forgetful | Difficulty in concentration | Procrastination | Philosophy mood',
                'Burning sensations all over | Itching | Unclean appearance | Foul smell | Skin conditions',
                'Better: Dry weather, motion | Worse: Bathing, warmth, 11 AM, rest',
                'Deep-acting remedy - requires professional supervision',
                'Avoid Camphor',
                'May cause temporary aggravation',
                'Followed by: Calcarea, Lycopodium, Thuja',
                'Mercury, Alcohol',
                'Thin, lank, seemingly unhealthy',
                'Dislikes heat | Loves dirty, warm surroundings | Craves sweets',
                'One of the deepest acting remedies | Kingpost of homoeopathy',
                'Non-metallic substance - Burns in air',
                'Excellent antipsoric remedy',
            ),
            # Thuja Occidentalis
            (
                'Thuja Occidentalis',
                'Arbor Vitae, White Cedar',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Warts, immunological disorders, vaccination effects, skin growths, tinnitus',
                'Warts and abnormal growths | Fixed ideas | Sensation of expansion | Coldness of left side | Suppressions',
                'Paranoid ideas (thinks she is made of glass) | Fixed ideas | Mistrustful | Desire to escape',
                'Warts, papillomas | Skin growths | Perspiration onefront of body | Offensive smell | Trembling',
                'Better: Lying on right side, after discharge | Worse: Damp, cold, morning, 3 PM, bathing, left side',
                'Constitutional remedy - careful prescribing',
                'Avoid Mercury',
                'Generally safe in recommended doses',
                'Followed by: Sulphur, Nitric acid',
                'Mercury, Camphor',
                'Thin, flabby, unhealthy type',
                'Chilly | Craves coffee, onions | Dislikes fat',
                'Antidote to: Vaccinations | Follows well after many remedies',
                'Plant origin - Cupressaceae family',
                'Important nosode remedy',
            ),
            # Hepar Sulphuris Calcareum
            (
                'Hepar Sulphuris Calcareum',
                'Calcium Sulphide',
                '6C, 12C, 30C, 200C, 1M',
                '2-3 tablets 3-4 times daily',
                'Suppurating conditions, hypersensitivity to cold, skin infections, cough',
                'Extreme hypersensitivity | Disposition to suppurate | Splinter sensation | Chilly',
                'Irritable, fault-finding | Sensitive to slightest pain | Weeping, whining',
                'Offensive discharges | Oozing from ears | Skin abscesses | Desire for strong foods (salt, fat)',
                'Better: Warmth, damp weather, wrapping up | Worse: Cold air, dry wind, slightest draft',
                'Constitutional remedy for skin conditions',
                'Avoid Camphor',
                'May cause temporary aggravation',
                'Followed by: Silica, Sulphur',
                'Camphor, Mercury',
                'Scrofulous, unhealthy type',
                'Very chilly | Craves fat and salt',
                'Antidoted by: Camphor, Coffee, Bell | Bridging remedy between remedies',
                'Compound preparation - Calcium Sulphide',
                'Important for chronic suppurative conditions',
            ),
        ]
        
        for medicine in medicines_data:
            try:
                cursor.execute('''
                    INSERT INTO materia_medica 
                    (medicine_name, common_name, potencies, dosage_recommendation, indications, 
                     keynote_symptoms, mental_state, physical_symptoms, modalities, 
                     contraindications, interactions, side_effects, complementary_medicines, 
                     incompatible_medicines, constitutional_type, temperature_preference, 
                     relations, source, remarks)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', medicine)
            except Exception as e:
                print(f"Error inserting {medicine[0]}: {str(e)}")
        
        conn.commit()
        print("Materia Medica database populated successfully!")
