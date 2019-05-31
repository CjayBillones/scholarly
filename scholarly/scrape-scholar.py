import scholarly
import csv

if __name__ == '__main__':

    search_query = scholarly.search_author('ELMER P DADIOS')
    author = next(search_query).fill()

    with open('publication-data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow(['Title', 'Authors', 'Journal', 'URL'])

        for publication in author.publications:
            pub = publication.fill()

            pub_details = []

            if 'title' in pub.bib:
                pub_details.append(pub.bib['title'])
            else:
                pub_details.append('')

            if 'author' in pub.bib:
                pub_details.append(pub.bib['author'])
            else:
                pub_details.append('')

            if 'journal' in pub.bib:
                pub_details.append(pub.bib['journal'])
            else:
                pub_details.append('')

            if 'url' in pub.bib:
                pub_details.append(pub.bib['url'])
            else:
                pub_details.append('')

            csv_writer.writerow([pub_details[0], pub_details[1], pub_details[2], pub_details[3]])
            print(pub)