from lxml import etree

def extract_text_with_inlines(element):
<<<<<<< HEAD
    text_parts = []
    if element.text:
        text_parts.append(element.text.strip())
    for child in element:
        if child.tag.endswith('Citation'):
            citation_text = f"{child.text.strip()} ({child.attrib.get('Number')})" if child.text else ""
            text_parts.append(citation_text)
        elif child.tag.endswith('Term'):
            text_parts.append(f"'{child.text.strip()}'")
        else:
            text_parts.append(extract_text_with_inlines(child))
=======
    """Recursively extracts text content from an element, including nested inline elements."""
    text_parts = []
    
    if element.text:
        text_parts.append(element.text.strip())  # Add the text part of the current element
    
    # Process child elements like <Citation>, <Term>, etc.
    for child in element:
        # Handle different inline element cases if necessary (like <Citation>)
        if child.tag.endswith('Citation'):
            # Example of handling <Citation> elements
            citation_text = f"{child.text.strip()} ({child.attrib.get('Number')})" if child.text else ""
            text_parts.append(citation_text)
        elif child.tag.endswith('Term'):
            # Handle <Term> elements (e.g., for definitions)
            text_parts.append(f"'{child.text.strip()}'")
        else:
            # Default case: recurse for any nested element
            text_parts.append(extract_text_with_inlines(child))
        
        # Append any trailing tail text in the current element
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        if child.tail:
            text_parts.append(child.tail.strip())
    
    return ' '.join(text_parts)


<<<<<<< HEAD
def get_text_from_xpath(root, xpath, namespaces):
=======

def get_text_from_xpath(root, xpath, namespaces):
    """Get text from a specified XPath with namespaces."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    element = root.find(xpath, namespaces)
    return element.text.strip() if element is not None and element.text else None

def extract_metadata(root, namespaces):
<<<<<<< HEAD
=======
    """Extracts metadata from the XML root."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    return {
        'title': get_text_from_xpath(root, './/dc:title', namespaces),
        'subject': get_text_from_xpath(root, './/dc:subject', namespaces),
        'number': get_text_from_xpath(root, './/leg:Number', namespaces) or 'None',
    }

def extract_dates(root, namespaces):
 return {
        'made_date': get_text_from_xpath(root, './/leg:MadeDate/leg:DateText', namespaces) or 'None',
        'coming_into_force_date': get_text_from_xpath(root, './/leg:ComingIntoForce/leg:DateText', namespaces) or 'None',
        'laid_before_parliament_date': get_text_from_xpath(root, './/leg:LaidDate/leg:DateText', namespaces) or 'None'
    }


def extract_section_text(root, namespaces, section_xpaths):
<<<<<<< HEAD
=======
    """Extracts text from specified sections in the XML."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    section_texts = []
    for xpath in section_xpaths:
        texts = root.xpath(xpath, namespaces=namespaces)
        section_texts.extend(extract_text_with_inlines(text) for text in texts)
    
    text =  " ".join(section_texts) if section_texts else "No relevant text found."
    text.split('.')
    return text


def extract_body_content(root, namespaces):
<<<<<<< HEAD
=======
    """Extracts content from the Body section of the XML and formats it with correct line breaks."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    formatted_output = {}
    body = root.find('.//leg:Body', namespaces)

    if body is not None:
<<<<<<< HEAD
=======
        # Process P1group elements
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        for p1_group in body.findall('.//leg:P1group', namespaces):
            title_elem = p1_group.find('.//leg:Title', namespaces)
            group_title = title_elem.text if title_elem is not None else "Untitled\n"

<<<<<<< HEAD
=======
            # Initialize the group's item list
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
            group_items = {}

            for p1 in p1_group.findall('.//leg:P1', namespaces):
                p1_number = p1.find('.//leg:Pnumber', namespaces)
                p1_number_text = f"{p1_number.text}" if p1_number is not None else "Unknown"

<<<<<<< HEAD
                p1_texts = []
                for p1para in p1.findall('.//leg:P1para', namespaces):
                    para_texts = []

