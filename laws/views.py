import requests
from django.shortcuts import render, redirect
from .forms import LawForm
from django.contrib.auth.decorators import login_required
from lxml import etree
from .extract_data import (
    extract_metadata,
    extract_dates,
    extract_section_text,
    extract_body_content,
    extract_signatory_info,
    extract_explanatory_notes,
    
)

def law_retrieve(request):
    form = LawForm()
    
    if request.method == "POST":
        form = LawForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            number = form.cleaned_data['number']
            return redirect('law_display', year=year, number=number)

    return render(request, 'laws/law-retrieve.html', {'form': form})



def law_display(request, year, number):
<<<<<<< HEAD

    url = f"https://www.legislation.gov.uk/uksi/{year}/{number}/made/data.xml"
    try:
        
        response = requests.get(url)
        response.raise_for_status()  
        xml_data = response.content
        
        tree = etree.fromstring(xml_data)
        
        namespaces = {
            'leg': 'http://www.legislation.gov.uk/namespaces/legislation',
            'dc': 'http://purl.org/dc/elements/1.1/'
        }

=======
    # Construct the URL using the year and number from the parameters
    url = f"https://www.legislation.gov.uk/uksi/{year}/{number}/made/data.xml"

    try:
        # Send a GET request to retrieve the XML data
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        xml_data = response.content
        
        # Parse the XML data
        tree = etree.fromstring(xml_data)
        
        # Define XML namespaces
        namespaces = {
            'leg': 'http://www.legislation.gov.uk/namespaces/legislation',
            'dc': 'http://purl.org/dc/elements/1.1/',
            'ukm': 'http://www.legislation.gov.uk/namespaces/metadata',
            'dct': "http://purl.org/dc/terms/",
            'atom': "http://www.w3.org/2005/Atom",
        }

        # Call the extraction functions
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        metadata = extract_metadata(tree, namespaces)
        dates = extract_dates(tree, namespaces)
        secondary_preamble_text = extract_section_text(tree, namespaces, [
            './/leg:RoyalPresence/leg:Para/leg:Text',
            './/leg:IntroductoryText/leg:P/leg:Text',
            './/leg:EnactingText/leg:Para/leg:Text'
        ])
        body_content = extract_body_content(tree, namespaces)
        signatory_info = extract_signatory_info(tree, namespaces)
        explanatory_notes = extract_explanatory_notes(tree, namespaces)

<<<<<<< HEAD
=======
        # Prepare the structured data to be sent to the template
>>>>>>> 94b488100885d27898d2b4af0c64a63b7a8d2d04
        context = {
            'heading': "Statutory Instruments",
            'metadata': metadata,
            'dates': dates,
            'secondary_preamble_text': secondary_preamble_text.split('. '),
            'body_content': body_content,
            'signatory_info': signatory_info,
            'explanatory_notes': explanatory_notes,
        }

        return render(request, 'laws/law-display.html', context)
        
    except requests.exceptions.RequestException as e:
        return render(request, 'laws/law-display.html', {'error': str(e)})
