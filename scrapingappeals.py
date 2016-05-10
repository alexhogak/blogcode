


def appeal_scrape(soup, appeal_no):

    appeals_array = []
    top_dict = {}
    appeal_cursor = 1
    rating_cursor = 1
    #print "looking for appeals"
    appeal_tables = soup.find_all('table', attrs={'summary': 'Property Valuation Table'})
    for appeal_table in appeal_tables:
        #print "found appeal Table"
        #appeals_dict["Appeal: "+str(appeal_cursor)+" Rating: "+str(rating_cursor)+" Valuation: "+str(appeal_no)+""] = {}
        tbody = appeal_table.find_all('tbody')
        appeal_data = tbody[0]
        rows = appeal_data.find_all('tr')
        for row in rows:
            #print "found appeal"
            appeal_dict = {}
            columns = row.find_all('td')
            referenceNo = columns[0].text.strip()
            applicant = columns[1].text.strip()
            agent = columns[2].text.strip()
            grounds = columns[3].text.strip()
            start_date = columns[5].text.strip()
            end_date = columns[6].text.strip()
            Settlement = columns[7].text.strip()
            appeal_dict["ReferenceNo"] = referenceNo
            appeal_dict["Applicant"] = applicant
            appeal_dict["Agent"] = agent
            appeal_dict["Grounds_for_Appeal"] = grounds
            appeal_dict["Start_Date"] = start_date
            appeal_dict["End_Date"] = end_date
            appeal_dict["Settlement"] = Settlement
            appeals_array.append(appeal_dict)
            #print appeals_array
            appeal_cursor = appeal_cursor + 1
        rating_cursor = rating_cursor + 1

    #top_dict["Appeals"] = appeals_array

    return appeals_array