=======
                # Initialize a list to hold all paragraphs under this P1
                p1_texts = []

                # Extract paragraphs within P1 (including nested P2 elements)
                for p1para in p1.findall('.//leg:P1para', namespaces):
                    para_texts = []

                    # Handle P2 elements inside P1para
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
                    for p2 in p1para.findall('.//leg:P2', namespaces):
                        p2_number = p2.find('.//leg:Pnumber', namespaces)
                        p2_number_text = f"({p2_number.text})" if p2_number is not None else "(Unknown)"

<<<<<<< HEAD
                        for p2para in p2.findall('.//leg:P2para', namespaces):
                            p2para_text = extract_text_with_inlines(p2para)
                            if p2para_text:
                                para_texts.append(f'    {p2_number_text} {p2para_text.strip()}\n')


                    if not para_texts:
                        p1para_text = extract_text_with_inlines(p1para)
                        if p1para_text:
                            para_texts.append(f'{p1para_text.strip()}') 

                    if para_texts:
                        p1_texts.append(''.join(para_texts))

                if p1_texts:
                    group_items[f"{p1_number_text}"] = '\n'.join(p1_texts)
            formatted_output[group_title] = group_items

=======
                        # Extract P2 paragraphs
                        for p2para in p2.findall('.//leg:P2para', namespaces):
                            p2para_text = extract_text_with_inlines(p2para)
                            if p2para_text:
                                # Format each P2 subpoint
                                para_texts.append(f'    {p2_number_text} {p2para_text.strip()};\n')  # Indent and add a semicolon

                    # If no P2 elements, extract text directly from P1para
                    if not para_texts:
                        p1para_text = extract_text_with_inlines(p1para)
                        if p1para_text:
                            para_texts.append(f'{p1para_text.strip()};')  # Ensure semicolon

                    if para_texts:
                        # Join paragraphs together, ensuring correct format with newlines
                        p1_texts.append(''.join(para_texts))

                # Store the P1 number and its paragraphs, formatted with line breaks
                if p1_texts:
                    group_items[f"{p1_number_text}"] = '\n'.join(p1_texts)

            # Add the group title and its items to the formatted_output
            formatted_output[group_title] = group_items

        # Collect all P1 elements not in a P1group
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        all_p1_elements = body.findall('.//leg:P1', namespaces)
        for p1 in all_p1_elements:
            if not any(p1 in group.findall('.//leg:P1', namespaces) for group in body.findall('.//leg:P1group', namespaces)):
                p1_number = p1.find('.//leg:Pnumber', namespaces)
                p1_number_text = f"{p1_number.text}\n" if p1_number is not None else "Unknown"

                p1_texts = []
                for p1para in p1.findall('.//leg:P1para', namespaces):
                    p1para_text = extract_text_with_inlines(p1para)
                    if p1para_text:
<<<<<<< HEAD
                        p1_texts.append(f'{p1para_text.strip()};\n')
=======
                        p1_texts.append(f'{p1para_text.strip()};\n')  # Ensure semicolon
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04

                if p1_texts:
                    if "Unattributed" not in formatted_output:
                        formatted_output["Unattributed"] = {}
                    formatted_output["Unattributed"][f"{p1_number_text}"] = '\n'.join(p1_texts)

    return formatted_output



