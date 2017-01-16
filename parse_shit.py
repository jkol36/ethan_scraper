from lxml import etree
from bs4 import BeautifulSoup
import csv
import unicodedata
import codecs

mockSection = {
  'name': '01',
  'SIS_ID':'AFS_102_O2',
  'COURSE_SIS_Id': 'AFS_102'
}
def parse():
  courseNames = {}
  sections = []

  html = codecs.open('class_schedule.htm')
  soup = BeautifulSoup(html)
  for header in soup.find_all('th'):
    class_name = header.get('class')[0].encode('utf-8')
    if class_name == 'ddtitle':
      courseString = header.find('a').string.encode('utf-8')
      courseName = courseString.split('-')[2]
      courseId = '_'.join(courseName.split(' ')).strip('_')
      sectionName = courseString.split('-')[3].encode('utf-8')
      if sectionName[1] == '0':
        sections.append({
          'name': sectionName,
          'SIS_ID':courseId+'_'+sectionName,
          'COURSE_SIS_Id': courseId
          })
      else:
        courseName = sectionName
        courseId = '_'.join(courseName.split(' ')).strip('_')
        sectionName = courseString.split('-')[4].strip()
        sections.append({
          'name':sectionName,
          'SIS_ID':courseId+'_'+sectionName,
          'COURSE_SIS_Id':courseId
        })
      courseNames[courseId] = courseName
  return [courseNames, sections]

print parse()


    



dayDict = {
  'M': 1,
  'T': 2,
  'W': 3,
  'R': 4,
  'F': 5

}
# with open('sections.csv', 'wb') as csvfile:
#   fieldNames = ['name', 'SIS_ID', 'COURSE_SIS_Id']
#   sections = parse()[1]
#   writer = csv.DictWriter(csvfile, fieldNames)
#   writer.writeheader()
#   for section in sections:
#     writer.writerow(section)
  







