from requests_html import HTMLSession

url = 'http://web.dmi.unict.it/corsi/l-31/insegnamenti?seuid=989DD4EB-0197-4768-B868-04B379B16EED'

s = HTMLSession()
r = s.get(url)

r.html.render(sleep=1)
syllabus_content = r.html.find('#content-wrap')[0].text
print(syllabus_content)