def extract_signatory_info(root, namespaces):
<<<<<<< HEAD
=======
    """Extracts signatory information from the SignedSection."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    signatory_info = {}
    signed_section = root.find('.//leg:SignedSection', namespaces)

    if signed_section is not None:
        signatory = signed_section.find('./leg:Signatory', namespaces)
        if signatory is not None:
            for field in ['PersonName', 'JobTitle', 'Department']:
                signatory_info[field] = signatory.find(f'./leg:Signee/leg:{field}', namespaces).text.strip() if signatory.find(f'./leg:Signee/leg:{field}', namespaces) is not None else None
            date_signed = signatory.find('./leg:Signee/leg:DateSigned', namespaces)
            signatory_info['DateSigned'] = date_signed.get('Date') if date_signed is not None else None
            signatory_info['DateText'] = signatory.find('./leg:Signee/leg:DateSigned/leg:DateText', namespaces).text.strip() if date_signed is not None else None

    return signatory_info

def extract_explanatory_notes(root, namespaces):
<<<<<<< HEAD
=======
    """Extracts Explanatory Notes content from the XML."""
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
    formatted_output = {}
    explanatory_notes = root.find('.//leg:ExplanatoryNotes', namespaces)

    if explanatory_notes is not None:
<<<<<<< HEAD
=======
        # Extract title
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        title_elem = explanatory_notes.find('leg:Title', namespaces)
        if title_elem is not None:
            formatted_output['Title'] = title_elem.text.strip()

<<<<<<< HEAD
=======
        # Extract comment (like the '(This note is not part of the Regulations)')
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        comment = explanatory_notes.find('leg:Comment/leg:Para/leg:Text', namespaces)
        if comment is not None:
            formatted_output['Comment'] = comment.text.strip()

<<<<<<< HEAD
        paragraph_list = []
        paragraphs = explanatory_notes.findall('leg:P', namespaces)
        for para in paragraphs:
            para_text = extract_text_with_inlines(para)
            if para_text:
                paragraph_list.append(para_text.strip())

        if paragraph_list:
            formatted_output['Paragraphs'] = ' \n\n '.join(paragraph_list)
    
    return formatted_output
=======
        # Extract all paragraphs inside <P> tags
        paragraph_list = []
        paragraphs = explanatory_notes.findall('leg:P', namespaces)
        for para in paragraphs:
            para_text = extract_text_with_inlines1(para)  # Assumes inline elements are correctly handled
            if para_text:
                paragraph_list.append(para_text.strip())

        # Ensure paragraphs are joined with two newlines for better formatting
        if paragraph_list:
            formatted_output['Paragraphs'] = ' \n\n '.join(paragraph_list)
    
    return formatted_output


def extract_text_with_inlines1(element):
    """Extracts text from an XML element, including inline amendments."""
    texts = []
    for node in element.iter():
        if node.tag.endswith('Text'):
            if node.text:
                texts.append(node.text.strip())
        elif node.tag.endswith('Citation') or node.tag.endswith('Term'):
            # Handle inlines like <Citation> and <Term>
            if node.text:
                texts.append(f"{node.text.strip()}")
        if node.tail:
            texts.append(node.tail.strip())
    return ' '.join(texts).strip()

def parse_complex_xml(file_path):
    """Main function to parse the XML file and extract all relevant data."""
    # Define XML namespaces
    namespaces = {
        'leg': 'http://www.legislation.gov.uk/namespaces/legislation',
        'dc': 'http://purl.org/dc/elements/1.1/',
        'ukm': 'http://www.legislation.gov.uk/namespaces/metadata',
        'dct': "http://purl.org/dc/terms/",
        'atom': "http://www.w3.org/2005/Atom",
    }

    # Load and parse the XML file
    tree = etree.parse(file_path)
    root = tree.getroot()

    # Extract all relevant information
    metadata = extract_metadata(root, namespaces)
    dates_data = extract_dates(root, namespaces)
    secondary_preamble_text = extract_section_text(root, namespaces, [
        './/leg:RoyalPresence/leg:Para/leg:Text',
        './/leg:IntroductoryText/leg:P/leg:Text',
        './/leg:EnactingText/leg:Para/leg:Text'
    ])
    body_content = extract_body_content(root, namespaces)
    signatory_info = extract_signatory_info(root, namespaces)
    explanatory_notes = extract_explanatory_notes(root, namespaces)

    # Return the results
    return {
        'Heading': 'Statutory Instruments',
        'Metadata': metadata,
        'Dates': dates_data,
        'Secondary Preamble Text': secondary_preamble_text,
        'Body Content': body_content,
        'Signatory Information': signatory_info,
        'Explanatory Notes': explanatory_notes,
    }
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
