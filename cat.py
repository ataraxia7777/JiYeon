from flask import Flask, render_template, jsonify
import cfscrape
import requests
import json
from collections import OrderedDict
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/hoovers/<company>')
def findCompanyInfoH(company):
	i = 0

	group_data = OrderedDict()
	company_data = OrderedDict()

	scraper = cfscrape.create_scraper()

	hooversReq = scraper.get('http://www.hoovers.com/company-information/company-search.html?term='+company)

	html = hooversReq.text

	soup = BeautifulSoup(html,'html.parser')

	#name: <td class="company_name">
	companyNameList = soup.find_all('td',{'class':'company_name'})

	#location: <td class="company_location">
	companyLocationList = soup.find_all('td',{'class':'company_location'})

	#sales: <td class="company_sales">
	companySalesList = soup.find_all('td',{'class':'company_sales'})

	for data in companyNameList:
		name = data.text
		location = companyLocationList[i].text
		sales = companySalesList[i].text

		company_data[name]={"Location":location,"Sales":sales}

		i = i + 1

	group_data["hoovers"]=company_data

	return jsonify(group_data)

@app.route('/crunchbase/<company>')
def findCompanyInfoC(company):
	i = 0

	crunchReq = requests.get('https://api.crunchbase.com/v3.1/organizations/' + company + '?user_key=09bbd7096498c9dca036d0f6f07ee420')

	return jsonify(crunchReq.json)

if __name__ == '__main__':
    app.run()
