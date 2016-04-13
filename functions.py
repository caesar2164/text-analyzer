import sys

def generate_tables(definitions_file, text_lines_to_analyze):
    power_diff_table = []
    binary_power_diff_table = []
    connection_table = []
    attribute_table = []
    person_table = []

    print '\nCounting times names appear in text file...'
    # iterate through each person in name file
    for person in definitions_file:
        latin_dict = definitions_file[person].get('latin', False)
        position = definitions_file[person].get('position', False)
        lines = []

        # only do stuff if they have latin names defined and are NOT a diissident
        if latin_dict and position and position != 'Dissident':
            # iterate through analysis text lines and see if name is there
            for index, line in enumerate(text_lines_to_analyze):

                for latin_item in latin_dict:
                    latin_name = ""
                    weight = 1

                    # check format of
                    if isinstance(latin_item, dict):
                        for declension, latin_text in latin_item.items():
                            latin_name = latin_text

                            # add in weights
                            if declension == 'nominative':
                                weight = 3
                            elif declension == 'genitive':
                                weight = 3
                            elif declension == 'dative':
                                weight = 2
                            elif declension == 'ablative':
                                weight = 2
                            elif declension == 'accusative':
                                weight = 1
                    else:
                        latin_name = latin_item

                    # lowercasing both the key string and the line of text to maximize matches
                    if line.lower().find(latin_name.lower()) != -1:
                        lines.append([index, weight])

            person_attributes = [person, lines, position]
            person_table.append(person_attributes)

            print('.'),

    print '\n\nCalculating relationship power differentials and connections...'
    title_vector = [None]
    
    for person in person_table:
        person_name = person[0]
        person_mentions = person[1]
        person_position = person[2]

        power_vector = list(person_table)
        binary_power_vector = list(person_table)
        relationship_vector = list(person_table)
        connection_vector = list(person_table)
        attribute_vector = [person_name]
        title_vector.append(person_name)

        for index, relationship in enumerate(relationship_vector):
            relationship_name = relationship[0]
            relationship_mentions = relationship[1]

            num_person_mentions = 0
            num_weighted_person_mentions = 0
            num_connections = 0

            if relationship_name == person_name:
                power_vector[index] = 0
                binary_power_vector[index] = 0
                num_connections = 0
            else:
                for person_mention in person_mentions:
                    mention_weight = person_mention[1]
                    num_person_mentions += 1
                    num_weighted_person_mentions += mention_weight

                    num_relationship_mentions = 0
                    num_weighted_relationship_mentions = 0

                    for relationship_mention in relationship_mentions:
                        relationship_mention_weight = relationship_mention[1]
                        num_relationship_mentions += 1
                        num_weighted_relationship_mentions += relationship_mention_weight

                        if relationship_mention[0] == person_mention[0]:
                            num_connections = 1

                power_differential = num_weighted_person_mentions - num_weighted_relationship_mentions
                if power_differential > 0:
                    power_vector[index] = 2 * power_differential
                    binary_power_vector[index] = 1
                else:
                    power_vector[index] = 0
                    binary_power_vector[index] = 0

            connection_vector[index] = num_connections

        attribute_vector.append(num_person_mentions)
        attribute_vector.append(num_weighted_person_mentions)
        attribute_vector.append(person_position)
        power_vector.insert(0, person_name)
        binary_power_vector.insert(0, person_name)
        connection_vector.insert(0, person_name)

        attribute_table.append(attribute_vector)
        power_diff_table.append(power_vector)
        binary_power_diff_table.append(binary_power_vector)
        connection_table.append(connection_vector)
        
        print('.'),

    power_diff_table.insert(0, title_vector)
    binary_power_diff_table.insert(0, title_vector)
    connection_table.insert(0, title_vector)
    attribute_table.insert(0, ['Person Name', '# Mentions', '# Weighted Mentions', 'Position'])

    return power_diff_table, binary_power_diff_table, connection_table, attribute_table
