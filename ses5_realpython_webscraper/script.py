import requests
from bs4 import BeautifulSoup

URL = 'https://realpython.github.io/fake-jobs/'
page = requests.get(URL) #sender http get request til url, får html tilbage og gemmer det i objekt

print(page.text)

soup = BeautifulSoup(page.content, "html.parser") #laver beautilful soup objekt som 
#har HTML og ser det som html, der er funktioner til at rode rundt i html'en. det er dog stadig text
#vi parser page.content som er rå bytes vi får fra serveren modsat page.text som har konverteret
#det til text og derfor har character encoding. bs skal have rå bytes og lave sin egen parsing
#html.parser siger at vi skal bruge en parser for html specifikt. de andre parser er stadig
#html og xml, lml specifikke

#på siden er cards vist i div med id=resultsContainer. beautiful soup kan finde den:
results = soup.find(id="ResultsContainer")

print(results.prettify())

job_elements = results.find_all('div', class_="card-content") #ved class skal element
# specificeres da class jo kan være på mange elementer. class skal være med underscore åbenbart
# underscore er fordi class er reserved keyword i python til at lave en klasse, og her referes
# til css classes så derfor class_ for at undgå name conflicts
# .find_all returnere en iterable med alle elementerne

for job_element in job_elements:   # kan også printes direkte print(job_elements)
    print(job_element, end="\n"*2)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")  #de elementer for hver job_element
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text) # uden .text får vi html element: <h2 class="title is-5">Ship broker</h2>
    print(company_element.text) # med text får vi selve teksten i, Ship broker
    print(location_element.text.strip()) #alle pythons string metoder kan bruges, .strip() fjerner
    print()                              # white spaces. Uden strip() så output underligt ud

# selecter kun python jobs. kigger på overskrifter og string filtrerer resultat baseret på text content
python_jobs = results.find_all("h2", string="Python")
print(python_jobs) # printer tom string fordi den er case sensitive

# man kan parse anonyme funktioner til beautiful soup metoder
# find_all er en loop metode. hver index på results loopes igennem
# for hver h2 i hver index tages h2'en ind som parameter, som text, i den anonyme funktion
# text gøres lowercase så søgningen ikke er case sensitive. 
# det er ligesom at bruge arrow functions i loop metoder i js, her .filter()
# lambda funktionen returnerer True or False baseret på om h2 indeholder "python" og hvis true
# vil .find_all metoden returnerer result-indholdet på det indeks til den nye array python_jobs
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
#    "h2", string=lambda text: "python" in text.lower()
#    const isPythonInText = (text) => text.toLowerCase().includes("python");
# her tages KUN h2 tags med i python_jobs, men vi vil have også company og location
# i beautiful soup objekter kan man finde sibling, child og parent elementer af et element
# så her vil vi have et parent element for går vi op i DOM'en kan vi få company og location med

# list comprehension: [expression for x in iterable]
# vi looper gennem python_jobs som kun består af h2 elementer. for hver element tager vi 
# tre parents ud da det er her vi når til en div som har både titel, company og location som
# child elementer. vi laver så en ny liste med elementer som er hele det parent element
python_job_elements = [
    element.parent.parent.parent for element in python_jobs
]
#dette gøres fordi før da vi ville printe alt ud ud fra python_jobs array fik
#vi en typisk fejl om at elementer var null/NoType eller hvad de hed, og det var fordi
# vi kun har h2 elementer i python_jobs, så ikke company eller location


print(len(python_jobs)) #der er 10 jobs med python i titel


for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")  #de elementer for hver job_element
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text) # uden .text får vi html element: <h2 class="title is-5">Ship broker</h2>
    print(company_element.text) # med text får vi selve teksten i, Ship broker
    print(location_element.text.strip()) #alle pythons string metoder kan bruges, .strip() fjerner
    print() 

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")  #de elementer for hver job_element
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text) # uden .text får vi html element: <h2 class="title is-5">Ship broker</h2>
    print(company_element.text) # med text får vi selve teksten i, Ship broker
    print(location_element.text.strip()) #alle pythons string metoder kan bruges, .strip() fjerner
    link = job_element.find_all("a")[1]["href"]
    print(f"{link}\n")